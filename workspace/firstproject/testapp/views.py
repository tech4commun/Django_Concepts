from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    # s="Hello and Welcome to first view"
    s="<h1>hello and welcome my name is khan</h1>"
    return HttpResponse(s)

# Create your views here.
