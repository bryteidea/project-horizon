# Django Flavor Template

This directory contains the Django-specific structure for Project Horizon.

## Directory Structure

```
src/
├─ apps/                # Django applications
│  ├─ app1/
│  │  ├─ migrations/
│  │  ├─ templates/
│  │  ├─ models.py
│  │  ├─ views.py
│  │  ├─ urls.py
│  │  └─ ...
│  └─ app2/
├─ templates/           # Global templates
├─ static/              # CSS, JS, images
└─ media/               # User-uploaded content
```

## Key Files

- `src/manage.py` - Django CLI utility
- `src/project/settings.py` - Django settings
- `src/project/urls.py` - Root URL configuration

## Recommended Extensions

- Django REST framework for APIs
- Django Allauth for authentication
- Celery for background tasks
- Django Debug Toolbar for development

## Example Usage

```python
# src/apps/api/views.py
from django.http import JsonResponse
from django.views import View

class HelloWorldView(View):
    def get(self, request):
        return JsonResponse({"message": "Hello, World!"})
```

```python
# src/apps/api/urls.py
from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]
```

## Error Handling

Standardized error handling approach for Django applications:

```python
# src/project/exceptions.py
from django.http import JsonResponse
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.exceptions import APIException

class BaseAPIException(APIException):
    """Base class for API exceptions."""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('A server error occurred.')
    
    def __init__(self, detail=None, status_code=None):
        self.detail = detail or self.default_detail
        if status_code is not None:
            self.status_code = status_code

class ResourceNotFoundException(BaseAPIException):
    """Resource not found exception."""
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('Resource not found.')

class ValidationException(BaseAPIException):
    """Validation exception."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Invalid input data.')

# In settings.py:
# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'src.project.exception_handlers.custom_exception_handler',
# }

# src/project/exception_handlers.py
def custom_exception_handler(exc, context):
    """Custom exception handler for REST framework."""
    if isinstance(exc, BaseAPIException):
        return JsonResponse({
            'error': True,
            'message': str(exc.detail),
            'status_code': exc.status_code
        }, status=exc.status_code)
    return None

# Usage in views:
# from src.project.exceptions import ResourceNotFoundException
# raise ResourceNotFoundException(f"User with id {user_id} not found")
```

## Running the Application

```bash
python src/manage.py runserver
```

*Made with pride by Bryte Idea – 2025* 