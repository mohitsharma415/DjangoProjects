from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsInfo(request):
    s='<h1>Hyderabad jobs information</h1>'
    return HttpResponse(s)

def punejobsInfo(request):
    s='<h1>pune jobs information</h1>'
    return HttpResponse(s)

def mumbaijobsInfo(request):
    s='<h1>mumbai jobs information</h1>'
    return HttpResponse(s)

def noidajobsInfo(request):
    s='<h1>noida jobs information</h1>'
    return HttpResponse(s)
