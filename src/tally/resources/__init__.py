"""Resources for the Tally API."""

from tally.resources.forms import FormsResource
from tally.resources.organizations import OrganizationsResource
from tally.resources.users import UsersResource
from tally.resources.webhooks import WebhooksResource
from tally.resources.workspaces import WorkspacesResource

__all__ = [
    "FormsResource",
    "OrganizationsResource",
    "UsersResource",
    "WebhooksResource",
    "WorkspacesResource",
]
