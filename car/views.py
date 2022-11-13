from imaplib import _Authenticator
from django.shortcuts import render,redirect
from .models import Members,Booking
from .forms import signup_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login as auth_login, logout

from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
def signup(request):
    return redirect('click_signup')
def click_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
       # user = User.objects.create_user(username=username,password=password)
        user = Members.objects.filter(username=username).values()
        if user is not None:
            return redirect('login')
        student = Members.objects.create(username=username,password=password)
        #user.save()
        student.save()
       
        return render(request, "login.html")
    return render(request, "creation.html")	
def click_login(request):
    # if(request.user.is_authenticated):
    #         return render(request,'dashboard.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = Members.objects.filter(username=username , password=password).values()
        # user = authenticate(username=username, password=password)
        if user is not None:
            return render(request,'dashboard.html',{'username':username})
        else:

            return redirect('signup')
    else:
        return redirect('login')

def dashboard(request):
    return render(request,'dashboard.html')

# @login_required(login_url='click_login')
def book(request):
    if request.method=='POST':
        username = request.POST['username']
        service = request.POST['service']
        place = request.POST['place']
        d = Booking.objects.create(service=service,place=place,approval='P',username=username)
        d.save()
    return render(request,'dashboard.html')
def profile(request):
    return render(request,'profile.html')

def view(request):
    username = request.POST['username']
    user = Members.objects.filter(username=username)
    book = Booking.objects.filter(username=username)
    return render(request,'view.html',{'username':username,'user':user,'book':book})
    

    
def Logout(request):
    logout(request)
    return redirect ("/")