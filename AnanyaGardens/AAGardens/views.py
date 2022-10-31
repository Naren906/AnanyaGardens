from django.shortcuts import redirect, render
from django.contrib.auth.models import *
from django.contrib import messages
from .models import *
import requests

from django.conf import settings
crm=settings.CRM_API


SMS_User="nananani"
SMS_Pwd="Ananya@2010"


sms_url="http://login.bulksmsservice.net.in/api/mt/SendSMS"


# Create your views here.

def dash_home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/aboutus.html')

def gallary(request):
    return render(request, 'pages/gallary.html')

def projects(request):
    return render(request, 'pages/projects.html')

def contact(request):
    if request.method == "POST":
        username=request.POST['username']
        phone=request.POST['phone']
        company=request.POST['company']
        email=request.POST['email']
        message=request.POST['message']
        Contact.objects.create(Name=username,Email=email,Company=company,MobileNumber=phone,Message=message)
        """
        api integrations in crm
        """
        params={
            "FIELDS[NAME]":username,
            "FIELDS[EMAIL][0][VALUE]":email,
            "FIELDS[PHONE][0][VALUE]":phone
        }
        contact=requests.post(crm,params=params).json()
        submit=True
        context={'username':username}
        return render(request, 'pages/contact.html',context=context)
    else:
        return render(request, 'pages/contact.html')


def Projectdetails(request):
    if request.method == "POST":
        # Otp=random.randint(1111,9999)
        Name=request.POST["txtname"]
        
        Email=request.POST["txtemail"]
        Mobilenumber=request.POST["txtmob"]
        request.session["Name"]=Name
        request.session["Email"]=Email
        """
        api integrations in crm
        """
        params={
            "FIELDS[NAME]":Name,
            "FIELDS[EMAIL][0][VALUE]":Email,
            "FIELDS[PHONE][0][VALUE]":Mobilenumber
        }
        contact=requests.post(crm,params=params).json()

        if "result" in contact:
            submit=True
            context={'submit':submit,'name':Name}
        return render(request, 'pages/projectdetails.html',context=context)
    else:
        return render(request, 'pages/projectdetails.html')
    


def checkotp(request):
    if request.method == "POST":
        Confirm_OTP=request.POST["confirmotp"]
        print(type(Confirm_OTP))
        OTP_Id=request.session["OTP_Id"]
        otp_data=SMS_OTP.objects.get(OTP_Id=OTP_Id)
        Otp=otp_data.OTP
        print(Otp)
        otpsent=True
        context={'otpsent':otpsent}
        if Otp == int(Confirm_OTP):
            context["status"]="Success"
            context["message"]="OTP match"
            return render(request, 'pages/projectdetails.html',context=context)
        else:
            context["status"]="Failure"
            context["message"]="OTP Mismatch"
            return render(request, 'pages/projectdetails.html',context=context)
    else:
        return render(request, 'pages/projectdetails.html')
		
		
def Projectcompleted1(request):
    return render(request, 'pages/projectcmpltd1.html')

