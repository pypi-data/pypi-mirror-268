from typing import Optional

import streamlit as st

from rhdzmota.utils.json_web_token import JsonWebToken
from rhdzmota.ext.streamlit_webapps.page_view import PageView, PageViewHeader


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


class PHEmailACLBouncerHeader(PageViewHeader, EmailACLUtils):

    @property
    def on_failure_view(self) -> str:
        # Feel free to overwrite this property
        from .comp_email_acl_error import PVEmailACLError

        return PVEmailACLError.refname

    def on_start(self):
        # Redirect to the failure view if the token is
        # not accessible via the query params.
        if not (token := self.get_token_from_query_params(fail=False)):
            return self.forward(self.on_failure_view)
