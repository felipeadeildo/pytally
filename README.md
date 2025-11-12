# pytally-sdk

[![PyPI version](https://badge.fury.io/py/pytally-sdk.svg)](https://badge.fury.io/py/pytally-sdk)
[![Python Versions](https://img.shields.io/pypi/pyversions/pytally-sdk.svg)](https://pypi.org/project/pytally-sdk/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Unofficial Python SDK for the [Tally.so](https://tally.so) API.

> **Early Development**: This SDK is currently in early development and does not yet cover the entire Tally API. We're actively working on adding more endpoints and features.

## Installation

Install the package using pip:

```bash
pip install pytally-sdk
```

Or using [uv](https://github.com/astral-sh/uv):

```bash
uv add pytally-sdk
```

## Quick Start

```python
from tally import Tally

# Initialize the client with your API key
client = Tally(api_key="tly-your-api-key-here")

# Get current user information
user = client.users.me()
print(f"Hello, {user.full_name}!")
print(f"Email: {user.email}")
print(f"Plan: {user.subscription_plan.value}")
```

### With Context Manager

```python
from tally import Tally

with Tally(api_key="tly-your-api-key-here") as client:
    user = client.users.me()
    print(f"Organization ID: {user.organization_id}")
```

## Features

### Currently Implemented

- **Authentication**: Bearer token authentication with API versioning support
- **Users Resource**:
  - `client.users.me()` - Get current authenticated user information
- **Error Handling**: Comprehensive exception handling for all HTTP error codes
- **Type Safety**: Full type hints support for better IDE experience
- **Context Manager**: Automatic resource cleanup

### Coming Soon

- **Forms Resource**: List, retrieve, and manage forms
- **Submissions Resource**: Access and filter form submissions
- **Webhooks Resource**: Manage webhooks and events
- **Organizations Resource**: Manage organization users and invites
- **Workspaces Resource**: List and manage workspaces

## API Versioning

The Tally API uses date-based versioning. You can specify a specific API version when initializing the client:

```python
from tally import Tally

client = Tally(
    api_key="tly-your-api-key-here",
    api_version="2025-02-01"  # Optional: specify API version
)
```

If not specified, the client will use the version tied to your API key.

## Error Handling

The SDK provides specific exceptions for different API errors:

```python
from tally import Tally, UnauthorizedError, RateLimitError, TallyAPIError

client = Tally(api_key="tly-your-api-key-here")

try:
    user = client.users.me()
except UnauthorizedError:
    print("Invalid API key!")
except RateLimitError:
    print("Rate limit exceeded. Please wait before retrying.")
except TallyAPIError as e:
    print(f"API error: {e.message} (status code: {e.status_code})")
```

## Configuration

The client accepts the following configuration options:

```python
from tally import Tally

client = Tally(
    api_key="tly-your-api-key-here",       # Required: Your Tally API key
    api_version="2025-02-01",              # Optional: API version
    timeout=30.0,                           # Optional: Request timeout in seconds
    base_url="https://api.tally.so"        # Optional: Custom base URL
)
```

## Getting Your API Key

1. Go to [Tally Settings > API Keys](https://tally.so/settings/api-keys)
2. Click "Create API key"
3. Copy and store your API key securely

> **Security Note**: Never commit your API key to version control. Use environment variables or a secure secrets manager.

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repository
git clone https://github.com/felipeadeildo/pytally.git

# Install dependencies
uv sync

# Run tests (coming soon)
uv run pytest
```

## Contributing

Contributions are welcome! This SDK is in early development, and we'd love your help to:

- Add missing API endpoints
- Improve documentation
- Report bugs
- Suggest new features

Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This is an unofficial SDK and is not affiliated with or endorsed by Tally. Tally and the Tally logo are trademarks of Tally B.V.

## Links

- [PyPI Package](https://pypi.org/project/pytally-sdk/)
- [GitHub Repository](https://github.com/felipeadeildo/pytally)
- [Tally API Documentation](https://tally.so/help/api)
- [Issue Tracker](https://github.com/felipeadeildo/pytally/issues)

---

Made with ❤️ by [Felipe Adeildo](https://github.com/felipeadeildo)
