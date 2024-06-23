import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from PIL import Image
from django.conf import settings
from .forms import *
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# DIN KYC VIEWS

def DIN_KYC_entry(request):
    title = "DIN KYC Entry"
    form = Add_DIN_KYC()
    if request.method == 'POST':
        form = Add_DIN_KYC(request.POST, request.FILES)
        if form.is_valid():
            # save the form data to model
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect("DIN_KYC") 
    return render(request, "input_data.html" , {'data': form , 'title':title})


def DIN_KYC(request):
    title = "DIN KYC"
    if request.method == 'POST':
            code = request.POST.get('DIN_no')
            if(DIN_KYC_file.objects.filter(din_no=code).exists()):
                data = DIN_KYC_file.objects.filter(din_no=code)
                a = True
                return render(request,'DIN_KYC_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
            else:
                errors = 'Invalid code'
                a = False
                return render(request,'DIN_KYC_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "DIN_KYC_search.html", { 'title' : title})


def DIN_KYC_edit(request, id):
    band = DIN_KYC_file.objects.get(din_no=id)

    if request.method == 'POST':
        #https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform
        #https://stackoverflow.com/questions/63298721/how-to-update-imagefield-in-django
        form = Add_DIN_KYC(request.POST, request.FILES, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            # photo = form.save(commit=False)
            # # set the uploader to the user before saving the model
            # photo.uploader = request.user
            # now we can save
            form.save()            
            # redirect to the detail page of the `Band` we just updated
            return redirect('DIN_KYC', band.din_no)
    else:
        form = Add_DIN_KYC(instance=band)

    return render(request,
                'update_data.html',
                {'form': form})
    
def DIN_KYC_no(request, code__no):
    title = "DIN KYC"
    if(DIN_KYC_file.objects.filter(din_no=code__no).exists()):
        data = DIN_KYC_file.objects.filter(din_no=code__no)
        a = True
        return render(request,'DIN_KYC_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
    else:
        errors = 'Invalid code'
        a = False
        return render(request,'DIN_KYC_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     

# def DIN_KYC_list(request):
#     title = "DIN KYC LIST"
#     data = DIN_KYC_file.objects.values()
#     return render(request,'list.html' ,{'title' : title , 'data' : data})     



# PTEC VIEWS


def PTEC_entry(request):
    title = "PTEC Entry"
    form = Add_PTEC_no()
    if request.method == 'POST':
        form = Add_PTEC_no(request.POST, request.FILES)
        if form.is_valid():
            # save the form data to model
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect("PTEC") 
    return render(request, "input_data.html" , {'data': form , 'title':title})


def PTEC(request):
    title = "PTEC"
    if request.method == 'POST':
            code = request.POST.get('DIN_no')
            if(PTEC_no_file.objects.filter(PTEC_no=code).exists()):
                data = PTEC_no_file.objects.filter(PTEC_no=code)
                a = True
                return render(request,'PTEC_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
            else:
                errors = 'Invalid code'
                a = False
                return render(request,'PTEC_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "PTEC_search.html", { 'title' : title})


def PTEC_edit(request, id):
    band = PTEC_no_file.objects.get(PTEC_no=id)

    if request.method == 'POST':
        #https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform
        #https://stackoverflow.com/questions/63298721/how-to-update-imagefield-in-django
        form = Add_PTEC_no(request.POST, request.FILES, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            # photo = form.save(commit=False)
            # # set the uploader to the user before saving the model
            # photo.uploader = request.user
            # now we can save
            form.save()            
            # redirect to the detail page of the `Band` we just updated
            return redirect('PTEC', band.PTEC_no)
    else:
        form = Add_PTEC_no(instance=band)

    return render(request,
                'update_data.html',
                {'form': form})
    
def PTEC_no(request, code__no):
    title = "PTEC"
    if(PTEC_no_file.objects.filter(PTEC_no=code__no).exists()):
        data = PTEC_no_file.objects.filter(PTEC_no=code__no)
        a = True
        return render(request,'PTEC_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
    else:
        errors = 'Invalid code'
        a = False
        return render(request,'PTEC_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     


# PTRC VIEWS


def PTRC_entry(request):
    title = "PTRC Entry"
    form = Add_PTRC_no_data()
    if request.method == 'POST':
        form = Add_PTRC_no_data(request.POST, request.FILES)
        if form.is_valid():
            # save the form data to model
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect("PTRC") 
    return render(request, "input_data.html" , {'data': form , 'title':title})

def PTRC_no_entry(request):
    title = "PTRC No Entry"
    form = Add_PTRC_no()
    if request.method == 'POST':
        form = Add_PTRC_no(request.POST, request.FILES)
        if form.is_valid():
            # save the form data to model
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect("PTRC") 
    return render(request, "input_data.html" , {'data': form , 'title':title})


def PTRC(request):
    title = "PTRC"
    if request.method == 'POST':
            code = request.POST.get('DIN_no')
            if(PTRC_no_file.objects.filter(PTRC_no=code).exists()):
                data = PTRC_no_file.objects.filter(PTRC_no=code)
                a = True
                return render(request,'PTRC_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
            else:
                errors = 'Invalid code'
                a = False
                return render(request,'PTRC_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "PTRC_search.html", { 'title' : title})


def PTRC_edit(request, id):
    band = PTRC_no_file.objects.get(PTRC_no=id)

    if request.method == 'POST':
        #https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform
        #https://stackoverflow.com/questions/63298721/how-to-update-imagefield-in-django
        form = Add_PTRC_no_data(request.POST, request.FILES, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            # photo = form.save(commit=False)
            # # set the uploader to the user before saving the model
            # photo.uploader = request.user
            # now we can save
            form.save()            
            # redirect to the detail page of the `Band` we just updated
            return redirect('PTRC', band.PTRC_no)
    else:
        form = Add_PTRC_no_data(instance=band)

    return render(request,
                'update_data.html',
                {'form': form})
    
def PTRC_no(request, code__no):
    title = "PTRC"
    if(PTRC_no_file.objects.filter(PTRC_no=code__no).exists()):
        data = PTRC_no_file.objects.filter(PTRC_no=code__no)
        a = True
        return render(request,'PTRC_search.html' ,{'title' : title , 'data' : data , 'a' : a })     
    else:
        errors = 'Invalid code'
        a = False
        return render(request,'PTRC_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     


