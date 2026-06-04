#har applications ki apni urls.py

# sabse pehle hame path function  ko call kar sake uske liye import statement

from django.urls import path
from testapp import views

urlpatterns=[
    path('hello',views.greetings),
    path('about',views.about),
    path('contact',views.contact),
]