

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("this is for About Page")
