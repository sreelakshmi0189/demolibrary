from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from students.models import CustomUser


# Create your views here.
def register(request):
    if (request.method == "POST"):
        u=request.POST['us']
        p=request.POST['ps']
        cp=request.POST['cp']
        fname=request.POST['fn']
        lname=request.POST['ln']
        em=request.POST['em']
        ph=request.POST['ph']
        pl=request.POST['pl']

        if (p==cp):
            user=CustomUser.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=em,phone=ph,place=pl)
            user.save()
            return redirect('books:home')
        else:
            return HttpResponse("Passwords are not same")

    return render(request,'register.html')

def userlogin(request):
    if(request.method=="POST"):
        u=request.POST['us']
        p=request.POST['ps']
        user=authenticate(username=u,password=p)    #buit in function
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("invalid credential")

    return render(request,'login.html')

@login_required
def userlogout(request):
    logout(request)
    return redirect('students:userlogin')

