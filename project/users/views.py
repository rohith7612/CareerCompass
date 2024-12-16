from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import  CreateUserForm

#Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = CreateUserForm()
    return render(request,"users/register.html",{"form" : form}) 

def homepage(request):
    #return HttpResponse("Hello, world!")
    return render(request,'home.html')

def success(request):
    return render(request,'success.html')