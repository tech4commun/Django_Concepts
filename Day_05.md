# Django App-Level URLs (Reusability)

## Agenda

1. Issue in reusability of apps  
2. Solution  
3. Steps to perform  
4. App level urls

---

## Issue in reusability of apps

An app should be easily attachable or removable from any project.

If URLs are defined only in the project's `urls.py`, it becomes difficult to reuse the same app in a different project because the URL configuration is tightly coupled with the project.

---

## Solution

Define URLs **at the app level** instead of the project level. Each app gets its own `urls.py` file, and the project only includes them using `include()`.

---

## Steps to Perform

1. **Create project**  
   `django-admin startproject firstproject`

2. **Create apps**  
   `python manage.py startapp testapp`  
   `python manage.py startapp exam`

3. **Update `settings.py`** – add apps to `INSTALLED_APPS`

4. **Define views** inside each app

5. **Set URLs** – create app-level `urls.py` and include them in the project

---

## Update settings.py

Make entries for the apps in the `INSTALLED_APPS` list.

```python
INSTALLED_APPS = [
    'testapp',
    'exam',
]
```

---

## Plan your views

### testapp
- `greetings()`
- `about()`
- `contact()`

### exam
- `testpaper()`
- `result()`

---

## Plan URLs (with app prefixes)

### testapp
- `greetings()` → `http://localhost:8000/testapp/hello`
- `about()`    → `http://localhost:8000/testapp/about`
- `contact()`  → `http://localhost:8000/testapp/contact`

### exam
- `testpaper()` → `http://localhost:8000/exam/testpaper`
- `result()`    → `http://localhost:8000/exam/result`

---

## App Level URLs – Implementation

### 1. Create `urls.py` inside each app

#### `testapp/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.greetings, name='greetings'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
```

#### `exam/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('testpaper', views.testpaper, name='testpaper'),
    path('result', views.result, name='result'),
]
```

### 2. Include app URLs in the project's `urls.py`

#### `firstproject/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('testapp/', include('testapp.urls')),
    path('exam/', include('exam.urls')),
    path('admin/', admin.site.urls),
]
```

---

## Define Views

### `testapp/views.py`
```python
from django.http import HttpResponse

def greetings(request):
    return HttpResponse("Hello from testapp - greetings")

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact page")
```

### `exam/views.py`
```python
from django.http import HttpResponse

def testpaper(request):
    return HttpResponse("Exam test paper")

def result(request):
    return HttpResponse("Exam results")
```

---

## Test your code

Run the server:
```bash
python manage.py runserver
```

Send requests from your browser using the following URLs:

- http://localhost:8000/testapp/hello
- http://localhost:8000/testapp/about
- http://localhost:8000/testapp/contact
- http://localhost:8000/exam/testpaper
- http://localhost:8000/exam/result

Each URL should return the corresponding `HttpResponse` from the respective app.

---

## Key Takeaway

> **App-level URLs make Django apps reusable.**  
> Each app defines its own URL patterns, and the project only includes them with a prefix. This allows you to drop the same app into any other project with minimal changes.