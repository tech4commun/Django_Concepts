# Django creating first view

client se request to webserver then webserver tranfers request to view and view perform buisness logic and provide response to webserver which later passed to client

## View

Django views are python functions that takes http request and return http response.

This response can be the HTML contents of a webpage , or a redirect, or a 404 error , or an XML , or an image, or .... anything.

## Purpose of views

Django uses MVT design pattern, where V stands for Views.

Views are part of user interface

Main job of views is to receive http request, perform business logic and return http response.

## Steps to perform

1.  create project (Already done)
    `django-admin startproject firstproject`
2.  Create web app (Already done)
    `python manage.py startapp testapp`
3.  Update settings.py (Already done)
4.  Defining views
5.  set url for the view in urls.py

## Defining Views

In `views.py` of `testapp`:

```python
from django.http import HttpResponse
def greeting(request):
    s="<h1>Hello and welcome to first view</h1>"
    return HttpResponse(s)
```

## Set URLs

In `urls.py` of child `firstproject` folder:

```python
from testapp import views
from django.urls import path

urlpatterns = [
    path('hello', views.greeting),
]
```

<http://localhost:8000/hello>

## Test your code

Run server

```bash
python manage.py runserver
```

send request from browser by writing following url

> <http://localhost:8000/hello>
