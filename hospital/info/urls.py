from django.urls import path

from . import views

app_name = "info"
urlpatterns = [
    path("", views.index, name="index"),
    #path("<str:name>", views.greet, name="greet"),
    path("history", views.history, name="history"),
    path("add", views.add, name="add"),

]
