"""Form models for the Tally API."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any

from tally.models.block_payloads import BlockPayload


class FormStatus(str, Enum):
    """Form status types."""

    BLANK = "BLANK"
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"


class BlockType(str, Enum):
    """Form block types."""

    FORM_TITLE = "FORM_TITLE"
    TEXT = "TEXT"
    LABEL = "LABEL"
    TITLE = "TITLE"
    HEADING_1 = "HEADING_1"
    HEADING_2 = "HEADING_2"
    HEADING_3 = "HEADING_3"
    DIVIDER = "DIVIDER"
    PAGE_BREAK = "PAGE_BREAK"
    THANK_YOU_PAGE = "THANK_YOU_PAGE"
    IMAGE = "IMAGE"
    EMBED = "EMBED"
    EMBED_VIDEO = "EMBED_VIDEO"
    EMBED_AUDIO = "EMBED_AUDIO"
    QUESTION = "QUESTION"
    MATRIX = "MATRIX"
    INPUT_TEXT = "INPUT_TEXT"
    INPUT_NUMBER = "INPUT_NUMBER"
    INPUT_EMAIL = "INPUT_EMAIL"
    INPUT_LINK = "INPUT_LINK"
    INPUT_PHONE_NUMBER = "INPUT_PHONE_NUMBER"
    INPUT_DATE = "INPUT_DATE"
    INPUT_TIME = "INPUT_TIME"
    TEXTAREA = "TEXTAREA"
    FILE_UPLOAD = "FILE_UPLOAD"
    LINEAR_SCALE = "LINEAR_SCALE"
    RATING = "RATING"
    HIDDEN_FIELDS = "HIDDEN_FIELDS"
    MULTIPLE_CHOICE_OPTION = "MULTIPLE_CHOICE_OPTION"
    CHECKBOX = "CHECKBOX"
    DROPDOWN_OPTION = "DROPDOWN_OPTION"
    RANKING_OPTION = "RANKING_OPTION"
    MULTI_SELECT_OPTION = "MULTI_SELECT_OPTION"
    PAYMENT = "PAYMENT"
    SIGNATURE = "SIGNATURE"
    MATRIX_ROW = "MATRIX_ROW"
    MATRIX_COLUMN = "MATRIX_COLUMN"
    WALLET_CONNECT = "WALLET_CONNECT"
    CONDITIONAL_LOGIC = "CONDITIONAL_LOGIC"
    CALCULATED_FIELDS = "CALCULATED_FIELDS"
    CAPTCHA = "CAPTCHA"
    RESPONDENT_COUNTRY = "RESPONDENT_COUNTRY"


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

    def to_dict(self) -> dict[str, Any]:
        """Convert to API request format."""
        return {
            "amount": self.amount,
            "currency": self.currency,
        }


@dataclass
class FormBlock:
    """Represents a form block element.

    The payload type is flexible and type-safe:
    - Use specific TypedDict payloads (FormTitlePayload, QuestionPayload, etc) for type safety
    - Use dict[str, Any] for maximum flexibility
    - All payload types support the common BasePayload fields
    """

    uuid: str
    type: BlockType | str
    group_uuid: str
    group_type: BlockType | str
    payload: BlockPayload | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to API request format."""
        block_dict: dict[str, Any] = {
            "uuid": self.uuid,
            "type": self.type.value if isinstance(self.type, BlockType) else self.type,
            "groupUuid": self.group_uuid,
            "groupType": self.group_type.value
            if isinstance(self.group_type, BlockType)
            else self.group_type,
        }
        if self.payload is not None:
            block_dict["payload"] = self.payload
        return block_dict


