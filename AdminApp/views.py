from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login
from PublicApp.models import UserProfile,Appointment,Department,ContactUs

# Create your views here.#

def INDEX(request):
    patients=UserProfile.objects.filter(userType="Public").count()
    doctorscount=UserProfile.objects.filter(userType="Doctor").count()
    appointments=Appointment.objects.all().count()
    showappointments=Appointment.objects.all()[:6]
    showpatients=Appointment.objects.all()[:6]
    departments=Department.objects.all().count()
    doctors=UserProfile.objects.filter(userType="Doctor")
    employee=UserProfile.objects.all().count()

    
    return render(request,'index.html',{"patients":patients,"doctorscount":doctorscount,"appointments":appointments,"departments":departments,"doctors":doctors,"showappointments":showappointments,"showpatients":showpatients,"employee":employee})


# -------APPOINTMENT RELATED VIEWS FUNCTIONS ---------

def APPOINTMENTS(request):
    u=UserProfile.objects.get(user=request.user)
    appointments=Appointment.objects.filter(user=u)
    adminappointments=Appointment.objects.all()
    return render(request,'appointments.html',{"appointments":appointments,"adminappointments":adminappointments})

def ADDAPPOINTMENT(request):
    doctors=UserProfile.objects.filter(userType="Doctor")
    departments=Department.objects.all()
    
    if request.method == 'POST':
                      
        patientName = request.POST.get('patientName')
        patientAge = request.POST.get('patientAge')
        department = request.POST.get('department')
        doctorName = request.POST.get('doctorName')
        appointmentDate = request.POST.get('appointmentDate')
        appointmentTime=request.POST.get('appointmentTime')
        msg = request.POST.get('msg')
        patientEmail = request.POST.get('patientEmail')
        patientMobile= request.POST.get('patientMobile')
        status=request.POST.get('status')
        #breakpoint()
        Appointment.objects.create(user=UserProfile.objects.get(user=request.user),patientName=patientName,patientAge=int(patientAge),department=department,doctorName=doctorName,appointmentDate=appointmentDate,appointmentTime=appointmentTime,msg=msg,patientEmail=patientEmail,patientMobile=patientMobile,status=status)
        body = f'Hello {patientName},\n\nAn appointment to {doctorName} has booked for you scheduled on {appointmentDate} at {appointmentTime}.\n\n\nThank you for using our platform.\nE-Doc Appointment System !'
        subject = 'Appointment Booked On E-Doc Appointment System.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [patientEmail]
        send_mail(subject, body, from_email, to_email, fail_silently=False)
        return redirect('appointments')
    return render(request,'add-appointment.html',{"doctors":doctors,"departments":departments}) 

def EDITAPPOINTMENT(request,id):
    if not id:
        return redirect('appoitnments')
    if not request.user.is_authenticated:
        return redirect('appoitnments')
    appointments = Appointment.objects.get(id=id)
    doctors=UserProfile.objects.filter(userType="Doctor")
    departments=Department.objects.all()
    if request.method == 'POST':
      
        patientName = request.POST.get('patientName')
        patientAge = request.POST.get('patientAge')
        department = request.POST.get('department')
        doctorName = request.POST.get('doctorName')
        appointmentDate = request.POST.get('appointmentDate')
        appointmentTime=request.POST.get('appointmentTime')
        msg = request.POST.get('msg')
        patientEmail = request.POST.get('patientEmail')
        patientMobile= request.POST.get('patientMobile')
        status=request.POST.get('status')

        appointments.patientName=patientName
        appointments.patientAge=patientAge
        appointments.department=department
        appointments.doctorName=doctorName
        appointments.appointmentDate=appointmentDate
        appointments.appointmentTime=appointmentTime
        appointments.msg=msg
        appointments.patientEmail=patientEmail
        appointments.patientMobile=patientMobile
        appointments.status=status
        appointments.save()
        return redirect('appointments')
    return render(request,'editappointment.html',{"appointments":appointments,"doctors":doctors,"departments":departments})

def DELETEAPPOINTMENT(request,id):
    if not id:
        return redirect('appointments')
    if not request.user.is_authenticated:
        return redirect('appointments')
    appointmentId = Appointment.objects.get(id=id)
    appointmentId.delete()
    return redirect('appointments')




