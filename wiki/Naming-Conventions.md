# Naming Conventions 📝

This document outlines the standard naming conventions used throughout the Project Horizon. Following these conventions ensures consistency, improves code readability, and facilitates collaboration.

## General Principles

- **Be descriptive**: Names should clearly indicate purpose
- **Be consistent**: Follow the same patterns throughout the codebase
- **Use standard conventions**: Follow language-specific conventions
- **Avoid abbreviations**: Unless they are widely understood
- **Keep it concise**: Balance descriptiveness with brevity

## Python Naming Conventions

### Modules and Packages

- Use lowercase words separated by underscores
- Names should be short, descriptive nouns
- Avoid generic names like "utils" without context

```python
# Good
from src.auth.permissions import check_user_access
from src.data.converters import xml_to_json

# Avoid
from src.utilities.helpers import process
```

### Classes

- Use CapWords (PascalCase) convention
- Names should be singular nouns
- Make names descriptive of what the class represents

```python
# Good
class UserProfile:
    pass

class DatabaseConnection:
    pass

# Avoid
class Data:  # Too vague
    pass
```

### Functions and Methods

- Use lowercase words separated by underscores (snake_case)
- Verb phrases that describe the action
- Be specific about what the function does

```python
# Good
def calculate_total_price(items):
    pass

def validate_user_input(form_data):
    pass

# Avoid
def process(data):  # Too vague
    pass
```

### Variables

- Use lowercase words separated by underscores (snake_case)
- Choose descriptive names that indicate purpose and content
- Use plural forms for collections (lists, dictionaries, etc.)

```python
# Good
user_id = 42
active_users = ["alice", "bob", "charlie"]
configuration_settings = {"debug": True, "timeout": 30}

# Avoid
x = 42  # Meaningless
u = get_user()  # Too abbreviated
```

### Constants

- Use uppercase letters with underscores
- Place constants at the module level

```python
# Good
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com/v1"

# Avoid
timeout = 30  # Should be uppercase for constants
```

### Type Aliases and TypedDict

- Use CapWords (PascalCase) convention similar to class names
- End with "Type" for type aliases

```python
from typing import List, Dict, TypedDict, NewType

# Good
UserId = NewType('UserId', int)
ConnectionOptions = Dict[str, str]
UserDataType = List[Dict[str, any]]

class UserDict(TypedDict):
    id: int
    name: str
    active: bool
```

## File Naming

### Python Files

- Use lowercase with underscores
- Names should reflect the primary class or function
- Test files should be prefixed with `test_`

```
# Good
user_profile.py
database_connection.py
test_user_profile.py

# Avoid
UserProfile.py  # Not lowercase
dbconn.py  # Too abbreviated
```

### Template Files

- Use lowercase with underscores or hyphens (based on template engine conventions)
- Group templates in directories by feature/function

```
templates/
  user/
    profile.html
    settings.html
  admin/
    dashboard.html
```

### Static Files

- Use lowercase with hyphens
- Include purpose in filename
- Include version or hash in production assets if needed

```
static/
  css/
    main-styles.css
    user-profile.css
  js/
    app.js
    user-module.js
  images/
    logo.png
    hero-banner.jpg
```

### Ad-hoc Scripts

- Prefix with ticket number
- Use lowercase with underscores
- Include descriptive purpose

```
adhoc/
  PH-123_migrate_user_data.py
  PH-145_cleanup_invalid_records.py
```

## Database Naming

### Tables

- Use plural snake_case names
- Prefix with application name for shared databases

```sql
-- Good
CREATE TABLE users (...);
CREATE TABLE order_items (...);
CREATE TABLE mp_settings (...);  -- With prefix

-- Avoid
CREATE TABLE user (...);  -- Should be plural
CREATE TABLE orderItem (...);  -- Should be snake_case
```

### Columns

- Use snake_case
- Include `id` suffix for foreign keys
- Include `_at` suffix for timestamps

```sql
-- Good
id                  -- Primary key
user_id             -- Foreign key
first_name          -- Regular column
created_at          -- Timestamp
is_active           -- Boolean

-- Avoid
userID              -- Should be snake_case
created             -- Ambiguous, use created_at
active              -- Ambiguous, use is_active
```

### Indexes

- Format: `idx_[table]_[column(s)]`
- For multi-column indexes, include all column names

```sql
-- Good
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id_created_at ON orders(user_id, created_at);

-- Avoid
CREATE INDEX email_index ON users(email);  -- Does not follow convention
```

### Constraints

- Primary keys: `pk_[table]`
- Foreign keys: `fk_[table]_[referenced_table]`
- Unique constraints: `uq_[table]_[column(s)]`

