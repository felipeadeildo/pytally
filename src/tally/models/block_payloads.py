"""Payload type definitions for form blocks.

This module defines TypedDict payloads for all Tally form block types.
All fields are optional (total=False) to support flexibility.

IMPORTANT DISTINCTION:
- Fields marked with "# Request" can be SENT when creating forms (POST)
- Fields marked with "# Response" are ONLY returned by the API (GET)
- Fields without markers can appear in both scenarios
"""

from typing import Any, Literal, TypedDict

# ! This code MUST change!! This code sucks!
# ! This code is trash, i need to think a way to separate request from response models while
# ! avoiding code duplication


class BasePayload(TypedDict, total=False):
    """Base payload with common fields across block types.

    These fields can be sent in requests and may appear in responses.
    """

    isHidden: bool  # Request & Response
    columnListUuid: str  # Request & Response
    columnUuid: str  # Request & Response
    columnRatio: float  # Request & Response
    name: str  # Request & Response


# Content Block Payloads


class MentionField(TypedDict, total=False):
    """Field reference in a mention (Request)."""

    uuid: str
    type: Literal["InputField", "CalculatedField", "HiddenField"]
    questionType: str
    blockGroupUuid: str
    title: str
    calculatedFieldType: Literal["NUMBER", "TEXT"]


class Mention(TypedDict, total=False):
    """Mention object for FormTitlePayload (Request)."""

    uuid: str
    field: MentionField
    defaultValue: Any


class CoverSettings(TypedDict, total=False):
    """Cover settings for FormTitlePayload (Request)."""

    objectPositionYPercent: float


class ButtonSettings(TypedDict, total=False):
    """Button settings for various payloads (Request & Response)."""

    label: str


class FormTitlePayload(BasePayload):
    """Payload for FORM_TITLE block type."""

    # Request fields (can be sent in POST)
    html: str  # Request
    logo: str  # Request (URI)
    cover: str  # Request (URI)
    coverSettings: CoverSettings  # Request
    mentions: list[Mention]  # Request
    button: ButtonSettings  # Request

    # Response-only fields (returned by GET, cannot be sent)
    safeHTMLSchema: list[Any]  # Response only
    title: str  # Response only


class TextPayload(BasePayload):
    """Payload for TEXT block type."""

    # Request fields
    html: str  # Request

    # Response-only fields
    safeHTMLSchema: list[Any]  # Response only
    isFolded: bool  # Response only


class LabelPayload(BasePayload):
    """Payload for LABEL block type."""

    # Request fields
    html: str  # Request
    isFolded: bool  # Request

    # Response-only fields
    safeHTMLSchema: list[Any]  # Response only


class TitlePayload(BasePayload):
    """Payload for TITLE block type."""

    # Request fields
    html: str  # Request
    isFolded: bool  # Request

    # Response-only fields
    safeHTMLSchema: list[Any]  # Response only


class Heading1Payload(BasePayload):
    """Payload for HEADING_1 block type."""

    # Request fields
    html: str  # Request

    # Response-only fields
    safeHTMLSchema: list[Any]  # Response only


class Heading2Payload(BasePayload):
    """Payload for HEADING_2 block type."""

    # Request fields
    html: str  # Request

    # Response-only fields
    safeHTMLSchema: list[Any]  # Response only


class Heading3Payload(BasePayload):
    """Payload for HEADING_3 block type."""

    # Request fields
    html: str  # Request

    # Response-only fields
    safeHTMLSchema: list[Any]  # Response only


class DividerPayload(BasePayload):
    """Payload for DIVIDER block type.

    Only uses base fields (isHidden, columnListUuid, etc).
    """

    pass


class PageBreakPayload(BasePayload):
    """Payload for PAGE_BREAK block type."""

    # Request fields
    index: int  # Request
    isFirst: bool  # Request
    isLast: bool  # Request
    isQualifiedForThankYouPage: bool  # Request
    isThankYouPage: bool  # Request

    # Response-only fields
    button: ButtonSettings  # Response only
    html: str  # Response only (legacy)


class ThankYouPagePayload(BasePayload):
    """Payload for THANK_YOU_PAGE block type."""

    # Request fields
    isThankYouPage: bool  # Request

    # Response-only fields
    html: str  # Response only
    safeHTMLSchema: list[Any]  # Response only


class ImageSettings(TypedDict, total=False):
    """Image settings (Request)."""

    name: str
    url: str


