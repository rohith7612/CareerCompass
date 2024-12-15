#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello, world!")
    return render(request,'home.html')

def roadmaps_view(request):
    #return HttpResponse("This is my about page.")
    return render(request,'roadmaps.html')

def frontend(request):
    return render(request,'frontend.html')

def DevOps(request):
    return render(request,'DevOps.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def success(request):
    return render(request,'success.html')