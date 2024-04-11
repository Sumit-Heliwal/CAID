from turtle import home
from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
        # Replace the existing path for ""
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("company_data/", views.company_data, name="company_data"),
    path("company_data_name/", views.company_data_name, name="company_data_name"),
    path("company_data_add/", views.company_data_entry, name="company_data_add"),
    # path("contact/", views.contact, name="contact"),

]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
