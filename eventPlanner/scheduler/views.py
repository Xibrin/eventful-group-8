from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def events(request):
    if request.method == "GET":
        return render(request, "index.html")

    return render(request, "events.html")
