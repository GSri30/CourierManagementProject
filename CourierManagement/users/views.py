from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.


def LoginView(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                #invalid creds entered
                return render(request,"login.html",{"form":form})
        else:
            #invalid creds entered
            return render(request,"login.html",{"form":form})
    form=AuthenticationForm()
    return render(request,'login.html',{"form":form})



def RegisterView(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            #Register with valid creds
            return render(request,"login.html",{"form":form})
    else:
        form=RegisterForm()
    return render(request,'register.html',{"form":form})


def LogoutView(request):
    logout(request)
    return redirect('home')