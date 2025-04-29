# Project Horizon – Testing Strategy Guide 🧪

> 🤖 *Beep boop! I'm your friendly robot guide to testing!*

Purpose: Establish a consistent approach to testing across all Project Horizon flavors (Flask, FastAPI, Django, CLI).

## Testing Philosophy 🔍

Our testing approach follows a layered pyramid structure:

1. **Unit Tests** (base): Test individual functions, classes, and components in isolation.
2. **Integration Tests** (middle): Test interactions between components and external dependencies.
3. **End-to-End Tests** (top): Test complete workflows from user perspective.

## Project Test Structure 📁

```
project-horizon/
├─ tests/
│   ├─ unit/                # Mirror src/ structure for unit tests
│   │   ├─ models/
│   │   ├─ services/
│   │   └─ utils/
│   ├─ integration/         # Tests involving multiple components
│   │   ├─ api/             # API integration tests
│   │   └─ db/              # Database integration tests
│   ├─ e2e/                 # End-to-end workflow tests
│   ├─ fixtures/            # Shared test fixtures and factories
│   │   ├─ factories.py     # Factory Boy factories
│   │   └─ data/            # Test data files (JSON, CSV, etc.)
│   ├─ conftest.py          # Pytest configuration and fixtures
│   └─ settings.py          # Test-specific settings
└─ .coveragerc              # Coverage configuration
```

## Testing Tools & Libraries 🛠️

**Core Testing Tools (All Flavors)**
- **pytest**: Primary test runner
- **pytest-cov**: Test coverage reporting
- **factory-boy**: Test data factories
- **freezegun**: Time freezing for tests
- **pytest-mock**: Mocking and patching

**Framework-Specific Testing Tools**
- **Flask**: pytest-flask, Flask Testing
- **FastAPI**: TestClient, pytest-asyncio
- **Django**: pytest-django, django.test.Client
- **CLI**: Click testing, pytest-console-scripts

## Testing Best Practices ✅

1. **Test Naming**
   - Use descriptive naming: `test_function_does_something_when_condition`
   - Group related tests in classes: `TestUserRegistration`, `TestAuthFlow`

2. **Test Isolation**
   - Each test should be independent (no state sharing between tests)
   - Use fixtures for common setup/teardown
   - Clean up any test data or mocks after each test

3. **Test Coverage**
   - Aim for 80%+ code coverage overall
   - 100% coverage for critical paths
   - Coverage reports generated during CI pipeline

4. **Mocking & Fixtures**
   - Mock external dependencies (APIs, services)
   - Use fixtures for database access
   - Create factory classes for test data generation

5. **Testing Edge Cases**
   - Test happy paths AND failure scenarios
   - Include boundary testing for inputs
   - Test validation and error handling

## Example Test Structure (by Flavor)

### Flask Test Example

```python
# tests/unit/test_user_service.py
import pytest
from src.services.user import UserService
from src.models.user import User
from tests.fixtures.factories import UserFactory

class TestUserService:
    def test_get_user_by_id_returns_user_when_exists(self, db_session):
        # Arrange
        user = UserFactory.create()
        db_session.commit()
        
        # Act
        service = UserService(db_session)
        result = service.get_by_id(user.id)
        
        # Assert
        assert result is not None
        assert result.id == user.id
        
    def test_get_user_by_id_returns_none_when_not_exists(self, db_session):
        # Arrange
        service = UserService(db_session)
        
        # Act
        result = service.get_by_id(999)
        
        # Assert
        assert result is None
```

### FastAPI Test Example

```python
# tests/integration/api/test_user_endpoints.py
from fastapi.testclient import TestClient
import pytest
from src.main import app
from tests.fixtures.factories import UserFactory

client = TestClient(app)

def test_get_user_returns_200_when_user_exists(db_session):
    # Arrange
    user = UserFactory.create()
    db_session.commit()
    
    # Act
    response = client.get(f"/users/{user.id}")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == user.id
    
def test_get_user_returns_404_when_user_not_found():
    # Act
    response = client.get("/users/999")
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
```

### Django Test Example

```python
# tests/integration/test_user_views.py
import pytest
from django.urls import reverse
from tests.fixtures.factories import UserFactory

@pytest.mark.django_db
class TestUserViews:
    def test_user_detail_view_returns_200_for_existing_user(self, client):
        # Arrange
        user = UserFactory.create()
        
        # Act
        url = reverse('user-detail', kwargs={'pk': user.id})
        response = client.get(url)
        
        # Assert
        assert response.status_code == 200
        assert response.context['user'].id == user.id
        
    def test_user_detail_view_returns_404_for_nonexistent_user(self, client):
        # Act
        url = reverse('user-detail', kwargs={'pk': 999})
        response = client.get(url)
        
        # Assert
        assert response.status_code == 404
```

### CLI Test Example

```python
# tests/unit/test_cli_commands.py
from click.testing import CliRunner
import pytest
from src.main import cli

def test_hello_command_outputs_greeting():
    # Arrange
    runner = CliRunner()
    
    # Act
    result = runner.invoke(cli, ['hello', '--name', 'Tester'])
    
    # Assert
    assert result.exit_code == 0
    assert 'Hello, Tester!' in result.output
    
def test_process_command_fails_with_nonexistent_file():
    # Arrange
    runner = CliRunner()
    
    # Act
    result = runner.invoke(cli, ['process', 'nonexistent.txt'])
    
    # Assert
    assert result.exit_code == 2
    assert 'File nonexistent.txt not found' in result.output
```

## Test Running & CI Integration 🔄

### Local Test Running

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src

# Run specific test directories or files
pytest tests/unit/
pytest tests/integration/api/

# Run tests matching a pattern
pytest -k "user or auth"
```

### CI Pipeline Integration

The CI pipeline runs tests and coverage on every pull request:

1. **Unit tests** run on all PRs
2. **Integration tests** run on PRs to staging and main
3. **E2E tests** run on PRs to main only

Failed tests block PR merging. Coverage reports are posted as PR comments.

## Test-Driven Development (TDD) 🔄

For new features or bug fixes:

1. Write failing test describing expected behavior
2. Implement minimum code to make the test pass
3. Refactor code while keeping tests passing
4. Repeat for each feature/fix

## Mock Strategy 🎭

- Unit tests: Heavily mock external dependencies
- Integration tests: Selective mocking (use test databases)
- E2E tests: Minimize mocking, use realistic test environments

*Made with pride by Bryte Idea – 2025* 🤖 