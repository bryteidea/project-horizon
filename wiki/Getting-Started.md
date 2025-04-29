# Getting Started with Project Horizon 🚀

Welcome to Project Horizon! This guide will help you set up your development environment and understand the basics of working with this framework.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10 or higher
- pip (Python package manager)
- Git
- A code editor (VS Code recommended)
- Docker (optional, for containerized development)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/bryte-idea/manhattan-project.git
   cd manhattan-project
   ```

2. **Set up a virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the project**

   ```bash
   python scripts/init_project.py
   ```

## Project Structure

Project Horizon follows a standardized directory structure. For a detailed explanation, see the [Project Structure](Project-Structure.md) documentation.

```
manhattan-project/
├── adhoc/               # One-off scripts
├── config/              # Configuration files
├── docs/                # Documentation
├── migrations/          # Database migrations
├── scripts/             # Utility scripts
├── src/                 # Main source code
├── templates/           # Template files for new projects
│   └── flavors/         # Framework-specific templates
│       ├── flask/       # Flask template
│       ├── fastapi/     # FastAPI template
│       ├── django/      # Django template
│       └── cli/         # CLI application template
├── tests/               # Test suite
└── tickets/             # Ticket templates and examples
```

## Choosing a Flavor

Project Horizon supports multiple frameworks or "flavors":

1. **Flask**: Lightweight web framework
2. **FastAPI**: Modern, high-performance API framework
3. **Django**: Full-featured web framework
4. **CLI**: Command-line interface applications

To create a new project with your chosen flavor:

```bash
python scripts/create_project.py --name my_project --flavor flask
```

## Basic Usage

### Starting a Development Server

For web applications (Flask, FastAPI, Django):

```bash
# Flask
cd my_project
python src/app.py

# FastAPI
cd my_project
uvicorn src.app:app --reload

# Django
cd my_project
python src/manage.py runserver
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific module
pytest tests/test_user_service.py

# Run tests with coverage report
pytest --cov=src
```

## Development Workflow

1. **Create or pick up a ticket**
   - Use the ticket template in the `tickets/` directory
   - Assign yourself to the ticket in your project management system

2. **Create a feature branch**
   - Branch naming: `feature/PH-XXX-short-description`
   - Example: `feature/PH-123-user-authentication`

3. **Implement the feature**
   - Follow the [Naming Conventions](Naming-Conventions.md)
   - Write tests for your code

4. **Run tests locally**
   - Ensure all tests pass before submitting your changes

5. **Submit a pull request**
   - Include the ticket number in the PR title
   - Fill out the PR template
   - Request code reviews from team members

## Common Tasks

### Creating a New Adhoc Script

Adhoc scripts should be created in the `adhoc/` directory and follow the naming convention: `PH-XXX_descriptive_name.py`

```bash
# Create a new adhoc script
python scripts/create_adhoc.py --ticket PH-123 --name import_legacy_data
```

### Database Migrations

For projects with databases:

```bash
# Flask/FastAPI with SQLAlchemy
alembic revision --autogenerate -m "Create user table"
alembic upgrade head

# Django
python src/manage.py makemigrations
python src/manage.py migrate
```

### Working with Configuration

Configuration files are stored in the `config/` directory. The base configuration is loaded from `config/base.py` or `config/base.yaml`, with environment-specific overrides.

```python
# Accessing configuration in your code
from src.config import config

database_url = config.get("DATABASE_URL")
debug_mode = config.get("DEBUG_MODE")
```

## Troubleshooting

### Common Issues

1. **Virtual environment issues**
   
   If you see `command not found` errors, ensure your virtual environment is activated.

2. **Import errors**
   
   Ensure you're running the application from the correct directory. The project root should be in your Python path.

3. **Configuration errors**
   
   Check that your environment variables or configuration files are properly set up.

### Getting Help

If you encounter problems:

1. Check the [wiki](https://github.com/bryte-idea/manhattan-project/wiki) for documentation
2. Look at the [issue tracker](https://github.com/bryte-idea/manhattan-project/issues) for known issues
3. Ask for help in the team's communication channel

## Next Steps

- Read the [Project Structure](Project-Structure.md) documentation
- Learn about [Naming Conventions](Naming-Conventions.md)
- Review the [Contribution Guidelines](Contribution-Guidelines.md)
- Explore the example applications in the `templates/flavors/` directory

---

*Made with pride by Bryte Idea – 2025*
