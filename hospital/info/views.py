from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "info/index.html")


def history(request):
    return render(request, "history/index.html")


def greet(request, name):
    if name == False:
        return render(request, "info/index1.html")
    else:
        return render(request, "info/index.html", {
            "name": name.capitalize()
        })
