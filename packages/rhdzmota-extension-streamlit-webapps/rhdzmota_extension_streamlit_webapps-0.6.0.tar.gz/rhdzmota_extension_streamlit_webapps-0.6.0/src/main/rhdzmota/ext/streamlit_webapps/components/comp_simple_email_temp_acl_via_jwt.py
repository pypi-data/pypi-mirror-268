import os
import uuid
import datetime as dt
from dataclasses import dataclass
from typing import Optional

import streamlit as st

from rhdzmota.mail.message import Message
from rhdzmota.settings import logger_manager
from rhdzmota.mail.server import EmailServerWrapper
from rhdzmota.utils.json_web_token import JsonWebToken
from rhdzmota.mail.validation import validate_email_pattern
from rhdzmota.ext.streamlit_webapps.page_view import (
    PageView,
    PageViewHeader,
)


logger = logger_manager.get_logger(name=__name__)


DEFAULT_TEMPLATE_PLAIN_TEXT = """
Hello! You have been provided with a temporal link to access "{service_title}":

{redirect_url}

"""


class EmailACLUtils:

    @classmethod
    def json_web_token_get_or_create(cls) -> 'JsonWebToken':
        return JsonWebToken.auto_configure()

    @classmethod
    def get_start_page_from_token(cls, or_else: str) -> str:
        token = cls.get_token_from_query_params(fail=False)
        if not token:
            return or_else
        jwt = cls.json_web_token_get_or_create()
        config = jwt.decode(token)
        return config.get("view", or_else)

    def get_start_page_or_use_me_instead(self) -> str:
        if not isinstance(self, PageView):
            raise ValueError("Only PageViews can use this method.")
        return self.get_start_page_from_token(or_else=self.refname)

    @classmethod
    def get_token_from_query_params(cls, fail: bool = False) -> Optional[str]:
        if "token" not in (params := st.query_params.to_dict()):
            if fail:
                raise ValueError("Token Not Found in query params")
            return
        jwt = cls.json_web_token_get_or_create()
        try:
            return params["token"]
        except Exception:
            if fail:
                raise


class PVEmailACLError(PageView):
    def view(self):
        return st.error("There seems to be an issue!")


class PHEmailACLBouncerHeader(PageViewHeader, EmailACLUtils):

    @property
    def on_failure_view(self) -> str:
        # Feel free to overwrite this property
        return PVEmailACLError.refname

    def on_start(self):
        # Redirect to the failure view if the token is
        # not accessible via the query params.
        if not (token := self.get_token_from_query_params(fail=False)):
            return self.forward(self.on_failure_view)


