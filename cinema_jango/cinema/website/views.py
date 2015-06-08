from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("return this string")
    return render(request, 'index.html')


def register(request):
    return HttpResponse("register.html")
