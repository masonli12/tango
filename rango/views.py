from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<b>work hard will get return</b><br><a href="/rango/about/">about</a>')

def about(request):
    return HttpResponse('About page<br><a href="/rango">home</a>')

def display(request, id):
    return HttpResponse("got id: %s" % (id))

def missing(request):
    return HttpResponse('Page is not here')