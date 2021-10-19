from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User


def user(request):
    if request.user.is_authenticated:
        return render(request, "scheduler/user.html", context={
            "user": request.user,
            "navItems": {
                "Logout": reverse("logout"),
            }
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        current_user = authenticate(request, username=email, password=password)
        if current_user:
            login(request, current_user)
            return HttpResponseRedirect(reverse("user"))
        else:
            return render(request, "scheduler/login.html", context={
                "invalidMessage": "Invalid Username and/or Password"
            })
    return render(request, "scheduler/login.html")


def logout_view(request):
    logout(request)
    return render(request, "scheduler/login.html", {
        "successMessage": "Successfully Logged Out"
    })


def register_view(request):
    if request.method == "POST":
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirmPassword"]
        if password != confirm_password:
            return render(request, "scheduler/register.html", context={
                "invalidMessage": "Passwords do not match"
            })
        try:
            current_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=email,
                email=email,
                password=password
            )
            current_user.save()
        except IntegrityError:
            return render(request, "scheduler/register.html", context={
                "invalidMessage": "Email address already in use"
            })
        login(request, current_user)
        return render(request, "scheduler/login.html", context={
            "successMessage": "Successfully created new user"
        })
    return render(request, "scheduler/register.html")

