"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# below jab bhi koi request server par aati hai oh sabse pehle child myproject ke urls.py me atti hai, isse uko pata chata hai kis view and python function ko call karna hai
'''from testapp  import views as v1
from exam  import views as v2

# saare urls yaha metion karte hai
urlpatterns = [
    
    path("hello", v1.greetings),
    path("about", v1.about),
    path("contact", v1.contact),
    
    path("testpaper", v2.testpaper),
    path("result", v2.result),
    
    
]
'''
from django.conf.urls import include
# it will direct respective application and where individually app urls will be resolved
urlpatterns = [
    path(('testapp/'),include('testapp.urls')),
    path(('exam/'),include('exam.urls')),
    path("admin/", admin.site.urls),
]
