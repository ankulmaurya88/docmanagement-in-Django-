from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import OTP,UserProfile,Department,ContactUs
from django.conf import settings



# Create your views here.
def HOMEPAGE(request):
    return render(request,'indexpublic.html')
def LOGIN(request):
    msg=''    
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        data=authenticate(username=uname,password=pwd)
        if data != None:
            login(request,data)
            return redirect('index')
        msg='Incorrect Username or Password'         
    return render(request,'login.html',{'msg':msg})

def LOGOUT(request):
    logout(request)
    return render(request,'indexpublic.html')    

def SERVICES(request):
    return render(request,'services.html')

def ABOUT(request):
    return render(request,'about.html')


def CONTACT(request):
    if request.method == 'POST':
        CustomerName = request.POST.get('name')
        CustomerEmail = request.POST.get('email')
        Subject = request.POST.get('subject')
        msg = request.POST.get('message')
        ContactUs.objects.create(CustomerName=CustomerName,CustomerEmail=CustomerEmail,Subject=Subject,msg=msg)
        return redirect('contact')
    return render(request,'contact.html')

def SIGNUP(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        DOB = request.POST.get('DOB')
        profile_pic = request.FILES.get('pic')
        address= request.POST.get('address')
        #breakpoint()
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'sign.html',{'msg':msg})
        try:
            user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        except:
            msg='Usename already exist.'
            return render(request,'sign.html',{'msg':msg})
        UserProfile.objects.create(user=user,profilePicture=profile_pic,contact_No=contact,DOB=DOB,address=address)
        body = f'Hello {first_name} {last_name},\n\nYou have successfully registered.Your username is {user.username}.\n\n\nThank you for using our platform.\nE-Doc Appointment System !'
        subject = 'Successfully Registered On E-Doc Appointment System.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        send_mail(subject, body, from_email, to_email, fail_silently=False)
        return redirect('/login/')
    return render(request,'sign.html')

def DOCSIGNUP(request):
    departments=Department.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        DOB = request.POST.get('DOB')
        profile_pic = request.FILES.get('pic')
        address= request.POST.get('address')
        specialist= request.POST.get('specialist')
        #breakpoint()
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'docsign.html',{'msg':msg})
        try:
            user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        except:
            msg='Usename already exist.'
            return render(request,'docsign.html',{'msg':msg})
        UserProfile.objects.create(user=user,userType="Doctor",profilePicture=profile_pic,contact_No=contact,DOB=DOB,address=address,specialist=specialist)
        body = f'Hello {first_name} {last_name},\n\nYou have successfully registered as a doctor as {specialist} specialist on E-Doc Appointment System.Your username is {user.username}.\n\n\nThank you for using our platform.\nE-Doc Appointment System !'
        subject = 'Successfully Registered On E-Doc Appointment System.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        send_mail(subject, body, from_email, to_email, fail_silently=False)
        return redirect('/login/')
    return render(request,'docsign.html',{"departments":departments})

def BLOG(request):
    return render(request,'blog.html')

def DEPARTMENT(request):
    return render(request,'department.html')

def GALLERY(request):
    return render(request,'gallery.html')

def TEAM(request):
    return render(request,'team.html')

def SendEmailForForgotPassword(request):
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            # breakpoint()
            user = User.objects.get(username=username)
        except:
            msg='Invalid Username.'
            return render(request, 'ForgotPassEmail.html', {'msg':msg})
        try:
            email = user.email
        except:
            msg='There is no Email Associated with this Account.'
            return render(request, 'ForgotPassEmail.html', {'msg':msg})
        
        otp = OTP.objects.create(user=user)

        body = f'Did you forgot your password ?? No Worries !!!\n\n\nThis is your OTP to get your password reset  {otp.otp}  \n\n\nThank You !'
        subject = 'Forgot Password for E-Doc Appointment Account'
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(subject, body, from_email, to_email, fail_silently=False)
        return redirect('forgot-password')
    return render(request, 'ForgotPassEmail.html')

def ForgotPassword(request):
    msg =''
    if request.method == "POST":
        username = request.POST.get('username')
        user_otp = request.POST.get('otp')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1!=password2:
            msg='Password should be same.'
            return render(request,'forgotpassword.html', {'msg':msg})
        try:
            user = User.objects.get(username=username)
        except:
            msg='Invalid Username.'
            return render(request, 'ForgotPassEmail.html', {'msg':msg})
        
        otp = OTP.objects.filter(user=user).order_by('-created_at').first()
        if str(otp.otp) == user_otp:
            user.set_password(password1)
            user.save()
            return redirect('login')
        msg = 'Please Enter Correct OTP'
    return render(request, 'forgotpassword.html', {'msg':msg})
