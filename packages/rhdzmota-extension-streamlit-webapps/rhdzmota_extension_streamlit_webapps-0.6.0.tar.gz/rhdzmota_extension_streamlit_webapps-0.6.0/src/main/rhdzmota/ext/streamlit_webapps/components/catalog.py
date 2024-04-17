import enum

from .comp_simple_email_access_request import SimpleEmailAccessRequest
from .collection_email_acl_via_token.comp_email_acl_failure import PVEmailACLFailure
from .collection_email_acl_via_token.comp_email_acl_success import PVEmailACLSuccess
from .collection_email_acl_via_token.comp_email_acl_gatekeeper import PVEmailACLGatekeeper


class CompCatalog(enum.Enum):
    SIMPLE_EMAIL_ACCESS_REQUEST = SimpleEmailAccessRequest
    # Email ACL via json-web-token
    EMAIL_ACL_FAILURE = PVEmailACLFailure
    EMAIL_ACL_SUCCESS = PVEmailACLSuccess
    EMAIL_ACL_GATEKEEPER = PVEmailACLGatekeeper

    def configure(self, **kwargs):
        return self.value(**kwargs)
