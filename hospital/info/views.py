from django.http import response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.


def history(request):
    return render(request, "history/index.html")


'''
def greet(request, name):
    return render(request, "info/greet.html", {
        "name": name.capitalize()
    })
'''


class NewR(forms.Form):
    r = forms.CharField(label="New R")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.


def index(request):
    if "rs" not in request.session:
        request.session["rs"] = []
    return render(request, "info/index.html", {
        "rs": request.session["rs"]
    })


def add(request):
    if request.method == "POST":
        form = NewR(request.POST)
        if form.is_valid():
            r = form.cleaned_data["r"]
            request.session["rs"] += [r]
            return HttpResponseRedirect(reverse("info:index"))
        else:
            return render(request, "info/add.html", {
                "form": form
            })

    return render(request, "info/add.html", {
        "form": NewR()
    })
