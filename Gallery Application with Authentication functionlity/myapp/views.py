from .forms import ImageForm
from .models import Image
from django.shortcuts import render, redirect
from .forms import RegisterForm


def home(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            form = ImageForm()
        img = Image.objects.all()
        return render(request, 'myapp/home.html', {'img': img, 'form': form, 'name': request.user})
    else:
        return redirect('/login/')


from django.contrib import messages
import os


def delete_image(request, id):
    Image.objects.get(id=1).photo.delete(save=True)
    messages.success(request, "Product Deleted Successfuly")
    return redirect('/home/')


def register(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully !!!")
            fm.save()
    else:
        fm = RegisterForm()
    return render(request, 'myapp/register.html', {'form': fm})


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return redirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request, 'myapp/login.html', {'form': fm})
    else:
        return redirect('/home/')


def user_logout(request):
    logout(request)
    return redirect('/login/')
