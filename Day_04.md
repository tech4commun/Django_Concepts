# Multiple apps multiple views

Note: Jab app kisi app ko run karte hain, to usme __pycache__ naam ka folder ban jata hai, jahan compiled files store ho jati hain.

 Agenda

1. Multiple Apps  
2. Multiple views  
3. Steps to perform  
4. Update settings  
5. Plan your views  
6. Plan urls  
7. Set urls  
8. Test your code

# Multiple Apps

You can create any number of web apps in a django project.

# Multiple views

You can define any number of views in an app.

# Steps to Perform

1. **Create project**  
   django-admin startproject firstproject

2. **Create apps**  
   python manage.py startapp testapp  
   python manage.py startapp exam

3. **Update settings.py**

4. **Define views**

5. **set urls**

# Update settings

Make entries for the apps in INSTALLED_APPS list.

```python
INSTALLED_APPS = [
	'testapp',
	'exam'
]
```

# Plan your views

**testapp**  
- greetings()  
- about()  
- contact()  

**exam**  
- testpaper()  
- result()

# Plan urls

## testapp
- greetings()
- about()
- contact()

http://localhost:9000/hello

http://localhost:9000/about

http://localhost:9000/contact

## exam
- testpaper()
- result()

http://localhost:9000/testpaper

http://localhost:9000/result

# Set urls

```python
from testapp import views as v1
from exam import views as v2

urlpatterns = [
	path('hello', v1.greetings),
	path('about', v1.about),
	path('contact', v1.contact),
	path('testpaper', v2.testpaper),
	path('result', v2.Result),
]
```

# Test your code

Run server  
→ `python manage.py runserver`

Send request from browser by writing following urls:

→ http://localhost:8000/hello  
→ http://localhost:8000/about  
→ http://localhost:8000/contact  
→ http://localhost:8000/testpaper  
→ http://localhost:8000/result

# Django Multiple Apps - URL Configuration

## ❌ The Error (First Screenshot)

In `firstproject/urls.py`, if you import views from both apps like this:

```python
from testapp import views
from exam import views   # This OVERWRITES the previous views
```

The second import overrides the first one because both are named `views`.  
Then only the views from `exam` will be accessible, and `testapp` views will cause errors.

### Resulting Problem:
- `views.greetings`, `views.about`, `views.contact` will refer to `exam.views` (which doesn't have those functions)
- Leads to `AttributeError` or wrong view being called.

---

## ✅ The Correct Solution (Second Screenshot)

Use **aliases** (as keyword) to give each app's views a unique name.

### Correct `firstproject/urls.py`:

```python
from django.contrib import admin
from django.urls import path

from testapp import views as v1   # alias for testapp views
from exam import views as v2      # alias for exam views

urlpatterns = [
	path('hello', v1.greetings),
	path('about', v1.about),
	path('contact', v1.contact),
	path('testpaper', v2.testpaper),
	path('result', v2.result),
	path('admin/', admin.site.urls),
]
```

### Explanation:
- `v1` refers to `testapp.views`
- `v2` refers to `exam.views`
- No name conflict – both sets of views are available.

---

## 📌 Alternative Approach (Recommended for Larger Projects)

Instead of putting all routes in the project-level `urls.py`, use **`include()`** to delegate URL handling to each app.

### 1. Project `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('testapp.urls')),   # handles /hello, /about, /contact
	path('', include('exam.urls')),      # handles /testpaper, /result
	path('admin/', admin.site.urls),
]
```

### 2. Inside `testapp/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
	path('hello', views.greetings),
	path('about', views.about),
	path('contact', views.contact),
]
```

### 3. Inside `exam/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
	path('testpaper', views.testpaper),
	path('result', views.result),
]
```

This approach is cleaner, modular, and avoids import conflicts entirely.

---

