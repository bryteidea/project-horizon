# Project Horizon – Flavor Migration Guide 🔄

> 🤖 *Beep boop! Framework change detected! Initializing migration sequence...*

Purpose: Provide structured guidance for migrating a Project Horizon from one framework flavor to another, preserving as much business logic and domain models as possible.

## Migration Paths Overview 🛣️

| From | To | Complexity | Recommended For |
|------|----|-----------:|-----------------|
| Flask | FastAPI | ⭐⭐☆☆☆ | Transitioning to async APIs |
| Flask | Django | ⭐⭐⭐☆☆ | Scaling to full-featured web apps |
| FastAPI | Flask | ⭐⭐☆☆☆ | Simpler WSGI deployment |
| FastAPI | Django | ⭐⭐⭐⭐☆ | Adding admin interfaces and ORM |
| Django | Flask | ⭐⭐⭐⭐☆ | Reducing complexity for simple apps |
| Django | FastAPI | ⭐⭐⭐☆☆ | Performance and async needs |
| Any | CLI | ⭐⭐☆☆☆ | Creating command-line utilities |

## Core Components for Preservation 📦

Regardless of migration path, these components typically require minimal changes:

- Business logic in `services/` directories
- Database models (with adapter changes)
- Helper utilities
- Configuration management
- Test fixtures and test data

## Migration Process 🔄

### 1. Setup New Project Structure

```bash
# Create a new branch
git checkout -b flavor-migration-to-[new-flavor]

# Initialize the new structure
python scripts/init_project.py --name "Your Project" --author "Your Name" --ticket MP-XXX --flavor [new-flavor]

# This will create a new directory with the target flavor structure
```

### 2. Migrate Core Components

1. **Data Models**
   - Copy and adapt models from src/models/ to the new flavor's model format
   - Adjust imports and framework-specific decorators

2. **Business Logic Services**
   - Move service classes with minimal changes
   - Update dependency imports and injection patterns

3. **Configuration**
   - Adapt config loading to the new framework pattern
   - Preserve environment variable names and semantics

4. **Utilities**
   - Copy utility functions directly
   - Update imports for framework-specific dependencies

### 3. Framework-Specific Components

#### Flask to FastAPI Migration

```python
# Flask Route:
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_by_id(user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

# FastAPI Equivalent:
@app.get('/users/{user_id}', response_model=UserSchema)
def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

#### FastAPI to Django Migration

```python
# FastAPI endpoint:
@app.get('/users/{user_id}', response_model=UserSchema)
def get_user(user_id: int):
    user = get_user_service().get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Django View equivalent:
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .services import get_user_service

class UserDetailView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        return JsonResponse(user.to_dict())

# urls.py
path('users/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
```

#### Django to Flask Migration

```python
# Django View:
class UserDetailView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        return JsonResponse(user.to_dict())

# Flask equivalent:
@app.route('/users/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())
```

### 4. Authentication Migration

| From | To | Migration Approach |
|------|----|--------------------|
| Flask-Login | FastAPI OAuth | Use JWT tokens with FastAPI security features |
| Django Auth | Flask-Login | Map Django User model to Flask-Login's UserMixin |
| FastAPI Auth | Django Auth | Convert JWT token auth to Django's session auth |

### 5. Template and Frontend Migration

| From | To | Migration Approach |
|------|----|--------------------|
| Jinja2 (Flask) | Django Templates | Convert template syntax and template tags |
| Django Templates | Jinja2 (Flask) | Simplify template tags and custom filters |
| Any | API-only (FastAPI) | Convert to SPA with separate frontend |

### 6. Database Migration Strategy

1. **Create schema migration scripts**
   - Use SQLAlchemy, Alembic, or Django migrations
   - Verify data integrity with sample migrations

2. **Data validation tests**
   - Run validation scripts to ensure data consistency

## Framework-Specific Migration Checklists ✅

### Flask to FastAPI

- [ ] Convert Flask routes to FastAPI path operations
- [ ] Replace Flask request.form/args with FastAPI Pydantic models
- [ ] Convert Flask error handling to FastAPI exception handling
- [ ] Replace Werkzeug security utilities with FastAPI/Pydantic ones
- [ ] Update dependencies from Flask extensions to FastAPI equivalents
- [ ] Update tests to use TestClient instead of Flask test_client

### FastAPI to Django

- [ ] Convert Pydantic models to Django models and serializers
- [ ] Move endpoints to Django class-based views or viewsets
- [ ] Set up Django URL patterns
- [ ] Adapt FastAPI dependency injection to Django middleware or view methods
- [ ] Convert async routes to Django async views or sync views
- [ ] Update authentication from FastAPI security to Django auth

### Django to Flask

- [ ] Simplify Django models to SQLAlchemy models
- [ ] Convert Django views to Flask routes
- [ ] Move validation from Django Forms to Flask-WTF or custom validation
- [ ] Replace Django ORM queries with SQLAlchemy equivalents
- [ ] Update middleware to Flask before/after request handlers
- [ ] Migrate Django admin features to Flask-Admin if needed

## Testing the Migration 🧪

1. **Unit Tests**
   - Update imports and mocks to reflect new framework
   - Run tests frequently during migration

2. **Integration Testing**
   - Create comparison tests for API responses between old and new implementations
   - Test data flows and persistence

3. **Migration Verification Utility**
   ```python
   # compare_responses.py - sample verification script
   import requests
   
   def compare_endpoints(old_base_url, new_base_url, endpoints):
       results = []
       for endpoint in endpoints:
           old_resp = requests.get(f"{old_base_url}{endpoint}")
           new_resp = requests.get(f"{new_base_url}{endpoint}")
           
           match = old_resp.json() == new_resp.json()
           results.append((endpoint, match, old_resp.status_code, new_resp.status_code))
       
       return results
   ```

## Common Challenges and Solutions 🔍

| Challenge | Solution |
|-----------|----------|
| Authentication differences | Create auth adapters between frameworks |
| ORM query translation | Use a repository pattern to isolate database access |
| Template engine differences | Consider a frontend/backend split for complex UIs |
| Middleware/extension handling | Focus on core functionality first, then add middleware |
| Performance differences | Benchmark critical paths in both implementations |

## Rollback Planning 🛠️

Always maintain the ability to roll back to the previous implementation:

1. Keep both implementations deployed in parallel during transition
2. Create a feature flag system to route traffic between implementations
3. Maintain database compatibility during the transition period
4. Document detailed rollback procedures

*Made with pride by Bryte Idea – 2025* 🤖 