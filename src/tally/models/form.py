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


class SubmissionFilter(str, Enum):
    """Submission filter types."""

    ALL = "all"
    COMPLETED = "completed"
    PARTIAL = "partial"


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

    @classmethod
    def from_dict(cls, data: dict) -> "FormBlock":
        """Create a FormBlock instance from API response data."""
        block_type = data["type"]
        group_type = data["groupType"]

        return cls(
            uuid=data["uuid"],
            type=BlockType(block_type)
            if block_type in BlockType.__members__.values()
            else block_type,
            group_uuid=data["groupUuid"],
            group_type=BlockType(group_type)
            if group_type in BlockType.__members__.values()
            else group_type,
            payload=data.get("payload"),
        )

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

    @classmethod
    def from_dict(cls, data: dict) -> "FormSettings":
        """Create a FormSettings instance from API response data."""
        return cls(
            language=data.get("language"),
            is_closed=data.get("isClosed", False),
            close_message_title=data.get("closeMessageTitle"),
            close_message_description=data.get("closeMessageDescription"),
            close_timezone=data.get("closeTimezone"),
            close_date=data.get("closeDate"),
            close_time=data.get("closeTime"),
            submissions_limit=data.get("submissionsLimit"),
            unique_submission_key=data.get("uniqueSubmissionKey"),
            redirect_on_completion=data.get("redirectOnCompletion"),
            has_self_email_notifications=data.get("hasSelfEmailNotifications", False),
            self_email_to=data.get("selfEmailTo"),
            self_email_reply_to=data.get("selfEmailReplyTo"),
            self_email_subject=data.get("selfEmailSubject"),
            self_email_from_name=data.get("selfEmailFromName"),
            self_email_body=data.get("selfEmailBody"),
            has_respondent_email_notifications=data.get("hasRespondentEmailNotifications", False),
            respondent_email_to=data.get("respondentEmailTo"),
            respondent_email_reply_to=data.get("respondentEmailReplyTo"),
            respondent_email_subject=data.get("respondentEmailSubject"),
            respondent_email_from_name=data.get("respondentEmailFromName"),
            respondent_email_body=data.get("respondentEmailBody"),
            has_progress_bar=data.get("hasProgressBar", False),
            has_partial_submissions=data.get("hasPartialSubmissions", False),
            page_auto_jump=data.get("pageAutoJump", False),
            save_for_later=data.get("saveForLater", True),
            styles=data.get("styles"),
            password=data.get("password"),
            submissions_data_retention_duration=data.get("submissionsDataRetentionDuration"),
            submissions_data_retention_unit=data.get("submissionsDataRetentionUnit"),
        )

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
        settings_dict["hasRespondentEmailNotifications"] = self.has_respondent_email_notifications
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
            settings_dict["submissionsDataRetentionUnit"] = self.submissions_data_retention_unit

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
            payments=[FormPayment.from_dict(payment) for payment in data.get("payments", [])]
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
            payments=[FormPayment.from_dict(payment) for payment in data.get("payments", [])]
            if data.get("payments")
            else None,
        )


