from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import  CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

#Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("success")
    else:
        form = CreateUserForm()
    return render(request,"users/register.html",{"form" : form}) 

def homepage(request):
    return render(request,'home.html')

def success(request):
    return render(request,'success.html')

def loginsuccess(request):
    return render(request,'loginsuccess.html')

def login_view(request):
    if request.method == "POST":
         form = AuthenticationForm(data=request.POST)
         if form.is_valid():
             login(request, form.get_user())
             if 'next' in request.POST:
                 return redirect(request.POST.get('next'))
             else:
                return redirect("homepage")
    else:
        form = AuthenticationForm()
    return render(request,"users/login.html",{"form" : form})   
    
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("homepage")
    
    
    
    
    
    
    
    
    
    
