from django.shortcuts import render
from .models import doctor, sp, diseases

# Create your views here.


def index(request):
    return render(request, "doc/index.html", {
        "doctor": doctor.objects.all()
    })


def doctorss(request, doctor_id):
    doctorss = doctor.objects.get(pk=doctor_id)
    return render(request, "doc/doctor.html", {
        "doctor": doctorss
    })
    


'''
def zosymchuk(request):
    return render(request, "doctors/zosymchuk.html")


def plis(request):
    return render(request, "doctors/plis.html")


def index(request):
    return render(request, "doctors/zosymchuk.html", {
        "doctors": doctor.objects.all()
    })
'''
