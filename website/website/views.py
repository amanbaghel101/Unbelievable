"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from website.models import websitee
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse


def signaction(request):
    if request.method=='POST':
        if request.POST.get('pname') and request.POST.get('city') and request.POST.get('email') and request.POST.get('number') and request.POST.get('password') and request.POST.get('cpassword') and request.POST.get('pin') and request.POST.get('address') and request.POST.get('year') and request.POST.get('role') and request.POST.get('date'):
            saverecord=websitee()
            saverecord.pname=request.POST.get('pname')
            saverecord.city=request.POST.get('city')
            saverecord.email=request.POST.get('email')
            saverecord.number=request.POST.get('number')
            saverecord.password=request.POST.get('password')
            saverecord.cpassword=request.POST.get('cpassword')
            saverecord.pin=request.POST.get('pin')
            saverecord.address=request.POST.get('address')
            saverecord.year=request.POST.get('year')
            saverecord.role=request.POST.get('role') 
            saverecord.date=request.POST.get('date') 
            saverecord.save()
            messages.success(request,'savesd.........!')
            
            return render(request,'signup.html', {})
    else:
            return render(request,'signup.html', {})
 


def login(request):
        return render(request,'login.html', {})

def home(request):
        return render(request,'Home.html', {})

def Visit(request):
        return render(request,'visit.html', {})