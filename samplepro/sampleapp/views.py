
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . forms import personForm
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def add_details(request):
    form=personForm()
    if request.method=='POST':
        form=personForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'base.html',{'form':form})

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('temporary')
        else:
            return HttpResponse("username or password is incorrect")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
        else:
            return HttpResponse("your password is not matching")
            return redirect('register/')
    return render(request,'register.html')

def temporary(request):
    return render(request, 'temp.html')

def redirecting(request):
    return render(request,'direct.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
