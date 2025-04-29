# Project Horizon – Dependency Management Strategy 📦

> 🤖 *Beep boop! Managing dependencies like a pro!*

Purpose: Define a consistent approach to managing dependencies across all Project Horizon flavors while ensuring reproducibility, security, and maintainability.

## Core Principles 🔑

1. **Explicit Over Implicit**: All dependencies are explicitly versioned
2. **Separation of Concerns**: Dev, test, and production dependencies are kept separate
3. **Security First**: Regular vulnerability scanning and updates
4. **Minimalism**: Only include what's needed, avoid bloat
5. **Compatibility**: Ensure dependencies work together without conflicts

## Dependency Structure 📋

```
manhattan-project/
├─ requirements.txt            # Core production dependencies
├─ requirements-dev.txt        # Development dependencies
├─ requirements-test.txt       # Testing dependencies
└─ flavor-specific/            # Flavor-specific requirements
   ├─ requirements-flask.txt   # Flask-specific dependencies
   ├─ requirements-fastapi.txt # FastAPI-specific dependencies
   ├─ requirements-django.txt  # Django-specific dependencies
   └─ requirements-cli.txt     # CLI-specific dependencies
```

## Version Pinning Strategy 📌

All dependencies must follow these version pinning rules:

1. **Direct Dependencies**: Pin to exact versions (`package==1.2.3`)
2. **Transitive Dependencies**: Auto-generate with `pip-compile` or similar tools
3. **Security Exceptions**: When urgent security fixes are needed, allow for compatible updates (`package>=1.2.3,<2.0.0`)

## Core Requirements Files 📄

### requirements.txt (Production)

```
# Core utility packages
python-dotenv==1.0.0
pyyaml==6.0.1
requests==2.31.0
structlog==23.1.0

# Date/time handling
pytz==2023.3
python-dateutil==2.8.2

# Database
sqlalchemy==2.0.19

# Security
cryptography==41.0.3
pyjwt==2.8.0
```

### requirements-dev.txt (Development)

```
-r requirements.txt
black==23.7.0
flake8==6.1.0
isort==5.12.0
pre-commit==3.3.3
mypy==1.5.1
pip-tools==7.3.0
```

### requirements-test.txt (Testing)

```
-r requirements.txt
pytest==7.4.0
pytest-cov==4.1.0
pytest-mock==3.11.1
factory-boy==3.3.0
freezegun==1.2.2
```

## Flavor-Specific Dependencies 🧩

### requirements-flask.txt

```
-r requirements.txt
flask==2.3.3
flask-sqlalchemy==3.0.5
flask-migrate==4.0.4
flask-wtf==1.1.1
flask-login==0.6.2
gunicorn==21.2.0
```

### requirements-fastapi.txt

```
-r requirements.txt
fastapi==0.101.1
pydantic==2.1.1
pydantic-settings==2.0.3
uvicorn==0.23.2
alembic==1.11.3
```

### requirements-django.txt

```
-r requirements.txt
django==4.2.4
djangorestframework==3.14.0
django-environ==0.10.0
django-filter==23.2
django-cors-headers==4.2.0
```

### requirements-cli.txt

```
-r requirements.txt
click==8.1.6
typer==0.9.0
rich==13.5.2
tabulate==0.9.0
```

## Dependency Management Workflow 🔄

### Adding New Dependencies

1. Evaluate the dependency for:
   - Security history
   - Maintenance status
   - License compatibility
   - Size and performance impact

2. Add to appropriate requirements file:
   ```bash
   # Add to requirements.txt for a production dependency
   echo "new-package==1.0.0" >> requirements.txt
   
   # Add to appropriate flavor-specific file for framework dependencies
   echo "new-flask-extension==2.0.0" >> flavor-specific/requirements-flask.txt
   ```

3. Regenerate locked dependencies:
   ```bash
   pip-compile requirements.txt > requirements.lock
   ```

4. Test compatibility with existing packages:
   ```bash
   pip install -r requirements.lock
   pytest
   ```

### Updating Dependencies

1. Schedule regular dependency reviews (monthly):
   ```bash
   # Check for outdated packages
   pip list --outdated
   ```

2. Update strategy:
   - **Security updates**: Immediate
   - **Bug fixes**: Monthly
   - **Feature updates**: Quarterly
   - **Major version upgrades**: Scheduled with testing

3. Update process:
   ```bash
   # Update specific package
   sed -i 's/package==1.0.0/package==1.0.1/' requirements.txt
   
   # Regenerate locked files
   pip-compile requirements.txt > requirements.lock
   
   # Test changes
   pip install -r requirements.lock
   pytest
   ```

## Security Scanning 🔒

Integrate with security scanners in CI/CD pipeline:

```yaml
# In .github/workflows/security-scan.yml
name: Security Scan

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly
  push:
    paths:
      - '**/requirements*.txt'

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install safety
        run: pip install safety
      - name: Run safety check
        run: safety check -r requirements.txt
```

## Virtual Environment Strategy 🌐

1. **Local Development**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate environment
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   
   # Install dependencies based on flavor
   pip install -r requirements-dev.txt -r flavor-specific/requirements-flask.txt
   ```

2. **CI/CD Environments**:
   - Use containerized environments with exact dependencies
   - Utilize pip's cache for faster builds

3. **Production**:
   - Deploy with locked dependencies
   - Include hash verification for security

## Handling Conflicts and Compatibility 🔧

1. **Dependency Resolution**:
   - Use `pip-compile` to resolve conflicts
   - Document known conflicts in a COMPATIBILITY.md file

2. **Framework Compatibility Matrix**:
   - Maintain a matrix of tested framework versions
   - Document breaking changes between major versions

## Example Dependency Usage Template 📝

```python
# Example of explicitly importing and using dependencies
# src/utils/config.py

import os
from typing import Dict, Any

import yaml
from dotenv import load_dotenv


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from YAML file.
    
    Args:
        config_path: Path to YAML configuration file
        
    Returns:
        Dictionary containing configuration
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Load YAML config
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Override with environment variables if they exist
    for key in config:
        env_value = os.getenv(f"APP_{key.upper()}")
        if env_value is not None:
            config[key] = env_value
            
    return config
```

## Dependency Documentation 📚

Each project should include a `DEPENDENCIES.md` file with:

1. List of key dependencies and their purpose
2. Any custom forks or patches
3. Upgrade notes and breaking changes
4. License information

*Made with pride by Bryte Idea – 2025* 🤖 