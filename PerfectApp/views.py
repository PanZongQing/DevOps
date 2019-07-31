from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello , Welcome come to django !! ")


def good(request):
    return HttpResponse("good")

