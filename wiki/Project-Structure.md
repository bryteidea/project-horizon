# Project Horizon Structure 📂

This document provides a detailed explanation of the Project Horizon directory structure and organizational principles.

## Overview

Project Horizon uses a standardized directory structure designed to:

- Promote consistency across different projects
- Facilitate easy navigation and discovery
- Support multiple framework flavors (Flask, FastAPI, Django, CLI)
- Provide clear separation of concerns
- Enable efficient development workflows

## Root Directory Structure

```
project-horizon/
├── adhoc/               # One-off scripts and data migration tools
├── config/              # Configuration files and settings
├── docs/                # Documentation and guides
├── logs/                # Log files (gitignored)
├── migrations/          # Database migrations
├── scripts/             # Utility scripts for development and deployment
├── src/                 # Main application source code
├── templates/           # Template files for new projects
│   └── flavors/         # Framework-specific templates
│       ├── flask/       # Flask template
│       ├── fastapi/     # FastAPI template
│       ├── django/      # Django template
│       └── cli/         # CLI application template
├── tests/               # Test suite
├── tickets/             # Ticket templates and examples
├── wiki/                # Wiki documentation
├── .gitignore           # Git ignore file
├── CHANGELOG.md         # Version changelog
├── LICENSE              # Project license
├── README.md            # Project readme
├── SECURITY.md          # Security policy
└── VERSION              # Current version number
```

## Directory Purposes

### `/adhoc`

Contains one-off scripts, data migrations, or ad-hoc utilities that are not part of the main application. Each script should:

- Reference a ticket number in its filename (e.g., `MP-123_import_legacy_data.py`)
- Include a comment header explaining its purpose
- Be self-contained or use relative imports from the main codebase

### `/config`

Stores configuration files for different environments:

```
config/
├── base.py              # Base configuration shared across all environments
├── development.py       # Development-specific configuration
├── production.py        # Production-specific configuration
├── testing.py           # Testing-specific configuration
└── local.py             # Local overrides (gitignored)
```

Configuration can also be in YAML format depending on project preferences.

### `/docs`

Contains project documentation, including:

- Architecture diagrams
- API specifications
- Database schemas
- User guides
- Development guides
- Boilerplate templates

### `/logs`

Directory for application logs (typically gitignored).

### `/migrations`

Database migration files:

- For SQLAlchemy projects: Alembic migrations
- For Django projects: Django migrations
- Each migration should include a descriptive name and timestamp

### `/scripts`

Utility scripts for development, deployment, and maintenance:

```
scripts/
├── create_project.py    # Creates a new project from a template
├── create_adhoc.py      # Creates a new adhoc script with proper template
├── deploy.py            # Deployment automation
├── lint.py              # Runs linting tools
└── init_db.py           # Initializes the database
```

### `/src`

Main application source code. Structure varies by framework flavor:

#### Flask/FastAPI Structure

```
src/
├── api/                 # API routes and controllers
├── models/              # Data models and database entities
├── services/            # Business logic and services
├── utils/               # Utility functions and helpers
├── app.py               # Application entry point
└── config.py            # Configuration loading code
```

#### Django Structure

```
src/
├── manage.py            # Django management script
├── project/             # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
└── apps/                # Django applications
    ├── app1/            # Individual app
    │   ├── models.py    # App models
    │   ├── views.py     # App views
    │   └── urls.py      # App URLs
    └── app2/            # Another app
```

#### CLI Structure

```
src/
├── commands/            # CLI commands
├── lib/                 # Library code
├── utils/               # Utility functions
└── main.py              # Entry point
```

### `/templates`

Template files for creating new projects with different framework flavors:

```
templates/
└── flavors/
    ├── flask/          # Flask template
    │   ├── README.md   # Flask-specific documentation
    │   └── src/        # Flask template source code
    ├── fastapi/        # FastAPI template
    ├── django/         # Django template
    └── cli/            # CLI template
```

Each flavor directory contains a complete project template that can be copied and customized.

### `/tests`

Test suite for the application:

```
tests/
├── unit/               # Unit tests
│   ├── test_models.py  # Tests for models
│   └── test_services.py # Tests for services
├── integration/        # Integration tests
├── functional/         # Functional tests
└── conftest.py         # pytest configuration
```

### `/tickets`

Contains a template for creating tickets and example tickets:

```
tickets/
├── TEMPLATE.md         # Ticket template
├── MP-001_example.md   # Example ticket
└── MP-002_example.md   # Another example ticket
```

### `/wiki`

Wiki documentation that can be synced with GitHub Wiki:

```
wiki/
├── Home.md             # Wiki home page
├── Getting-Started.md  # Getting started guide
├── Project-Structure.md # This document
├── Naming-Conventions.md # Naming conventions
└── _Sidebar.md         # Wiki sidebar navigation
```

## Framework Flavors

Project Horizon supports multiple framework flavors, each with its own structure and conventions:

### Flask Flavor

- Lightweight web framework
- Good for small to medium applications
- Flexible architecture
- Easy to extend

### FastAPI Flavor

- Modern, high-performance API framework
- Built-in OpenAPI documentation
- Asynchronous request handling
- Type hinting and validation

### Django Flavor

- Full-featured web framework
- Built-in admin interface
- ORM for database interactions
- Many built-in features

### CLI Flavor

- Command-line interface applications
- Argument parsing and validation
- Command structure and help text
- Distribution as executable tools

## Development Workflow

1. **Project Initialization**
   - Choose a framework flavor
   - Initialize project structure
   - Set up configuration

2. **Feature Development**
   - Create a ticket describing the feature
   - Create a feature branch
   - Implement the feature in the appropriate directory
   - Write tests

3. **Ad-hoc Scripts**
   - Create scripts for one-off tasks in the `/adhoc` directory
   - Reference ticket numbers in filenames
   - Document purpose and usage

4. **Testing**
   - Write tests in the `/tests` directory
   - Run tests with pytest
   - Ensure proper test coverage

5. **Documentation**
   - Update documentation in `/docs` and `/wiki`
   - Keep README and CHANGELOG up to date
   - Document APIs and features

## Best Practices

- **Keep it DRY**: Don't repeat yourself across different parts of the codebase
- **Follow the structure**: Place files in the appropriate directories
- **Respect naming conventions**: Follow the naming guidelines
- **Document extensively**: Add docstrings and comments to explain code
- **Write tests**: Maintain comprehensive test coverage
- **Reference tickets**: Link code changes to ticket numbers

## Adding New Directories

When adding new directories to the project:

1. Ensure the new directory serves a clear purpose
2. Update this document to include the new directory
3. Create a README.md file in the new directory explaining its purpose
4. Update any templates to include the new directory if appropriate

---

*Made with pride by Bryte Idea – 2025*
