import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import company_file
from PIL import Image
from django.conf import settings
from .forms import *
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Add these to existing imports at the top of the file:


# def home(request):
#    return HttpResponse("Hello, Django!")
# Replace the existing home function with the one below
def home(request):
   return render(request, "home.html")
# Remove the old home function if you want; it's no longer used

def about(request):
    return render(request, "about.html")

def company_data_entry(request):
    title = "Company Data Entry"
    form = Add_Company_Data()
    if request.method == 'POST':
        form = Add_Company_Data(request.POST, request.FILES)
        if form.is_valid():
            # save the form data to model
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect("company_data") 
    return render(request, "input_data.html" , {'data': form , 'title':title})

def company_data(request):
    title = "Company Data"
    if request.method == 'POST':
            code = request.POST.get('code_no')
            if(company_file.objects.filter(code_no=code).exists()):
                data = company_file.objects.filter(code_no=code)
                a = True
                return render(request,'company_data_search.html' ,{'title' : title , 'data' : data , 'a' : a})     
            else:
                errors = 'Invalid code'
                a = False
                return render(request,'company_data_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "company_data_search.html", { 'title' : title})


# def contact(request):
#     return render(request, "Studentdata/contact.html")


# # You can also remove the import re statement that's no longer used

def hello_there(request, name):
    return render(
        request,
        'hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Add this code elsewhere in the file:
# def log_message(request):
#     form = LogMessageForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.log_date = datetime.now()
#             message.save()
#             return redirect("home")
#     else:
#         return render(request, "hello/log_message.html", {"form": form})
    