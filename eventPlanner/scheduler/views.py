from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserForm
from django import forms

import datetime
from dateutil import parser

from .models import User, Event, State
from .support import event_finder
from .forms import UserForm
from .support import algorithm

# Attempt to fix

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
        # username = request.POST["username"]
        password = request.POST["password"]
        current_user = authenticate(request, username=email, password=password)
        if current_user:
            login(request, current_user)
            Event.objects.all().delete()
            # TODO: right now only MD is being input as the location
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
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data.get("first_name")
            last_name = data.get('last_name')
            email = data.get("email")
            username = data.get("username")
            music = data.get("music")
            visual = data.get("visual")
            performing = data.get("performing")
            film = data.get("film")
            lectures = data.get("lectures")
            fashion = data.get("fashion")
            food = data.get("food")
            festivals = data.get("festivals")
            charity = data.get("charity")
            sports = data.get("sports")
            nightlife = data.get("nightlife")
            family = data.get("family")
            password = data.get("password")
            confirm_password = data.get("confirm_password")
            state = data.get("state")
            # print("Music: " + str(music))
            print("REACHED POST")
            try:
                current_user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=email,
                    email=email,
                    password=password,
                    confirm_password=confirm_password,
                    music=music,
                    visual=visual,
                    performing=performing,
                    film=film,
                    lectures=lectures,
                    fashion=fashion,
                    food=food,
                    festivals=festivals,
                    charity=charity,
                    sports=sports,
                    nightlife=nightlife,
                    family=family,
                    state=state
                )

                # if not Event.objects.filter(state).exists():
                #     curr_state = State()
                #     curr_state.state = state
                #     curr_state.save()
                #     current_user.save()
            except IntegrityError:
                return render(request, "scheduler/register.html", context={
                    "invalidMessage": "Email address already in use"
                })
            login(request, current_user)
        else:
            return render(request, "scheduler/register.html", context={
                "invalidMessage": "Issue with registration"
            })
        login(request, current_user)

        return render(request, "scheduler/login.html", context={
            "successMessage": "Successfully created new user"
        })

    else:
        print("Is this working")
        return render(request, "scheduler/register.html", {
            "form": UserForm()
        })


def schedule_view(request):
    if request.method == "POST":
        start_time = parser.parse(request.POST["startTime"])
        end_time = parser.parse(request.POST["endTime"])
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        max_commute_time_hrs = int(request.POST["maxCommuteTimeHrs"])
        max_commute_time_mins = int(request.POST["maxCommuteTimeMins"])
        cost = request.POST["cost"]

        events = Event.objects.filter(
            start_time__gte=start_time,
            end_time__lte=end_time,
            # city=city,
            state=state
        )

        scheduled = algorithm.get_schedule(address, events, request.user)

        # algorithm.compareDist(address, events)

        return render(request, "scheduler/schedule.html", context={
            "events": scheduled
        })
    return render(request, "scheduler/schedule.html")


@login_required
def events_view(request):
    if request.method == "POST":
        start_time = parser.parse(request.POST["startTime"])
        end_time = parser.parse(request.POST["endTime"])
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        max_commute_time_hrs = int(request.POST["maxCommuteTimeHrs"])
        max_commute_time_mins = int(request.POST["maxCommuteTimeMins"])
        cost = request.POST["cost"]

        events = Event.objects.filter(
            start_time__gte=start_time,
            end_time__lte=end_time,
            city=city,
            state=state
        )

        all_events = algorithm.sortEventsByTime(events)
        # algorithm.compareDist(address, events)

        return render(request, "scheduler/events.html", context={
            "events": all_events
        })
    return render(request, "scheduler/events.html")
