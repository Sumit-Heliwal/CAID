from turtle import home
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home"),
        # Replace the existing path for ""
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("personal_data/", views.personal_data, name="personal_data"),
    path("personal_data/<str:code__no>/", views.personal_data_no, name="personal_data"),
    path('personal_data_edit/<str:id>/', views.personal_data_edit, name='personal_data_edit'),
    path("personal_data_add/", views.personal_data_entry, name="personal_data_add"),
    # path("contact/", views.contact, name="contact"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


