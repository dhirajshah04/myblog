from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth import  update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password=password)
        login(request, user)
        messages.success(request, 'Logged In successfully!')
        return redirect('post_new')

    return render(request, "user/login.html", {"form": form, "title": title})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct error below')
            return render(request, 'user/change_password.html', {'form': form})
    else:
        #messages.error(request, 'Please correct error below')
        form = PasswordChangeForm(request.user, request.POST)
        return render(request, 'user/change_password.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')