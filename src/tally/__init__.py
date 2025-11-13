"""Unofficial Python SDK for the Tally.so API."""

from tally.client import TallyClient
from tally.exceptions import (
    BadRequestError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    ServerError,
    TallyAPIError,
    TallyConnectionError,
    TallyError,
    TallyTimeoutError,
    UnauthorizedError,
)
from tally.models import (
    Invite,
    PaginatedWebhookEvents,
    PaginatedWebhooks,
    PaginatedWorkspaces,
    SubscriptionPlan,
    User,
    Webhook,
    WebhookCreated,
    WebhookDeliveryStatus,
    WebhookEvent,
    WebhookEventType,
    WebhookHeader,
    Workspace,
    WorkspaceInvite,
)
from tally.resources import (
    OrganizationsResource,
    UsersResource,
    WebhooksResource,
    WorkspacesResource,
)

__version__ = "0.1.0"

# Alias for convenience
Tally = TallyClient

__all__ = [
    # Main client
    "Tally",
    "TallyClient",
    # Resources
    "OrganizationsResource",
    "UsersResource",
    "WebhooksResource",
    "WorkspacesResource",
    # Models
    "Invite",
    "PaginatedWebhookEvents",
    "PaginatedWebhooks",
    "PaginatedWorkspaces",
    "User",
    "Webhook",
    "WebhookCreated",
    "WebhookDeliveryStatus",
    "WebhookEvent",
    "WebhookEventType",
    "WebhookHeader",
    "Workspace",
    "WorkspaceInvite",
    "SubscriptionPlan",
    # Exceptions
    "TallyError",
    "TallyAPIError",
    "BadRequestError",
    "UnauthorizedError",
    "ForbiddenError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
    "TallyConnectionError",
    "TallyTimeoutError",
]
