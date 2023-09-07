from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PasswordResetForm


# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        return render(request , 'dashboard.html')
    # else:
    #     return render(request, 'login-page.html')


def loginPage(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login-page.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login-page.html' , context=context )
        
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('loginPage')
    return render(request, 'register.html') 
        
def signout(request):
    logout(request)
    return redirect('loginPage')

def resetPassword(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        form1 = AuthenticationForm(data=request.POST)
        if form1.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = authenticate(username=request.user.username, password=password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                return redirect('loginPage')
    else:
        form = PasswordResetForm()
    
    return render(request, 'reset.html', {'form': form})