@dataclass
class FormDetails:
    """Represents a complete Tally form with all blocks and settings.

    This is returned by the get() method and includes the full form structure,
    unlike the simplified Form model used in list operations.
    """

    id: str
    name: str
    workspace_id: str
    status: FormStatus
    number_of_submissions: int
    is_closed: bool
    created_at: datetime
    updated_at: datetime
    settings: FormSettings
    blocks: list[FormBlock]
    payments: list[FormPayment] | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "FormDetails":
        """Create a FormDetails instance from API response data."""
        return cls(
            id=data["id"],
            name=data["name"],
            workspace_id=data["workspaceId"],
            status=FormStatus(data["status"]),
            number_of_submissions=data["numberOfSubmissions"],
            is_closed=data["isClosed"],
            created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updatedAt"].replace("Z", "+00:00")),
            settings=FormSettings.from_dict(data["settings"]),
            blocks=[FormBlock.from_dict(block) for block in data.get("blocks", [])],
            payments=[FormPayment.from_dict(payment) for payment in data.get("payments", [])]
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


@dataclass
class QuestionField:
    """Represents a field within a form question."""

    uuid: str
    type: BlockType | str
    block_group_uuid: str
    title: str
    has_responses: bool

    @classmethod
    def from_dict(cls, data: dict) -> "QuestionField":
        """Create a QuestionField instance from API response data."""
        field_type = data["type"]

        return cls(
            uuid=data["uuid"],
            type=BlockType(field_type)
            if field_type in BlockType.__members__.values()
            else field_type,
            block_group_uuid=data["blockGroupUuid"],
            title=data["title"],
            has_responses=data["hasResponses"],
        )


@dataclass
class Question:
    """Represents a question in a Tally form."""

    id: str
    type: BlockType | str
    title: str
    is_title_modified_by_user: bool
    form_id: str
    is_deleted: bool
    number_of_responses: int
    created_at: datetime
    updated_at: datetime
    fields: list[QuestionField]

    @classmethod
    def from_dict(cls, data: dict) -> "Question":
        """Create a Question instance from API response data."""
        question_type = data["type"]

        return cls(
            id=data["id"],
            type=BlockType(question_type)
            if question_type in BlockType.__members__.values()
            else question_type,
            title=data["title"],
            is_title_modified_by_user=data["isTitleModifiedByUser"],
            form_id=data["formId"],
            is_deleted=data["isDeleted"],
            number_of_responses=data["numberOfResponses"],
            created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updatedAt"].replace("Z", "+00:00")),
            fields=[QuestionField.from_dict(field) for field in data.get("fields", [])],
        )


@dataclass
class SubmissionResponse:
    """Represents a response to a question in a submission."""

    question_id: str
    value: str | int | float | bool | list | dict | None

    @classmethod
    def from_dict(cls, data: dict) -> "SubmissionResponse":
        """Create a SubmissionResponse instance from API response data."""
        return cls(
            question_id=data["questionId"],
            value=data.get("value"),
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert to API request format."""
        return {
            "questionId": self.question_id,
            "value": self.value,
        }


@dataclass
class Submission:
    """Represents a form submission."""

    id: str
    form_id: str
    is_completed: bool
    submitted_at: datetime
    responses: list[SubmissionResponse]

    @classmethod
    def from_dict(cls, data: dict) -> "Submission":
        """Create a Submission instance from API response data."""
        return cls(
            id=data["id"],
            form_id=data["formId"],
            is_completed=data["isCompleted"],
            submitted_at=datetime.fromisoformat(data["submittedAt"].replace("Z", "+00:00")),
            responses=[
                SubmissionResponse.from_dict(response) for response in data.get("responses", [])
            ],
        )


@dataclass
class SubmissionsFilterCount:
    """Represents submission counts per filter type."""

    all: int
    completed: int
    partial: int

    @classmethod
    def from_dict(cls, data: dict) -> "SubmissionsFilterCount":
        """Create a SubmissionsFilterCount instance from API response data."""
        return cls(all=data["all"], completed=data["completed"], partial=data["partial"])


@dataclass
class PaginatedSubmissions:
    """Represents a paginated response of form submissions."""

    page: int
    limit: int
    has_more: bool
    total_number_of_submissions_per_filter: SubmissionsFilterCount
    questions: list[Question]
    submissions: list[Submission]

    @classmethod
    def from_dict(cls, data: dict) -> "PaginatedSubmissions":
        """Create a PaginatedSubmissions instance from API response data."""
        return cls(
            page=data["page"],
            limit=data["limit"],
            has_more=data["hasMore"],
            total_number_of_submissions_per_filter=SubmissionsFilterCount.from_dict(
                data["totalNumberOfSubmissionsPerFilter"]
            ),
            questions=[Question.from_dict(q) for q in data.get("questions", [])],
            submissions=[Submission.from_dict(s) for s in data.get("submissions", [])],
        )


@dataclass
class SubmissionDetails:
    """Represents a complete form submission with all metadata.

    This is returned by the get_submission() method and includes additional
    timestamps (created_at, updated_at), unlike the simplified Submission
    model used in list operations.
    """

    id: str
    form_id: str
    is_completed: bool
    submitted_at: datetime
    created_at: datetime
    updated_at: datetime
    responses: list[SubmissionResponse]

    @classmethod
    def from_dict(cls, data: dict) -> "SubmissionDetails":
        """Create a SubmissionDetails instance from API response data."""
        return cls(
            id=data["id"],
            form_id=data["formId"],
            is_completed=data["isCompleted"],
            submitted_at=datetime.fromisoformat(data["submittedAt"].replace("Z", "+00:00")),
            created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updatedAt"].replace("Z", "+00:00")),
            responses=[
                SubmissionResponse.from_dict(response) for response in data.get("responses", [])
            ],
        )


@dataclass
class SubmissionWithQuestions:
    """Represents a submission response with its associated questions.

    This is the response structure from the get_submission() endpoint,
    which includes both the submission details and all form questions.
    """

    questions: list[Question]
    submission: SubmissionDetails

    @classmethod
    def from_dict(cls, data: dict) -> "SubmissionWithQuestions":
        """Create a SubmissionWithQuestions instance from API response data."""
        return cls(
            questions=[Question.from_dict(q) for q in data.get("questions", [])],
            submission=SubmissionDetails.from_dict(data["submission"]),
        )
