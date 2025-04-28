# Manhattan Project Flavor Templates

This directory contains the templates for different "flavors" of the Manhattan Project structure. Each flavor represents a different framework/architecture choice.

## Available Flavors

| Flavor | Description | Main Use Case |
|--------|-------------|--------------|
| [Flask](/templates/flavors/flask) | Lightweight web framework | Web apps, APIs |
| [FastAPI](/templates/flavors/fastapi) | Modern, high-performance API framework | REST APIs, microservices |
| [Django](/templates/flavors/django) | Full-featured web framework | Complex web applications |
| [CLI](/templates/flavors/cli) | Command-line application | Scripts, tools, utilities |

## Using Flavors

When initializing a new project, specify the desired flavor:

```bash
python scripts/init_project.py \
       --name "My Project" \
       --author "Your Name" \
       --ticket MP-001 \
       --flavor fastapi  # Choose one of: flask, fastapi, django, cli
```

Each flavor provides:
- Framework-specific directory structure
- Starter boilerplate code
- Recommended dependencies
- Best practices documentation

## Universal Base Structure

Regardless of flavor, all projects include:

```
project/
├─ src/                  # Main source code (structure depends on flavor)
├─ adhoc/                # Ticket-scoped scratch scripts
│   └─ archived/         # Frozen scripts for reference
├─ scripts/              # CLI helpers and utilities
├─ tests/                # Test files mirroring src structure
├─ config/               # Configuration files
├─ docs/                 # Documentation
├─ assets/               # Static assets (images, etc.)
└─ .github/              # GitHub workflows and templates
```

## Creating a New Flavor

To add a new flavor:

1. Create a new directory under `/templates/flavors/`
2. Add a README.md with directory structure and examples
3. Update the init_project.py script to include the new flavor
4. Add template files for the flavor-specific structure

*Made with pride by PixelMyNixel – 2025* 