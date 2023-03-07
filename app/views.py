from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def yadav(request):
    return HttpResponse('<marquee><h1>Yadav</h1></marquee>')