@dataclass
class FormSettings:
    """Form settings configuration."""

    language: str | None = None
    is_closed: bool = False
    close_message_title: str | None = None
    close_message_description: str | None = None
    close_timezone: str | None = None
    close_date: str | None = None
    close_time: str | None = None
    submissions_limit: int | None = None
    unique_submission_key: str | None = None
    redirect_on_completion: str | None = None
    has_self_email_notifications: bool = False
    self_email_to: str | None = None
    self_email_reply_to: str | None = None
    self_email_subject: str | None = None
    self_email_from_name: str | None = None
    self_email_body: str | None = None
    has_respondent_email_notifications: bool = False
    respondent_email_to: str | None = None
    respondent_email_reply_to: str | None = None
    respondent_email_subject: str | None = None
    respondent_email_from_name: str | None = None
    respondent_email_body: str | None = None
    has_progress_bar: bool = False
    has_partial_submissions: bool = False
    page_auto_jump: bool = False
    save_for_later: bool = True
    styles: str | None = None
    password: str | None = None
    submissions_data_retention_duration: int | None = None
    submissions_data_retention_unit: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to API request format."""
        settings_dict: dict[str, Any] = {}

        if self.language is not None:
            settings_dict["language"] = self.language
        settings_dict["isClosed"] = self.is_closed
        if self.close_message_title is not None:
            settings_dict["closeMessageTitle"] = self.close_message_title
        if self.close_message_description is not None:
            settings_dict["closeMessageDescription"] = self.close_message_description
        if self.close_timezone is not None:
            settings_dict["closeTimezone"] = self.close_timezone
        if self.close_date is not None:
            settings_dict["closeDate"] = self.close_date
        if self.close_time is not None:
            settings_dict["closeTime"] = self.close_time
        if self.submissions_limit is not None:
            settings_dict["submissionsLimit"] = self.submissions_limit
        if self.unique_submission_key is not None:
            settings_dict["uniqueSubmissionKey"] = self.unique_submission_key
        if self.redirect_on_completion is not None:
            settings_dict["redirectOnCompletion"] = self.redirect_on_completion
        settings_dict["hasSelfEmailNotifications"] = self.has_self_email_notifications
        if self.self_email_to is not None:
            settings_dict["selfEmailTo"] = self.self_email_to
        if self.self_email_reply_to is not None:
            settings_dict["selfEmailReplyTo"] = self.self_email_reply_to
        if self.self_email_subject is not None:
            settings_dict["selfEmailSubject"] = self.self_email_subject
        if self.self_email_from_name is not None:
            settings_dict["selfEmailFromName"] = self.self_email_from_name
        if self.self_email_body is not None:
            settings_dict["selfEmailBody"] = self.self_email_body
        settings_dict["hasRespondentEmailNotifications"] = (
            self.has_respondent_email_notifications
        )
        if self.respondent_email_to is not None:
            settings_dict["respondentEmailTo"] = self.respondent_email_to
        if self.respondent_email_reply_to is not None:
            settings_dict["respondentEmailReplyTo"] = self.respondent_email_reply_to
        if self.respondent_email_subject is not None:
            settings_dict["respondentEmailSubject"] = self.respondent_email_subject
        if self.respondent_email_from_name is not None:
            settings_dict["respondentEmailFromName"] = self.respondent_email_from_name
        if self.respondent_email_body is not None:
            settings_dict["respondentEmailBody"] = self.respondent_email_body
        settings_dict["hasProgressBar"] = self.has_progress_bar
        settings_dict["hasPartialSubmissions"] = self.has_partial_submissions
        settings_dict["pageAutoJump"] = self.page_auto_jump
        settings_dict["saveForLater"] = self.save_for_later
        if self.styles is not None:
            settings_dict["styles"] = self.styles
        if self.password is not None:
            settings_dict["password"] = self.password
        if self.submissions_data_retention_duration is not None:
            settings_dict["submissionsDataRetentionDuration"] = (
                self.submissions_data_retention_duration
            )
        if self.submissions_data_retention_unit is not None:
            settings_dict["submissionsDataRetentionUnit"] = (
                self.submissions_data_retention_unit
            )

        return settings_dict


@dataclass
class FormCreated:
    """Response from creating a form."""

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
    def from_dict(cls, data: dict) -> "FormCreated":
        """Create a FormCreated instance from API response data."""
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
