from turtle import home
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
        # Replace the existing path for ""
    
    # DIN
    
    path("DIN_KYC/", views.DIN_KYC, name="DIN_KYC"),
    # path("personal_data_name/", views.personal_data_name, name="personal_data_name"),
    path("DIN_KYC/<str:code__no>/", views.DIN_KYC_no, name="DIN_KYC"),
    path('DIN_KYC_edit/<str:id>/', views.DIN_KYC_edit, name='DIN_KYC_edit'),
    path('DIN_KYC_edit/', views.DIN_KYC, name='DIN_KYC_edit'),
    path("DIN_KYC_add/", views.DIN_KYC_entry, name="DIN_KYC_entry"),
    # path("DIN_KYC_list/", views.DIN_KYC_list, name="DIN_KYC_list"),
    # path("contact/", views.contact, name="contact"),
    
    
    # PTEC
   
    path("PTEC/", views.PTEC, name="PTEC"),
    # path("personal_data_name/", views.personal_data_name, name="personal_data_name"),
    path("PTEC/<str:code__no>/", views.PTEC_no, name="PTEC"),
    path('PTEC_edit/<str:id>/', views.PTEC_edit, name='PTEC_edit'),
    path('PTEC_edit/', views.PTEC, name='PTEC_edit'),
    path("PTEC_add/", views.PTEC_entry, name="PTEC_entry"),
    # path("contact/", views.contact, name="contact"),
 
    # PTRC
    
    path("PTRC/", views.PTRC, name="PTRC"),
    # path("personal_data_name/", views.personal_data_name, name="personal_data_name"),
    path("PTRC/<str:code__no>/", views.PTRC_no, name="PTRC"),
    path('PTRC_edit/<str:id>/', views.PTRC_edit, name='PTRC_edit'),
    path('PTRC_edit/', views.PTRC, name='PTRC_edit'),
    path("PTRC_add/", views.PTRC_entry, name="PTRC_entry"),
    path("PTRC_no_add/", views.PTRC_no_entry, name="PTRC_no_entry"),
    # path("contact/", views.contact, name="contact"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


