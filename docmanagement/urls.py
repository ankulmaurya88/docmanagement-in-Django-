"""docmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from PublicApp.views import HOMEPAGE,LOGIN,SERVICES,ABOUT,CONTACT,SIGNUP,BLOG,DEPARTMENT,GALLERY,TEAM,LOGOUT,DOCSIGNUP,SendEmailForForgotPassword,ForgotPassword
from AdminApp.views import INDEX,SEARCH,SEARCHPATIENT,DEPTWISEAPT,BOOKAPPOINTMENT,ADDAPPOINTMENT,EDITAPPOINTMENT,DELETEAPPOINTMENT,ADDDEPARTMENT,ADDDOCTOR,EDITDOCTOR,DELETEDOCTOR,ADDPATIENT,DELETEPATIENT,EDITPATIENT,ADMINPANEL,APPOINTMENTS,BOOKDOCTOR,CHANGEPASS,DEPARTMENTS,EDITDEPARTMENT,DELETEDEPARTMENT,DOCTORREGD,PATIENTREGD,DOCTORSCHEDULE,DOCTORSDETAIL,DOCTORSPANEL,DOCTORS,MYPROFILE,EDITPROFILE,OBSERVERDPATIENTS,USERRESCHEDULE,PATIENTS,CONTACTEDCUSTOMER,DELETECUSTOMERDETAILS
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HOMEPAGE,name="home"),
    path('indexpublic/',HOMEPAGE,name="home"),
    path('index/',INDEX,name="index"),
    path('search/',SEARCH,name="search"),
    path('searchpatient/',SEARCHPATIENT,name="searchpatient"),
    
    path('login/',LOGIN,name="login"),
    path('logout/',LOGOUT,name='logout'),
    path('services/',SERVICES,name="services"),
    path('about/',ABOUT,name="about"),
    path('contact/',CONTACT,name="contact"),
    path('contactedCustomer/',CONTACTEDCUSTOMER,name="contactedCustomer"),
    path('deleteCutomerDetails/<int:id>/',DELETECUSTOMERDETAILS,name="deleteCutomerDetails"),
    path('signin/',SIGNUP,name="signin"),
    path('sendotp/',SendEmailForForgotPassword,name="sendotp"),
    path('forgot-password/',ForgotPassword,name="forgot-password"),
    path('docsign/',DOCSIGNUP,name="docsign"),
    path('blog/',BLOG,name="blog"),
    path('gallery/',GALLERY,name="gallery"),
    path('team/',TEAM,name="team"),

    path('addappointment/',ADDAPPOINTMENT,name="addappointment"),
    path('departmentwiseappointmentbooking/',DEPTWISEAPT,name="departmentwiseappointmentbooking"),
    path('bookappointment/<str:key>/',BOOKAPPOINTMENT,name="bookappointment"),
    path('editappointment/<int:id>/',EDITAPPOINTMENT,name="editappointment"),
    path('deleteappointment/<int:id>/',DELETEAPPOINTMENT,name="deleteappointment"),
    path('adddepartment/',ADDDEPARTMENT,name="adddepartment"),
    path('editdepartment/<int:id>/',EDITDEPARTMENT,name="editdepartment"),
    path('deletedepartment/<int:id>/',DELETEDEPARTMENT,name="deletedepartment"),
    path('adddoctor/',ADDDOCTOR,name="adddoctor"),
    path('deletedoctor/<int:id>/',DELETEDOCTOR,name="deletedoctor"),
    path('editdoctor/<int:id>/',EDITDOCTOR,name="editdoctor"),
    path('addpatient/',ADDPATIENT,name="addpatient"),
    path('deletepatient/<int:id>/',DELETEPATIENT,name="deletepatient"),
    path('editpatient/<int:id>/',EDITPATIENT,name="editpatient"),
    path('adminpanel/',ADMINPANEL,name="adminpanel"),
    path('appointments/',APPOINTMENTS,name="appointments"),
    path('bookdoctor/',APPOINTMENTS,name="bookdoctor"),
    path('changepass/',CHANGEPASS,name="changepass"),
    path('departments/',DEPARTMENTS,name="departments"),
    path('doctorregd/',DOCTORREGD,name="doctorregd"),
    path('patientregd/',PATIENTREGD,name="patientregd"),
    path('doctorschedule/',DOCTORSCHEDULE,name="doctorschedule"),
    path('doctorsdetail/',DOCTORSDETAIL,name="doctorsdetail"),
    path('doctorspanel/',DOCTORSPANEL,name="doctorspanel"),
    path('doctors/',DOCTORS,name="doctors"),
    path('patients/',PATIENTS,name="patients"),
    path('myprofile/<int:id>/',MYPROFILE,name="myprofile"),
    path('editprofile/<int:id>/',EDITPROFILE,name="editprofile"),
    path('observedpatients/',OBSERVERDPATIENTS,name="observedpatients"),
    path('userreschedule/',USERRESCHEDULE,name="userreschedule"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)