```sql
-- Good
ALTER TABLE users ADD CONSTRAINT pk_users PRIMARY KEY (id);
ALTER TABLE orders ADD CONSTRAINT fk_orders_users FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE users ADD CONSTRAINT uq_users_email UNIQUE (email);
```

## API Naming

### Endpoints

- Use plural nouns for resources
- Use kebab-case for paths
- Follow RESTful conventions
- Version APIs using URL paths

```
# Good
GET /api/v1/users
POST /api/v1/users
GET /api/v1/users/{id}
PUT /api/v1/users/{id}
PATCH /api/v1/users/{id}
DELETE /api/v1/users/{id}

GET /api/v1/order-items?order_id=123

# Avoid
GET /api/v1/getUsers  # Use nouns, not verbs
GET /api/v1/user/1  # Use plural nouns
GET /api/v1/userProfile  # Use kebab-case
```

### Query Parameters

- Use snake_case for parameter names
- Make names descriptive and consistent

```
# Good
GET /api/v1/users?status=active&sort_by=created_at&order=desc

# Avoid
GET /api/v1/users?userStatus=active  # Not snake_case
GET /api/v1/users?s=active&sb=created_at  # Too abbreviated
```

## Git Conventions

### Branches

- Format: `[type]/[ticket-number]-[short-description]`
- Types: `feature`, `bugfix`, `hotfix`, `release`, `refactor`
- Use hyphens to separate words in the description

```
# Good
feature/PH-123-user-authentication
bugfix/PH-456-fix-login-validation
hotfix/PH-789-security-vulnerability
release/v1.2.0
refactor/PH-321-improve-performance

# Avoid
feature_ph_123  # Missing description
PH-123  # Missing type and description
feature/add-stuff  # Missing ticket number
```

### Commit Messages

- Format: `[Ticket] Short summary`
- First line should be concise (50 chars or less)
- Follow with a blank line and detailed description if needed
- Use present tense, imperative mood

```
# Good
[PH-123] Add user authentication system

Implement OAuth2 integration with Google and GitHub.
Add database models for storing user tokens.
Update configuration to include OAuth settings.

# Avoid
fixed stuff  # Too vague, missing ticket reference
[PH-123] Fixed a bug where users couldn't login because the authentication service was rejecting valid credentials due to an issue with token validation  # Too long
```

### Tags

- Use semantic versioning
- Format: `v[major].[minor].[patch]`

```
# Good
v1.0.0
v1.2.3
v2.0.0-beta.1

# Avoid
version1
release-1.0
1.0
```

## Configuration Keys

- Use lowercase with underscores
- Group related settings with prefixes
- Make keys descriptive

```python
# Good
DATABASE_URL = "postgresql://user:pass@localhost/db"
JWT_SECRET_KEY = "secret"
JWT_ACCESS_TOKEN_EXPIRES = 3600

# Avoid
DB = "postgresql://user:pass@localhost/db"  # Too abbreviated
jwtSecretKey = "secret"  # Not snake_case
```

## Directory Naming

- Use lowercase with underscores
- Be descriptive and consistent
- Follow framework conventions where applicable

```
# Good
src/
  models/
  services/
  api/
  utils/

# Avoid
src/
  Models/  # Not lowercase
  svc/  # Too abbreviated
  APIEndpoints/  # Not lowercase with underscores
```

## Documentation

### Code Comments and Docstrings

- Start with a capital letter
- End with a period
- Docstrings should follow Google, NumPy, or reST format consistently

```python
def calculate_total_price(items, tax_rate=0.0):
    """Calculate the total price including tax.

    Args:
        items: A list of dictionaries with 'price' and 'quantity'.
        tax_rate: The tax rate as a decimal. Defaults to 0.0.

    Returns:
        The total price as a float.
    
    Raises:
        ValueError: If tax_rate is negative.
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")
    
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    return subtotal * (1 + tax_rate)
```

### Wiki Pages

- Use title case for page names
- Be descriptive and specific
- Use hyphens to separate words

```
# Good
Getting-Started.md
Naming-Conventions.md
API-Documentation.md

# Avoid
getting started.md  # Not using hyphens
gettingstarted.md  # Words not separated
docs.md  # Too vague
```

## Enforcing Conventions

Project Horizon provides tools to help enforce naming conventions:

- Linting tools (flake8, pylint) with custom rules
- Pre-commit hooks to check naming conventions
- Code review templates that include naming convention checks
- Documentation generators that verify consistent naming

## Exceptions to Conventions

While consistency is important, there are legitimate reasons to deviate from these conventions:

- Compatibility with external libraries and frameworks
- Maintaining consistency with existing code during incremental refactoring
- Following language-specific idioms that conflict with these guidelines

When making exceptions, document the reason for the deviation in comments or documentation.

---

*Made with pride by Bryte Idea – 2025*
