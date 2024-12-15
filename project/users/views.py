from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm

#Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = UserCreationForm()
    return render(request,"users/register.html",{"form" : form}) 

def homepage(request):
    #return HttpResponse("Hello, world!")
    return render(request,'home.html')

def success(request):
    return render(request,'success.html')