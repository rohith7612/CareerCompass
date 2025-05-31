#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,'home.html')

@login_required(login_url='/users/login/')
def companies(request):
    return render(request,'companies.html')

@login_required(login_url='/users/login/')
def roadmaps_view(request):
    return render(request,'roadmaps.html')




def frontend(request):
    return render(request,'frontend.html')

def DevOps(request):
    return render(request,'DevOps.html')

def Ai(request):
    return render(request,'Aiengineer.html')

def Cloud(request):
    return render(request,'Cloudcomputing.html')

def fullstack(request):
    return render(request,'fullstack.html')

def cybersecurity(request):
    return render(request,'cybersecurity.html')

def mobile(request):
    return render(request,'mobile.html')

def machinelearning(request):
    return render(request,'machinelearning.html')

def backend(request):
    return render(request,'backend.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def success(request):
    return render(request,'success.html')

def loginsuccess(request):
    return render(request,'loginsuccess.html')

    