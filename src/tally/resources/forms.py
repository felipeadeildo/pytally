"""Forms resource for the Tally API."""

from typing import TYPE_CHECKING, Any, Iterator

from tally.models.form import (
    Form,
    FormBlock,
    FormCreated,
    FormDetails,
    FormSettings,
    FormStatus,
    PaginatedForms,
    PaginatedSubmissions,
    Question,
    SubmissionFilter,
    SubmissionWithQuestions,
)

if TYPE_CHECKING:
    from tally.client import TallyClient


class FormsResource:
    """Resource for managing Tally forms."""

    def __init__(self, client: "TallyClient") -> None:
        """Initialize the Forms resource.

        Args:
            client: The TallyClient instance
        """
        self._client = client

    def all(
        self,
        page: int = 1,
        limit: int = 50,
        workspace_ids: list[str] | None = None,
    ) -> PaginatedForms:
        """Get all forms with pagination.

        Returns a paginated list of form objects.

        Args:
            page: Page number for pagination (default: 1, min: 1)
            limit: Number of forms per page (default: 50, max: 500)
            workspace_ids: Filter forms by specific workspace IDs (optional)

        Returns:
            PaginatedForms object containing forms and pagination info

        Example:
            ```python
            from tally import Tally

            client = Tally(api_key="tly-xxxx")

            # Get first page
            result = client.forms.all()
            print(f"Page {result.page} of {result.total} forms")

            for form in result.items:
                print(f"Form: {form.name}")
                print(f"  Status: {form.status.value}")
                print(f"  Submissions: {form.number_of_submissions}")
                print(f"  Closed: {form.is_closed}")

            # Get next page with custom limit
            if result.has_more:
                next_page = client.forms.all(page=2, limit=100)

            # Filter by workspace IDs
            workspace_forms = client.forms.all(workspace_ids=["ws_123", "ws_456"])
            ```
        """
        params: dict[str, str | int | list[str]] = {"page": page, "limit": limit}

        if workspace_ids is not None:
            params["workspaceIds"] = workspace_ids

        data = self._client.request("GET", "/forms", params=params)
        return PaginatedForms.from_dict(data)

    def get(self, form_id: str) -> FormDetails:
        """Get a single form by ID with all its blocks and settings.

        Returns the complete form structure including all blocks, settings,
        and configuration details.

        Args:
            form_id: The ID of the form to retrieve

        Returns:
            FormDetails object containing the complete form with blocks and settings

        Raises:
            NotFoundError: If the form doesn't exist or you don't have access
            UnauthorizedError: If authentication credentials are invalid

        Example:
            ```python
            from tally import Tally

            client = Tally(api_key="tly-xxxx")

            # Get a form by ID
            form = client.forms.get("form_abc123")

            print(f"Form: {form.name}")
            print(f"Status: {form.status.value}")
            print(f"Workspace: {form.workspace_id}")
            print(f"Submissions: {form.number_of_submissions}")
            print(f"Is Closed: {form.is_closed}")

            # Access settings
            print(f"Language: {form.settings.language}")
            print(f"Has Progress Bar: {form.settings.has_progress_bar}")
            print(f"Save for Later: {form.settings.save_for_later}")

            # Access blocks
            print(f"Total blocks: {len(form.blocks)}")
            for block in form.blocks:
                print(f"  Block {block.uuid}: {block.type}")
                print(f"    Group: {block.group_type}")
                if block.payload:
                    print(f"    Payload: {block.payload}")

            # Access payments if configured
            if form.payments:
                for payment in form.payments:
                    print(f"Payment: {payment.amount} {payment.currency}")
            ```
        """
        data = self._client.request("GET", f"/forms/{form_id}")
        return FormDetails.from_dict(data)

    def create(
        self,
        status: FormStatus | str,
        blocks: list[FormBlock] | list[dict[str, Any]],
        workspace_id: str | None = None,
        template_id: str | None = None,
        settings: FormSettings | dict[str, Any] | None = None,
    ) -> FormCreated:
        """Create a new form.

        Creates a new form, optionally based on a template or within a specific workspace.

        Args:
            status: Initial status of the form (BLANK, DRAFT, PUBLISHED, DELETED)
            blocks: Array of form block objects defining the form structure
            workspace_id: ID of the workspace to create the form in (optional)
            template_id: ID of the template to base the form on (optional)
            settings: Form settings configuration (optional)

        Returns:
            FormCreated object with the created form details

        Raises:
            BadRequestError: If the request parameters are invalid

        Example:
            ```python
            from tally import Tally
            from tally.models import FormStatus, FormBlock, BlockType, FormSettings

            client = Tally(api_key="tly-xxxx")

            # Create a simple form with type-safe objects
            blocks = [
                FormBlock(
                    uuid="3c90c3cc-0d44-4b50-8888-8dd25736052a",
                    type=BlockType.FORM_TITLE,
                    group_uuid="3c90c3cc-0d44-4b50-8888-8dd25736052a",
                    group_type=BlockType.FORM_TITLE,
                    payload={"html": "<h1>My Form</h1>"}
                )
            ]

            settings = FormSettings(
                is_closed=False,
                save_for_later=True,
                has_progress_bar=True
            )

            form = client.forms.create(
                status=FormStatus.DRAFT,
                blocks=blocks,
                workspace_id="ws_123",
                settings=settings
            )

            print(f"Created form: {form.id}")
            print(f"Status: {form.status.value}")

            # Or use simple dicts for flexibility
            form = client.forms.create(
                status="DRAFT",
                blocks=[{
                    "uuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                    "type": "FORM_TITLE",
                    "groupUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                    "groupType": "FORM_TITLE",
                    "payload": {"html": "<h1>My Form</h1>"}
                }],
                settings={
                    "isClosed": False,
                    "saveForLater": True
                }
            )
            ```
        """
        body: dict[str, Any] = {
            "status": status.value if isinstance(status, FormStatus) else status,
            "blocks": [
                block.to_dict() if isinstance(block, FormBlock) else block
                for block in blocks
            ],
        }

        if workspace_id is not None:
            body["workspaceId"] = workspace_id

        if template_id is not None:
            body["templateId"] = template_id

        if settings is not None:
            body["settings"] = (
                settings.to_dict() if isinstance(settings, FormSettings) else settings
            )

        data = self._client.request("POST", "/forms", json=body)
        return FormCreated.from_dict(data)

    def update(
        self,
        form_id: str,
        name: str | None = None,
        status: FormStatus | str | None = None,
        blocks: list[FormBlock] | list[dict[str, Any]] | None = None,
        settings: FormSettings | dict[str, Any] | None = None,
    ) -> Form:
        """Update an existing form.

        Updates one or more properties of an existing form. All parameters except
        form_id are optional - only provide the fields you want to update.

        Args:
            form_id: The ID of the form to update
            name: New name for the form (optional)
            status: New status for the form (BLANK, DRAFT, PUBLISHED, DELETED) (optional)
            blocks: Updated array of form blocks (optional)
            settings: Updated form settings (optional)

        Returns:
            Form object with the updated form details

        Example:
            ```python
            from tally import Tally
            from tally.models import FormStatus, FormSettings

            client = Tally(api_key="tly-xxxx")

            # Update form name only
            form = client.forms.update(
                form_id="form_abc123",
                name="Updated Form Name"
            )

            # Update status to published
            form = client.forms.update(
                form_id="form_abc123",
                status=FormStatus.PUBLISHED
            )

            # Update multiple fields at once
            form = client.forms.update(
                form_id="form_abc123",
                name="New Name",
                status="PUBLISHED",
                settings=FormSettings(
                    is_closed=True,
                    close_message_title="Form Closed",
                    close_message_description="Thank you for your interest"
                )
            )

            # Update with dict for flexibility
            form = client.forms.update(
                form_id="form_abc123",
                settings={
                    "isClosed": False,
                    "hasProgressBar": True,
                    "saveForLater": True
                }
            )
            ```
        """
        body: dict[str, Any] = {}

        if name is not None:
            body["name"] = name

        if status is not None:
            body["status"] = status.value if isinstance(status, FormStatus) else status

        if blocks is not None:
            body["blocks"] = [
                block.to_dict() if isinstance(block, FormBlock) else block
                for block in blocks
            ]

        if settings is not None:
            body["settings"] = (
                settings.to_dict() if isinstance(settings, FormSettings) else settings
            )

        data = self._client.request("PATCH", f"/forms/{form_id}", json=body)
        return Form.from_dict(data)

    def delete(self, form_id: str) -> None:
        """Delete a form by its ID.

        Deletes a form and moves it to the trash. This operation is reversible
        from the Tally web interface.

        Args:
            form_id: The ID of the form to delete

        Example:
            ```python
            from tally import Tally

            client = Tally(api_key="tly-xxxx")

            client.forms.delete("form_abc123")
            ```
        """
        self._client.request("DELETE", f"/forms/{form_id}")

    def list_questions(self, form_id: str) -> list[Question]:
        """Get all questions in a form.

        Returns a list of all questions in a form, including their fields,
        response counts, and metadata.

        Args:
            form_id: The ID of the form

        Returns:
            List of Question objects

        Example:
            ```python
            from tally import Tally

            client = Tally(api_key="tly-xxxx")

            # Get all questions in a form
            questions = client.forms.list_questions("form_abc123")

            for question in questions:
                print(f"Question: {question.title}")
                print(f"  Type: {question.type}")
                print(f"  ID: {question.id}")
                print(f"  Responses: {question.number_of_responses}")

                # Access question fields
                print(f"  Fields ({len(question.fields)}):")
                for field in question.fields:
                    print(f"    - {field.title} ({field.type})")
                    print(f"      UUID: {field.uuid}")
                    print(f"      Has responses: {field.has_responses}")
            ```
        """
        data = self._client.request("GET", f"/forms/{form_id}/questions")
        return [Question.from_dict(q) for q in data.get("questions", [])]

    def list_submissions(
        self,
        form_id: str,
        page: int = 1,
        filter: SubmissionFilter | str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        after_id: str | None = None,
    ) -> PaginatedSubmissions:
        """Get form submissions with pagination and filtering.

        Returns a paginated list of submissions for a specific form, including
        all questions and responses. Supports filtering by completion status,
        date range, and cursor-based pagination.

        Args:
            form_id: The ID of the form
            page: Page number for pagination (default: 1)
            filter: Filter by completion status ("all", "completed", "partial")
            start_date: Filter submissions on or after this date (ISO 8601 format)
            end_date: Filter submissions on or before this date (ISO 8601 format)
            after_id: Get submissions that came after a specific submission ID

        Returns:
            PaginatedSubmissions object containing submissions, questions, and pagination info

        Example:
            ```python
            from tally import Tally
            from tally.models import SubmissionFilter

            client = Tally(api_key="tly-xxxx")

            # Get first page of all submissions
            result = client.forms.list_submissions("form_abc123")

            print(f"Page {result.page}, Has more: {result.has_more}")
            print(f"Total: {result.total_number_of_submissions_per_filter.all}")
            print(f"Completed: {result.total_number_of_submissions_per_filter.completed}")
            print(f"Partial: {result.total_number_of_submissions_per_filter.partial}")

            # Access questions
            for question in result.questions:
                print(f"Question: {question.title} ({question.type})")

            # Access submissions
            for submission in result.submissions:
                print(f"Submission {submission.id}:")
                print(f"  Completed: {submission.is_completed}")
                print(f"  Submitted at: {submission.submitted_at}")

                # Access responses
                for response in submission.responses:
                    print(f"    Question {response.question_id}: {response.value}")

            # Filter by completion status
            completed = client.forms.list_submissions(
                "form_abc123",
                filter=SubmissionFilter.COMPLETED
            )

            # Filter by date range
            recent = client.forms.list_submissions(
                "form_abc123",
                start_date="2024-01-01T00:00:00Z",
                end_date="2024-12-31T23:59:59Z"
            )

            # Cursor-based pagination
            next_batch = client.forms.list_submissions(
                "form_abc123",
                after_id=result.submissions[-1].id
            )
            ```
        """
        params: dict[str, str | int] = {"page": page}

        if filter is not None:
            params["filter"] = (
                filter.value if isinstance(filter, SubmissionFilter) else filter
            )

        if start_date is not None:
            params["startDate"] = start_date

        if end_date is not None:
            params["endDate"] = end_date

        if after_id is not None:
            params["afterId"] = after_id

        data = self._client.request(
            "GET", f"/forms/{form_id}/submissions", params=params
        )
        return PaginatedSubmissions.from_dict(data)

    def get_submission(
        self, form_id: str, submission_id: str
    ) -> SubmissionWithQuestions:
        """Get a specific submission by ID with all its responses and questions.

        Returns the complete submission details including all responses and
        the associated form questions.

        Args:
            form_id: The ID of the form
            submission_id: The ID of the submission to retrieve

        Returns:
            SubmissionWithQuestions object containing the submission and all form questions

        Raises:
            NotFoundError: If the form or submission doesn't exist or you don't have access
            UnauthorizedError: If authentication credentials are invalid

        Example:
            ```python
            from tally import Tally

            client = Tally(api_key="tly-xxxx")

            result = client.forms.get_submission(
                form_id="form_abc123",
                submission_id="sub_xyz789"
            )

            submission = result.submission
            print(f"Submission ID: {submission.id}")
            print(f"Form ID: {submission.form_id}")
            print(f"Completed: {submission.is_completed}")
            print(f"Submitted at: {submission.submitted_at}")

            # Access questions
            print(f"\nQuestions ({len(result.questions)}):")
            for question in result.questions:
                print(f"  - {question.title} ({question.type})")

            # Access responses
            print(f"\nResponses ({len(submission.responses)}):")
            for response in submission.responses:
                # Find the corresponding question
                question = next(
                    (q for q in result.questions if q.id == response.question_id),
                    None
                )
                if question:
                    print(f"  {question.title}: {response.value}")
                else:
                    print(f"  Question {response.question_id}: {response.value}")
            ```
        """
        data = self._client.request(
            "GET", f"/forms/{form_id}/submissions/{submission_id}"
        )
        return SubmissionWithQuestions.from_dict(data)

    def delete_submission(self, form_id: str, submission_id: str) -> None:
        """Delete a specific submission by ID.

        Permanently removes a submission from a form. This operation cannot be undone.

        Args:
            form_id: The ID of the form
            submission_id: The ID of the submission to delete

        Example:
            ```python
            from tally import Tally

            client = Tally(api_key="tly-xxxx")

            client.forms.delete_submission(
                form_id="form_abc123",
                submission_id="sub_xyz789"
            )
            ```
        """
        self._client.request("DELETE", f"/forms/{form_id}/submissions/{submission_id}")

    def __iter__(self) -> Iterator[Form]:
        """Iterate through all forms across all pages.

        Automatically fetches all pages and yields each form.

        Yields:
            Form objects one at a time

        Example:
            ```python
            from tally import Tally

            client = Tally(api_key="tly-xxxx")

            # Iterate through all forms automatically
            for form in client.forms:
                print(f"Form: {form.name}")
                print(f"  Status: {form.status.value}")
                print(f"  Submissions: {form.number_of_submissions}")
            ```
        """
        page = 1
        while True:
            result = self.all(page=page)

            for form in result.items:
                yield form

            if not result.has_more:
                break

            page += 1