@dataclass(frozen=True, slots=True, kw_only=True)
class PVEmailACLGatekeeper(PageView, EmailACLUtils):
    from_email: str
    reference_url_pattern: str
    reference_page_redirect: str
    reference_page_on_success: str
    reference_page_on_failure: str
    reference_service_title: Optional[str] = None
    overwrite_component_subtitle: Optional[str] = None
    overwrite_submit_button_label: Optional[str] = None

    @property
    def service_title(self) -> str:
        return self.reference_service_title or \
            self.reference_page_redirect.title()

    @property
    def submit_button_label(self) -> str:
        return self.overwrite_submit_button_label or "Submit"

    @property
    def component_subtitle(self) -> str:
        return self.overwrite_component_subtitle or (
            "Request temporal access"
        )

    @property
    def component_description(self) -> str:
        return (
            "Use this form to request temporal access "
            f"to '{self.service_title}' via email."
        )

    def additional_form_inputs_before(self) -> dict:
        return {}

    def additional_form_inputs_after(self) -> dict:
        return {}

    def should_trust_this_domain_pass(self, target_domain: str) -> bool:
        # Overwrite this implementation with
        # custom logic to verify the domain
        if not (
            trusted_domains := os.environ.get(
                "TRUSTED_DOMAINS",
                default="",
            )
        ):
            logger.warning(
                "The trusted domains list is empty... "
                "consider defining the env.var: TRUSTED_DOMAINS"
            )
        match trusted_domains:
            case "ALL":
                return True
            case seq if ";" in seq:
                return target_domain in seq
            case single_domain:
                return target_domain == single_domain

    def should_this_email_pass(self, target_email: str) -> bool:
        # Overwrite this implementation with
        # custom logic to verify the email
        if not (
            trusted_emails := os.environ.get(
                "TRUSTED_EMAILS",
                default="",
            )
        ):
            logger.warning(
                "The trusted emails list is empty... "
                "consider defining the env.var: TRUSTED_EMAILS"
            )
        match trusted_emails:
            case "ALL":
                return True
            case seq if ";" in seq:
                return target_email in seq
            case single_email:
                return target_email == single_email

    def email_validation_error_message(self):
        st.error("There's an error with the data you provided.")

    def email_content_plain_text(
            self,
            redirect_url: str,
            payload: dict
    ) -> str:
        return DEFAULT_TEMPLATE_PLAIN_TEXT.format(
            redirect_url=redirect_url,
            service_title=self.service_title,
        )

    def email_content_html(
            self,
            redirect_url: str,
            payload: dict,
    ) -> Optional[str]:
        return

    def procedure_validate_email(
            self,
            email: str,
            domain: str,
    ) -> bool:
        # Start with a regex validation
        if not validate_email_pattern(target_email=email):
            logger.error(f"Invalid email pattern: {email}")
            return False
        # Verify the domain... This should be custom logic.
        elif not self.should_this_domain_pass(target_domain=domain):
            logger.error(f"Invalid domain: {domain}")
            return False
        # Verify the email... This should be custom logic.
        elif not self.should_this_email_pass(target_email=email):
            logger.error(f"Invalid email: {email}")
            return False
        return True

    def procedure_email_send(
            self,
            email: str,
            domain: str,
            form_data: dict,
    ) -> bool:
        # Generate token with relevant data
        jwt = self.json_web_token_get_or_create()
        payload = {
            "email": email,
            "domain": domain,
            "valid_until": None,
            "view": self.reference_page_redirect,
            "form_data": form_data,
        }
        token = jwt.encode(payload)
        redirect_url = self.reference_url_pattern.format(
            token=token,
        )
        # Create email message
        msg = Message.content_plain_text(
            subject=f"Temporal Access: {self.service_title}",
            content=self.email_content_plain_text(
                redirect_url=redirect_url,
                payload=payload,
            ),
            author=self.from_email,
            include_html=self.email_content_html(
                redirect_url=redirect_url,
                payload=payload,
            ),
        )
        # Send email message
        try:
            server_wrapper = EmailServerWrapper.gmail()
            with server_wrapper.login() as server:
                server.send(
                    email,
                    message=msg,
                    disable_tls=False,
                )
            logger.info("The email has been dispatched!")
            return True
        except Exception as e:
            logger.error(f"Error detected when dispatching email: {str(e)}")
            return False

    def view(self, **kwargs):
        st.markdown(f"## {self.component_subtitle}")
        st.markdown(self.component_description)
        with st.form("form-" + self.refname):
            form_outputs_before = self.additional_form_inputs_before()
            email = st.text_input("Email")
            form_outputs_after = self.additional_form_inputs_after()
            submitted = st.form_submit_button(self.submit_button_label)
        if not submitted:
            return
        form_data = {
            **form_outputs_before,
            **form_outputs_after,
        }
        # Start with a simple validation...
        # Can the user-input be an email?
        if "@" not in email:
            return self.email_validation_error_message()

        _, domain = email.split("@")

        with st.spinner(text="Reviewing your data..."):
            if not self.procedure_validate_email(
                email=email,
                domain=domain,
            ):
                return self.email_validation_error_message()

        with st.spinner(text="Processing your request..."):
            if self.procedure_email_send(
                email=email,
                domain=domain,
                form_data=form_data,
            ):
                st.success("Done!")
                return self.forward(self.reference_page_on_success)
            return self.forward(self.reference_page_on_failure)
