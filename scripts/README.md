# scripts Directory

This directory contains reusable command-line scripts that support the project's development, deployment, and maintenance. Unlike `adhoc/` scripts, these are permanent, well-tested utilities.

## Purpose
Scripts in this directory should:
- Be well-documented with docstrings and help text
- Include proper error handling
- Work across environments (dev, staging, prod)
- Have clear command-line interfaces

## Examples
- `init_project.py` - Project initialization script
- `seed_db.py` - Database seeding for development/testing
- `deploy.py` - Deployment automation
- `generate_api_docs.py` - API documentation generator
- `backup_data.py` - Database backup utility

## Example Usage

```bash
# Initialize a new project
python scripts/init_project.py --name "My Project" --author "Team Name" --ticket MP-001 --flavor flask

# Seed the database with test data
python scripts/seed_db.py --environment dev --count 100

# Generate API documentation
python scripts/generate_api_docs.py --output docs/api/
```

## Adding New Scripts
1. Follow the naming convention: `verb_noun.py`
2. Include a docstring that explains purpose, usage, and parameters
3. Add proper argument parsing (use argparse)
4. Add the script to this README

Made with love by Bryte Idea
