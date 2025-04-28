# Django Flavor Template

This directory contains the Django-specific structure for Manhattan Project.

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

## Running the Application

```bash
python src/manage.py runserver
```

*Made with pride by PixelMyNixel – 2025* 