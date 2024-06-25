from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(DIN_KYC_file)
admin.site.register(PTEC_no_file)
admin.site.register(PTRC_no)
admin.site.register(PTRC_no_file)


# admin.site.register(Hostel)
