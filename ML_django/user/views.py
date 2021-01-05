from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.
def login(request):
    return HttpResponse('Login')
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