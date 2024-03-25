import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime
from .models import personal_file
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

def personal_data_entry(request):
    title = "Personal Data Entry"
    form = Add_Personal_Data()
    if request.method == 'POST':
        form = Add_Personal_Data(request.POST, request.FILES)
        if form.is_valid():
            # save the form data to model
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect("personal_data") 
    return render(request, "input_data.html" , {'data': form , 'title':title})

def personal_data(request):
    title = "Personal Data"
    if request.method == 'POST':
            code = request.POST.get('code_no')
            if(personal_file.objects.filter(code_no=code).exists()):
                data = personal_file.objects.filter(code_no=code)
                a = True
                return render(request,'personal_data_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
            else:
                errors = 'Invalid code'
                a = False
                return render(request,'personal_data_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "personal_data_search.html", { 'title' : title})

def personal_data_no(request, code__no):
    title = "Personal Data"
    if(personal_file.objects.filter(code_no=code__no).exists()):
        data = personal_file.objects.filter(code_no=code__no)
        a = True
        return render(request,'personal_data_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
    else:
        errors = 'Invalid code'
        a = False
        return render(request,'personal_data_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages


# listings/views.py

# def personal_data_edit(request, id):
#     band = personal_file.objects.get(code_no=id)
#     form = Add_Personal_Data(instance=band) # prepopulate the form with an existing band
#     return render(request,
#                     'update_data.html',
#                     {'form': form})

def personal_data_edit(request, id):
    band = personal_file.objects.get(code_no=id)

    if request.method == 'POST':
        #https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform
        #https://stackoverflow.com/questions/63298721/how-to-update-imagefield-in-django
        form = Add_Personal_Data(request.POST, request.FILES, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            # photo = form.save(commit=False)
            # # set the uploader to the user before saving the model
            # photo.uploader = request.user
            # now we can save
            form.save()            
            # redirect to the detail page of the `Band` we just updated
            return redirect('personal_data', band.code_no)
    else:
        form = Add_Personal_Data(instance=band)

    return render(request,
                'update_data.html',
                {'form': form})

# def personal_data_edit(request, id):
    title = "Personal Data Edit"
    instance = get_object_or_404(personal_file, code_no=id)
    form = Add_Personal_Data()
    if request.method == 'POST':
        form = Add_Personal_Data(request.POST, request.FILES, instance = instance)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": title,
        "instance": instance,
        "form":form,
    }
    return render(request,'update_personal_data.html', context)

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
    