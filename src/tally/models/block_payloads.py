"""Payload type definitions for form blocks."""

from typing import Any, TypedDict


class BasePayload(TypedDict, total=False):
    """Base payload with common fields across block types."""

    isHidden: bool
    columnListUuid: str
    columnUuid: str
    columnRatio: float


class FormTitlePayload(BasePayload):
    """Payload for FORM_TITLE block type."""

    html: str


class TextPayload(BasePayload):
    """Payload for TEXT block type."""

    html: str


class LabelPayload(BasePayload):
    """Payload for LABEL block type."""

    html: str


class TitlePayload(BasePayload):
    """Payload for TITLE block type."""

    html: str


class Heading1Payload(BasePayload):
    """Payload for HEADING_1 block type."""

    html: str


class Heading2Payload(BasePayload):
    """Payload for HEADING_2 block type."""

    html: str


class Heading3Payload(BasePayload):
    """Payload for HEADING_3 block type."""

    html: str


class DividerPayload(BasePayload):
    """Payload for DIVIDER block type."""

    pass


class PageBreakPayload(BasePayload):
    """Payload for PAGE_BREAK block type."""

    html: str


class ThankYouPagePayload(BasePayload):
    """Payload for THANK_YOU_PAGE block type."""

    html: str


class ImagePayload(BasePayload):
    """Payload for IMAGE block type."""

    url: str
    alt: str
    width: float
    height: float


class EmbedPayload(BasePayload):
    """Payload for EMBED block type."""

    html: str
    url: str


class EmbedVideoPayload(BasePayload):
    """Payload for EMBED_VIDEO block type."""

    url: str


class EmbedAudioPayload(BasePayload):
    """Payload for EMBED_AUDIO block type."""

    url: str


class QuestionPayload(BasePayload):
    """Payload for QUESTION block type."""

    html: str
    required: bool
    description: str


class MatrixPayload(BasePayload):
    """Payload for MATRIX block type."""

    html: str
    required: bool


class InputTextPayload(BasePayload):
    """Payload for INPUT_TEXT block type."""

    placeholder: str
    defaultValue: str
    minLength: int
    maxLength: int


class InputNumberPayload(BasePayload):
    """Payload for INPUT_NUMBER block type."""

    placeholder: str
    defaultValue: float
    min: float
    max: float


class InputEmailPayload(BasePayload):
    """Payload for INPUT_EMAIL block type."""

    placeholder: str
    defaultValue: str


class InputLinkPayload(BasePayload):
    """Payload for INPUT_LINK block type."""

    placeholder: str
    defaultValue: str


class InputPhoneNumberPayload(BasePayload):
    """Payload for INPUT_PHONE_NUMBER block type."""

    placeholder: str
    defaultValue: str


class InputDatePayload(BasePayload):
    """Payload for INPUT_DATE block type."""

    format: str
    defaultValue: str


class InputTimePayload(BasePayload):
    """Payload for INPUT_TIME block type."""

    format: str
    defaultValue: str


class TextareaPayload(BasePayload):
    """Payload for TEXTAREA block type."""

    placeholder: str
    defaultValue: str
    minLength: int
    maxLength: int
    rows: int


class FileUploadPayload(BasePayload):
    """Payload for FILE_UPLOAD block type."""

    accept: str
    maxSize: int
    multiple: bool


class LinearScalePayload(BasePayload):
    """Payload for LINEAR_SCALE block type."""

    min: int
    max: int
    minLabel: str
    maxLabel: str


class RatingPayload(BasePayload):
    """Payload for RATING block type."""

    max: int
    icon: str


class HiddenFieldsPayload(BasePayload):
    """Payload for HIDDEN_FIELDS block type."""

    fields: dict[str, str]


class OptionPayload(BasePayload):
    """Payload for option-based block types (MULTIPLE_CHOICE, CHECKBOX, etc)."""

    label: str
    value: str


class PaymentPayload(BasePayload):
    """Payload for PAYMENT block type."""

    amount: float
    currency: str
    description: str


class SignaturePayload(BasePayload):
    """Payload for SIGNATURE block type."""

    pass


class MatrixRowPayload(BasePayload):
    """Payload for MATRIX_ROW block type."""

    label: str


class MatrixColumnPayload(BasePayload):
    """Payload for MATRIX_COLUMN block type."""

    label: str


class WalletConnectPayload(BasePayload):
    """Payload for WALLET_CONNECT block type."""

    chains: list[str]


class ConditionalLogicPayload(BasePayload):
    """Payload for CONDITIONAL_LOGIC block type."""

    conditions: list[dict[str, Any]]
    actions: list[dict[str, Any]]


class CalculatedFieldsPayload(BasePayload):
    """Payload for CALCULATED_FIELDS block type."""

    formula: str


class CaptchaPayload(BasePayload):
    """Payload for CAPTCHA block type."""

    provider: str


class RespondentCountryPayload(BasePayload):
    """Payload for RESPONDENT_COUNTRY block type."""

    pass


# Union type for all possible payloads
BlockPayload = (
    FormTitlePayload
    | TextPayload
    | LabelPayload
    | TitlePayload
    | Heading1Payload
    | Heading2Payload
    | Heading3Payload
    | DividerPayload
    | PageBreakPayload
    | ThankYouPagePayload
    | ImagePayload
    | EmbedPayload
    | EmbedVideoPayload
    | EmbedAudioPayload
    | QuestionPayload
    | MatrixPayload
    | InputTextPayload
    | InputNumberPayload
    | InputEmailPayload
    | InputLinkPayload
    | InputPhoneNumberPayload
    | InputDatePayload
    | InputTimePayload
    | TextareaPayload
    | FileUploadPayload
    | LinearScalePayload
    | RatingPayload
    | HiddenFieldsPayload
    | OptionPayload
    | PaymentPayload
    | SignaturePayload
    | MatrixRowPayload
    | MatrixColumnPayload
    | WalletConnectPayload
    | ConditionalLogicPayload
    | CalculatedFieldsPayload
    | CaptchaPayload
    | RespondentCountryPayload
    | dict[str, Any]  # Fallback for flexibility
)

__all__ = [
    # Base
    "BasePayload",
    "BlockPayload",
    # Payloads
    "FormTitlePayload",
    "TextPayload",
    "LabelPayload",
    "TitlePayload",
    "Heading1Payload",
    "Heading2Payload",
    "Heading3Payload",
    "DividerPayload",
    "PageBreakPayload",
    "ThankYouPagePayload",
    "ImagePayload",
    "EmbedPayload",
    "EmbedVideoPayload",
    "EmbedAudioPayload",
    "QuestionPayload",
    "MatrixPayload",
    "InputTextPayload",
    "InputNumberPayload",
    "InputEmailPayload",
    "InputLinkPayload",
    "InputPhoneNumberPayload",
    "InputDatePayload",
    "InputTimePayload",
    "TextareaPayload",
    "FileUploadPayload",
    "LinearScalePayload",
    "RatingPayload",
    "HiddenFieldsPayload",
    "OptionPayload",
    "PaymentPayload",
    "SignaturePayload",
    "MatrixRowPayload",
    "MatrixColumnPayload",
    "WalletConnectPayload",
    "ConditionalLogicPayload",
    "CalculatedFieldsPayload",
    "CaptchaPayload",
    "RespondentCountryPayload",
]
