# FastAPI Flavor Template

This directory contains the FastAPI-specific structure for Project Horizon.

## Directory Structure

```
src/
├─ routers/        # API route handlers organized by feature
├─ models/         # Data models (SQLAlchemy, etc.)
├─ schemas/        # Pydantic schemas for validation
├─ services/       # Business logic and external services
└─ dependencies/   # FastAPI dependencies (auth, logging, etc.)
```

## Key Files

- `src/main.py` - Main application entry point
- `src/config.py` - Configuration settings
- `src/database.py` - Database connection and session

## Recommended Extensions

- SQLAlchemy for database ORM
- Alembic for database migrations
- Pydantic for data validation
- Python-jose for JWT authentication

## Example Usage

```python
# src/main.py
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="API description",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

## Error Handling

Standardized error handling approach for FastAPI applications:

```python
# src/exceptions.py
from fastapi import HTTPException, status

class BaseAPIException(HTTPException):
    """Base exception for all API errors."""
    def __init__(self, detail: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        super().__init__(status_code=status_code, detail=detail)

class NotFoundException(BaseAPIException):
    """Resource not found exception."""
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(detail=detail, status_code=status.HTTP_404_NOT_FOUND)

class BadRequestException(BaseAPIException):
    """Invalid request exception."""
    def __init__(self, detail: str = "Invalid request"):
        super().__init__(detail=detail, status_code=status.HTTP_400_BAD_REQUEST)

# Usage in routers:
# from src.exceptions import NotFoundException
# raise NotFoundException("User with id {user_id} not found")
```

## Troubleshooting Common Issues

### Application Startup Problems

- **Issue**: Import errors when starting the application
  - **Solution**: Check your Python path and ensure all dependencies are installed with `pip install -r requirements.txt`

- **Issue**: Port already in use
  - **Solution**: Change the port with `uvicorn src.main:app --port 8001`

- **Issue**: Environment variables not loading
  - **Solution**: Check that `.env` file exists and `python-dotenv` is configured properly in your settings

### Database and ORM Issues

- **Issue**: SQLAlchemy connection errors
  - **Solution**: Verify database URL in config and ensure database server is running

- **Issue**: Alembic migration errors
  - **Solution**: Check migration scripts for errors and ensure they're executed in the correct order

- **Issue**: SQLAlchemy "lazy loading" errors in async context
  - **Solution**: Use `selectinload()` or similar eager loading methods in async functions

### Schema Validation

- **Issue**: Pydantic validation errors with complex models
  - **Solution**: Use `Config` class in Pydantic models for custom validation or ensure data types match

- **Issue**: Validation errors not showing detailed information
  - **Solution**: Configure FastAPI to include validation error details:
    ```python
    app = FastAPI(
        title="My API",
        description="API description",
        version="0.1.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    ```

### Authentication Problems

- **Issue**: JWT token validation failing
  - **Solution**: Check token expiration, signing algorithm, and secret key configuration

- **Issue**: OAuth2 scopes not working properly
  - **Solution**: Verify scope definitions and usage in security dependencies

### Performance Issues

- **Issue**: Slow response times
  - **Solution**: Check for N+1 query problems, use profiling tools, consider adding caching

- **Issue**: Memory leaks
  - **Solution**: Check for improper resource cleanup, especially with database connections

### Debugging Tips

1. Use FastAPI's interactive docs for testing:
   - Visit `/docs` for Swagger UI
   - Visit `/redoc` for ReDoc

2. Enable debug logs in Uvicorn:
   ```bash
   uvicorn src.main:app --log-level debug
   ```

3. Use FastAPI's debug mode during development:
   ```python
   if __name__ == "__main__":
       import uvicorn
       uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
   ```

4. For detailed logging, configure logging in your app:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

5. Use FastAPI's dependency debugging:
   ```python
   from fastapi import Depends, FastAPI, Request
   
   async def log_request(request: Request):
       print(f"Request to {request.url}")
       return None
   
   @app.get("/items/{item_id}", dependencies=[Depends(log_request)])
   def read_item(item_id: int):
       return {"item_id": item_id}
   ```

## Running the Application

```bash
uvicorn src.main:app --reload
```

*Made with pride by Bryte Idea – 2025* 