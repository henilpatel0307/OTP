import re
from django.shortcuts import render, redirect
from .models import Company_data
from django.http import HttpResponse, request
# Create your views here.

import smtplib
import random
import email.message
# ------------------------- company ---------------------------

def Company_login(request):
    if request.POST:
        em = request.POST['email']
        ps = request.POST['pass']
        
        try:
            var = Company_data.objects.get(com_em = em)
            print(var)
            if var.com_pass == ps:
                request.session['comp_data'] = var.id
                return redirect('ComDashBoard')
            else:
                return HttpResponse("<h1><a href=""> You Have Entered Wrong Password ... </a></h1>")
        except:
            return HttpResponse("<h1><a href=""> You Have Entered Wrong Email Id </a></h1>")
            
    return render(request,'company/login/login.html')

def Company_regi(request):
    if request.POST:
        nm = request.POST['name']
        em = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        
        try:
            var = Company_data.objects.get(com_em = em)
            return HttpResponse("<h1><a href=""> Email Id Already Registered... </a></h1>")
        except:
            if pass1 == pass2:
                obj = Company_data()
                obj.com_name = nm
                obj.com_em = em
                obj.com_pass = pass2
                obj.save()
                return redirect('c_login')
            else:
                return HttpResponse("<h1><a href=""> Passwords are Not Match </a></h1>")
        
    return render(request,'company/login/regi.html')

def CompForgetPass(request):
    if request.POST:
        em1 = request.POST['em']
        print(em1)
        try:
            valid = Company_data.objects.get(com_em = em1)
            print(valid)

            sender_email = 'pip install secure-smtplib'
            sender_pass = 'dhruv0905'
            reciv_email = em1
            server = smtplib.SMPT('smpt.gmail.com',587)

            nos = [1,2,3,4,5,6,7,8,9,0]
            otp = ""
            for i in range(6):
                otp += str(random.choice(nos))
                print(otp)
            print(otp)

            mes1 = f"""
            This is Your OTP For Account
            {otp}

            Do not share this OTP with anyone

            """    
            msg = email.message.Message()
            msg['Subject'] = "Forget Pass OTP"
            msg['From'] = sender_email
            msg['To'] = reciv_email
            password = sender_pass
            msg.add_header('Content-Type','text/html')
            msg.set_payload(mes1)

            server.starttls()
            server.login(msg['From'],password)
            server.sendmail(msg['From'],msg['To'],msg.as_string())
            
            request.session['otp'] = otp
            
            request.session['new_user'] = valid.id
            return redirect('OTP_check')


        except:
            return HttpResponse('<a href="">You Have Entered Wrong Email ID </a>')
    return render(request,'company/login/Forget_pass.html')

def ComDashBoard(req):
    if 'comp_data' in req.session.keys():
        User = Company_data.objects.get(id = int(req.session['comp_data']))
        return render(req,'company/dash/index.html',{'USERS':User})
    else:
        return redirect('c_login')


# ------------------------- company ---------------------------