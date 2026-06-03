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

**1. Configure project level `urls.py` (firstproject/urls.py)**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('testapp.urls')),
	path('', include('exam.urls')),
]
```

**2. Create `urls.py` inside `testapp` app**

```python
from django.urls import path
from . import views

urlpatterns = [
	path('hello', views.greetings, name='greetings'),
	path('about', views.about, name='about'),
	path('contact', views.contact, name='contact'),
]
```

**3. Create `urls.py` inside `exam` app**

```python
from django.urls import path
from . import views

urlpatterns = [
	path('testpaper', views.testpaper, name='testpaper'),
	path('result', views.result, name='result'),
]
```

**4. Define view functions in `testapp/views.py`**

```python
from django.http import HttpResponse

def greetings(request):
	return HttpResponse("Hello from testapp - greetings")

def about(request):
	return HttpResponse("About page")

def contact(request):
	return HttpResponse("Contact page")
```

**5. Define view functions in `exam/views.py`**

```python
from django.http import HttpResponse

def testpaper(request):
	return HttpResponse("Exam test paper")

def result(request):
	return HttpResponse("Exam results")
```

# Test your code

1. Run the development server (ensure port 9000 if needed):
   ```bash
   python manage.py runserver 9000
   ```

2. Open your browser and test the URLs:
   - http://localhost:9000/hello
   - http://localhost:9000/about
   - http://localhost:9000/contact
   - http://localhost:9000/testpaper
   - http://localhost:9000/result

3. Verify that each URL returns the expected HttpResponse.
