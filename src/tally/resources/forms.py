"""Forms resource for the Tally API."""

from typing import TYPE_CHECKING, Iterator

from tally.models.form import Form, PaginatedForms

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
