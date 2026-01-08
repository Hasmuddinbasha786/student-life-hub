from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.decorators import login_required




@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})
    


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout_view(request):
    auth_logout(request)
    return redirect('home')
