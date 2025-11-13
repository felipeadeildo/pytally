"""Form models for the Tally API."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class FormStatus(str, Enum):
    """Form status types."""

    BLANK = "BLANK"
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"


@dataclass
class FormPayment:
    """Represents a payment configuration for a form."""

    amount: float
    currency: str

    @classmethod
    def from_dict(cls, data: dict) -> "FormPayment":
        """Create a FormPayment instance from API response data."""
        return cls(
            amount=data["amount"],
            currency=data["currency"],
        )


@dataclass
class Form:
    """Represents a Tally form."""

    id: str
    name: str
    workspace_id: str
    status: FormStatus
    number_of_submissions: int
    is_closed: bool
    created_at: datetime
    updated_at: datetime
    payments: list[FormPayment] | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "Form":
        """Create a Form instance from API response data."""
        return cls(
            id=data["id"],
            name=data["name"],
            workspace_id=data["workspaceId"],
            status=FormStatus(data["status"]),
            number_of_submissions=data["numberOfSubmissions"],
            is_closed=data["isClosed"],
            created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updatedAt"].replace("Z", "+00:00")),
            payments=[
                FormPayment.from_dict(payment) for payment in data.get("payments", [])
            ]
            if data.get("payments")
            else None,
        )


@dataclass
class PaginatedForms:
    """Represents a paginated response of forms."""

    items: list[Form]
    page: int
    limit: int
    total: int
    has_more: bool

    @classmethod
    def from_dict(cls, data: dict) -> "PaginatedForms":
        """Create a PaginatedForms instance from API response data."""
        return cls(
            items=[Form.from_dict(form) for form in data.get("items", [])],
            page=data["page"],
            limit=data["limit"],
            total=data["total"],
            has_more=data["hasMore"],
        )
