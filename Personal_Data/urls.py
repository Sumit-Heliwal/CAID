from turtle import home
from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
        # Replace the existing path for ""
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("personal_data/", views.personal_data, name="personal_data"),
    path("personal_data_add/", views.personal_data_entry, name="personal_data_add"),
    # path("contact/", views.contact, name="contact"),

]

