from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from .models import CustomUser
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import check_password
# Create your views here.
def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.get(username=username)
        print(user)
        print(username)
        print(password)
        if check_password(password, user.password):
            login(request,user)
            return redirect('space:home')
        else:
            return render(request, 'user/login.html',{'form':form})
    else:
        
        return render(request, 'user/login.html',{'form':form})
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("done")
            return HttpResponse('Done')
        else:
            return render(request, 'user/signup.html', {'form':form})
    else:
        form = UserForm()
        return render(request, 'user/signup.html', {'form':form})
def logoutuser(Request):
    logout(Request)
    return redirect('space:home')