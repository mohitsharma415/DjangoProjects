from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def welcome(request):
    s='<h1>Hello welome to django classes </h1>'
    return HttpResponse(s)
