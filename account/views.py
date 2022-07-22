from django.shortcuts import render
from telnetlib import AUTHENTICATION
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def userLogin(request):
    if request.method == "POST":
        user=authenticate(request,
        username=request.POST['username'],
        password=request.POST['password'])
        # print(user)

        if user is not None:
            login(request,user)
            return redirect("store")
        else:
            return redirect("/account/userLogin")
    else:
        return render(request,"account/userLogin.html")


def userRegister(request):

    # request.method for loop the form 
    if request.method == "POST":
        print(request.POST)
        user = User.objects.create_user(
            username=request.POST['username'],
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect("/account/userLogin")
        
    else:
        return render(request,"account/userRegister.html")


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out.')
        return redirect('userLogin')
    return redirect('home')

