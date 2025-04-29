# tests Directory

This directory contains all test files for the project. Tests ensure functionality works as expected and prevent regressions when code changes.

## Directory Structure
Tests should mirror the structure of the `src/` directory:

```
tests/
├─ conftest.py              # Shared pytest fixtures
├─ test_config.py           # Configuration tests
├─ blueprints/              # For Flask
│  ├─ test_auth.py
│  ├─ test_users.py
├─ routers/                 # For FastAPI
│  ├─ test_items_api.py
├─ models/
│  ├─ test_user.py
│  ├─ test_item.py
├─ services/
│  ├─ test_email_service.py
├─ utils/
│  ├─ test_validators.py
└─ integration/             # Integration tests
   ├─ test_user_workflow.py
```

## Example Test

```python
# tests/models/test_user.py
import pytest
from src.models.user import User

def test_user_creation():
    """Test that a user can be created with valid attributes."""
    user = User(username="testuser", email="test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert not user.is_admin  # Default value

def test_user_validation():
    """Test that user validation works correctly."""
    with pytest.raises(ValueError):
        User(username="", email="invalid")  # Should raise validation error
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest tests/models/test_user.py

# Run tests matching a pattern
pytest -k "user"
```

## Writing Good Tests
1. Each function should have at least one test
2. Test both valid and invalid inputs
3. Use descriptive test names (test_what_happens_when_condition)
4. Use fixtures for repeated setup code
5. Keep tests independent

Made with love by Bryte Idea
