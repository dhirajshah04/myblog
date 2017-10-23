from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm

def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('post_new')

    return render(request, "user/login.html", {"form": form, "title": title})



def logout_view(request):
    logout(request)
    return redirect('index')
