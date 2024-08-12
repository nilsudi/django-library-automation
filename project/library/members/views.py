from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST ['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("Bir hata oluştu, tekrar deneyin..."))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Çıkış Yaptınız"))
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Başarıyla giriş yaptınız!"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register_user.html', {'form':form})