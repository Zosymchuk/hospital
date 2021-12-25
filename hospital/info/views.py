from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "info/index.html")


def history(request):
    return render(request, "history/index.html")


'''
def greet(request, name):
    return render(request, "info/greet.html", {
        "name": name.capitalize()
    })
'''
