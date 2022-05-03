from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, redirect, render
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=='POST':
        usn=request.POST['usn']
        password=request.POST['password']

        user=auth.authenticate(username=usn,password=password)
        if user is not None:
            auth.login(request,user)
            print("logged in sucessfully")
            return redirect('/')

    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['fullname']
        college=request.POST['college']
        usn=request.POST['usn']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:

            user=User.objects.create_user(username=usn,email=email,password=password)#to create a new user by djangoi
            print("new user created")
            return redirect('/')
        else:
            print("password mismatch")
    else:

        return render(request,'signup.html')

def index(request):
    return render(request,'index.html')