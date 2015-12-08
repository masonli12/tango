from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse('About page<br><a href="/rango">home</a>')

def display(request, id):
    return HttpResponse("got id: %s" % (id))

def missing(request):
    return HttpResponse('Page is not here')