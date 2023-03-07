from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse ('this is first_app2 view function')

def second_app2(request):
    return HttpResponse ('this is second_app2 view function')