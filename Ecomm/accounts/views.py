from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse



# Create your views here.

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        
        if not user_obj.exists():
            messages.warning(request, 'User does not exist')
            HttpResponseRedirect(request.path_info)
        
        if user_obj[0].profile.is_email_verified == False:
            messages.warning(request, 'Email is not verified')
            HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(email, password)
        
        if user_obj:
            login(request, user_obj)
            return HttpResponseRedirect('/')
        
        messages.warning(request, 'Invalid credentials')
        HttpResponseRedirect(request.path_info)
        
    
    return render(request,'accounts/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)
        
        if user_obj.exists():
            messages.error(request, 'User already exists')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create_user(username=email,password=password,first_name=first_name,last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'An email was sent to your account for verification')
        return HttpResponseRedirect(request.path_info)
    
    else:
        return render(request,'accounts/register.html')
    
    
def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return HttpResponseRedirect('/accounts/login')
    except Exception as e:
        return HttpResponse("Invalid Email Token")