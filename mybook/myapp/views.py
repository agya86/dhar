from django.shortcuts import render
from django.http import HttpResponse
def Indexpage(request):
    return HttpResponse("<h1>Hello India</h1>")
