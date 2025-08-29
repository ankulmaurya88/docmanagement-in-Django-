from django.db import models
from django.contrib.auth.models import User 
import random

# Create your models here.
class UserProfile(models.Model):

    USER_TYPES = [
        ('Public', 'Public'),
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilePicture = models.ImageField(blank=True, null=True)
    DOB = models.DateField()
    address = models.TextField()
    contact_No = models.IntegerField()
    gender=models.CharField(max_length=50,null=True,blank=True)
    specialist=models.CharField(max_length=255,null=True,blank=True)
    userType = models.CharField(max_length=10, choices=USER_TYPES, default='Public')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
class OTP(models.Model):
    def Get_OTP():
        return random.randint(100000, 999999)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField(default=Get_OTP)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        
    patientAge=models.PositiveIntegerField(null=True)    
    patientName=models.CharField(max_length=40,null=True)
    department=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField()
    appointmentTime=models.TimeField()
    msg=models.TextField(max_length=500)
    patientEmail=models.EmailField(max_length=100)
    patientMobile=models.IntegerField()
    status=models.CharField(max_length=40,null=True)
    def __str__(self):
        return self.patientName
    
class Department(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    departmentName=models.CharField(max_length=40,null=True)
    description=models.TextField(max_length=500)
    status=models.CharField(max_length=40,null=True)
    def __str__(self):
        return self.departmentName

class ContactUs(models.Model):
    CustomerName=models.CharField(max_length=40,null=True)
    CustomerEmail=models.EmailField(max_length=100)
    Subject=models.TextField(max_length=100)
    msg=models.TextField(max_length=500)
    def __str__(self):
        return self.CustomerName