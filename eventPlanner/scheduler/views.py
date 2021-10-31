from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import datetime
from dateutil import parser

from .models import User, Event
from .support import event_finder


def user_view(request):
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
            Event.objects.all().delete()
            new_event_finder = event_finder.EventFinder(location="MD", start_time=int(
                parser.parse(datetime.datetime.now().isoformat()).timestamp()))
            new_event_finder.save_all_events()
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
            print(request.POST['row-1'])
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


@login_required
def events_view(request):
    if request.method == "POST":
        start_time = parser.parse(request.POST["startTime"])
        end_time = parser.parse(request.POST["endTime"])
        city = request.POST["city"]
        state = request.POST["state"]
        max_commute_time_hrs = int(request.POST["maxCommuteTimeHrs"])
        max_commute_time_mins = int(request.POST["maxCommuteTimeMins"])

        events = Event.objects.filter(
            start_time__gte=start_time,
            end_time__lte=end_time,
            city=city,
            state=state
        )

        return render(request, "scheduler/events.html", context={
            "events": events
        })
    return render(request, "scheduler/events.html")

