from django import forms
from .models import *

# class DateInput(forms.DateInput):
#     input_type = 'date'


class Add_DIN_KYC(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = DIN_KYC_file
        fields = "__all__"


class Add_PTEC_no(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = PTEC_no_file
        fields = "__all__"

class Add_PTRC_no(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = PTRC_no
        fields = "__all__"

class Add_PTRC_no_data(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = PTRC_no_file
        fields = "__all__"

# class Product(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Add_Product
#         fields = ['Product_Name']


# class Sale_Form(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Customer_Sale
#         fields = "__all__"
#         widgets = {
#             'Sale_Date': DateInput(),
#             'Payment_Date': DateInput()
#         }

