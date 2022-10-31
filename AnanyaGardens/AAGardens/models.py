from email import message
from pyexpat import model
from django.db import models

# Create your models here.


class SMS_OTP(models.Model):
    OTP_Id=models.BigAutoField(primary_key=True,editable=False)
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=250)
    MobileNumber=models.CharField(max_length=100) 
    Message=models.TextField()
    OTP=models.IntegerField()

    def __str__(self):
        return self.Email


class Contact(models.Model):
    Contact_Id=models.BigAutoField(primary_key=True,editable=False)
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=250)
    Company=models.CharField(max_length=500)
    MobileNumber=models.CharField(max_length=100) 
    Message=models.TextField()

    def __str__(self):
        return self.Email