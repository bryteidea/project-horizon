# Flask Flavor Template

This directory contains the Flask-specific structure for Project Horizon.

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

## Error Handling

Standardized error handling approach for Flask applications:

```python
# src/errors.py
from flask import jsonify

class APIError(Exception):
    """Base class for API exceptions."""
    status_code = 500
    
    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status_code
        return rv

class NotFoundError(APIError):
    """Resource not found error."""
    status_code = 404

class ValidationError(APIError):
    """Input validation error."""
    status_code = 400

# In app.py:
@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Usage in blueprints:
# from src.errors import NotFoundError
# raise NotFoundError(f"User with id {user_id} not found")
```

## Troubleshooting Common Issues

### Application Not Starting

- **Issue**: Import errors when running the application
  - **Solution**: Check your Python path and ensure all dependencies are installed with `pip install -r requirements.txt`

- **Issue**: Port already in use
  - **Solution**: Change the port in `app.run(port=5001)` or kill the process using the default port

- **Issue**: Environment variables not loading
  - **Solution**: Ensure `.env` file exists in root directory and `python-dotenv` is installed

### Database Connectivity

- **Issue**: SQLAlchemy "unable to connect to database" error
  - **Solution**: Verify database URL in config, check that database server is running, and database exists

- **Issue**: "No such table" errors
  - **Solution**: Run migrations with `flask db upgrade` or make sure models are registered before creating tables

### Template Rendering

- **Issue**: "Template not found" errors
  - **Solution**: Check template folder structure and ensure Flask can find your templates (use `template_folder` parameter)

- **Issue**: Variables not available in templates
  - **Solution**: Verify that you're passing all required variables to `render_template()`

### Authentication Problems

- **Issue**: Login not persisting between requests
  - **Solution**: Configure session properly, ensure secret key is set and Flask-Login is set up correctly

- **Issue**: CSRF protection failing
  - **Solution**: Include CSRF token in forms and ensure `WTF_CSRF_ENABLED` is True

### Performance Issues

- **Issue**: Slow response times
  - **Solution**: Use Flask debug toolbar to identify bottlenecks, consider caching with Flask-Caching

- **Issue**: Memory usage growing over time
  - **Solution**: Look for resource leaks, improper session cleanup, or connection pooling issues

### Debugging Tips

1. Use Flask's debug mode during development:
   ```python
   app.run(debug=True)
   ```

2. For detailed logging, configure logging in your app:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

3. For complex applications, use Flask debug toolbar:
   ```python
   from flask_debugtoolbar import DebugToolbarExtension
   toolbar = DebugToolbarExtension(app)
   ```

4. Check application error logs:
   ```bash
   tail -f logs/application.log
   ```

## Running the Application

```bash
python src/app.py
```

*Made with pride by Bryte Idea – 2025* 