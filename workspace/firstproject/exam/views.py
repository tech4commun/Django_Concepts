from django.shortcuts import render
from django.http import HttpResponse

# Create your multiple views here.
def testpaper(request):
    s="<h1>This is a test paper</h1>"
    return HttpResponse(s)


def result(request):
    s="<h1>This is a test result</h1>"
    return HttpResponse(s)