# ----------DEPARTMENT RELATED VIEWS FUNCTIONS ---------


def DEPARTMENTS(request):
    departments=Department.objects.all()
    return render(request,'departments.html',{"departments":departments})

def ADDDEPARTMENT(request):
    if request.method == 'POST':
        departmentName = request.POST.get('departmentName')
        description = request.POST.get('description')
        status=request.POST.get('status')
        Department.objects.create(user=UserProfile.objects.get(user=request.user),departmentName=departmentName,description=description,status=status)
        return redirect('departments')
    return render(request,'add-department.html')


def DEPTWISEAPT(request):
    deptdetails=Department.objects.all()
    doctors=UserProfile.objects.filter(userType="Doctor")
    dept=list()
    for d in deptdetails:
        dept.append(d.departmentName)
    # print(dept)

    doct=list()
    for d in doctors:
        doct.append(d.specialist)
    # print(doct)
    count={}
    for i in dept:
        count[i]=0
    for i in doct:
        if i in dept:
            count[i]+=1
    listOfTuples=[(k,v) for k,v in count.items()]
    dictionary={}
    def convert(tup,di):
        di=dict(tup)
        return di
    docCount=convert(listOfTuples,dictionary)

    
    # doct=list(for d.spceialisation in doctors)
    # print(type(dept),type(doct))
   
    return render(request,'deptwisebookapt.html',{"deptdetails":deptdetails,"doctors":doctors,"docCount":docCount})


def BOOKAPPOINTMENT(request,key):
    if not key:
        return redirect('appoitnments')
    if not request.user.is_authenticated:
        return redirect('appoitnments')
    doctors=UserProfile.objects.filter(userType="Doctor")
    departments=Department.objects.filter(departmentName=key)
    if request.method == 'POST':
                      
        patientName = request.POST.get('patientName')
        patientAge = request.POST.get('patientAge')
        department = request.POST.get('department')
        doctorName = request.POST.get('doctorName')
        appointmentDate = request.POST.get('appointmentDate')
        appointmentTime=request.POST.get('appointmentTime')
        msg = request.POST.get('msg')
        patientEmail = request.POST.get('patientEmail')
        patientMobile= request.POST.get('patientMobile')
        status=request.POST.get('status')
        #breakpoint()
        Appointment.objects.create(user=UserProfile.objects.get(user=request.user),patientName=patientName,patientAge=int(patientAge),department=department,doctorName=doctorName,appointmentDate=appointmentDate,appointmentTime=appointmentTime,msg=msg,patientEmail=patientEmail,patientMobile=patientMobile,status=status)
        return redirect('appointments')
    return render(request,'add-appointment.html',{"doctors":doctors,"departments":departments}) 



def EDITDEPARTMENT(request,id):
    if not id:
        return redirect('departments')
    if not request.user.is_authenticated:
        return redirect('departments')
    departments = Department.objects.get(id=id)
    
    if request.method == 'POST':
        
        departmentName = request.POST.get('departmentName')
        description = request.POST.get('description')
        status=request.POST.get('status')
        
        departments.departmentName=departmentName
        departments.description=description
        departments.status=status
        departments.save()
        return redirect('departments')
    return render(request,'editdepartment.html',{"departments":departments})

def DELETEDEPARTMENT(request,id):
    if not id:
        return redirect('departments')
    if not request.user.is_authenticated:
        return redirect('departments')
    departmentId = Department.objects.get(id=id)
    departmentId.delete()
    return redirect('departments')

        

# ------- DOCTOR RELATED VIEWS FUNCTIONS -------



def DOCTORS(request):
    if not request.user.is_authenticated:
        return redirect('login')
    doctor=UserProfile.objects.filter(userType="Doctor")
    return render(request,'doctors.html',{"doctors":doctor}) 

def ADDDOCTOR(request):
    departments=Department.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender=request.POST.get('gender')
        DOB = request.POST.get('DOB')
        profile_pic = request.FILES.get('pic')
        address= request.POST.get('address')
        specialist= request.POST.get('specialist')
        #breakpoint()
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'add-doctor.html',{'msg':msg})
        try:
            user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        except:
            msg='Usename already exist.'
            return render(request,'add-doctor.html',{'msg':msg})
        UserProfile.objects.create(user=user,userType="Doctor",profilePicture=profile_pic,contact_No=contact,gender=gender,DOB=DOB,address=address,specialist=specialist)
        return redirect('doctors')
    return render(request,'add-doctor.html',{"departments":departments}) 

