from django.contrib import admin
from .models import UserProfile,Appointment,Department,ContactUs,OTP

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(ContactUs)
admin.site.register(OTP)


