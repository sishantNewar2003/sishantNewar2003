from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hi(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')