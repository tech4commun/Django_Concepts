#har applications ki apni urls.py

# sabse pehle hame path function  ko call kar sake uske liye import statement

from django.urls import path
from exam import views

urlpatterns=[
    path('testpaper',views.testpaper),
    path('result',views.result),
]