class ImagePayload(BasePayload):
    """Payload for IMAGE block type."""

    # Request fields
    images: list[ImageSettings]  # Request
    caption: str  # Request
    link: str  # Request (URI)
    altText: str  # Request

    # Response-only fields (legacy)
    url: str  # Response only (legacy)
    alt: str  # Response only (legacy)
    width: float  # Response only (legacy)
    height: float  # Response only (legacy)


class EmbedDisplay(TypedDict, total=False):
    """Embed display settings (Request)."""

    url: str


class EmbedPayload(BasePayload):
    """Payload for EMBED block type."""

    # Request fields
    type: Literal["rich", "video", "photo", "link", "pdf", "gist"]  # Request
    provider: str  # Request
    title: str  # Request
    inputUrl: str  # Request (URI)
    display: EmbedDisplay  # Request
    width: str | int  # Request
    height: str | int  # Request

    # Response-only fields (legacy)
    html: str  # Response only (legacy)
    url: str  # Response only (legacy)


class EmbedVideoPayload(BasePayload):
    """Payload for EMBED_VIDEO block type."""

    # Request fields
    url: str  # Request (URI)
    provider: str  # Request


class EmbedAudioPayload(BasePayload):
    """Payload for EMBED_AUDIO block type."""

    # Request fields
    url: str  # Request (URI)
    provider: str  # Request


# Question Block Payloads


class QuestionPayload(BasePayload):
    """Payload for QUESTION block type."""

    # Request fields
    isRequired: bool  # Request

    # Response-only fields (legacy)
    html: str  # Response only (legacy)
    required: bool  # Response only (legacy)
    description: str  # Response only (legacy)
    hasDefaultAnswer: bool  # Response only (legacy)
    defaultAnswer: Any  # Response only (legacy)


class MatrixPayload(BasePayload):
    """Payload for MATRIX block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request

    # Response-only fields (legacy)
    html: str  # Response only (legacy)
    required: bool  # Response only (legacy)


class InputTextPayload(BasePayload):
    """Payload for INPUT_TEXT block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request
    hasMinCharacters: bool  # Request
    minCharacters: int  # Request
    hasMaxCharacters: bool  # Request
    maxCharacters: int  # Request

    # Response-only fields (legacy)
    minLength: int  # Response only (legacy)
    maxLength: int  # Response only (legacy)
    defaultValue: str  # Response only (legacy)


class InputNumberPayload(BasePayload):
    """Payload for INPUT_NUMBER block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request
    hasMinValue: bool  # Request
    minValue: float  # Request
    hasMaxValue: bool  # Request
    maxValue: float  # Request
    decimalSeparator: Literal["COMMA", "DOT"]  # Request
    thousandsSeparator: Literal["COMMA", "DOT", "SPACE", "NONE"]  # Request
    numberFormat: Literal["NUMBER", "CURRENCY", "PERCENTAGE"]  # Request
    currency: Literal["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "CNY", "INR"]  # Request

    # Response-only fields (legacy)
    min: float  # Response only (legacy)
    max: float  # Response only (legacy)
    defaultValue: float  # Response only (legacy)


class InputEmailPayload(BasePayload):
    """Payload for INPUT_EMAIL block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request

    # Response-only fields (legacy)
    defaultValue: str  # Response only (legacy)


class InputLinkPayload(BasePayload):
    """Payload for INPUT_LINK block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request

    # Response-only fields (legacy)
    defaultValue: str  # Response only (legacy)


class InputPhoneNumberPayload(BasePayload):
    """Payload for INPUT_PHONE_NUMBER block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request

    # Response-only fields (legacy)
    defaultValue: str  # Response only (legacy)


class InputDatePayload(BasePayload):
    """Payload for INPUT_DATE block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request
    disableDays: list[
        Literal[
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
            "PAST",
            "FUTURE",
            "TODAY",
        ]
    ]  # Request

    # Response-only fields (legacy)
    format: str  # Response only (legacy)
    defaultValue: str  # Response only (legacy)


class InputTimePayload(BasePayload):
    """Payload for INPUT_TIME block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request

    # Response-only fields (legacy)
    format: str  # Response only (legacy)
    defaultValue: str  # Response only (legacy)


