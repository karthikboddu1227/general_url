from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_app1(request):
    return HttpResponse ('this is first_app1 view function')

def second_app1(request):
    return HttpResponse ('this is second_app1 view function')
