# Flask Flavor Template

This directory contains the Flask-specific structure for Manhattan Project.

## Directory Structure

```
src/
├─ blueprints/        # Route handlers/views organized by feature
├─ models/            # Data models (SQLAlchemy, Pydantic, etc.)
├─ services/          # Business logic and external services
├─ utils/             # Helper functions and utilities
├─ templates/         # Jinja2 templates
└─ static/            # CSS, JS, images
```

## Key Files

- `src/app.py` - Main application entry point
- `src/config.py` - Configuration settings
- `src/extensions.py` - Flask extensions initialization

## Recommended Extensions

- Flask-SQLAlchemy for database ORM
- Flask-Migrate for database migrations
- Flask-WTF for forms
- Flask-Login for authentication

## Example Usage

```python
# src/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

## Running the Application

```bash
python src/app.py
```

*Made with pride by PixelMyNixel – 2025* 