from django.db import models
from Personal_Data.models import *
from django.utils import timezone

import datetime

# def din_no_extract():
#         return (personal_file.din_no)


# Create your models here.
class DIN_KYC_file(models.Model):
    
    din_no = models.IntegerField(unique= True)
    KYC_date = models.DateField(default=timezone.now)
    KYC_year = models.IntegerField(default=datetime.date.today().year)
    KYC_proof = models.FileField(upload_to='reporting_file', blank=True, null=True)

    Remarks = models.CharField(max_length=300)
    
    
    def __str__(self):
         return (str(self.din_no))
    
class PTEC_no_file(models.Model):
    
    PTEC_no = models.IntegerField(unique= True)
    PTEC_date = models.DateField(default=timezone.now)
    PTEC_year = models.IntegerField(default=datetime.date.today().year)
    PTEC_proof = models.FileField(upload_to='reporting_file', blank=True, null=True)
    Remarks = models.CharField(max_length=300)
    
    
    def __str__(self):
         return (str(self.PTEC_no))
    

class PTRC_no(models.Model):
    
    PTRC_no = models.IntegerField(unique= True)
    
    
    def __str__(self):
         return (str(self.PTRC_no))



class PTRC_no_file(models.Model):
    
    PTRC_no = models.ForeignKey(PTRC_no, on_delete=models.CASCADE)
    PTRC_year = models.IntegerField(default=datetime.date.today().year)
    PTRC_month = models.IntegerField(default=datetime.date.today().month)
    PTRC_date = models.DateField(default=timezone.now)
    PTRC_proof = models.FileField(upload_to='reporting_file', blank=True, null=True)
    Remarks = models.CharField(max_length=300)
    
    
    def __str__(self):
         return (str(self.PTRC_no))