class TextareaPayload(BasePayload):
    """Payload for TEXTAREA block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    placeholder: str  # Request
    hasMinCharacters: bool  # Request
    minCharacters: int  # Request
    hasMaxCharacters: bool  # Request
    maxCharacters: int  # Request

    # Response-only fields (legacy)
    minLength: int  # Response only (legacy)
    maxLength: int  # Response only (legacy)
    rows: int  # Response only (legacy)
    defaultValue: str  # Response only (legacy)


class AllowedFiles(TypedDict, total=False):
    """Allowed file types for FILE_UPLOAD (Request)."""

    images: bool
    documents: bool
    audio: bool
    video: bool
    other: bool


class FileUploadPayload(BasePayload):
    """Payload for FILE_UPLOAD block type."""

    # Request fields
    isRequired: bool  # Request
    allowedFiles: AllowedFiles  # Request
    hasMaxFileSize: bool  # Request
    maxFileSize: int  # Request
    hasMaxFiles: bool  # Request
    maxFiles: int  # Request

    # Response-only fields (legacy)
    accept: str  # Response only (legacy)
    maxSize: int  # Response only (legacy)
    multiple: bool  # Response only (legacy)


class LinearScalePayload(BasePayload):
    """Payload for LINEAR_SCALE block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    minValue: int  # Request
    maxValue: int  # Request
    minLabel: str  # Request
    maxLabel: str  # Request

    # Response-only fields (legacy)
    min: int  # Response only (legacy)
    max: int  # Response only (legacy)


class RatingPayload(BasePayload):
    """Payload for RATING block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    maxValue: int  # Request

    # Response-only fields (legacy)
    max: int  # Response only (legacy)
    icon: str  # Response only (legacy)


class HiddenField(TypedDict):
    """Hidden field definition (Request)."""

    uuid: str
    name: str


class HiddenFieldsPayload(BasePayload):
    """Payload for HIDDEN_FIELDS block type."""

    # Request fields
    fields: list[HiddenField]  # Request

    # Response-only fields (legacy - may appear as dict)
    # fields can also be dict[str, str] in responses


# Selection Block Payloads


class MultipleChoiceOptionPayload(BasePayload):
    """Payload for MULTIPLE_CHOICE_OPTION block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    index: int  # Request
    isFirst: bool  # Request
    isLast: bool  # Request
    colorCodeOptions: bool  # Request
    color: str  # Request
    hasBadge: bool  # Request
    badgeType: Literal["OFF", "NUMBERS", "LETTERS"]  # Request
    hasOtherOption: bool  # Request
    isOtherOption: bool  # Request
    image: str  # Request

    # Response-only fields
    text: str  # Response only
    label: str  # Response only


class CheckboxPayload(BasePayload):
    """Payload for CHECKBOX block type."""

    # Request fields
    label: str  # Request
    isRequired: bool  # Request
    defaultChecked: bool  # Request

    # Response-only fields
    index: int  # Response only
    isFirst: bool  # Response only
    isLast: bool  # Response only
    hasMaxChoices: bool  # Response only
    maxChoices: int  # Response only
    hasMinChoices: bool  # Response only
    minChoices: int  # Response only
    text: str  # Response only


class DropdownOptionPayload(BasePayload):
    """Payload for DROPDOWN_OPTION block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    index: int  # Request
    isFirst: bool  # Request
    isLast: bool  # Request

    # Response-only fields
    text: str  # Response only
    label: str  # Response only


class RankingOptionPayload(BasePayload):
    """Payload for RANKING_OPTION block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    index: int  # Request
    isFirst: bool  # Request
    isLast: bool  # Request

    # Response-only fields
    text: str  # Response only
    colorCodeOptions: bool  # Response only
    color: str  # Response only
    hasBadge: bool  # Response only
    badgeType: Literal["OFF", "NUMBERS", "LETTERS"]  # Response only
    hasOtherOption: bool  # Response only
    isOtherOption: bool  # Response only
    image: str  # Response only


class MultiSelectOptionPayload(BasePayload):
    """Payload for MULTI_SELECT_OPTION block type."""

    # Request fields
    isRequired: bool  # Request
    hasDefaultAnswer: bool  # Request
    defaultAnswer: Any  # Request
    index: int  # Request
    isFirst: bool  # Request
    isLast: bool  # Request
    colorCodeOptions: bool  # Request
    color: str  # Request
    hasBadge: bool  # Request
    badgeType: Literal["OFF", "NUMBERS", "LETTERS"]  # Request
    hasOtherOption: bool  # Request
    isOtherOption: bool  # Request
    image: str  # Request

    # Response-only fields
    text: str  # Response only
    label: str  # Response only


# Special Block Payloads


