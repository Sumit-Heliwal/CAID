from django.db import models

# Create your models here.


class personal_file(models.Model):
    code_no =  models.CharField(max_length= 4, primary_key=True)
    name = models.CharField(max_length=50)
    passport_size_photo = models.FileField(upload_to='personal_file', blank=True, null=True)
    pan_card = models.FileField(upload_to='personal_file', blank=True, null=True)
    pan_no = models.CharField(max_length=50)
    aadhar_card = models.FileField(upload_to='personal_file', blank=True, null=True)
    aadhar_card_no = models.CharField(max_length=50)
    passport = models.FileField(upload_to='personal_file', blank=True, null=True)
    passport_no = models.CharField(max_length=50)
    driving_licence = models.FileField(upload_to='personal_file', blank=True, null=True)
    driving_licence_no = models.CharField(max_length=50)
    gst = models.FileField(upload_to='personal_file', blank=True, null=True)
    gst_no = models.CharField(max_length=50)
    din = models.FileField(upload_to='personal_file', blank=True, null=True)
    din_no = models.CharField(max_length=50)
    PTEC = models.FileField(upload_to='personal_file', blank=True, null=True)
    PTEC_no = models.CharField(max_length=50)
    
    # Passport_Photo = models.FileField(upload_to='personal_file', blank=True, null=True)
    # Passport_Photo = models.FileField(upload_to='personal_file', blank=True, null=True)
    Remarks = models.CharField(max_length=300)
    
    def __str__(self):
         return (self.code_no)
    
    
