# CLI Flavor Template

This directory contains the CLI-specific structure for Manhattan Project.

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

*Made with pride by PixelMyNixel – 2025* 