def EDITDOCTOR(request,id):
    if not id:
        return redirect('login')
    if not request.user.is_authenticated:
        return redirect('login')
    departments=Department.objects.all()
    doctordetail = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        #breakpoint()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact') 
        gender=request.POST.get('gender')
        DOB = request.POST.get('DOB')
        profile_pic = request.FILES.get('pic')
        address= request.POST.get('address')
        specialist= request.POST.get('specialist')
        doctordetail.user.first_name=first_name
        doctordetail.user.last_name=last_name
        doctordetail.user.email=email
        doctordetail.contact_No=contact
        doctordetail.gender=gender
        if DOB:
            doctordetail.DOB=DOB
        doctordetail.profilePicture=profile_pic
        doctordetail.address=address
        doctordetail.specialist=specialist
        doctordetail.user.save()
        doctordetail.save()
        return redirect('doctors')
       
    return render(request,'editdoctor.html',{"doctor":doctordetail,"departments":departments})


def DELETEDOCTOR(request,id):
    if not id:
        return redirect('login')
    if not request.user.is_authenticated:
        return redirect('login')
    uid = UserProfile.objects.get(id=id)
    uid.user.delete()
    return redirect('doctors')

# ------- PATIENT RELATED VIEWS FUNCTIONS -------



def PATIENTS(request):
    if not request.user.is_authenticated:
        return redirect('login')
    patients=UserProfile.objects.filter(userType="Public")
    return render(request,'patients.html',{"patients":patients}) 


def ADDPATIENT(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender=request.POST.get('gender')
        DOB = request.POST.get('DOB')
        profile_pic = request.FILES.get('pic')
        address= request.POST.get('address')
        
        #breakpoint()
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'add-patient.html',{'msg':msg})
        try:
            user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        except:
            msg='Usename already exist.'
            return render(request,'add-patient.html',{'msg':msg})
        UserProfile.objects.create(user=user,userType="Public",profilePicture=profile_pic,contact_No=contact,gender=gender,DOB=DOB,address=address)
        return redirect('patients')
     
    return render(request,'add-patient.html') 


def EDITPATIENT(request,id):
    if not id:
        return redirect('login')
    if not request.user.is_authenticated:
        return redirect('login')
    
    patientdetail = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        #breakpoint()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact') 
        gender=request.POST.get('gender')
        DOB = request.POST.get('DOB')
        profile_pic = request.FILES.get('pic')
        address= request.POST.get('address')
        
        patientdetail.user.first_name=first_name
        patientdetail.user.last_name=last_name
        patientdetail.user.email=email
        patientdetail.contact_No=contact
        patientdetail.gender=gender
        if DOB:
            patientdetail.DOB=DOB
        patientdetail.profilePicture=profile_pic
        patientdetail.address=address
        
        patientdetail.user.save()
        patientdetail.save()
        # if request.user.userprofile_set.first.userType=="Admin":
        return redirect('patients')
        # return redirect(f"/myprofile/{id}/")
    return render(request,'editpatient.html',{"patient":patientdetail})


def DELETEPATIENT(request,id):
    if not id:
        return redirect('login')
    if not request.user.is_authenticated:
        return redirect('login')
    uid = UserProfile.objects.get(id=id)
    uid.user.delete()
    return redirect('patients')


def ADMINPANEL(request):
    patients=UserProfile.objects.filter(userType="Public").count()
    doctors=UserProfile.objects.filter(userType="Doctor").count()
    employee=UserProfile.objects.all().count()
    return render(request,'admin-panel.html',{"patients":patients,"doctors":doctors,"employee":employee}) 





def BOOKDOCTOR(request):
    doctors=UserProfile.objects.filter(userType="Doctor")
    return render(request,'book-doctor.html',{"doctors":doctors}) 



