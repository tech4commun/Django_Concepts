from django.shortcuts import render
from django.http import HttpResponse

# Create your multiple views here.

def greetings(request):
    # s="Hello and Welcome to first view"
    s="<h1>hello and welcome my name is khan</h1>"
    return HttpResponse(s)

def about(request):
    # s="Hello and Welcome to first view"
    s="<h1>About Page</h1>"
    return HttpResponse(s)

def contact(request):
    # s="Hello and Welcome to first view"
    s="<h1>Contact Page</h1>"
    return HttpResponse(s)