class PaymentPayload(BasePayload):
    """Payload for PAYMENT block type."""

    # Request fields
    isRequired: bool  # Request
    amount: float  # Request
    currency: Literal["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "CNY", "INR"]  # Request

    # Response-only fields (legacy)
    description: str  # Response only (legacy)


class SignaturePayload(BasePayload):
    """Payload for SIGNATURE block type."""

    # Request fields
    isRequired: bool  # Request


class MatrixRowPayload(BasePayload):
    """Payload for MATRIX_ROW block type."""

    # Request fields
    isRequired: bool  # Request
    index: int  # Request
    isFirst: bool  # Request
    isLast: bool  # Request

    # Response-only fields (legacy)
    label: str  # Response only (legacy)


class MatrixColumnPayload(BasePayload):
    """Payload for MATRIX_COLUMN block type."""

    # Request fields
    isRequired: bool  # Request
    index: int  # Request
    isFirst: bool  # Request
    isLast: bool  # Request

    # Response-only fields (legacy)
    label: str  # Response only (legacy)


class WalletConnectPayload(BasePayload):
    """Payload for WALLET_CONNECT block type."""

    # Request fields
    isRequired: bool  # Request

    # Response-only fields (legacy)
    chains: list[str]  # Response only (legacy)


class Conditional(TypedDict, total=False):
    """Conditional object for conditional logic (Request)."""

    uuid: str
    type: Literal["SINGLE", "GROUP"]
    payload: dict[str, Any]


class ConditionalAction(TypedDict, total=False):
    """Action object for conditional logic (Request)."""

    uuid: str
    type: Literal["SHOW_BLOCKS", "HIDE_BLOCKS", "SKIP_TO"]
    payload: dict[str, Any]


class ConditionalLogicPayload(BasePayload):
    """Payload for CONDITIONAL_LOGIC block type."""

    # Request fields
    conditionals: list[Conditional]  # Request
    actions: list[ConditionalAction]  # Request

    # Response-only fields
    updateUuid: str  # Response only
    logicalOperator: Literal["AND", "OR"]  # Response only


class CalculatedField(TypedDict):
    """Calculated field definition (Request)."""

    uuid: str
    name: str
    type: Literal["NUMBER", "TEXT"]
    value: Any


class CalculatedFieldsPayload(BasePayload):
    """Payload for CALCULATED_FIELDS block type."""

    # Request fields
    fields: list[CalculatedField]  # Request

    # Response-only fields (legacy)
    formula: str  # Response only (legacy)


class CaptchaPayload(BasePayload):
    """Payload for CAPTCHA block type."""

    # Request fields
    isRequired: bool  # Request

    # Response-only fields (legacy)
    provider: str  # Response only (legacy)


class RespondentCountryPayload(BasePayload):
    """Payload for RESPONDENT_COUNTRY block type."""

    # Request fields
    isRequired: bool  # Request


# Legacy/General Option Payload


class OptionPayload(BasePayload):
    """Generic payload for option-based block types.

    This is kept for backwards compatibility.
    Use specific payloads (MultipleChoiceOptionPayload, etc) for type safety.
    """

    label: str
    value: str
    text: str


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
    | MultipleChoiceOptionPayload
    | CheckboxPayload
    | DropdownOptionPayload
    | RankingOptionPayload
    | MultiSelectOptionPayload
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
    "AllowedFiles",
    "BasePayload",
    "BlockPayload",
    "ButtonSettings",
    "CalculatedField",
    "CalculatedFieldsPayload",
    "CaptchaPayload",
    "CheckboxPayload",
    "Conditional",
    "ConditionalAction",
    "ConditionalLogicPayload",
    "CoverSettings",
    "DividerPayload",
    "DropdownOptionPayload",
    "EmbedAudioPayload",
    "EmbedDisplay",
    "EmbedPayload",
    "EmbedVideoPayload",
    "FileUploadPayload",
    "FormTitlePayload",
    "Heading1Payload",
    "Heading2Payload",
    "Heading3Payload",
    "HiddenField",
    "HiddenFieldsPayload",
    "ImagePayload",
    "ImageSettings",
    "InputDatePayload",
    "InputEmailPayload",
    "InputLinkPayload",
    "InputNumberPayload",
    "InputPhoneNumberPayload",
    "InputTextPayload",
    "InputTimePayload",
    "LabelPayload",
    "LinearScalePayload",
    "MatrixColumnPayload",
    "MatrixPayload",
    "MatrixRowPayload",
    "Mention",
    "MentionField",
    "MultiSelectOptionPayload",
    "MultipleChoiceOptionPayload",
    "OptionPayload",
    "PageBreakPayload",
    "PaymentPayload",
    "QuestionPayload",
    "RankingOptionPayload",
    "RatingPayload",
    "RespondentCountryPayload",
    "SignaturePayload",
    "TextPayload",
    "TextareaPayload",
    "ThankYouPagePayload",
    "TitlePayload",
    "WalletConnectPayload",
]