def CHANGEPASS(request):
    if not request.user.is_authenticated:
        return redirect('login')
    msg = ''
    if request.method == "POST":
        username = request.user.username
        oldpass = request.POST.get('oldpass')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1!=password2:
            msg='New and Confirm Password should be same.'
            return render(request,'changepass.html', {'msg':msg})
        user = User.objects.get(username=username)
        newpass = user.check_password(oldpass)
        
        if newpass:
            user.set_password(password1)
            user.save()
            data=authenticate(username=username,password=password1)
            if data !=None:
                login(request,data)
                return redirect('index')
        msg='Old Password should be same.'
        return render(request,'changepass.html', {'msg':msg})
    return render(request,'changepass.html', {'msg':msg})

   

def DOCTORREGD(request):
    docdetails=UserProfile.objects.filter(userType="Doctor")
    return render(request,'doctor-regd.html',{"docdetails":docdetails})

def PATIENTREGD(request):
    patientdetails=UserProfile.objects.filter(userType="Public")
    return render(request,'patient-regd.html',{"patientdetails":patientdetails})

def DOCTORSCHEDULE(request):
    u=UserProfile.objects.get(user=request.user)
    fname=''
    fname=request.user.first_name + ' ' +request.user.last_name
    # fname+=request.user.last_name
    # print(fname)
    appointments=Appointment.objects.filter(doctorName=fname)
       
    return render(request,'doctor-schedule.html',{"appointments":appointments})

def USERRESCHEDULE(request):
    u=UserProfile.objects.get(user=request.user)
    fname=''
    fname=request.user.first_name + ' ' +request.user.last_name
    # fname+=request.user.last_name
    # print(fname)
    appointments=Appointment.objects.filter(patientName=fname)

    return render(request,'user-reschedule.html',{"appointments":appointments})     

def DOCTORSDETAIL(request):
    return render(request,'doctors-detail.html')  

def DOCTORSPANEL(request):
    totalappointments=Appointment.objects.all().count()
    u=UserProfile.objects.get(user=request.user)
    appointments=Appointment.objects.filter(user=u).count()
    employees=UserProfile.objects.all().count()
    return render(request,'doctors-panel.html',{"totalappointments":totalappointments,"appointments":appointments,"employees":employees})  



def MYPROFILE(request,id):
    if not id:
        return redirect('login')
    if not request.user.is_authenticated:
        return redirect('login')
    u=User.objects.get(id=id)
    profiledetails = UserProfile.objects.get(user=u)
       
    return render(request,'myprofile.html',{"profiledetails":profiledetails}) 

def EDITPROFILE(request,id):
    if not id:
        return redirect('login')
    if not request.user.is_authenticated:
        return redirect('login')
    
    profiledetails = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_No = request.POST.get('contact_No')
        DOB = request.POST.get('DOB')
        profilePicture = request.FILES.get('profilePicture')
        address= request.POST.get('address')

        profiledetails.user.first_name=first_name
        profiledetails.user.last_name=last_name
        profiledetails.user.email=email
        profiledetails.contact_No=contact_No
        profiledetails.DOB=DOB
        profiledetails.profilePicture=profilePicture
        profiledetails.address=address

        profiledetails.user.save()
        profiledetails.save()
        return redirect(f"/myprofile/{id}/")       
    return render(request,'editprofile.html',{"profiledetails":profiledetails})

def OBSERVERDPATIENTS(request):
    patients=Appointment.objects.all()
    return render(request,'observed-patients.html',{"patients":patients})  



def SEARCH(request):
    query=request.GET['query']
    foundAppointments=Appointment.objects.filter(patientName__icontains=query)
    return render(request,"search.html",{"foundAppointments":foundAppointments,"query":query})

def SEARCHPATIENT(request):
    query=request.GET['query']
    foundPatient=Appointment.objects.filter(patientName__icontains=query)
    return render(request,"searchpatient.html",{"foundPatient":foundPatient,"query":query})


def CONTACTEDCUSTOMER(request):
    customerDetails=ContactUs.objects.all()
    return render(request,'contactedCustomer.html',{"customerDetails":customerDetails})

def DELETECUSTOMERDETAILS(request,id):
    if not id:
        return redirect('contactedCustomer')
    if not request.user.is_authenticated:
        return redirect('login')
    customerId = ContactUs.objects.get(id=id)
    customerId.delete()
    return redirect('contactedCustomer')
