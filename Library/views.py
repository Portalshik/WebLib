from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, it's library!")
