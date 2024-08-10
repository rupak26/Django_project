from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request , username=username , password = password)
        if user is not None:
           auth.login(request,user)
           return redirect('home')
        else:
           messages.info(request,"Invalid Username or Password")
           return redirect('login')
    else:
        return render(request,"login.html")

        
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.info(request,'Email exist')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')