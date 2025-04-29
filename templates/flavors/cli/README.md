# CLI Flavor Template

This directory contains the CLI-specific structure for Project Horizon.

## Directory Structure

```
src/
├─ commands/        # Command handlers organized by feature
├─ utils/           # Helper functions and utilities 
└─ config/          # Configuration and settings
```

## Key Files

- `src/main.py` - Main application entry point
- `src/config.py` - Configuration settings
- `src/commands/__init__.py` - Command registry

## Recommended Extensions

- Click for command-line interfaces
- Rich for terminal formatting
- PyYAML for configuration files
- Typer for typed CLI apps

## Example Usage

```python
# src/main.py
import click

@click.group()
def cli():
    """Command line utility."""
    pass

@cli.command()
@click.option('--name', default='World', help='Who to greet')
def hello(name):
    """Simple command that greets NAME."""
    click.echo(f'Hello, {name}!')

@cli.command()
@click.argument('src', type=click.Path(exists=True))
@click.argument('dst', type=click.Path())
def copy(src, dst):
    """Copy SRC to DST."""
    click.echo(f'Copying {src} to {dst}')

if __name__ == '__main__':
    cli()
```

## Error Handling

Standardized error handling approach for CLI applications:

```python
# src/exceptions.py
import sys
import click

class CLIException(Exception):
    """Base exception for CLI errors."""
    exit_code = 1
    
    def __init__(self, message, exit_code=None):
        self.message = message
        if exit_code is not None:
            self.exit_code = exit_code
    
    def __str__(self):
        return self.message

class FileNotFoundException(CLIException):
    """File not found exception."""
    exit_code = 2

class ValidationException(CLIException):
    """Input validation exception."""
    exit_code = 3

class ConfigurationException(CLIException):
    """Configuration error exception."""
    exit_code = 4

# In main.py:
def handle_exceptions(func):
    """Decorator to handle exceptions in CLI commands."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CLIException as e:
            click.secho(f"Error: {e}", fg="red")
            sys.exit(e.exit_code)
        except Exception as e:
            click.secho(f"Unexpected error: {e}", fg="red")
            sys.exit(1)
    return wrapper

# Usage in commands:
# from src.exceptions import FileNotFoundException
# @cli.command()
# @click.argument('filename')
# @handle_exceptions
# def process(filename):
#     if not os.path.exists(filename):
#         raise FileNotFoundException(f"File {filename} not found")
#     # process file...
```

## Running the Application

```bash
python src/main.py hello --name Friend
python src/main.py copy data.txt backup.txt
```

## Packaging as a CLI Tool

To make your CLI installable via pip:

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="mycli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        mycli=src.main:cli
    """,
)
```

*Made with pride by Bryte Idea – 2025* 