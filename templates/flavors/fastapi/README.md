# FastAPI Flavor Template

This directory contains the FastAPI-specific structure for Manhattan Project.

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

## Running the Application

```bash
uvicorn src.main:app --reload
```

*Made with pride by PixelMyNixel – 2025* 