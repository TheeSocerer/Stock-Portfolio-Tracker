from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def portfolio(request):
    return HttpResponse("Hello, world. This is the portfolio view.")
