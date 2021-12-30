from django.shortcuts import render
from .models import doctor, sp

# Create your views here.


def index(request):
    return render(request, "doc/index.html", {
        "doctor": doctor.objects.all()
    })


def zosymchuk(request):
    return render(request, "doctors/zosymchuk.html")


def plis(request):
    return render(request, "doctors/plis.html")


'''
def index(request):
    return render(request, "doctors/zosymchuk.html", {
        "doctors": doctor.objects.all()
    })
'''
