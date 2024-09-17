from django.shortcuts import render,redirect
from django.contrib import messages
from .models import student,type,course
from django.contrib.auth import authenticate,login,logout
import datetime

# Create your views here.
def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        login_validate=authenticate(request,username=username,password=password)
        if login_validate is not None:
            return redirect('dashboard')
        return redirect('login')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return render(request,'login.html')
    
def home(request):
    std_fees=student.objects.all()
    tot_std=len(student.objects.all())
    
    totalfees=0
    for fee in std_fees:
        totalfees+=fee.fees
        
    current_month=datetime.datetime.now().month #get current month
    current_year=datetime.datetime.now().year
    month_fees=0
 
    
    for j in student.objects.all():
        if j.slot1date and j.slot1date.month==current_month and j.slot1date.year==current_year:
            month_fees+=j.slot1
        if j.slot2date and j.slot2date.month==current_month and j.slot2date.year==current_year:
            month_fees+=j.slot2
        if j.slot3date and j.slot3date.month==current_month and j.slot3date.year==current_year:
            month_fees+=j.slot3


    pending_fee=student.objects.all()
    tot_pending=0
    for p in pending_fee:
        tot_pending+=p.pending
    
    return render(request,'dashboard.html',{'totalstd':tot_std,'totalfee':totalfees,'monthfee':month_fees,'pendingfee':tot_pending})

def addStd(request):
    stdtype=type.objects.all()
    stdcourse=course.objects.all()
    if request.method=='POST':
        stdid=request.POST.get('stdid')
        name=request.POST.get('name')
        college=request.POST.get('college')
        dept=request.POST.get('dept')
        type_id=request.POST.get('type')
        course_id=request.POST.get('course')
        fees=request.POST.get('fees')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        joindate=request.POST.get('joindate')
        
        selected_type=type.objects.get(id=type_id)
        pending_fees=fees
        
        selected_course=course.objects.get(id=course_id)
        add_student=student.objects.create(
            stdid=stdid,
            name=name,
            college=college,
            department=dept,
            student_type=selected_type,
            courses=selected_course,
            fees=fees,
            contact=contact,
            email=email,
            joindate=joindate,
            pending=pending_fees
            )
        add_student.save()
        
        return redirect('addStd')
    return render(request,'addStudent.html',{'stype':stdtype,'scourses':stdcourse})

def payment(request):
    stdid_drop=student.objects.all()
    
    
    if request.method=='POST':
        student_id=request.POST.get('std_id')
        payment_amt=request.POST.get('payamt')
        payment_amt=int(payment_amt)
        pay_date=request.POST.get('paydate')
        
        std_slot=student.objects.get(id=student_id)
        totalamt=std_slot.fees

        if  payment_amt <= std_slot.pending:
            
            if std_slot.slot1==0:
                std_slot.slot1=payment_amt
                if payment_amt>0:
                    std_slot.slot1date=pay_date
                    std_slot.pending=totalamt-payment_amt
            elif std_slot.slot2==0:
                if payment_amt>0:
                    std_slot.slot2=payment_amt
                    std_slot.slot2date=pay_date
                    std_slot.pending=totalamt-(std_slot.slot1+payment_amt)
            else:
                if payment_amt>0:
                    std_slot.slot3=payment_amt
                    std_slot.slot3date=pay_date
                    std_slot.pending=totalamt-(std_slot.slot1+std_slot.slot2+payment_amt)
                    
            messages.success(request,"payment received successfully")  
            std_slot.save()
            
            return render(request, 'payment.html', {'drop': stdid_drop})
        else:
            messages.error(request,"you enter more then amount in your fees.")
                
            
    return render(request,'payment.html',{'drop':stdid_drop})

def details(request):
    std_details=student.objects.all()
    return render(request,'stdDetails.html',{'detail':std_details})

def payDetails(request):
    pay_detail=student.objects.all()
    return render(request,'paymentDetails.html',{'payment':pay_detail})