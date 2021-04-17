from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def application_home(request):
    return render(request, 'application_home/application_home.html')


