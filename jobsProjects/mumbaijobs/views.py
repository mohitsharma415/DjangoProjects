from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mumjobs(request):
    s='mumbai jobs information'
    return HttpResponse(s)


def punejobs(request):
    s='pune jobs information'
    return HttpResponse(s)

def hydjobs(request):
    s='<h1>hyderabad jobs information</h1>'
    return HttpResponse(s)
