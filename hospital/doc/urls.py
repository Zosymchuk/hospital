from django import urls
from django.urls import path

from . import views

app_name = "doc"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:doctor_id>", views.doctorss, name="doctorss"),
    #path("zosymchuk", views.zosymchuk, name="zosymchuk"),
    #path("plis", views.plis, name="plis"),
]
