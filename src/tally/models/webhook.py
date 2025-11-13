"""Webhook models for the Tally API."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class WebhookEventType(str, Enum):
    """Webhook event types."""

    FORM_RESPONSE = "FORM_RESPONSE"


class WebhookDeliveryStatus(str, Enum):
    """Webhook delivery status."""

    QUEUED = "QUEUED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    DROPPED = "DROPPED"


@dataclass
class WebhookHeader:
    """Represents a custom HTTP header for webhook requests."""

    name: str
    value: str

    @classmethod
    def from_dict(cls, data: dict) -> "WebhookHeader":
        """Create a WebhookHeader instance from API response data."""
        return cls(
            name=data["name"],
            value=data["value"],
        )


@dataclass
class Webhook:
    """Represents a Tally webhook."""

    id: str
    form_id: str
    url: str
    signing_secret: str | None
    http_headers: list[WebhookHeader] | None
    event_types: list[WebhookEventType]
    external_subscriber: str | None
    is_enabled: bool
    last_synced_at: datetime | None
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict) -> "Webhook":
        """Create a Webhook instance from API response data."""
        return cls(
            id=data["id"],
            form_id=data["formId"],
            url=data["url"],
            signing_secret=data.get("signingSecret"),
            http_headers=[
                WebhookHeader.from_dict(header) for header in data.get("httpHeaders") or []
            ]
            if data.get("httpHeaders")
            else None,
            event_types=[WebhookEventType(event) for event in data["eventTypes"]],
            external_subscriber=data.get("externalSubscriber"),
            is_enabled=data["isEnabled"],
            last_synced_at=datetime.fromisoformat(data["lastSyncedAt"].replace("Z", "+00:00"))
            if data.get("lastSyncedAt")
            else None,
            created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updatedAt"].replace("Z", "+00:00")),
        )


@dataclass
class WebhookCreated:
    """Represents the response when creating a webhook."""

    id: str
    url: str
    event_types: list[WebhookEventType]
    is_enabled: bool
    created_at: datetime

    @classmethod
    def from_dict(cls, data: dict) -> "WebhookCreated":
        """Create a WebhookCreated instance from API response data."""
        return cls(
            id=data["id"],
            url=data["url"],
            event_types=[WebhookEventType(event) for event in data["eventTypes"]],
            is_enabled=data["isEnabled"],
            created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
        )


@dataclass
class WebhookEvent:
    """Represents a webhook delivery event."""

    id: str
    webhook_id: str
    webhook_url: str
    event_type: WebhookEventType
    delivery_status: WebhookDeliveryStatus
    status_code: int | None
    response: str | None
    retry: int
    payload: dict
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict) -> "WebhookEvent":
        """Create a WebhookEvent instance from API response data."""
        return cls(
            id=data["id"],
            webhook_id=data["webhookId"],
            webhook_url=data["webhookUrl"],
            event_type=WebhookEventType(data["eventType"]),
            delivery_status=WebhookDeliveryStatus(data["deliveryStatus"]),
            status_code=data.get("statusCode"),
            response=data.get("response"),
            retry=data["retry"],
            payload=data["payload"],
            created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updatedAt"].replace("Z", "+00:00")),
        )


@dataclass
class PaginatedWebhookEvents:
    """Represents a paginated response of webhook events."""

    events: list[WebhookEvent]
    page: int
    limit: int
    has_more: bool
    total_number_of_events: int

    @classmethod
    def from_dict(cls, data: dict) -> "PaginatedWebhookEvents":
        """Create a PaginatedWebhookEvents instance from API response data."""
        return cls(
            events=[WebhookEvent.from_dict(event) for event in data.get("events", [])],
            page=data["page"],
            limit=data["limit"],
            has_more=data["hasMore"],
            total_number_of_events=data["totalNumberOfEvents"],
        )


@dataclass
class PaginatedWebhooks:
    """Represents a paginated response of webhooks."""

    webhooks: list[Webhook]
    page: int
    limit: int
    has_more: bool
    total_count: int

    @classmethod
    def from_dict(cls, data: dict) -> "PaginatedWebhooks":
        """Create a PaginatedWebhooks instance from API response data."""
        return cls(
            webhooks=[Webhook.from_dict(wh) for wh in data.get("webhooks", [])],
            page=data["page"],
            limit=data["limit"],
            has_more=data["hasMore"],
            total_count=data["totalCount"],
        )
