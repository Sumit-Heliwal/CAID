from django.db import models

# Create your models here.


class personal_file(models.Model):
    code_no =  models.CharField(max_length= 4, primary_key=True)
    passport_size_photo = models.FileField(upload_to='personal_file', blank=True, null=True)
    pan_card = models.FileField(upload_to='personal_file', blank=True, null=True)
    aadhar_card = models.FileField(upload_to='personal_file', blank=True, null=True)
    passport = models.FileField(upload_to='personal_file', blank=True, null=True)
    driving_licence = models.FileField(upload_to='personal_file', blank=True, null=True)
    gst = models.FileField(upload_to='personal_file', blank=True, null=True)
    # Passport_Photo = models.FileField(upload_to='personal_file', blank=True, null=True)
    # Passport_Photo = models.FileField(upload_to='personal_file', blank=True, null=True)
    Remarks = models.CharField(max_length=300)
    
    
