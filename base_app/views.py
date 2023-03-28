from argparse import Action
from asyncio.windows_events import NULL
from fileinput import filename
from importlib.resources import contents
from urllib import response
import qrcode
import random
import csv
import pandas as pd

import os, json, math
# import psycopg2
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt
from django. contrib import messages
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render, redirect
from base_app.models import *
from datetime import datetime,date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.db.models import Q
from num2words import num2words
from django.utils.dateparse import parse_date

from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Sum

from cal.models import *


# Create your views here.
def login(request):
    
    
    
    if request.method == 'POST':
        
        
        email  = request.POST['email']
        password = request.POST['password']
        user =authenticate(username=email, password=password)
        if user is not None:
                request.session['SAdm_id'] = user.id
                Num1 = project.objects.count()
                Num = user_registration.objects.count()
                Trainer = designation.objects.get(designation='trainer')
                trcount=user_registration.objects.filter(designation=Trainer).count()
                return redirect( 'SuperAdmin_dashboard')
        
        
        
        # des2 = designation.objects.get(designation='trainee')
        
       
        # Adm1 = designation.objects.get(designation="Admin")
        
        
      
        des2 = designation.objects.get(designation='trainee')
        if user_registration.objects.filter(email=email, password=password, designation_id=des2.id,status="active").exists():
                member = user_registration.objects.get(
                email=request.POST['email'],password=request.POST['password'])
                request.session['usernametrns'] = member.designation_id
                request.session['usernametrns1'] = member.fullname
                request.session['usernametrns2'] = member.id
                request.session['usernametrns3'] = member.team_id
                return render(request, 'traineesec.html', {'member': member})
            
        des = designation.objects.get(designation='trainingmanager')   
        if user_registration.objects.filter(email=email, password=password, designation_id=des.id,status="active").exists():
            member = user_registration.objects.get(
            email=request.POST['email'], password=request.POST['password'])
            request.session['usernametm'] = member.designation_id
            request.session['usernametm1'] = member.fullname
            request.session['usernametm2'] = member.id
            #request.session['usernamehr2'] = member.branch
            return render(request, 'dashsec.html', {'member': member})
            
        des1 = designation.objects.get(designation='trainer')
        if user_registration.objects.filter(email=email, password=password, designation_id=des1.id,status="active").exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['usernametrnr'] = member.designation_id
                request.session['usernametrnr1'] = member.fullname
                request.session['usernametrnr2'] = member.team_id
                request.session['usernametrnr2'] = member.id
                return render(request, 'trainersec.html', {'member': member})
    
        
        des3 = designation.objects.get(designation='account')       
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des3.id,status="active").exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['usernameacnt'] = member.designation_id
                request.session['usernameacnt1'] = member.fullname
                request.session['usernameacnt2'] = member.id
                return render(request, 'accountsec.html', {'member': member})
    
            
        manag = designation.objects.get(designation="manager")    
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=manag.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['m_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['usernamehr2'] = member.branch_id
                request.session['m_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                Num = user_registration.objects.count()
                Num1 = project.objects.count()
                Trainer = designation.objects.get(designation='trainer')
                trcount=user_registration.objects.filter(designation=Trainer).count()
                return render(request,'MAN_profiledash.html',{'mem':mem,'num':Num,'Num1':Num1,'trcount':trcount})
    
        Adm1 = designation.objects.get(designation="Admin")   
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Adm1.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Adm_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['usernamehr2'] = member.branch_id
                request.session['Adm_id'] = member.id 
                Adm=user_registration.objects.filter(id= member.id)
                Num = user_registration.objects.count()
                Num1 = project.objects.count()
                Trainer = designation.objects.get(designation='trainer')
                trcount=user_registration.objects.filter(designation=Trainer).count()
                return redirect('BRadmin_profiledash')
            
        design2 = designation.objects.get(designation="tester")   
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation_id=design2.id,status="active").exists():
               
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['usernamets'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['usernamehr2'] = member.branch_id
                request.session['usernametsid'] = member.id
                if request.session.has_key('usernamets'):
                    usernamets = request.session['usernamets']
                if request.session.has_key('usernamets1'):
                    usernamets1 = request.session['usernamets1']
                else:
                   return redirect('/')
                mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
                return render(request,'TSdashboard.html',{'mem':mem})
    
        design = designation.objects.get(designation="team leader")
        
      
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design.id,status="active").exists():
                 member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                 request.session['tlid'] = member.id
                 
                 return redirect('TLdashboard')
        
        design1 = designation.objects.get(designation="project manager")
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design1.id,status="active").exists():
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['prid'] = member.id
               
                return redirect('pmanager_dash')
            
        design3 = designation.objects.get(designation="developer")
        
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design3.id,status="active").exists():
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['devid'] = member.id
                
                return redirect('devdashboard')
        
        design4 = designation.objects.get(designation="hr")    
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design4.id,status="active").exists():
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['hr_id'] = member.id
                
                return redirect('HR_Dashboard')

        design8 = designation.objects.get(designation="Data Collector")    
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design8.id,status="active").exists():
                data_collector=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['datacollector_id'] = data_collector.id
                
                return redirect('DatacollectorDashboard')
            
        
        design7 = designation.objects.get(designation="auditor")    
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design7.id,status="active").exists():
                auduser=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['aud_id'] = auduser.id
                
                return redirect('Auditdashboard')


        # design5 = designation.objects.get(designation="Digital manager")    
        # if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design5.id,status="active").exists():
        #         dmmanager=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
        #         request.session['pm_id'] = dmmanager.id
                
        #         return redirect('dm_pmdashboard')
               
        # design6 = designation.objects.get(designation="Digital Developer")    
        # if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design6.id,status="active").exists():
        #         dmdev=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
        #         request.session['dmdev_id'] = dmdev.id
                
        #         return redirect('dm_devdashboard')

      
        
       
        else:
                context = {'msg_error': 'Invalid data'}
                return render(request, 'login.html', context)

       
    return render(request,'login.html')

#######################################################   training Manager   ##############################################
def Dashboard(request):
    if 'usernametm2' in request.session:

        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']

        mem = user_registration.objects.filter(id=usernametm2)
        des = designation.objects.get(designation="trainer")
        des1 = designation.objects.get(designation="trainee")
        le = leave.objects.filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0)

        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametm2)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'Dashboard.html', {'mem': mem, 'labels': labels, 'data': data, 'le': le})
    else:
        return redirect('/')
        
        
def Newtrainees(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        des = course.objects.all()
        dept = department.objects.all()
        team = create_team.objects.filter(~Q(team_status=1))
        mem1 = designation.objects.get(designation="trainee")
        batc= Batch.objects.filter(~Q(bt_status='1'))
        memm = user_registration.objects.filter(designation_id=mem1).order_by('-id')
        return render(request, 'Newtrainees.html', {'mem': mem, 'memm': memm, 'des': des, 'dept': dept, 'team': team,'batc':batc})
    else:
        return redirect('/')

def newtraineeesteam(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        tid = request.GET.get('tid')
        register = user_registration()
        des  = course.objects.all()
        dept = department.objects.all()
        team = create_team.objects.all()
        mem1 = designation.objects.get(designation="trainee")
        memm = user_registration.objects.filter(designation_id=mem1)
        
        if request.method == 'POST':
            register = user_registration.objects.get(id=tid)
            register.course =course.objects.get(id=int(request.POST['cou']))
            register.team =create_team.objects.get(id=int(request.POST['team']))
            register.department =department.objects.get(id=int(request.POST['dept']))
            bt=Batch.objects.get(batch_name=request.POST['batch'])
            register.startdate=bt.bt_start_date
            register.enddate=bt.bt_end_date
            users =  previousTeam()
            datesteam=create_team.objects.get(id=int(request.POST['team']))
            users.teamname = create_team.objects.get(id=int(request.POST['team']))
            users.user = user_registration.objects.get(id=tid)
            users.pstatus = 0
            users.tr_start_date=datesteam.startdate
            users.tr_end_date=datesteam.enddate
            users.save()
            register.save()
            return redirect('Newtrainees')
        return render(request, 'Newtrainees.html', {'memm': memm, 'des': des, 'dept': dept, 'team': team, })
    else:
        return redirect('/')

# def new_team(request):
#     if 'usernametm2' in request.session:
#         if request.session.has_key('usernametm'):
#             usernametm = request.session['usernametm']
#         if request.session.has_key('usernametm1'):
#             usernametm1 = request.session['usernametm1']
#         else:
#             return redirect('/')
#         mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
#         var = create_team.objects.all().order_by('-id')
#         des = designation.objects.get(designation='trainer')
#         var1 = user_registration.objects.filter(designation_id=des.id)
#         return render(request, 'new_team.html', {'mem': mem, 'var': var, 'var1': var1})
#     else:
#         return redirect('/')

def new_team(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        var = create_team.objects.filter(team_status=0).order_by('-id')
        des = designation.objects.get(designation='trainer')
        var1 = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'new_team.html', {'mem': mem, 'var': var, 'var1': var1})
    else:
        return redirect('/')

def team_trainee(request,tm_tnr):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        var = previousTeam.objects.filter(teamname_id=tm_tnr).order_by('-id')
        return render(request, 'new_team_trainees.html', {'mem': mem, 'var': var})
    else:
        return redirect('/')

def trainee_delete(request,tm_trainee):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        t= previousTeam.objects.get(id=tm_trainee)
        tm=t.teamname_id
        t.delete()
        var = previousTeam.objects.filter(teamname_id=tm).order_by('-id')
        return render(request, 'new_team_trainees.html', {'mem': mem, 'var': var})
    else:
        return redirect('/')

        
def new_team1(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        var = user_registration.objects.filter(designation_id=des.id)
        batc = Batch.objects.all()
        return render(request, 'new_team1.html', {'mem': mem, 'var': var,'batc':batc})
    else:
        return redirect('/')

def new_batch(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        batc = Batch.objects.all()
        return render(request, 'new_batch.html', {'mem': mem, 'batc': batc})
    else:
        return redirect('/')
        
        
# def newteamcreate(request):
    
#     if request.session.has_key('usernametm'):
#         usernametm = request.session['usernametm']
#     if request.session.has_key('usernametm1'):
#         usernametm1 = request.session['usernametm1']
#     else:
#         return redirect('/')
#     if request.method == 'POST':
#         team = request.POST['team']
#         trainer = request.POST.get('trainer')
#         tra= user_registration.objects.get(id=trainer)
#         try:
#             user = create_team.objects.get(name=team)
#             mem = user_registration.objects.filter(
#                 designation_id=usernametm) .filter(fullname=usernametm1)
#             context = {
#                 'msg': 'Team already exists!!!....  Try another name', 'mem': mem}
#             return render(request, 'new_team1.html', context)
#         except:
#             user = create_team(name=team, trainer=tra.fullname, progress=0,trainer_id=trainer)
#             user.save()
#     return redirect('new_team')


def newteamcreate(request):

    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    if request.method == 'POST':
        btc= request.POST['batch_name']
        team = request.POST['team']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        trainer = request.POST.get('trainer')
        tra= user_registration.objects.get(id=trainer)
        try:
            user = create_team.objects.get(name=team)
            mem = user_registration.objects.filter(
                designation_id=usernametm) .filter(fullname=usernametm1)
            context = {
                'msg': 'Team already exists!!!....  Try another name', 'mem': mem}
            return render(request, 'new_team1.html', context)
        except:
            user = create_team(bt_name=btc,name=team, trainer=tra.fullname, progress=0,trainer_id=trainer,startdate=startdate,enddate=enddate)
            user.save()
    return redirect('new_team')


def newbatchcreate(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    if request.method == 'POST':
        team = request.POST['batc']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        try:
            user = newbatchcreate.objects.get(name=team)
            mem = user_registration.objects.filter(
                designation_id=usernametm) .filter(fullname=usernametm1)
            context = {
                'msg': 'Batch already exists!!!....  Try another name', 'mem': mem}
            return render(request, 'new_batch.html', context)
        except:
            user = Batch(batch_name=team,bt_start_date=startdate,bt_end_date=enddate)
            user.save()
    return redirect('new_batch')

    
def batch_complete(request,pk):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        batc = Batch.objects.get(id=pk)
        batc.bt_status=1
        batc.save()
        batc = Batch.objects.all()
        return render(request, 'new_batch.html', {'mem': mem, 'batc': batc})
    else:
        return redirect('/')
        
    

def trainer_trainees_details(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'trainer_trainees_details.html', {'vars': vars, 'tre': tre,  'z': z, 'labels': labels, 'data': data,'k':k })
    else:
        return redirect('/')
        
        
        
def teamdelete(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')

    tid = request.GET.get('tid')
    var = create_team.objects.filter(id=tid)
    var.delete()
    return redirect("new_team")
        
def batchdelete(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')

    tid = request.POST.get('btid')
    bts = Batch.objects.get(id=tid)
    var = create_team.objects.filter(bt_name=bts.batch_name)
    var.delete()
    bts.delete()
    return redirect("new_batch")


def submit(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    tid = request.GET.get('tid')
    if request.method == 'POST':
        var1 = create_team.objects.get(id=tid)
        var1.team_status = 1
        
        var1.save()
    return redirect("new_team")

def trainee_submit(request,tr_sub_id):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    print(tr_sub_id)
    var1 = previousTeam.objects.get(id=tr_sub_id)
    var1.pstatus = 1
    var1.save()
    return redirect("team_trainee",var1.teamname.id)

# def teamupdate(request):
#     if request.session.has_key('usernametm'):
#         usernametm = request.session['usernametm']
#     if request.session.has_key('usernametm1'):
#         usernametm1 = request.session['usernametm1']
#     else:
#         return redirect('/')
#     if request.method == 'POST':
#         tid = request.GET.get('tid')
#         a= request.POST.get('trainer')
#         abc = create_team.objects.get(id=tid)
#         abc.name = request.POST.get('teams')
#         abc.trainer_id = request.POST.get('trainer')
#         tra= user_registration.objects.get(id=a)
#         abc.trainer = tra.fullname

#         abc.save()
#         return redirect('new_team')
#     else:
#         pass

def teamupdate(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    if request.method == 'POST':
        tid = request.GET.get('tid')
        a= request.POST.get('trainer')
        
        abc = create_team.objects.get(id=tid)
        abc.name = request.POST.get('teams')
        abc.trainer_id = request.POST.get('trainer')
        abc.startdate = request.POST.get('startdate')
        abc.enddate = request.POST.get('enddate')
        tra= user_registration.objects.get(id=a)
        abc.trainer = tra.fullname

        abc.save()
        return redirect('new_team')
    else:
        pass

def batchudate(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    if request.method == 'POST':
        tid = request.POST.get('batc')
    
        abc = Batch.objects.get(id=tid)
        abc.batch_name =request.POST.get('batchname')
        if request.POST.get('startdate'):
            abc.bt_start_date = request.POST.get('startdate')
        else:
            abc.bt_start_date = abc.bt_start_date 
        if request.POST.get('enddate'):
            abc.bt_end_date = request.POST.get('enddate')
        else:
             abc.bt_end_date =  abc.bt_end_date 
        abc.save()
        return redirect('new_batch')
    else:
        pass

def traineupdate(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    if request.method == 'POST':
        tid = request.POST.get('preid')
        tm = request.POST.get('tmid')
        ct = create_team.objects.get(id=tm)
       
        abc = previousTeam.objects.get(id=tid)
        abc.tr_start_date = request.POST.get('startdate')
        abc.tr_end_date = request.POST.get('enddate')
        abc.save()
        return redirect('team_trainee',ct.id)
    else:
        pass




def attendance_tm(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id)
    
        return render(request, 'attendance_tm.html',{'mem':mem})
    else:
        return redirect('/')
def Trainees_Calendar(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id)
        
        return render(request, 'Trainees_Calendar.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')

def Trainees_Attendancetable(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)   
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainee']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user).order_by('-id')
        return render(request, 'Trainees_Attendancetable.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
def Trainers_Calendar(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        vars = user_registration.objects.filter(designation=des.id)
        return render(request,'Trainers_Calendar.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
def Trainers_Attendancetable(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainer']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user).order_by('-id')  
    
        return render(request, 'Trainers_Attendancetable.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
    
def Trainee(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        tre = user_registration.objects.filter(designation=des.id, status="active").all().order_by('-id')
    
        return render(request, 'traineetable.html', {'tre': tre, 'vars': vars,'mem':mem})
    else:
        return redirect('/')
def reportedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'reportedissue.html', {'mem': mem})
    else:
        return redirect('/')
def reportissuetrainers(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'reportissuetrainers.html', {'mem': mem})
    else:
        return redirect('/')
def trainerunsolvedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
       
        cut = reported_issue.objects.filter(reported_to_id=usernametm2,designation_id=des.id,issuestatus=0)
        a=cut.count()
        
        context = {'cut': cut, 'vars': vars, 'mem': mem,'a':a}
        return render(request,'trainerunsolvedissue.html',context)
    else:
        return redirect('/')
def savetmreplaytrnr(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            
            
            vars.reply = request.POST['review']
            
            vars.issuestatus = 1
           
            
            vars.save()
        return redirect('reportissuetrainers')
    else:
        return redirect('/')
def trainersolvedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=1)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainersolvedissue.html',context)
    else:
        return redirect('/')
def reportissuetrainees(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request,'reportissuetrainees.html', {'mem': mem})
    else:
        return redirect('/')
def traineesunsolved(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=0)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'traineesunsolved.html', context)
    else:
        return redirect('/')

def savetmreplytrns(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            
            vars.reply = request.POST['reply']
            
            vars.issuestatus = 1
           
            vars.save()
        return redirect('reportissuetrainees')
    else:
        return redirect('/')
def traineessolved(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=1)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'traineessolved.html', context)
    else:
        return redirect('/')
def reportissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        
        des = designation.objects.get(designation='manager')
        des1 = designation.objects.get(designation='trainingmanager')
        # cut = user_registration.objects.get(designation_id=usernametm2)
        ree = user_registration.objects.get(designation_id=des.id)
        # ree1 = user_registration.objects.get(designation_id=usernametm)
    
        if request.method == 'POST':
          
            vars = reported_issue()
           
            vars.issue = request.POST['issue']
            
            vars.issuestatus = 0
            vars.reporter_id = usernametm2
            vars.designation_id = des1.id
            vars.reported_to = ree
            vars.reported_date = datetime.now()
            vars.save()
            return redirect('reportedissue')
    
        return render(request, 'reportissue.html', {'mem': mem})
    else:
        return redirect('/')
def reportedissuesub(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
     
        cut = reported_issue.objects.filter(reporter=usernametm2).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'reportedissuesub.html', context)

    else:
        return redirect('/')
def Applyleave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'Applyleave.html', {'mem': mem})
    else:
        return redirect('/')
def trainers_leave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'trainers_leave.html', {'mem': mem})
    else:
        return redirect('/')
def trainees_leave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'trainees_leave.html', {'mem': mem})
    else:
        return redirect('/')
def trainees_leavestatus(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainee')
        n = leave.objects.filter(designation_id=des.id).order_by('-id')
        return render(request, 'trainees_leavestatus.html', {'mem': mem,'n':n})
    else:
        return redirect('/')
def trainer_leavestatus(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainer')
        n = leave.objects.filter(designation_id=des.id).order_by('-id')
        
    
        return render(request, 'trainer_leavestatus.html', {'mem': mem ,'n': n})
    else:
        return redirect('/')
def Leave_rejected(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = leave.objects.get(id=id)       
            
            vars.leave_rejected_reason = request.POST['review']
            
            vars.leaveapprovedstatus = 2
           
            
            vars.save()
        return redirect('trainers_leave')
    else:
        return redirect('/')
def Trainee_Leave_rejected(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = leave.objects.get(id=id)       
            
            vars.leave_rejected_reason = request.POST['review']
            
            vars.leaveapprovedstatus = 2
           
            
            vars.save()
        return redirect('trainees_leave')
    else:
        return redirect('/')

def applyleavesub(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='manager')
        des1 = designation.objects.get(designation='trainingmanager')
        cut = user_registration.objects.get(id=usernametm2)
        ree = user_registration.objects.get(designation_id=des.id)
        ree1 = user_registration.objects.get(designation_id=usernametm)
        if request.method == 'POST':
            vars = leave()
            vars.from_date = request.POST['from']
            vars.to_date = request.POST['to']
            vars.reason = request.POST['reason']
            vars.leave_status = request.POST['haful']
            vars.leaveapprovedstatus = 0
            vars.user = cut
            vars.designation_id = des1.id
     
     
            start = datetime.strptime(vars.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(vars.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                vars.days = 1
            else:
                vars.days = diff - cnt
                
                
            vars.save()
            return redirect('Applyleave')
    
    
        return render(request,'applyleavesub.html', {'mem': mem})
    else:
        return redirect('/')

def Requestedleave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainingmanager')
        
        cut = leave.objects.filter(designation_id=des.id).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'Requestedleave.html', context)

    else:
        return redirect('/')
def trainers_leavelist(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        
    
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        cut = leave.objects.filter(designation_id=des.id).filter(leaveapprovedstatus=0).order_by('-id')
        
        
        
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainers_leavelist.html', context)
    else:
        return redirect('/')

       
def approvedstatus(request,id):
    a=leave.objects.get(id=id)
    a.leaveapprovedstatus=1
    a.save()
    return redirect('trainers_leave')

def approvedstatus_trainee(request,id):
    a=leave.objects.get(id=id)
    a.leaveapprovedstatus=1
    a.save()
    return redirect('trainees_leave')



def trainees_leavelist(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        # .objects.filter(reported_to_id=usernametm2)
        des = designation.objects.get(designation='trainee')
       
        cut = leave.objects.filter(designation_id=des.id).filter(leaveapprovedstatus=0).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainees_leavelist.html', context)

    else:
        return redirect('/')
def trainer(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(
            id=usernametm2)
        des = designation.objects.get(designation='trainer')
        vars = user_registration.objects.filter(designation=des.id).all().order_by('-id')
        context = {'vars': vars, 'mem': mem}
        return render(request,'trainer.html', context)
    else:
        return redirect('/')

def team1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        return render(request, 'Trainer_Team_manager.html', {'d': d, 'mem': mem})

    return redirect('/')
    
    
def current(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tm = create_team.objects.filter(trainer_id=d.id).filter(team_status=0).order_by('-id')
        des = designation.objects.get(designation='trainer')
        cut = user_registration.objects.filter(designation_id=des.id)
        vars = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'Trainer_Current_Team.html', {'vars': vars, 'des': des, 'tm': tm, 'cut': cut, 'mem': mem})
    else:
        return redirect('/')

def task(request, id):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(id=usernametm2)
        d = create_team.objects.get(id=id)
        return render(request,'Trainer_Current_task.html',{'d': d, 'mem': mem})
    else:
        return redirect('/')

def Trainer_Current_Assigned(request, id):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
      
    
        mem = user_registration.objects.filter(id=usernametm2)
        d = create_team.objects.get(id=id)
        vars = topic.objects.filter(team_id=d.id).order_by('-id')
        return render(request, 'Trainer_Current_Assigned.html', {'vars': vars, 'mem': mem})

    else:
        return redirect('/')
def Trainer_Currenttrainee(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = previousTeam.objects.filter(teamname_id=id)
       
        des = designation.objects.get(designation='trainee')
        # vars = user_registration.objects.filter(team=d.id,designation=des.id).order_by('-id')
        # .filter(designation=des.id)
        # for item in vars:
        #     import pdb;pdb.set_trace()
        #     item['avg']=(item['attitude']+item['creativity']+item['workperformance'])/100
    
    
        return render(request, 'Trainer_Currenttrainees.html', {'d': d, 'mem': mem})
    else:
        return redirect('/')
    
def Trainer_Currenttrainee_delete(request, id):
    
    d = previousTeam.objects.filter(id=id)
       
    d.delete()
    
    return redirect('trainer')

def Empdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team_id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []

        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'Trainer_Current_Empdetails.html', {'vars': vars, 'tre': tre, 'mem': mem, 'labels': labels, 'data': data,'k':k})
    else:
        return redirect('/')

def Trainer_Previousattendance(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
    
        return render(request, 'Trainer_Previousattendance.html', {'vars':vars,'mem': mem})
    else:
        return redirect('/')
def List(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user)
            
        return render(request,'Trainer_Current_AttendanceList.html',{'mem':mem,'vars': vars, 'atten':atten})

    else:
        return redirect('/')
def task1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.filter(user_id=d.id).order_by('-id')
    
        return render(request, 'Trainer_Current_task1.html', {'tsk': tsk, 'mem': mem})

    else:
        return redirect('/')
def tdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.get(id=d.id)
        return render(request, 'Trainer_Current_Taskdetails.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')

def Previous(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tm = create_team.objects.filter(trainer_id=d.id).filter(team_status=1)
        des = designation.objects.get(designation='trainer')
        cut = user_registration.objects.filter(designation_id=des.id)
        vars = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'Trainer_Previous_Team.html', {'vars': vars, 'des': des, 'tm': tm, 'cut': cut, 'mem': mem})
    else:
        return redirect('/')

def Previous_Task(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        return render(request, 'Trainer_Previous_Task.html', {'d': d, 'mem': mem})

    return redirect('/')
def Previous_Assigned(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        vars = topic.objects.filter(id=d.id)
        return render(request, 'Trainer_Previous_Assigned.html', {'vars': vars, 'mem': mem})

    else:
        return redirect('/')
def Trainer_Previous_Trainees(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(
            team=d.id).filter(designation=des.id).order_by('-id')
        vars1 = previousTeam.objects.filter(teamname=id)
        return render(request, 'Trainer_Previous_Trainees_manager.html', {'vars': vars, 'mem': mem,'vars1':vars1})

    else:
        return redirect('/')
def PEmpdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []

        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'Trainer_Previous_Empdetails.html', {'vars': vars, 'tre': tre, 'mem': mem, 'labels': labels, 'data': data,'k':k})
    else:
        return redirect('/')

def PAttendance(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
    
        return render(request, 'Trainer_Previous_Attendance.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
def PList(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user).order_by('-id')
        return render(request, 'Trainer_Previous_Attendance_List.html',{'mem':mem,'vars': vars, 'atten':atten})
    else:
        return redirect('/')
def Ptask1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.filter(user=d.id)
        return render(request, 'Trainer_Previous_Task1.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')

def Ptdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        tsk = trainer_task.objects.get(id=id)
        return render(request, 'Trainer_Previous_Taskdetails.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')
        
        
def traineedetails(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)

        vars = user_registration.objects.get(id=id)
        if vars.team :
            tre = create_team.objects.get(id=vars.team.id)
            k=user_registration.objects.get(id=tre.trainer_id)
        else:
           tre=NULL 
           k=NULL
       
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'traineedetails.html', {'mem': mem, 'vars': vars, 'tre': tre, 'labels': labels, 'data': data,'k':k})
    else:
        return redirect('/')


def taineestatuschange(request,pk):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        
        if request.method == 'POST':
    
            k=user_registration.objects.get(id=pk)
            k.trainee_status=request.POST['status_change']
            k.save()
            return redirect('Trainee')
    
    else:
        return redirect('/')
        
        
        
def statusTable(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars= user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user)
        
        return render(request,'trainee_statustable.html',{'mem':mem,'vars':vars, 'atten':atten})
    else:
        return redirect('/')
########################################################   trainers      ###############################################


def trainer_dashboard(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainee')
        le = leave.objects.filter(
            designation_id=des.id, leaveapprovedstatus=0).all()

        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametrnr2)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'trainer_dashboard.html', {'z': z, 'labels': labels, 'data': data, 'le': le})
    else:
        return redirect('/')


def trainer_applyleave(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2) 
        return render(request, 'trainer_applyleave.html', {'z': z})
    else:
        return redirect('/')

def trainer_applyleave_form(request):
    if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    z = user_registration.objects.filter(id=usernametrnr2)
    le = user_registration.objects.get(id=usernametrnr2)
    des1 = designation.objects.get(designation='trainer')
    
    if request.method == 'POST':
        mem = leave()
        mem.from_date = request.POST['from']
        mem.to_date = request.POST['to']
        mem.leave_status = request.POST['haful']
        mem.reason = request.POST['reason']
        mem.user = le
        mem.designation_id = des1.id
        mem.leaveapprovedstatus=0
        
        start = datetime.strptime(mem.from_date, '%Y-%m-%d').date() 
        end = datetime.strptime(mem.to_date, '%Y-%m-%d').date()

        diff = (end  - start).days
        
        cnt =  Event.objects.filter(start_time__range=(start,end)).count()
        
        if diff == 0:
            mem.days = 1
        else:
            mem.days = diff - cnt
            
            
        mem.save()
        return render(request, 'trainer_applyleave.html', {'z': z})
    return render(request, 'trainer_applyleave_form.html', {'z': z})
    

def trainer_traineesleave_table(request):
    if 'usernametrnr2' in request.session:
        
            
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
    
        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainee')
        tm = leave.objects.filter(designation_id=des.id) .all().order_by('-id')
        return render(request, 'trainer_traineesleave_table.html', {'tm': tm, 'z': z})
    else:
        return redirect('/')


def trainer_feedbacks(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)

        if request.method == 'POST':
         
            var = Feedbacks()
            
            # ree= user_registration.objects.get(designation_id=mem1)
            var.fb_from=user_registration.objects.get(id=usernametrnr2)
            var.fb_to = user_registration.objects.get(id=int(request.POST['fbname']))
            var.fb = request.POST['fb']
            var.save()
    
        return render(request, 'trainer_feedback.html', {'z': z})
    else:
        return redirect('/')

def trainer_give_feedback(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        
        tre = designation.objects.get(designation='trainee')
        use = user_registration.objects.filter(designation_id=tre.id)
    
        return render(request, 'trainer_givefeedback.html', {'z': z,'memteam':use})
    else:
        return redirect('/')

def trainer_given_feedback(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        n = Feedbacks.objects.filter(fb_from=usernametrnr2).order_by('-id')
    
        return render(request, 'trainer_givenfeedback.html', {'z': z,'n':n})
    else:
        return redirect('/')



def trainer_reportissue(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        return render(request, 'trainer_reportissue.html', {'z': z})
    else:
        return redirect('/')

# def trainer_reportissue_form(request):
#     if request.session.has_key('usernametrnr'):
#         usernametrnr = request.session['usernametrnr']
#     if request.session.has_key('usernametrnr1'):
#         usernametrnr1 = request.session['usernametrnr1']
#     if request.session.has_key('usernametrnr2'):
#         usernametrnr2 = request.session['usernametrnr2']
#     else:
#         return redirect('/')
#     z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
#         fullname=usernametrnr1) .filter(id=usernametrnr2)

#     mem = reported_issue()
#     des = designation.objects.get(designation='trainingmanager')
#     cut = user_registration.objects.get(designation_id=des.id)
#     mem1 = user_registration.objects.get(id=usernametrnr2)
#     des1 = designation.objects.get(designation='trainer')
#     print(mem1)
#     if request.method == "POST":
#         mem.issue = request.POST['issues']
#         mem.reported_date = datetime.now()
#         mem.reported_to = cut
#         mem.reporter = mem1
#         mem.designation_id = des1.id
#         mem.issuestatus =0
#         mem.save()
#         return render(request, 'trainer_reportissue.html', {'z': z})
#     return render(request, 'trainer_reportissue_form.html', {'mem': mem, 'z': z})
def trainer_reportissue_form(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        mem = reported_issue()
        des = designation.objects.get(designation='trainingmanager')
        cut = user_registration.objects.get(designation_id=des.id)
        mem1 = user_registration.objects.get(id=usernametrnr2)
        des1 = designation.objects.get(designation='trainer')
        
        if request.method == "POST":
            mem.issue = request.POST['issues']
            mem.reported_date = datetime.now()
            mem.reported_to = cut
            mem.reporter = mem1
            mem.designation_id = des1.id
            mem.issuestatus =0
            mem.save()
            return render(request, 'trainer_reportissue.html', {'z': z})
        return render(request, 'trainer_reportissue_form.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_reportedissue_table(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        des = designation.objects.get(designation='trainee')
        
        cut = reported_issue.objects.filter(reported_to_id=usernametrnr2).filter(
            designation_id=des.id).filter(issuestatus=0).order_by('-id')
    
        return render(request, 'trainer_reportedissue_table.html', {'cut': cut, 'vars': vars,  'z': z})
    else:
        return redirect('/')

def savereplaytnee(request, id):
    if request.method == 'POST':
        vars = reported_issue.objects.get(id=id)
        
        vars.reply = request.POST['reply']
        
        vars.issuestatus = 1
        vars.save()
    return redirect('trainer_reportedissue_table')


def trainer_myreportissue_table(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        rm = reported_issue.objects.filter(reporter_id=usernametrnr2).order_by('-id')
    
        return render(request, 'trainer_myreportissue_table.html', {'rm': rm, 'z': z})


    else:
        return redirect('/')
def trainer_topic(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
    
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_topic.html', {'z': z})
    else:
        return redirect('/')

def trainer_addtopic(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        uname = user_registration.objects.get(id=usernametrnr2)
        crt = create_team.objects.filter(trainer_id=uname.id,team_status=0)
        mem = topic()
        if request.method == 'POST':
            # mem = user_registration()
            mem.team_id = request.POST['select']
            mem.topic = request.POST['topic']
            mem.startdate = request.POST['start']
            mem.enddate = request.POST['end']
            mem.topic_status = 0
            mem.trainer_id = uname.id
            mem.save()
            return render(request, 'trainer_addtopic.html', {'mem': mem, 'crt': crt, 'z': z})
        return render(request, 'trainer_addtopic.html', {'mem': mem, 'crt': crt, 'z': z})
    else:
        return redirect('/')

def trainer_viewtopic(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
            
        if request.method=="POST":
            uid = request.POST.get('sts')
            tem_id = topic.objects.get(id=uid)
            tem_id.topic_status = 1
            tem_id.save()
            return redirect('trainer_viewtopic')
        else:      
            z = user_registration.objects.filter(id=usernametrnr2)
            mem = topic.objects.filter(trainer_id=usernametrnr2).order_by('-id')
            return render(request, 'trainer_viewtopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')
def trainer_attendance(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainees.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainer.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer_viewattendance(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainer_viewattendance.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer_viewattendancelist(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        
        z = user_registration.objects.filter(id=usernametrnr2)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=usernametrnr2).order_by('-id')
        return render(request, 'trainer_attendance_trainer_viewattendancelist.html',{'z':z,'atten':atten})
    else:
        return redirect('/')



def trainer_team(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_team.html', {'z': z})
    else:
        return redirect('/')

def trainer_currentteam(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')

        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tm = create_team.objects.filter(trainer_id=usernametrnr2).filter(
            team_status=0).order_by('-id')
        return render(request, 'trainer_current_team_list.html', {'tm': tm, 'z': z})
    else:
        return redirect('/')



def attenperform(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = create_team.objects.get(id=id)
        abc.progress = request.POST['sele']
        abc.save()
        return redirect('trainer_currentteam')
    else:
         return render(request,'trainer_current_team_list.html')


def trainer_currenttrainees(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        mem = user_registration.objects.filter(
            designation_id=des.id).filter(team_id=d).order_by('-id')
        return render(request, 'trainer_current_trainees_list.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_currenttraineesdetails(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=mem.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=mem.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'trainer_current_tainees_details.html', {'mem': mem, 'tre': tre, 'z': z, 'labels': labels, 'data': data, 'k':k})
    else:
        return redirect('/')


def trainer_currentattentable(request, id):
    if 'usernametrnr2' in request.session:
   
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=mem
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user).order_by('-id')
        return render(request, 'trainer_current_atten_table.html', {'mem': mem, 'z': z,'atten':atten})

    else:
        return render('/')
def trainer_currentperform(request, id):
    if 'usernametrnr2' in request.session:
   
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem.attitude = request.POST['sele1']
            mem.creativity = request.POST['sele2']
            mem.workperformance = request.POST['sele3']
            mem.save()
            return render(request, 'trainer_current_perform.html', {'mem': mem, 'z': z})
        return render(request, 'trainer_current_perform.html', {'mem': mem, 'z': z})
    else:
        return render('/')
        
        


def trainer_currentattenadd(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        atten = attendance()
        if request.method == 'POST':
            atten.date = request.POST['date']
            atten.user = mem
            atten.attendance_status = request.POST['pres']
            atten.save()
            return render(request, 'trainer_current_tainees_details.html', {'mem': mem, 'atten': atten, 'z': z})
        return render(request, 'trainer_current_atten_add.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_previousteam(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')

        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tm = create_team.objects.filter(trainer_id=usernametrnr2).filter(team_status=1).order_by('-id')
        return render(request, 'trainer_previous_team_list.html', {'tm': tm, 'z': z})
    else:
        return redirect('/')

def trainer_previoustrainees(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d)
        memm=previousTeam.objects.filter(teamname=d)
        return render(request, 'trainer_previous_trainess_list.html', {'mem': mem, 'z': z,'memm': memm})

    else:
        return redirect('/')
        
def trainer_previoustraineesdetails(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)

        tre = create_team.objects.get(id=mem.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=mem.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'trainer_previous_trainees_details.html', {'mem': mem, 'tre': tre, 'z': z, 'labels': labels, 'data': data,'k':k })

    else:
        return redirect('/')
        
        
        
def trainer_previousattentable(request, id):
    if 'usernametrnr2' in request.session:
        
        if  request.session.has_key('usernametrnr2'): 
             usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
    
        mem = user_registration.objects.get(id=id)
        att = attendance.objects.filter(user_id=mem.id).order_by('-id')
        return render(request, 'trainer_previous_atten_table.html', {'mem': mem, 'att': att, 'z': z})
    else:
        return redirect('/')

def trainer_previousperfomtable(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
      
        z = user_registration.objects.filter(id=usernametrnr2)
        num = user_registration.objects.get(id=id)
        return render(request, 'trainer_previous_performtable.html', {'num': num, 'z': z})
    else:
        return redirect('/')

def trainer_current_attendance(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        return render(request, 'trainer_current_attendance.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')


def trainer_Task(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_task.html', {'z': z})
    else:
        return redirect('/')

def trainer_teamlistpage(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tam = create_team.objects.filter(trainer_id=usernametrnr2, team_status=0).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)

        return render(request, 'trainer_teamlist.html', {'tam': tam, 'cut': cut, 'z': z})
    else:
        return redirect('/')

def trainer_taskpage(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
    
        return render(request, 'trainer_taskfor.html', {'d': d, 'z': z})
    else:
        return redirect('/')

def trainer_givetask(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        var = user_registration.objects.filter(team_id=d).filter(designation_id=des.id)
        
    
        
        if request.method == 'POST':
            list= request.POST.get('trainee_list')
            name = request.POST.get('taskname')
            desc = request.POST.get('description')
            files= request.FILES['files']
            start= request.POST.get('start')
            end = request.POST.get('end')
            task_status = 0
            tptype = request.POST.get('task_proj')
            team_name_id = d.id
         
    
            vars = trainer_task(user_id=list,taskname=name,description=desc,files=files,startdate=start,
                    enddate=end,task_status=task_status, team_name_id=team_name_id,task_type=tptype)
            vars.save()
            msg_success = "Task Assigned Successfully"
            return render(request, 'trainer_givetask.html', {'z': z, 'var': var, 'msg_success':msg_success})
        else:
            return render(request, 'trainer_givetask.html', {'z': z, 'var': var})

    else:
        return redirect('/')
    
def trainer_taskgivenpage(request, id):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
            
        correction=Trainer_Task_Correction.objects.all()    
        if request.method == 'POST':
            id = request.POST['uid']
            abc = trainer_task.objects.get(id=id)
            abc.task_progress = request.POST['sele']
            abc.save()
            msg_success = "progress added"
            return render(request,'trainer_taskgiven.html',{'msg_success':msg_success,'correction':correction})
        else:
            
            z = user_registration.objects.filter(id=usernametrnr2)
        
            
            d = create_team.objects.get(id=id)
            c = trainer_task.objects.filter(team_name_id=d.id)
            des = designation.objects.get(designation='trainee')
            mem1 = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).order_by('-id')
            mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).values_list('id')
            tsk = trainer_task.objects.filter(team_name_id=d.id).filter(user_id__in=mem).order_by('-id')
            
            return render(request, 'trainer_taskgiven.html', {'mem': mem,'mem1': mem1, 'tsk': tsk, 'z': z,'correction':correction})
    else:
        return redirect('/')
    

def trainer_task_statuschange(request,tr_tm_id):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
            
            
        if request.method == 'POST':
            id = request.POST['tskid']
            abc = trainer_task.objects.get(id=id)
            abc.task_status = '3'
            abc.save()
            msg_success = "Status Changed"
            task_coorection = Trainer_Task_Correction()
            task_coorection.task_id = abc
            task_coorection.correction_description = request.POST['c_dis']
            task_coorection.correctionfiles = request.FILES.get('c_file')
            task_coorection.save()
            correction=Trainer_Task_Correction.objects.all()

            z = user_registration.objects.filter(id=usernametrnr2)
            
            d = create_team.objects.get(id=tr_tm_id)
            c = trainer_task.objects.filter(team_name_id=d.id)
            des = designation.objects.get(designation='trainee')
            mem1 = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).order_by('-id')
            mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).values_list('id')
            tsk = trainer_task.objects.filter(team_name_id=d.id).filter(user_id__in=mem).order_by('-id')
            
            return render(request, 'trainer_taskgiven.html', {'mem': mem,'mem1': mem1, 'tsk': tsk, 'z': z,'msg_success':msg_success,'correction':correction})
    else:
        return redirect('/')

    

def trainer_taska(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_taska.html', {'z': z})
    else:
        return redirect('/')

def trainer_task_completed_teamlist(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(fullname=usernametrnr1).filter(id=usernametrnr2)
    
        tam = create_team.objects.filter(trainer=usernametrnr1,team_status = 1).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)
        
        return render(request, 'trainer_task_completed_teamlist.html',  {'z': z, 'cut':cut, 'tam':tam})
    else:
        return redirect('/')

def trainer_task_completed_team_tasklist(request, id):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
    
        d=create_team.objects.get(id=id)
        tsk = trainer_task.objects.filter(team_name_id=d.id).order_by('-id')
        return render(request, 'trainer_task_completed_team_tasklist.html', {'z': z, 'tsk':tsk})
    else:
        return redirect('/')

def trainer_task_previous_teamlist(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tam = create_team.objects.filter(trainer_id=usernametrnr2, team_status=1).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)

        return render(request, 'trainer_task_previous_teamlist.html', {'z': z, 'cut': cut, 'tam': tam})
    else:
        return redirect('/')

def trainer_task_previous_team_tasklist(request, id):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        
        d=create_team.objects.get(id=id)
        tsk = trainer_task.objects.filter(team_name_id=d.id).order_by('-id')
    
        return render(request, 'trainer_task_previous_team_tasklist.html', {'z': z, 'tsk':tsk})

    else:
        return redirect('/')
def trainer_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        return render(request, 'trainer_trainees.html', {'z': z})
    else:
        return redirect('/')

def trainer_current_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
    
        # import pdb;pdb.set_trace()
        
        z = user_registration.objects.filter(fullname=usernametrnr1,id=usernametrnr2) 
        cut = create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        
        des = designation.objects.get(designation='trainee')
        user = user_registration.objects.filter(designation_id=des.id,team_id__in=cut)
        
        return render(request, 'trainer_current_trainees.html', {'z': z, 'n': user})
    else:
        return redirect('/')
################################   NEW    ####################################

def trainer_paymentlist(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
        mem=acntspayslip.objects.filter(user_id=usernametrnr2).all().order_by('-id')
        
        return render(request, 'trainer_paymentlist.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def trainer_payment_viewslip(request,id,tid):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        names = acntspayslip.objects.all()
        
        
        return render(request, 'trainer_payment_viewslip.html', {'z': z,'user':user,'acc':acc})
    else:
        return redirect('/')

def trainer_payment_print(request,id,tid):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
        z = user_registration.objects.filter(id=usernametrnr2)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        
        
        return render(request, 'trainer_payment_print.html', {'z': z,'user':user,'acc':acc})
    else:
        return redirect('/')

def trainer_current_attendance_view(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        return render(request, 'trainer_current_attendance_view.html', {'mem': mem, 'z': z})

    else:
        return redirect('/')

def trainer_attendance_trainees_viewattendance(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(fullname=usernametrnr1) .filter(id=usernametrnr2)
        cut=create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id,team_id__in=cut)
        return render(request, 'trainer_attendance_trainees_viewattendance.html',{'z':z,'vars':vars})
    else:
        return redirect('/')

def trainer_attendance_trainees_viewattendancelist(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainee']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
        return render(request, 'trainer_attendance_trainees_viewattendancelist.html',{'z':z,'attend':attend})
    else:
        return redirect('/')

def trainer_attendance_trainees_addattendance(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(fullname=usernametrnr1) .filter(id=usernametrnr2)
        cut=create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id,team_id__in=cut)
       
    
        if request.method == 'POST':
            atten = attendance()
            atten.date = request.POST['date']
            atten.user_id =request.POST['sele']
            atten.attendance_status = request.POST['pres']
    
            atten.save()
        return render(request, 'trainer_attendance_trainees_addattendance.html',{'z':z,'vars':vars})
    else:
        return redirect('/')
    
########################################################   trainees       ###############################################
def trainee_dashboard_trainee(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametrns2)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
    
        
        return render(request, 'trainee_dashboard_trainee.html', {'z': z , 'labels': labels,'data': data,})
    else:
        return redirect('/')

def trainee_topic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request, 'trainee_topic.html', {'z': z})
    else:
        return redirect('/')

def trainee_currentTopic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        if request.session.has_key('usernametrns3'):
            usernametrns3 = request.session['usernametrns3']
       
        z = user_registration.objects.filter(id=usernametrns2)
        mem = topic.objects.filter(team_id=usernametrns3) .filter(topic_status=0).order_by('-id')
        return render(request, 'trainee_currentTopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def save_trainee_review(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        tid = request.GET.get('tid')
        vars = topic.objects.get(id=tid)
        
        vars.review = request.POST.get('review')
        vars.topic_status = 1
        
        vars.save()
        return redirect('trainee_currentTopic')
    else:
        return redirect('/')

def trainee_previousTopic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        if request.session.has_key('usernametrns3'):
            usernametrns3 = request.session['usernametrns3']
        else:
            return redirect('/')
        z = user_registration.objects.filter(id=usernametrns2)
        mem = topic.objects.filter(team_id=usernametrns3).filter(topic_status=1)
        return render(request, 'trainee_previousTopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_task(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request, 'trainee_task.html', {'z': z})
    else:
        return redirect('/')

def trainee_task_list(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        

        correction=Trainer_Task_Correction.objects.all()
        z = user_registration.objects.filter(id=usernametrns2)
        mem = trainer_task.objects.filter(Q(user_id=usernametrns2)).filter( Q(task_status=0) | Q(task_status=3)).order_by('-id')
        return render(request, 'trainee_task_list.html', {'mem': mem, 'z': z,'correction':correction})
    else:
        return redirect('/')

# def trainee_task_details(request,id):
#     if 'usernametrns2' in request.session:
        
#         if request.session.has_key('usernametrns2'):
#             usernametrns2 = request.session['usernametrns2']
        
#         z = user_registration.objects.filter(id=usernametrns2)
#         tid = request.GET.get('tid')
#         mem = trainer_task.objects.get(id=id)
#         if request.method == 'POST':
#             mem.user_description = request.POST['description']
#             mem.user_files = request.FILES['files']
#             mem.submitteddate = datetime.now()
#             mem.task_status=1
#             mem.save()
#             return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
#         return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
#     else:
#         return redirect('/')

def trainee_task_details(request, id):
    if 'usernametrns2' in request.session:

        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']

        z = user_registration.objects.filter(id=usernametrns2)
        tid = request.GET.get('tid')
        mem = trainer_task.objects.get(id=id)
        de = mem.enddate
        if request.method == 'POST':
            akm = datetime.now().date()
            mem.user_description = request.POST['description']
            mem.user_files = request.FILES['files']
            mem.submitteddate = datetime.now()
           

            dee = (akm-de).days
            if dee <= 0:
                mem.delay=0
                mem.task_status = 1
                mem.save()
            else:
                mem.delay=(akm-de).days
                mem.task_status = 1
                mem.save()
            return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
        return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_completed_taskList(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        mem = trainer_task.objects.filter(user_id=usernametrns2).filter(task_status=1).order_by('-id')
        return render(request, 'trainee_completed_taskList.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_reported_issue(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        n = reported_issue.objects.filter(reporter_id=usernametrns2).order_by('-id')
        return render(request, 'trainee_reported_issue.html', {'n': n, 'z': z})
    else:
        return redirect('/')

def trainee_given_feedback(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        n = Feedbacks.objects.filter(fb_from=usernametrns2).order_by('-id')
        return render(request, 'trainee_given_feedback.html', {'n': n, 'z': z})
    else:
        return redirect('/')


def trainee_report_reported(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
    
        
    
        z=user_registration.objects.filter(designation_id=usernametrns).filter(id=usernametrns2)
        var = reported_issue()
        if request.method == 'POST':
         
    
            
            # ree= user_registration.objects.get(designation_id=mem1)
            var.designation_id=usernametrns
            var.reported_to = user_registration.objects.get(id=int(request.POST['reportto']))
            var.issue = request.POST['report']
            var.reporter_id = usernametrns2
            var.reported_date = datetime.now()
            var.issuestatus=0
            var.save()
            
            
        return render(request, 'trainee_report_reported.html', {'z':z})
    else:
        return redirect('/')

def trainee_feedbacks(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
    
        z=user_registration.objects.filter(designation_id=usernametrns).filter(id=usernametrns2)
       
        if request.method == 'POST':
         
            var = Feedbacks()
            
            # ree= user_registration.objects.get(designation_id=mem1)
            var.fb_from=user_registration.objects.get(id=usernametrns2)
            var.fb_to = user_registration.objects.get(id=int(request.POST['fbname']))
            var.fb = request.POST['fb']
            var.save()
            
            
        return render(request, 'trainee_feedback.html', {'z':z})
    else:
        return redirect('/')


def trainee_report_issue(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
        desi = designation.objects.get(designation='trainingmanager')
        mem3 = user_registration.objects.filter(designation_id=desi.id)
    
        
    
        team = create_team.objects.all()
        
        tre = designation.objects.get(designation='trainer')
        use = user_registration.objects.filter(designation_id=tre.id)
        
        
        
        
        return render(request, 'trainee_report_issue.html', {'list': mem3, 'memteam': use, 'z': z})
    else:
        return redirect('/')


def trainee_give_feedback(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
        
        team = create_team.objects.all()
        
        tre = designation.objects.get(designation='trainer')
        use = user_registration.objects.filter(designation_id=tre.id)
        

        
        return render(request, 'trainee_givefeedback.html', { 'memteam': use, 'z': z})
    else:
        return redirect('/')


def trainee_applyleave_form(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        if request.session.has_key('usernametrns1'):
            usernametrns1 = request.session['usernametrns1']
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        else:
            return redirect('/')
        z = user_registration.objects.filter(id=usernametrns2)
        le = user_registration.objects.get(id=usernametrns2)
        if request.method == 'POST':
            mem = leave()
            mem.from_date = request.POST['from']
            mem.to_date = request.POST['to']
            mem.leave_status = request.POST['haful']
            mem.reason = request.POST['reason']
            mem.user = le
            mem.designation_id=usernametrns
            mem.leaveapprovedstatus=0
            
            start = datetime.strptime(mem.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(mem.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                mem.days = 1
            else:
                mem.days = diff - cnt
                
                
            mem.save()
            return render(request, 'trainee_applyleave_form.html', {'z': z})
        return render(request, 'trainee_applyleave_form.html', {'z': z})
    else:
        return redirect('/')



def trainer_applyleave_cards(request):
   
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        return render(request, 'trainer_applyleave_cards.html',{'z' : z})
    else:
        return redirect('/')

def trainer_appliedleave(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainer')
        tm = leave.objects.filter(user_id=usernametrnr2).order_by('-id')
        
        return render(request, 'trainer_appliedleave.html',{'tm': tm, 'z': z})
    else:
        return redirect('/')

def logout4(request):
    if 'usernametrns2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
def logout2(request):
    if 'usernametrnr2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def logout3(request):
    if 'usernametm2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
 ############ attendence #############

def trainee_applyleave_cards(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
        
        return render(request, 'trainee_applyleave_cards.html',{'z' : z})
    else:
        return redirect('/')
def trainee_appliedleave(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2)
        lee = user_registration.objects.get(id=usernametrns2)
    
        des = designation.objects.get(designation='trainee')
        n = leave.objects.filter(user_id=lee.id) .all().order_by('-id')
        
        return render(request, 'trainee_appliedleave.html',{'z' : z,'n' : n})
    else:
        return redirect('/')

def Attendance(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainees_attendance.html',{'z':z})
    else:
        return redirect('/')
def trainees_attendance_viewattendance(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainees_attendance_viewattendance.html',{'z':z})
    else:
        return redirect('/')
def trainees_attendance_viewattendancelist(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2) 
        
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user=usernametrns2
            vars=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
           
        return render(request,'trainees_attendance_viewattendancelist.html',{'z':z,'vars':vars})
    else:
        return redirect('/')
    ##########################  Account ############################################
def account_tr_mg(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(id=usernametm2)
    
    
        return render(request, 'account_tr_mg.html', {'mem': mem})
    else:
        return redirect('/')
def imagechange_tr(request):
  
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('account_tr_mg')
    return render(request, 'account_tr_mg.html')

    





def account_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        z = user_registration.objects.filter(id=usernametrnr2)
    
    
        return render(request, 'account_trainer.html', {'z': z})
    else:
        return redirect('/')
def imagechange(request):
    
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filenamees']
        abc.save()
        return redirect('account_trainer')
    return render(request, 'account_trainer.html' )



def account_trainees(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
    
        return render(request, 'account_trainees.html', {'z': z})
    else:
        return redirect('/')

def imagechange_trainees(request):
    
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filenamees']
        abc.save()
        return redirect('account_trainees')
    return render(request, 'account_trainees.html' )






###################################  change password ################################  

def changepassword_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametrnr2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'trainer_dashboard.html', {'z': z})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'changepassword_trainer.html', {'z': z})
    
        return render(request, 'changepassword_trainer.html', {'z': z})
    
    else:
        return redirect('/')
        

def changepassword_tr_mg(request):
    if 'usernametm2' in request.session:
       
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
       
        mem = user_registration.objects.filter(id=usernametm2)
    
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametm2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'Dashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'changepassword_tr_mg.html', {'mem': mem})
    
        return render(request, 'changepassword_tr_mg.html', {'mem': mem})

    else:
        return redirect('/')

def changepassword_trainees(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
    
        z = user_registration.objects.filter(id=usernametrns2)
    
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametrns2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'trainee_dashboard_trainee.html', {'z': z})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
                
    
            return render(request, 'changepassword_trainees.html', {'z': z})
    
        return render(request, 'changepassword_trainees.html', {'z': z})
    else:
        return redirect('/')

############################################# Amal ###########################################################
def Admlogout(request):
    if 'Adm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def Mnlogout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
        
@csrf_exempt
def BRadmin_emp_ajax(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        br_id = department.objects.get(id=dept_id)
        Desig = user_registration.objects.filter(branch_id=br_id.branch_id, designation=desigId, status="active")

        return render(request,'BRadmin_emp_ajax.html',{'Adm': Adm,'Desig': Desig,})
    else:
        return redirect('/')
        
@csrf_exempt
def BRadmin_designations(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        
        
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="manager"),~Q(designation="project manager"),~Q(designation="tester"),~Q(designation="trainingmanager"),~Q(designation="trainer"),~Q(designation="trainee"),~Q(designation="account"),~Q(designation="hr")).filter(branch_id=br_id.branch_id)
        return render(request,'BRadmin_designations.html',{'Adm': Adm,'Desig': Desig, })
    else:
        return redirect('/')

#********************Admin account setting****************************
def BRadmin_accsetting(request):
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_accsetting.html', {'Adm': Adm})
    else:
        return redirect('/')

def BRadmin_accsettingimagechange(request,id):
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('BRadmin_accsetting')
        return render(request, 'BRadmin_accsetting.html',{'Adm':Adm})
    else:
        return redirect('/')

#********************Manager account setting****************************

def MAN_accsetting(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_accsetting.html', {'mem': mem})
    else:
        return redirect('/')

def MAN_accsettingimagechange(request,id):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('MAN_accsetting')
        return render(request, 'MAN_accsetting.html',{'mem':mem})
    else:
        return redirect('/')


#***************Admin change password*****************
def BRadmin_changepwd(request):
    
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']     
        Adm = user_registration.objects.filter(id=Adm_id)     
        if request.method == 'POST':
            abc = user_registration.objects.get(id=Adm_id)
            cur = abc.password
            oldps = request.POST["currentPassword"]
            newps = request.POST["newPassword"]
            cmps = request.POST["confirmPassword"]
            if oldps == cur:
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request, 'BRadmin_profiledash.html', {'Adm': Adm})
                elif oldps == newps:
                    messages.add_message(request, messages.INFO, 'Current and New password same')
                else:
                    messages.info(request, 'Incorrect password same')

                return render(request, 'BRadmin_profiledash.html', {'Adm': Adm})
            else:
                messages.add_message(request, messages.INFO, 'old password wrong')
                return render(request, 'BRadmin_changepwd.html', {'Adm': Adm})
        return render(request, 'BRadmin_changepwd.html', {'Adm': Adm})         
    else:
        return redirect('/')

#***************Manager change password*****************

def MAN_changepwd(request):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=m_id)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'MAN_profiledash.html', {'mem': mem})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'MAN_changepwd.html', {'mem': mem})
    
        return render(request, 'MAN_changepwd.html', {'mem': mem})
    
    else:
        return redirect('/')


#***********************anandu*****************************************
def MAN_index(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_index.html',{'mem':mem})
    else:
        return redirect('/') 

def MAN_profiledash(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Num = user_registration.objects.count()
        Num1 = project.objects.count()
        Trainer = designation.objects.get(designation='Trainer')
        trcount=user_registration.objects.filter(designation=Trainer).count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation = Man1)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=m_id)
        for i in queryset:
                labels=[i.workperformance,i.attitude,i.creativity]
                data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'MAN_profiledash.html',{'labels':labels,'data':data,'Man1':Man2,'mem':mem,'num':Num,'trcount':trcount,'Num1':Num1})   
    else:
        return redirect('/') 
        
def MAN_employees(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Dept = department.objects.all()
        return render(request,'MAN_employees.html',{'mem':mem,'Dept':Dept})
    else:
        return redirect('/')
        
def MAN_python(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        Dept = department.objects.get(id = id)
        deptid=id
        mem = user_registration.objects.filter(id=m_id)
        Desig = designation.objects.all()
        return render(request,'MAN_python.html',{'mem':mem,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')

def MAN_projectman(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did).order_by("-id")
        return render(request,'MAN_projectman.html',{'pro_man_data':Project_man_data,'mem':mem,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
        
def MAN_proname(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Project_man_data = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'MAN_proname.html',{'labels':labels,'data':data,'pro_man_data':Project_man_data,'mem':mem})
    else:
        return redirect('/')
        
def MAN_proinvolve(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
        return render(request,'MAN_proinvolve.html',{'pro_data':Pro_data,'mem':mem})
    else:
        return redirect('/')
        
def MAN_promanatten(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        id = id
        return render(request, 'MAN_promanatten.html',{'mem':mem,'id':id})
    else:
        return redirect('/')

def MAN_promanattendsort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'MAN_promanattendsort.html',{'mem1':mem1,'mem':mem,'id':id})
    else:
        return redirect('/')     


def BRadmin_index(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_index.html',{'mem':mem})
    else:
        return redirect('/')
    
def BRadmin_profiledash(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Num = user_registration.objects.filter(status="active").count()
        Num1 = project.objects.count()
        lead_count = Leads_Register.objects.count()
        Trainer = designation.objects.get(designation='Trainer')
        trcount = user_registration.objects.filter(designation=Trainer).count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation=Man1)
        des = designation.objects.get(designation="trainee")
        le = leave.objects.filter(
            leaveapprovedstatus=0).exclude(designation_id=des.id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=Adm_id)

        tlde=designation.objects.get(designation='team leader')
        d=designation.objects.get(designation='developer')
        l=leave.objects.filter(to_date__gte=date.today())
       
        count=user_registration.objects.filter(~Q(id__in=l.values_list('user_id', flat=True)),Q(designation_id=tlde.id) | Q(designation_id=d.id),status="active",work_status='0').count()
       
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'BRadmin_profiledash.html', {'labels': labels, 'data': data, 'Num1': Num1, 'Man1': Man2, 'Adm': Adm, 'num': Num, 'trcount': trcount, 'le': le,'count':count,'lead_count':lead_count})
    else:
        return redirect('/')


# Display the count of not work assigned developers

def BRadmin_Work_not_assign(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        tlde=designation.objects.get(designation='team leader')
        d=designation.objects.get(designation='developer')
        l=leave.objects.filter(to_date__gte=date.today())
       
        dev=user_registration.objects.filter(~Q(id__in=l.values_list('user_id', flat=True)),Q(designation_id=tlde.id) | Q(designation_id=d.id),status="active",work_status='0')
       
        pmde=designation.objects.get(designation='project manager')
        tl=user_registration.objects.filter(designation=tlde)
        pman=user_registration.objects.filter(designation=pmde)
        req=WorkRequest.objects.filter(wrkreq_date=date.today())
        return render(request, 'BRadmin_Work_not_assign.html', {'Adm': Adm,'dev':dev,'tl':tl,'pman':pman,'req':req})
    else:
        return redirect('/')


def BRadminleaveupdate(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        if request.method =='POST':
        
            p = user_registration.objects.get(id=request.POST['pmname'])
            t = user_registration.objects.get(id=request.POST['tlname'])
            d = user_registration.objects.get(id=request.POST['devname'])
            try:
                ls=leave.objects.get(user=p,to_date__gte=date.today())
            except leave.DoesNotExist:
                lea=leave()
                lea.user=p
                lea.from_date=date.today()
                lea.to_date=date.today()
                lea.reason='Work not Assign'
                lea.days=1
                lea.leave_status='full Day'
                lea.save()
            try:
                ls=leave.objects.get(user=t,to_date__gte=date.today())
            except leave.DoesNotExist:
                lea1=leave()
                lea1.user=t
                lea1.from_date=date.today()
                lea1.to_date=date.today()
                lea1.reason='Work not Assign'
                lea1.days=1
                lea1.leave_status='full Day'
                lea1.save()
            try:
                req=WorkRequest.objects.get(wrk_develp=d,wrkreq_date=date.today())
            except WorkRequest.DoesNotExist:
                lea2=leave()
                lea2.user=d
                lea2.from_date=date.today()
                lea2.to_date=date.today()
                lea2.reason='Work not Assign'
                lea2.days=1
                lea2.leave_status='full Day'
                lea2.save()
            

            return redirect('BRadmin_profiledash')

    else:
        return redirect('/')



def BRadmin_employees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Dept = department.objects.all()
        return render(request,'BRadmin_employees1.html',{'Adm':Adm,'Dept':Dept})
    else:
        return redirect('/')

def BRadmin_python(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Dept = department.objects.get(id = id)
        deptid=id
        Adm = user_registration.objects.filter(id=Adm_id)
        Desig = designation.objects.all()
        return render(request,'BRadmin_python.html',{'Adm':Adm,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')
        
def BRadmin_projectman(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did,status="active").order_by("-id")
        return render(request,'BRadmin_projectman.html',{'pro_man_data':Project_man_data,'Adm':Adm,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
        
def BRadmin_proname(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Project_man_data = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'BRadmin_proname.html',{'labels':labels,'data':data,'pro_man_data':Project_man_data,'Adm':Adm})
    else:
        return redirect('/')
        
def BRadmin_proinvolve(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
        return render(request,'BRadmin_proinvolve.html',{'pro_data':Pro_data,'Adm':Adm})
    else:
        return redirect('/')
        
def BRadmin_promanatten(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        return render(request, 'BRadmin_promanatten.html',{'Adm':Adm,'id':id})
    else:
        return redirect('/')

def BRadmin_promanattendsort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id).order_by('-id')
        return render(request, 'BRadmin_promanattendsort.html',{'mem1':mem1,'Adm':Adm,'id':id})
    else:
        return redirect('/') 


#***********************praveen************************
def BRadmin_trainerstable(request,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Dept = department.objects.get(id = did)
        deptid=did
        Adm = user_registration.objects.filter(id=Adm_id)
        Trainer = designation.objects.get(designation='Trainer')
        # Trainer = designation.objects.get(id=id)
        trainers_data=user_registration.objects.filter(designation=Trainer).filter(department=did)
        topics=topic.objects.all()
        return render(request,'BRadmin_trainerstable.html',{'Adm':Adm,'trainers_data':trainers_data,'topics':topics,'Dept':Dept,'deptid':deptid})
    else:
        return redirect('/')

    
def BRadmin_Training(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        #team=create_team.objects.filter(user_id=id)
        #return render(request,'BRadmin_Training.html',{'team':team})
            #team=create_team.objects.all()
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all().order_by('-id')
        return render(request,'BRadmin_Training.html',{'team':team,'user':user,'Adm':Adm})
    else:
        return redirect('/') 
    
def BRadmin_trainingteam1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=previousTeam.objects.filter(teamname_id=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'BRadmin_trainingteam1.html',{'id':id,'num':num,'num1':num1,'Adm':Adm})
    else:
        return redirect('/') 
    
def BRadmin_traineestable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=previousTeam.objects.filter(teamname_id=id)
        return render(request,'BRadmin_traineestable.html',{'trainees_data':trainees_data,'Adm':Adm}) 
    else:
        return redirect('/') 
        
def BRadmin_trainingprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        trainees_data=user_registration.objects.get(id=id)
        #Trainee = designation.objects.get(designation='Trainee')
        #trainees_data=user_registration.objects.filter(designation=Trainee)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(task_status='1').count()
        return render(request,'BRadmin_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'Adm':Adm})
    else:
        return redirect('/') 
        
def BRadmin_completedtasktable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user).order_by('-id')
        return render(request,'BRadmin_completedtasktable.html',{'task_data':task,'Adm':Adm})   
    else:
        return redirect('/')
        
def BRadmin_topictable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        topics=topic.objects.filter(team=id).order_by("-id")
        return render(request,'BRadmin_topictable.html',{'topics':topics,'Adm':Adm})
    else:
        return redirect('/')

def MAN_trainerstable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.get(id=id)
        Trainer = designation.objects.get(designation='Trainer')
        trainers_data=user_registration.objects.filter(designation=Trainer).filter(department=id).order_by("-id")
        topics=topic.objects.all()
        return render(request,'MAN_trainerstable.html',{'trainers_data':trainers_data,'topics':topics,'mem':mem,'departments':departments})
    else:
        return redirect('/')
        
def MAN_Training(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        #team=create_team.objects.filter(user_id=id)
        #return render(request,'BRadmin_Training.html',{'team':team})
            #team=create_team.objects.all()
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'MAN_Training.html',{'team':team,'user':user,'mem':mem})
    else:
        return redirect('/')
        
def MAN_trainingteam1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'MAN_trainingteam1.html',{'id':id,'num':num,'num1':num1,'mem':mem})
    else:
        return redirect('/')
        
def MAN_traineestable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
        return render(request,'MAN_traineestable.html',{'trainees_data':trainees_data,'mem':mem}) 
    else:
        return redirect('/')
        
def MAN_trainingprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        trainees_data=user_registration.objects.get(id=id)
        #Trainee = designation.objects.get(designation='Trainee')
        #trainees_data=user_registration.objects.filter(designation=Trainee)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(status='Completed').count()
        return render(request,'MAN_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'mem':mem})
    else:
        return redirect('/')
        
def MAN_completedtasktable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'MAN_completedtasktable.html',{'task_data':task,'mem':mem})
    else:
        return redirect('/')
        
def MAN_topictable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        topics=topic.objects.filter(team=id).order_by("-id")
        return render(request,'MAN_topictable.html',{'topics':topics,'mem':mem})
    else:
        return redirect('/')



#*******************    anwar     ****************************

def BRadmin_View_Trainers(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
        return render(request,'BRadmin_View_Trainers.html', {'Adm':Adm,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')

def BRadmin_View_Trainerprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Trainerprofile.html', {'Adm':Adm,'user_registration':userreg})
    else:
        return redirect('/')

def BRadmin_View_Currenttraineesoftrainer(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'BRadmin_View_Currenttraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def BRadmin_View_Previoustraineesoftrainer(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'BRadmin_View_Previoustraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineeprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Currenttraineeprofile.html', {'Adm':Adm,'user_registration':userreg})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineetasks(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'BRadmin_View_Currenttraineetasks.html',{'Adm':Adm,'trainer_task':tasks})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineeattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Currenttraineeattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineeprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Previoustraineeprofile.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineetasks(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)
        return render(request,'BRadmin_View_Previoustraineetasks.html',{'Adm':Adm,'trainer_task':tasks})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineeattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Previoustraineeattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Trainerattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Trainerattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewTrainerattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Trainerattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewCurrenttraineeattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Currenttraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewPrevioustraineeattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Previoustraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def admin_page1(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == "POST":
            empname1=request.POST.get('empname')
            atten=attendance.objects.filter(user_id=empname1).order_by('-id')
            return render(request,'BRadmin_attendanceshow.html',{'Adm':Adm,'atten':atten,'empname1':empname1}) 
        dpt=department.objects.all()
        dsg=designation.objects.all()
        userreg=user_registration.objects.all()
        return render(request,'BRadmin_attendance.html', {'Adm':Adm,'department':dpt,'designation':dsg,'user_registration':userreg})  
    else:
        return redirect('/')

def admin_page3(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        return render(request,'BRadmin_attendanceshow.html',{'Adm':Adm}) 
    else:
        return redirect('/')

def admin_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.all()
    return render(request, 'BRadmin_designation.html', {'Desig': Desig,'departments':departments})

def admin_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects        .filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
    
    
    return render(request, 'BRadmin_employee.html',{'user':user,'dept':dept,'desi':desi})

def MAN_View_Trainers(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
        return render(request,'MAN_View_Trainers.html', {'mem':mem,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')

def MAN_View_Trainerprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Trainerprofile.html', {'mem':mem,'user_registration':userreg})
    else:
        return redirect('/')

def MAN_View_Currenttraineesoftrainer(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
       
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='Trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'MAN_View_Currenttraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def MAN_View_Previoustraineesoftrainer(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
       
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='Trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'MAN_View_Previoustraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def MAN_View_Currenttraineeprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Currenttraineeprofile.html', {'mem':mem,'user_registration':userreg})
    else:
        return redirect('/')

def MAN_View_Currenttraineetasks(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'MAN_View_Currenttraineetasks.html',{'mem':mem,'trainer_task':tasks})
    else:
        return redirect('/')

def MAN_View_Currenttraineeattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Currenttraineeattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Previoustraineeprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Previoustraineeprofile.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Previoustraineetasks(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)
        return render(request,'MAN_View_Previoustraineetasks.html',{'mem':mem,'trainer_task':tasks})
    else:
        return redirect('/')

def MAN_View_Previoustraineeattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Previoustraineeattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Trainerattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Trainerattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewTrainerattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Trainerattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewCurrenttraineeattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Currenttraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewPrevioustraineeattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Previoustraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_dev_attendance(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_dev_attendance.html') 
    else:
        return redirect('/')
       

def man_page1(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == "POST":
            empname1=request.POST.get('empname')
            atten=attendance.objects.filter(user_id=empname1)
            return render(request,'MAN_attendanceshow.html',{'mem':mem,'atten':atten,'empname1':empname1}) 
        dpt=department.objects.all()
        dsg=designation.objects.all()
        userreg=user_registration.objects.all()
        return render(request,'MAN_attendance.html', {'mem':mem,'department':dpt,'designation':dsg,'user_registration':userreg}) 
    else:
        return redirect('/')

def man_page3(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        # mem = user_registration.objects.filter(id=m_id)
        
        
        return render(request,'MAN_attendanceshow.html') 
    else:
        return redirect('/')
   
def man_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.filter( ~Q(designation="admin"), ~Q(designation="manager"))
    return render(request, 'MAN_designation.html', {'Desig': Desig,'departments':departments})


def man_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id, department_id=dept_id, status="active")
    
    
    return render(request, 'MAN_employee.html',{'user':user,'dept':dept,'desi':desi})

#************************  anwar end  *********************************************


 # current projects- sharon
def BRadmin_pythons(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        return render(request,'BRadmin_projects.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_dept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        depart =department.objects.all()
        return render(request,'BRadmin_dept.html',{'proj_det':project_details,'department':depart,'Adm':Adm})
    else:
        return redirect('/')


def BRadmin_leads(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        depart =department.objects.all()
        return render(request,'BRadmin_leads.html',{'proj_det':project_details,'department':depart,'Adm':Adm})
    else:
        return redirect('/')


def BRadmin_currentleads(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        leads=Leads_Register.objects.filter(Q(r_type_status='') | Q(r_type_status=1),r_status=3)
        return render(request,'BRadmin_currentleads.html',{'leads':leads,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_watingleads(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        leads=Leads_Register.objects.filter(r_type_status=2)
        return render(request,'BRadmin_watingleads.html',{'leads':leads,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_confirmedleads(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        leads=Leads_Register.objects.filter(r_status=1)
        return render(request,'BRadmin_confirmedleads.html',{'leads':leads,'Adm':Adm})
    else:
        return redirect('/')
    


def BRadmin_internshipleads(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        leads=Leads_Register.objects.filter(r_type='Internship')
        return render(request,'BRadmin_internship_jobleads.html',{'leads':leads,'Adm':Adm})
    else:
        return redirect('/')
    
def BRadmin_jobleads(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        leads=Leads_Register.objects.filter(r_type='job')
        return render(request,'BRadmin_internship_jobleads.html',{'leads':leads,'Adm':Adm})
    else:
        return redirect('/')
# def BRadmin_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'BRadmin_profiledash.html',{'proj_det':project_details,'num':Num})

def BRadmin_projects(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Num= project.objects.filter(~Q(status='Completed'),~Q(status='Rejected')).filter(department=id).count()
        num= project.objects.filter(status='Completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'BRadmin_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_list(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(~Q(status='Completed'),department_id=id)
        return render(request,'BRadmin_proj_list.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_det(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        proj=DM_projects.objects.all()
        return render(request,'BRadmin_proj_det.html',{'proj_det':project_details,'Adm':Adm,'proj':proj})
    else:
        return redirect('/')

def BRadmin_proj_mngrs(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_mngrs.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1)
        return render(request,'BRadmin_proj_mangrs1.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs2(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project_taskassign.objects.filter(project_id=id)
        # proj1=project_details.designation_id
        # dept_id=project_details.department_id
        # user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'BRadmin_proj_mangrs2.html',{'project_details':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_daily_report(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id) 
        proj_name =  project_taskassign.objects.all()
        tester_name = user_registration.objects.all()
        tester = tester_status.objects.filter(user_id=id)
        return render(request,'BRadmin_daily_report.html',{'Adm':Adm,'test':tester, 'tester_name':tester_name, 'proj_name':proj_name})
    else:
        return redirect('/')

def BRadmin_developers(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(id=id)
        project_task = project_taskassign.objects.filter(project_id = project_details).filter(tl_id=id)
        user_det=user_registration.objects.filter(tl_id=id).order_by("-id")
        progress_bar= tester_status.objects.all()
        return render(request,'BRadmin_developers.html',{'Adm':Adm,'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'user_det':user_det})
    else:
        return redirect('/')

# completed projects- subeesh
 
def BRadmin_proj_cmpltd_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details=project.objects.filter(department=id)
        
        return render(request,'BRadmin_proj_cmpltd_show.html',{'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_cmpltd_proj_det_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_cmpltd_proj_det_show.html',{'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mngrs_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_mngrs_show.html', {'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs1_new(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1).order_by("-id")
        return render(request,'BRadmin_proj_mangrs1_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
        
    else:
        return redirect('/')

def BRadmin_proj_mangrs2_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'BRadmin_proj_mangrs2_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
        
    else:
        return redirect('/')

def BRadmin_developers_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'BRadmin_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_daily_report_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'BRadmin_daily_report_show.html', {'project':project_task,'tester_status':tester,'Adm':Adm})
    else:
        return redirect('/')






 # current projects-sharon -manager module
def MAN_pythons(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.all()
        return render(request,'MAN_projects.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_dept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.all()
        depart =department.objects.all()
        return render(request,'MAN_dept.html',{'proj_det':project_details,'department':depart,'mem':mem})
    else:
        return redirect('/')
    
# def MAN_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'MAN_profiledash.html',{'proj_det':project_details,'num':Num})

def MAN_projects(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Num= project.objects.filter(status='accepted').filter(department=id).count()
        num= project.objects.filter(status='completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'MAN_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_list(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.filter(department=id)
        
        return render(request,'MAN_proj_list.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_det(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_det.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mngrs(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_mngrs.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mangrs1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1)
        return render(request,'MAN_proj_mangrs1.html',{'user_det':user_det,'proj_det':project_details,'mem':mem,'proj1':proj1})
    else:
        return redirect('/')

def MAN_proj_mangrs2(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'MAN_proj_mangrs2.html',{'user_det':user_det,'proj_det':project_details,'mem':mem,'proj1':proj1})
    else:
        return redirect('/')

def MAN_daily_report(request,id): 
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        proj_name =  project_taskassign.objects.all()
        tester_name = user_registration.objects.all()
        tester = tester_status.objects.filter(user_id=id)
        return render(request,'MAN_daily_report.html',{'proj_name':proj_name,'test':tester,'mem':mem,'tester_name':tester_name})
    else:
        return redirect('/')

def MAN_developers(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.filter(id=id) 
        project_task = project_taskassign.objects.filter(project_id = project_details).filter(tl_id = id)
        user_det=user_registration.objects.filter(tl_id=id).order_by("-id")
        progress_bar= tester_status.objects.all()
        return render(request,'MAN_developers.html',{'user_det':user_det,'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'mem':mem})
    else:
        return redirect('/')

# completed projects- subeesh -manager module
  
def MAN_proj_cmpltd_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details=project.objects.filter(department=id)
        
        return render(request,'MAN_proj_cmpltd_show.html',{'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_cmpltd_proj_det_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_cmpltd_proj_det_show.html',{'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mngrs_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_mngrs_show.html', {'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mangrs1_new(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1).order_by("-id")
        return render(request,'MAN_proj_mangrs1_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'mem':mem})
        
    else:
        return redirect('/')

def MAN_proj_mangrs2_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'MAN_proj_mangrs2_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'mem':mem})
        
    else:
        return redirect('/')

def MAN_developers_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'MAN_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'mem':mem})
    else:
        return redirect('/')

def MAN_daily_report_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'MAN_daily_report_show.html', {'project':project_task,'tester_status':tester,'mem':mem})
    else:
        return redirect('/')
        
def MAN_training_department(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.all()
        return render(request, 'MAN_training_department.html',{'department':departments,'mem':mem})
    else:
        return redirect('/')
############## end ##########


#reported issue- akhil-admin mod

def BRadmin_Reportedissue_department(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        departments=department.objects.all()
        return render(request, 'BRadmin_Reportedissue_department.html',{'department':departments,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_Reportedissue(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        departments=department.objects.get(id=id)
        deptid=id
        designations=designation.objects.filter(~Q(designation="admin"))
        return render(request, 'BRadmin_Reportedissue.html',{'Adm':Adm,'department':departments,'designation':designations,'dept_id':deptid})
    else:
        return redirect('/')

def BRadmin_ReportedissueShow(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        reported_issues=reported_issue.objects.all()
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation=designations).filter(department=did).order_by("-id")
        return render(request,'BRadmin_ReportedissueShow.html',{'Adm':Adm,'designation':designations,'reported_issue':reported_issues,'user_registration':user})
    else:
        return redirect('/')

def BRadmin_ReportedissueShow1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'BRadmin_ReportedissueShow1.html',{'reported_issue':reported_issues,'Adm':Adm})
    else:
        return redirect('/')

#reported issue- akhil-man mod

def MAN_Reportedissue_department(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.all()
        return render(request, 'MAN_Reportedissue_department.html',{'department':departments,'mem':mem})
    else:
        return redirect('/')

def MAN_Reportedissue(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.get(id=id)
        deptid=id
        designations=designation.objects.filter(~Q(designation='admin'),~Q(designation='manager'))
        return render(request, 'MAN_Reportedissue.html',{'mem':mem,'department':departments,'designation':designations,'dept_id':deptid})
    else:
        return redirect('/')

def MAN_ReportedissueShow(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.all()
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation=designations).filter(department=did).order_by("-id")
        return render(request,'MAN_ReportedissueShow.html',{'mem':mem,'designation':designations,'reported_issue':reported_issues,'user_registration':user})
    else:
        return redirect('/')


def MAN_reported(request,id):
        
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            
            
            vars.reply = request.POST['review']
            
            vars.issuestatus = 1
           
            
            vars.save()
        return redirect('MAN_Reportedissue_department')

def MAN_ReportedissueShow1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_ReportedissueShow1.html',{'reported_issue':reported_issues,'mem':mem}) 
    else:
        return redirect('/')

############## end ##########


#task section-nimisha- man mod

def MAN_tasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_tasks.html',{'mem':mem})
    else:
        return redirect('/')

def MAN_givetask(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['task']
            sc7 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            
            catry = tasks(tasks=sc4,files=ogo,description=sc7,startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        emp = user_registration.objects.all()
        return render(request,'MAN_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'mem':mem})
    else:
        return redirect('/')

def MAN_taskdesignation(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)   
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.all()
        
        return render(request, 'MAN_taskdesignation.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')

def MAN_taskemployee(request):   
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        desig_id = request.GET.get('desig_id')
        emp = user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
        
        return render(request, 'MAN_taskemployee.html', {'emp': emp,'mem':mem})
    else:
        return redirect('/')
        
def MAN_currenttasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)  
        names =tasks.objects.all().order_by("-id")
        return render(request,'MAN_currenttask.html',{'names': names,'mem':mem})
    else:
        return redirect('/')

def MAN_previoustasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)  
        names =tasks.objects.all().order_by("-id")
        return render(request,'MAN_previoustasks.html',{'names': names,'mem':mem})
    else:
        return redirect('/')

#task section-nimisha- admin mod

def BRadmin_tasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_tasks.html',{'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_givetask(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['task']
            sc7 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
         
            ogo = request.FILES['img[]']
            
            catry = tasks(tasks=sc4,files=ogo,description=sc7,startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        emp = user_registration.objects.all()
        return render(request,'BRadmin_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_taskdesignation(request):  
     
    dept_id = request.GET.get('dept_id')
    # Desig = designation.objects.filter(department_id=dept_id)
    Desig = designation.objects.all()
    
    return render(request, 'BRadmin_taskdesignation.html', {'Desig': Desig,'Adm':Adm})
    

def BRadmin_taskemployee(request): 
      
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
   
    return render(request, 'BRadmin_taskemployee.html', {'emp': emp,'Adm':Adm})
  

def BRadmin_currenttasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)  
        names =tasks.objects.filter(~Q(status=1)).order_by("-id")
        return render(request,'BRadmin_currenttask.html',{'names': names,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_previoustasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)  
        names =tasks.objects.filter(status=1).order_by("-id")
        return render(request,'BRadmin_previoustasks.html',{'names': names,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_trainersdepartment(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Dept = department.objects.all()
        Desig = designation.objects.all()
        return render(request,'BRadmin_trainersdepartment.html',{'Adm':Adm,'Dept':Dept,'Desig':Desig})
    else:
        return redirect('/')

############## end ##########

#upcoming projects -safdhar -admin mod


def BRadmin_upcoming(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_upcomingprojects.html',{'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_viewprojectform(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            progress=0
            catry = project_taskassign(project_id=sc3,description=sc4,startdate=sc5, enddate=sc6,extension='0')
            catry.save()
        return render(request,'BRadmin_viewprojects.html',{'Adm':Adm,'desig':desig,'dept':dept,'project':proj})
    else:
        return redirect('/')

def BRadmin_acceptedprojects(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.filter(~Q(status='Rejected')).order_by("-id")
        return render(request,'BRadmin_acceptedprojects.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_rejected(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.filter(status='Rejected').order_by("-id")
        return render(request,'BRadmin_rejectedprojectes.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_createproject(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)  
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            
            progress=0
            catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                      description=sc4,
                                      startdate=sc5, enddate=sc6, files=ogo,progress=progress)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()	
        return render(request,'BRadmin_createproject.html',{'Adm':Adm,'dept':dept,'desig':desig})
    else:
        return redirect('/')
        
def BRadmin_upcomingpro(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.all().order_by("-id")
        return render(request,'BRadmin_upcomingpro.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_seradmintraineedesi1(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(~Q(designation='admin'), ~Q(designation='manager'), ~Q(designation='account'))
        
        return render(request, 'BRadmin_dropdown.html', {'Desig': Desig,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_seradmindesig(request):
	
	dept_id = request.GET.get('dept_id')
	Desig = designation.objects.filter(~Q(designation="admin"), ~Q(designation="manager"), ~Q(designation="account"))
	
	return render(request, 'BRadmin_giveprojectdropdown.html', {'Desig': Desig})
	
def BRadmin_selectproject(request):
    
    
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    
    proj = project.objects.filter(department_id=dept_id)
    
    return render(request, 'BRadmin_selectproject.html',{'project':proj})
    
#upcoming projects -safdhar -man mod


def MAN_upcoming(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_upcomingprojects.html',{'mem':mem})
    else:
        return redirect('/')
        
def MAN_viewprojectform(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            
            progress=0
            catry = project_taskassign(project_id=sc3,description=sc4,startdate=sc5,enddate=sc6,extension='0')
            catry.save()
        return render(request,'MAN_viewprojects.html',{'desig':desig,'dept':dept,'project':proj,'mem':mem})
    else:
        return redirect('/')

def MAN_acceptedprojects(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        pro = project.objects.filter(status='Accepted').order_by("-id")
        return render(request,'MAN_acceptedprojects.html',{'projects':pro,'mem':mem})
    else:
        return redirect('/')

def MAN_rejected(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        pro = project.objects.filter(status='Rejected').order_by("-id")
        return render(request,'MAN_rejectedprojectes.html',{'projects':pro,'mem':mem})
    else:
        return redirect('/')

def MAN_createproject(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            
            progress=0
            catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                      description=sc4,
                                      startdate=sc5, enddate=sc6, files=ogo,progress=progress)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all() 
        return render(request,'MAN_createproject.html',{'desig':desig,'dept':dept,'mem':mem})
    else:
        return redirect('/')

def MAN_upcomingprojectsview(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        pro =project.objects.all().order_by("-id")
        return render(request,'MAN_upcomingprojectsview.html',{'projects': pro,'mem':mem})
    else:
        return redirect('/')

def MAN_seradmintraineedesi1(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(~Q(designation="admin"), ~Q(designation="manager"), ~Q(designation="account"))
        
        return render(request, 'MAN_createprojectdropdown.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')

def MAN_seradmindesig(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(~Q(designation='admin'),~Q(designation='manager'),~Q(designation='account'))
        pr
        return render(request, 'MAN_giveprojectdropdown.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')
        
def Manager_selectproject(request):
    
    
    dept_id = request.GET.get('dept_id')
    proj = project.objects.filter(department_id=dept_id)
    
    return render(request,'manager_selectproject.html',{'project':proj})
    
    
#*************************meenu**********************
def newdept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        condent = department.objects.all()
        return render(request,'BRadmin_Department.html',{'condent':condent,'Adm':Adm})
    else:
        return redirect('/')

def add_dept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,"BRadmin_add_dept.html",{'Adm':Adm})
    else:
        return redirect('/')

def add_deptsave(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            depart = request.POST['dept']
            logo = request.FILES['logo']
            a=department(department=depart,files=logo)
            a.save()
            m="Successfully department added"
        return render(request,'BRadmin_add_dept.html',{'m':m,'Adm':Adm})
    else:
        return redirect('/')

def delete(request, id):
    m = department.objects.get(id=id)
    os.remove(m.files.path)
    m.delete()
    return redirect('newdept')

def man_newdept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        condent = department.objects.all()
        return render(request,'man_Department.html',{'condent':condent,'mem':mem})
    else:
        return redirect('/')


def man_dept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,"man_add_dept.html",{'mem':mem})
    else:
        return redirect('/')

def man_add_deptsave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            depart = request.POST['dept']
            newfile = request.FILES['newfile']
            a=department(department=depart,files=newfile)
            a.save()
            m="Successfully department added"
        return render(request,'man_add_dept.html',{'m':m,'mem':mem})
    else:
        return redirect('/')

def man_delete(request, id):
    
    m = department.objects.get(id=id)
    try:
        m.delete()
        return redirect('man_newdept')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('man_newdept')


############## end ##########


#######################################################christin########################

def logout(request):
    if 'usernametsid' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def ProMANlogout(request):
    if 'prid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def TLlogout(request):
    if 'tlid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def devlogout(request):
    if 'devid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')



def internshipform(request):
    branch = branch_registration.objects.all()
    return render(request, 'internship.html',{'branch':branch})

def internship_save(request):
    branch = branch_registration.objects.all()
    a = internship()
    if request.method == 'POST':
        try:
            a.fullname = request.POST['name']
            a.collegename = request.POST['college_name']
            a.reg_date = datetime.now()
            a.reg_no = request.POST['reg_no']
            a.course = request.POST['course']
            a.stream = request.POST['stream']
            a.platform = request.POST['platform']
            #a.branch_id  =  request.POST['branch']
            a.start_date =  request.POST['start_date']
            a.end_date  =  request.POST['end_date']
            a.mobile  =  request.POST['mobile']

            a.alternative_no  =  request.POST['alternative_no']

            a.email = request.POST['email']
            a.profile_pic  =  request.FILES['profile_pic']
            if (a.end_date<a.start_date):
                return render(request,'internship.html',{'a':a})
            else:
                a.save()
                qr = qrcode.make("https://altoscore.in/admin_code?id=" + str(a.id))
                qr.save(settings.MEDIA_ROOT + "\\" +str(a.id) + ".png")
                with open(settings.MEDIA_ROOT + "\\" + str(a.id) + ".png", "rb") as reopen:
                        djangofile = File(reopen)
                        a.qr = djangofile

                        a.save()
           
            msg_success="Your application has been sent successfully"
            Flag='True'
            return render(request, 'internship.html',{'msg_success':msg_success})
        except:
            message = "Enter all details !!!"
            return render(request, 'internship.html',{'message':message})
    else:
        
        return render(request, 'internship.html')



def imagechange_pr(request):
  
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('pr_mg')
    return render(request, 'pr_mg.html')

def leave1(request):
    return render(request, 'leave.html')

def man_registration_form(request):
    branch = branch_registration.objects.all()
    depart = department.objects.all()
    a = user_registration()
    b = qualification()
    c = extracurricular()
    des = designation.objects.get(designation="trainee")
    if request.method == 'POST':
        if  user_registration.objects.filter(email=request.POST['email']).exists():
            
            msg_error = "Mail id already exist"
            return render(request, 'man_registration_form.html',{'msg_error': msg_error})
        else:
            
            a.fullname = request.POST['fname']
            a.fathername = request.POST['fathername']
            a.mothername = request.POST['mothername']
            a.dateofbirth = request.POST['dob']
            a.gender = request.POST['gender']
            a.presentaddress1 = request.POST['address1']
            a.presentaddress2  =  request.POST['address2']
            a.presentaddress3 =  request.POST['address3']
            a.pincode = request.POST['pincode']
            a.district  =  request.POST['district']
            a.state  =  request.POST['state']
            a.country  =  request.POST['country']
            a.permanentaddress1 = request.POST['paddress1']
            a.permanentaddress2  =  request.POST['paddress2']
            a.permanentaddress3  =  request.POST['paddress3']
            a.permanentpincode = request.POST['ppincode']
            a.permanentdistrict  =  request.POST['pdistrict']
            a.permanentstate  =  request.POST['pstate']
            a.permanentcountry =  request.POST['pcountry']
            a.mobile = request.POST['mobile']
            a.alternativeno = request.POST['alternative']
            a.department_id = request.POST['department']
            a.email = request.POST['email']
            a.status = "active"
            a.designation_id = des.id
            a.password= random.SystemRandom().randint(100000, 999999)
            
            #a.branch_id = request.POST['branch']
            a.photo = request.FILES['photo']
            a.idproof = request.FILES['idproof']
            a.save()
            
            x = user_registration.objects.get(id=a.id)
            today = date.today()
            tim = today.strftime("%m%y")
            x.employee_id = "ALT"+str(tim)+''+"B"+str(x.id)
            passw=x.password
            email_id=x.email
            x.save()
            y1 = user_registration.objects.get(id=a.id)
            qr = qrcode.make("http://altoscore.in/offerletter/" + str(y1.id))
            qr.save(settings.MEDIA_ROOT + "/images"+"//" +"offer"+str(y1.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"offer"+ str(y1.id) +".png","rb") as reopen:
                    djangofile = File(reopen)
                    y1.offerqr = djangofile
                    y1.save()
    
            y2 = user_registration.objects.get(id=a.id)
            qr1 = qrcode.make("http://altoscore.in/relieveletter/" + str(y2.id))
            qr1.save(settings.MEDIA_ROOT + "/images"+"//"+"re" +str(y2.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"re" + str(y2.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y2.relieveqr = djangofile
                    y2.save()
            y3 = user_registration.objects.get(id=a.id)
            qr2 = qrcode.make("http://altoscore.in/experienceletter/" + str(y3.id))
            qr2.save(settings.MEDIA_ROOT + "/images"+"//"+"exp" +str(y3.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"exp" + str(y3.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y3.expqr = djangofile
                    y3.save()
           
    
            b.user_id = a.id
            b.plustwo = request.POST.get('plustwo')
            b.school = request.POST['school']
            b.schoolaggregate = request.POST['aggregate']
            if request.FILES.get('cupload') is not None:
                b.schoolcertificate = request.FILES['cupload']
            b.ugdegree = request.POST['degree']
            b.ugstream = request.POST['stream']
            b.ugpassoutyr = request.POST['passoutyear']
            b.ugaggregrate = request.POST['aggregate1']
            b.backlogs = request.POST['supply']
            if request.FILES.get('cupload1') is not None:
                b.ugcertificate = request.FILES['cupload1']
            b.pg = request.POST['pg']
            b.save()
    
            c.user_id = a.id
            c.internshipdetails = request.POST['details']
            c.internshipduration = request.POST['duration']
            c.internshipcertificate = request.FILES.get('certificate')
            c.onlinetrainingdetails = request.POST['details1']
            c.onlinetrainingduration = request.POST['duration1']
            c.onlinetrainingcertificate= request.FILES.get('certificate1')
            c.projecttitle = request.POST['title']
            c.projectduration = request.POST['duration2']
            c.projectdescription = request.POST['description']
            c.projecturl = request.POST['url']
            c.skill1 = request.POST['skill1']
            c.skill2 = request.POST['skill2']
            c.skill3 = request.POST['skill3']
            c.save()
            
            subject = 'Greetings from ALTOS TECHNOLOGIES'
            message = 'Congratulations,\nYou have successfully registered ALTOS TECHNOLOGIES.\nYour login credentials \n\nEmail :'+str(email_id)+'\nPassword :'+str(passw)+'\n\nNote: This is a system generated email, do not reply to this email id.'
            email_from = settings.EMAIL_HOST_USER
            
            recipient_list = [email_id, ]
            send_mail(subject,message , email_from, recipient_list, fail_silently=True)
            msg_success = "Registration successfully Check Your Registered Mail"
            return render(request, 'man_registration_form.html',{'msg_success': msg_success,'branch':branch})
        
    return render(request, 'man_registration_form.html',{'branch':branch,'depart':depart})

def offerletter(request,id):
    mem = user_registration.objects.filter(id=id)
    return render(request,'qrofferview.html',{'mem':mem})

def relieveletter(request,id):
    mem = user_registration.objects.filter(id=id)
    return render(request,'qrreview.html',{'mem':mem})

def experienceletter(request,id):
    mem = user_registration.objects.filter(id=id)
    skill = extracurricular.objects.get(user_id=id)
    return render(request,'qrexpview.html',{'mem':mem, 'skill':skill})
    
    
def render_pdfof_view(request,id):

    date = datetime.now()  
    con = conditions.objects.get(id=1)
    mem = user_registration.objects.get(id=id)
    br_admin = branch_registration.objects.get(id=mem.branch_id)
    if request.method == 'POST':
        salr= request.POST['sal']
    template_path = 'pdfof.html'
    context = {'mem': mem,
    'con':con,
    'media_url':settings.MEDIA_URL,
    'date':date,
    'br_admin':br_admin,
    'salr':salr,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdfre_view(request,id):

    date = datetime.now()   
    mem = user_registration.objects.get(id=id)
    br_admin = branch_registration.objects.get(id=mem.branch_id)
    template_path = 'pdfre.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date,
    'br_admin':br_admin
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdfex_view(request,id):

    date = datetime.now()   
    mem = user_registration.objects.get(id=id)
    br_admin = branch_registration.objects.get(id=mem.branch_id)
    template_path = 'pdfex.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date,
    'br_admin':br_admin
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
def render_pdfau_view(request,id):

    date = datetime.now()   
    mem = user_registration.objects.get(id=id)
    template_path = 'pdfau.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def admin_code(request):
    id=request.GET.get('id')

    empid=internship.objects.filter(id=id)
    context = {
        'mem':empid,
        'media_url':settings.MEDIA_URL
        }
    return render(request, 'admin_code.html', context)


def promanagerindex(request):
    return render(request, 'promanagerindex.html')
    
    
def pr_mg(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=prid)
        return render(request, 'account_tr_mg.html', {'mem': mem})
    else:
        return redirect('/')

def pmanager_dash(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation="team leader")
        des1 = designation.objects.get(designation="developer")
        dev = user_registration.objects.filter(projectmanager_id=prid)
        ids = dev.values_list('id', flat="true")
        le = leave.objects.filter(user_id__in=ids.all()).filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0).order_by('-id')
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        
        l=leave.objects.filter(to_date__gte=date.today())
       
        count=user_registration.objects.filter(~Q(id__in=l.values_list('user_id', flat=True)),Q(designation_id=des.id) | Q(designation_id=des1.id),status="active",work_status='0').count()

        return render(request, 'pmanager_dash.html', {'pro': pro, "labels": labels, "data": data, 'le': le,'count':count})
    else:
        return redirect('/')


# work not assign tl and developer list shows

def pm_Work_not_assign(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pman = user_registration.objects.filter(id=prid)
        tlde=designation.objects.get(designation='team leader')
        d=designation.objects.get(designation='developer')
        l=leave.objects.filter(to_date__gte=date.today())
       
        dev=user_registration.objects.filter(~Q(id__in=l.values_list('user_id', flat=True)),Q(designation_id=tlde.id) | Q(designation_id=d.id),status="active",work_status='0')

        tl=user_registration.objects.filter(designation=tlde)
        req=WorkRequest.objects.filter(wrkreq_date=date.today())
        return render(request, 'projectmanager_work_not_assign.html',{'pro':pro,'dev':dev,'tl':tl,'req':req,'pman':pman})
    else:
        return redirect('/')


def pmdeveloper_task_assign(request,pmdev_id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        e = designation.objects.get(designation="tester")
        t = designation.objects.get(designation="team leader")
        t1=t.id
        e1 = e.id
        dev = user_registration.objects.get(id=pmdev_id)
        spa1 = user_registration.objects.filter(designation_id=e1, status="active")
        tls= user_registration.objects.get(id=dev.tl_id, status="active")
        tasks = project_taskassign.objects.filter(developer_id=dev.tl_id,worktype='0').values('project').distinct()
        proje=project.objects.all()
        return render(request, 'projectmanager_dev_task_assign.html',{'pro':pro,'proje':proje,'spa1':spa1,
        'tasks':tasks,'tls':tls,'dev':dev})
    else:
        return redirect('/')


def pmproject_task_assingdev(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method =='POST':
            
            var = project_taskassign()
           
            var.developer_id =  request.POST['dname']
            var.tl_id = request.POST['tl']
            var.tester_id = request.POST['tesname']
            var.tl_description=request.POST.get('description')
            var.subtask=request.POST.get('subtask')
            var.task = request.POST.get('task')
            var.startdate= request.POST.get('start_date')
            var.enddate= request.POST.get('date')
            var.files=request.FILES['files']
            var.extension=0
            var.project_id =  request.POST['prj']
            var.description = request.POST.get('description')
            var.worktype='1'
            var.save()
            
            ptask = Projectmanagerworkassign()
            ptask.pm_project_task=var
            ptask.pm_task_status='1'
            ptask.save()

            user=user_registration.objects.get(id=request.POST['dname']) #developer work status change
            user.work_status='1'
            user.save()

            # Team Leader  leave mark
            t = user_registration.objects.get(id=int(request.POST['tl']))
            try:
                ls=leave.objects.get(user=t,to_date__gte=date.today())
            except leave.DoesNotExist:
                lea1=leave()
                lea1.user=t
                lea1.from_date=date.today()
                lea1.to_date=date.today()
                lea1.reason='Work not Assign'
                lea1.days=1
                lea1.leave_status='full Day'
                lea1.save()


            return redirect('pm_Work_not_assign')
    else:
        return redirect('/')


def projectmanager_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectmanager_projects.html',{'pro':pro})
    else:
        return redirect('/')


    
#nirmal
def projectmanager_assignproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
       
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        desi_id = user_registration.objects.get(id=prid)
        d = designation.objects.get(designation="team leader")
        t = designation.objects.get(designation="tester")
        
        
        tes = user_registration.objects.filter(designation_id= t.id)#department_id = desi_id.department_id, 
        spa = user_registration.objects.filter(department_id = desi_id.department_id, designation_id= d.id)
       
        
        pvar = project.objects.filter(Q(status="accepted")|Q(status="assigned"))
        modules = project_module_assign.objects.all()
        
        if request.method =='POST':
           
            var = project_taskassign()
           
            var.user_id = prid
            var.tl_id = request.POST['pname']
            var.task = request.POST['task']
            var.description=request.POST.get('desc')
            var.startdate=request.POST.get('sdate')
            var.enddate=request.POST.get('edate')
            var.worktype=request.POST.get('individual_work')
            var.projmodule=''
            
            bb= datetime.strptime(var.startdate, '%Y-%m-%d').strftime('%d-%m-%Y')
            
            cc= datetime.strptime(var.enddate, '%Y-%m-%d').strftime('%d-%m-%Y')
            if request.FILES.get('pfile') is not None:
                var.files=request.FILES.get('pfile')
                
            var.project_id = request.POST.get('yyy')

            var.developer_id= request.POST['pname']
            var.teamleader_id = request.POST['pname']            
            var.tester_id= request.POST['tname']

            var.save()
            new = project.objects.get(id=var.project_id)
            new.status = "assigned"
            new.save()
            v = request.POST.get('pname')
            em=user_registration.objects.get(id=v)
            em.projectmanager_id=prid
            em.save()

            up=request.POST.get('update')
           
            if up == '1':
                updates=ProjectCorrectionUpdation()
                updates.project_cu_module= request.POST['task']
                updates.project_cu_descrip= request.POST.get('desc')
                updates.project_cu_status='updation'
                updates.project_cu_id = project.objects.get(id=request.POST.get('yyy'))
                tlname= user_registration.objects.get(id=request.POST['pname'])
                updates.ptl_name=tlname.fullname
                updates.save()


            # subject = 'Greetings from iNFOX TECHNOLOGIES'
            # message = 'Congratulations,\n' \
            # 'You are assigned new project from iNFOX TECHNOLOGIES.\n' \
            # 'following is your Project Details\n'\
            # 'Project : '+str(new.project)+'\n' 'Task : '+str(var.task) +'\n' 'Description : '+str(var.description)+'\n''Start Date : '+bb+'\n' 'End Date : '+cc+'\n'\
            # '\n' 'Complete your project on or before Enddate \n'\
            #     'NOTE : THIS IS A SYSTEM GENETATED MAIL PLEASE DO NOT REPLY' 
            # recepient = str(em.email)
            # send_mail(subject, message, settings.EMAIL_HOST_USER,
            #       [recepient], fail_silently=False)
            msg_success = "Project assigned successfully"
            
            return render(request, 'projectmanager_assignproject.html',{'pro':pro,'spa':spa,'pvar':pvar,'tes':tes, 'msg_success':msg_success,'modules':modules})
        return render(request, 'projectmanager_assignproject.html', {'pro':pro,'spa':spa,'pvar':pvar,'tes':tes,'modules':modules})
    else:
        return redirect('/')


@csrf_exempt
def pmprojectmodule(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
       
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)

        pid = request.GET.get('prid')
        Desig=project_module_assign.objects.filter(project_name_id=pid)
        return render(request,'pm_module_data.html',{'pro': pro,'Desig':Desig})

    else:
   
        return redirect('/')
        

def projectmanager_projectstatus(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation="team leader")
        dev = designation.objects.get(designation="developer")
        var = project_taskassign.objects.filter(project_id=id).order_by('-id')
        data = test_status.objects.filter(project_id=id).order_by('-id')
        data1 = tester_status.objects.filter(project_id=id).order_by('-id')
        newdata = project_taskassign.objects.filter(project_id=id,subtask__isnull = False).order_by('-id')
        return render(request, 'projectmanager_projectstatus.html',{'pro':pro,'var':var,'data':data,'data1':data1,'newdata':newdata})
    else:
        return redirect('/')
        
def projectmanager_projectlist(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        var=project.objects.filter(Q(status="accepted")|Q(status="assigned")|Q(status="completed")).order_by("-id")
        return render(request, 'projectmanager_projectlist.html',{'pro':pro,'var':var})
    else:
        return redirect('/')
   
#jensin
def projectmanager_createproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
      
            
        mem = user_registration.objects.filter(id=prid)  
        br_id = user_registration.objects.get(id=prid)  
        dept = department.objects.all()
        if request.method =='POST':
            mem = user_registration.objects.filter(id=prid)
            mem2 = user_registration.objects.get(id=prid)
            var = project()
            doc = PM_ProjectDocument()
            var.projectmanager_id = prid
            var.department_id = mem2.department_id 
            # dept_id=department.objects.get(id=request.POST.get('dpt_name')) 
            # var.department_id = dept_id.id
           
            var.project=request.POST.get('pname')
            var.startdate=request.POST.get('sdate')
            var.enddate=request.POST.get('edate')
            var.description=request.POST.get('desc')
            var.files=request.FILES.get('pfile')
            var.branch_id=br_id.branch_id
            
            var.save()
            doc.doc_project_id= var
            doc.doc_project_name = request.POST.get('pname')
            doc.doc_project_startdate = request.POST.get('sdate')
            doc.doc_project_enddate = request.POST.get('edate')
            doc.save()



            msg_success = "Project created successfully"
            return render(request, 'projectmanager_createproject.html',{'msg_success':msg_success})
        return render(request, 'projectmanager_createproject.html',{'pro':mem,'dept':dept})
    else:
        return redirect('/')

def pmstart_new_document(request):
     if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
      
        mem = user_registration.objects.filter(id=prid) 
        if request.method == 'POST':
            docid=request.POST['docid']
            var = project.objects.get(id=docid)
            doc = PM_ProjectDocument() 
            doc.doc_project_id= var
            doc.doc_project_name =var.project
            doc.doc_project_startdate =  var.startdate
            doc.doc_project_enddate = var.enddate
            doc.save()
            return  redirect('projectManager_project_document')

def pm_doc_upload(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
            if request.method == 'POST':
                
                if request.FILES.get('upload_file'):
                    docid=request.POST['docid']
                    doc = PM_ProjectDocument.objects.get(id=docid) 
                    doc.doc_project_ui=request.FILES.get('upload_file')
                    doc.save()
                    return  redirect('projectManager_project_document')

def uiupdate(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
          
        mem = user_registration.objects.filter(id=prid)  
        if request.method =='POST':
            var = project.objects.get(id=request.POST.get('proj'))
            var.uifile=request.FILES.get('uifile')
            var.save()
            return redirect('projectmanager_currentdetail',var.id)

    else:
        return redirect('/')

    # if 'prid' in request.session:
    #     if request.session.has_key('prid'):
    #         prid = request.session['prid']
       
    #     else:
    #        return redirect('/')
    #     pro = user_registration.objects.filter(id=prid)
    #     if request.method == 'POST':
    #         prj =  project()
    #         prj.projectmanager = prid
    #         prj.department = pro.department
         

    #     return render(request, 'projectmanager_createproject.html',{'pro':pro})
    # else:
    #     return redirect('/')

#maneesh
def projectmanager_description(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(id=id)  
        return render(request, 'projectmanager_description.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')

def projectmanager_table(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(status__isnull = True).order_by("-id")
        return render(request, 'projectmanager_table.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')


def proMAN_acceptproj(request,id):
    
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro_sts = project.objects.filter(id=id).update(status="accepted")

        pro = user_registration.objects.filter(id=prid)
        msg_success = "Project accepted successfully"
        return render(request, 'projectmanager_table.html',{'pro':pro,'msg_success':msg_success})
    else:
        return redirect('/')

def proMAN_rejectproj(request,id):
   
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')

        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            user_reason=request.POST.get('reply')
            rejectdate = datetime.now()
            pro_sts = project.objects.filter(id=id).update(user_reason= user_reason,status ='rejected',rejectdate=rejectdate)
            msg_success_sub = "Project Rejected successfully"
            return render(request, 'projectmanager_table.html',{'pro':pro,'msg_success_sub':msg_success_sub})
        else:
            
            projects = project.objects.filter(status__isnull = True).order_by('-id')
            return render(request, 'projectmanager_table.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')


def projectmanager_upprojects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectmanager_upprojects.html',{'pro':pro})
    else:
        return redirect('/')

#praveesh

def projectmanager_accepted_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        projects = project.objects.filter(~Q(status="Completed"),~Q(status="completed"), ~Q(status="rejected"))
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        return render(request, 'projectManager_accepted_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')
        
def projectmanager_edit_assigned_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        if 'proj_date_change' in request.POST:
            uid = request.POST.get('proj_id')
            assin = project_taskassign.objects.get(id=uid)
            assin.enddate = request.POST.get('sdate')
            assin.save()
            msg_success = "Date Changed successfully"
            return render(request, 'projectManager_edit_accepted_projects.html',{'pro':pro,'msg_success':msg_success})
        elif "delete_proj" in request.POST:
            uid = request.POST.get('proj_id')
            proj = project_taskassign.objects.get(id=uid)
            proj.delete()
            msg_success = "Task deleted successfully"
            return render(request, 'projectManager_edit_accepted_projects.html',{'pro':pro,'msg_success':msg_success})
        else:
            projects = project_taskassign.objects.filter(~Q(status="submitted"), ~Q(status="Completed"),~Q(status="completed")).order_by("-id")
            
            return render(request, 'projectManager_edit_accepted_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')
        
def projectManager_edit_projects_status(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
           
        if request.method=="POST":
            uid = request.POST.get('proj_id')
            proj = project.objects.get(id=uid)
            proj.progress = request.POST.get('progress')
            proj.save()
            msg_success = "Progress update successfully"
            return render(request, 'projectManager_edit_projects_status.html',{'msg_success':msg_success})
        else:
            projects = project.objects.filter().order_by("-id")
            pro = user_registration.objects.filter(id=prid).order_by("-id")
            return render(request, 'projectManager_edit_projects_status.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')
    

#******************************** Project Documents ***********************(27/10/22)
    
#  project manager project Document list page   
    
def projectManager_project_document(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        projects = project.objects.all().order_by("-id")
        proj_doc=PM_ProjectDocument.objects.filter(Q(doc_status='0') | Q(doc_status='1'))
        return render(request, 'projectManager_project_documnent_list.html',{'pro':pro,'proj_doc':proj_doc,'projects':projects})
    else:
        return redirect('/')

    

# project document start
def project_manager_doc_start(request,pmdoc_id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        pdoc= PM_ProjectDocument.objects.get(id=pmdoc_id)
        pdoc.doc_project_currentdate=date.today()
        pdoc.doc_status=1
        pdoc.save()
        proj_doc=PM_ProjectDocument.objects.all()
        return render(request, 'projectManager_project_documnent_list.html',{'pro':pro,'proj_doc':proj_doc})
    else:
        return redirect('/')

# project document module view
    
def project_manager_doc_module(request,pmdoc_md_id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        pdoc= PM_ProjectDocument.objects.get(id=pmdoc_md_id)
       
        corre=ProjectCorrectionUpdation.objects.filter(project_cu_id=pdoc.doc_project_id,project_cu_status='correction')
        updte=ProjectCorrectionUpdation.objects.filter(project_cu_id=pdoc.doc_project_id,project_cu_status='updation')

        pdocd=ProjectDocDetails.objects.filter(doc_project_d=pdoc.doc_project_id)
        pdocm=ProjectDocModels.objects.filter(doc_project_md=pdoc.doc_project_id)
        pdocv=ProjectDocViews.objects.filter(doc_project_v=pdoc.doc_project_id)
        pdochp=ProjectDochtmlpages.objects.filter(doc_project_hp=pdoc.doc_project_id)
        pdoclb=ProjectDoclibraryies.objects.filter(doc_project_lb=pdoc.doc_project_id)
        pdocdot=ProjectDocother.objects.filter(doc_project_oth=pdoc.doc_project_id)
        devp=project_taskassign.objects.filter(project=pdoc.doc_project_id).values('developer').distinct()
        doc_user = user_registration.objects.all()
        work_days= date.today() - pdoc.doc_project_startdate
        work_days=work_days.days

        # client requriments
        proj=project_module_assign.objects.filter(project_name=pdoc.doc_project_id)
        pro_table=project_table.objects.filter(project=pdoc.doc_project_id)
        poj_other= project_other_assign.objects.filter(othproject_name=pdoc.doc_project_id)

        return render(request, 'projectManager_project_module_list.html',{'pro':pro,'proj':proj,'pdoc':pdoc,'corre':corre,
                                'updte':updte,'pdocd':pdocd,'pdocm':pdocm,'pdocv':pdocv,'pdochp':pdochp,'pdoclb':pdoclb,'pdocdot':pdocdot,
                                'work_days':work_days,'devp':devp,'doc_user':doc_user,'pro_table':pro_table,'poj_other':poj_other})
    else:
        return redirect('/')


def project_manager_usermanuvel(request,pm_usermanuvel_id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        pdoc= PM_ProjectDocument.objects.get(id=pm_usermanuvel_id)
        um=UserManuvel.objects.filter(user_project=pdoc.doc_project_id)
        ump=UserManuvelPoints.objects.filter(userp_project=pdoc.doc_project_id)
        return render(request, 'projectManager_project_usermanuvel.html',{'pro':pro,'pdoc':pdoc,'um':um,'ump':ump})
    else:
        return redirect('/')
    

def pm_usermanuvel_add(request,pm_usermanuveladd):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        pdoc= PM_ProjectDocument.objects.get(id=pm_usermanuveladd)
        um=UserManuvel.objects.filter(user_project=pdoc.doc_project_id)
        ump=UserManuvelPoints.objects.filter(userp_project=pdoc.doc_project_id)

        if request.method=="POST":
            um1= UserManuvel()
            um1.user_project=pdoc.doc_project_id
            um1.um_head = request.POST.get('um_head')
            um1.um_subhead = request.POST.get('um_subhead')
            um1.um_dese = request.POST.get('um_dese')
            um1.um_files = request.FILES.get('um_file')
            um1.save()
            msg_success = "Update successfully"

        return render(request, 'projectManager_project_usermanuvel.html',{'pro':pro,'pdoc':pdoc,'um':um,'ump':ump})
    else:
        return redirect('/')

def pm_userpoints_add(request):
    if request.method=="POST":
        um= UserManuvel.objects.get(id=request.POST.get('umhead_id'))
        ump=UserManuvelPoints()
        ump.userp_project=um.user_project
        ump.user_manuvelid =um
        ump.um_points = request.POST.get('um_points')
        ump.um_pfiles = request.FILES.get('ump_file')
        ump.save()
        msg_success = "Update successfully"
        pdoc= PM_ProjectDocument.objects.get(doc_project_id=um.user_project)
        return redirect('project_manager_usermanuvel',pdoc.id)

    else:
        return redirect('/')


# Document correction or Updation add
def pm_doc_corre_updattion(request,pmdoc_pid,pmdoc_cu):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        
        if request.method =="POST":
            p1=request.POST['doc_pm_cumodule_name']
            p2=request.POST['doc_pm_cumodule_dese']
            p3=request.POST['doc_pm_cuname']
            proj=project.objects.get(id=pmdoc_pid)
            proj_doc_cu=ProjectCorrectionUpdation()
            proj_doc_cu.project_cu_module=p1
            proj_doc_cu.project_cu_descrip=p2
            proj_doc_cu.ptl_name=p3
            proj_doc_cu.project_cu_id=proj
            proj_doc_cu.project_cu_start=date.today()
            if pmdoc_cu == 0:
                proj_doc_cu.project_cu_status='correction'
            else:
                proj_doc_cu.project_cu_status='updation'
            proj_doc_cu.save()

        return redirect('projectManager_project_document')
    else:
        return redirect('/')


# Document complete

def pm_doc_complete(request,pmdoc_complete):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        doc=PM_ProjectDocument.objects.get(id=pmdoc_complete)
        doc.doc_status='completed'
        doc.save()
        return redirect('projectmanager_projects')
 
    else:
        return redirect('/')






 #********************************** Project manager project Document 

 
def pm_docfull_pdf(request,pmfulldocs_pdf):
    date = datetime.now()  
    
    try:
        project_datils=PM_ProjectDocument.objects.get(id=pmfulldocs_pdf)

    except PM_ProjectDocument.DoesNotExist:
        project_datils=None
        return redirect('projectManager_project_document')
    pdoc= PM_ProjectDocument.objects.get(id=pmfulldocs_pdf)
    proj=project_module_assign.objects.filter(project_name=pdoc.doc_project_id)
    corre=ProjectCorrectionUpdation.objects.filter(project_cu_id=pdoc.doc_project_id,project_cu_status='correction')
    updte=ProjectCorrectionUpdation.objects.filter(project_cu_id=pdoc.doc_project_id,project_cu_status='updation')

    pdocd=ProjectDocDetails.objects.filter(doc_project_d=pdoc.doc_project_id)
    pdocm=ProjectDocModels.objects.filter(doc_project_md=pdoc.doc_project_id)
    pdocv=ProjectDocViews.objects.filter(doc_project_v=pdoc.doc_project_id)
    pdochp=ProjectDochtmlpages.objects.filter(doc_project_hp=pdoc.doc_project_id)
    pdoclb=ProjectDoclibraryies.objects.filter(doc_project_lb=pdoc.doc_project_id)
    pdocdot=ProjectDocother.objects.filter(doc_project_oth=pdoc.doc_project_id)
    devp=project_taskassign.objects.filter(project=pdoc.doc_project_id).values('developer').distinct()
    doc_user = user_registration.objects.all()
    
    work_days=pdoc.doc_project_enddate - pdoc.doc_project_startdate
    work_days=work_days.days
   

    template_path = 'pm_project_document_fullpdf.html'
    context = {'proj':proj,'pdoc':pdoc,'corre':corre,
                                'updte':updte,'pdocd':pdocd,'pdocm':pdocm,'pdocv':pdocv,'pdochp':pdochp,'pdoclb':pdoclb,'pdocdot':pdocdot,
                                'devp':devp,'doc_user':doc_user,'date':date,'work_days':work_days,'path':settings.NEWPATH,}
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-Document.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def pm_doccode_pdf(request,pm_code_pdf):
    date = datetime.now()  
    
    try:
        project_datils=PM_ProjectDocument.objects.get(id=pm_code_pdf)

    except PM_ProjectDocument.DoesNotExist:
        project_datils=None
        return redirect('projectManager_project_document')
    pdoc= PM_ProjectDocument.objects.get(id=pm_code_pdf)
    proj=project_module_assign.objects.filter(project_name=pdoc.doc_project_id)
    
    pdocd=ProjectDocDetails.objects.filter(doc_project_d=pdoc.doc_project_id)
    pdocm=ProjectDocModels.objects.filter(doc_project_md=pdoc.doc_project_id)
    pdocv=ProjectDocViews.objects.filter(doc_project_v=pdoc.doc_project_id)
    pdochp=ProjectDochtmlpages.objects.filter(doc_project_hp=pdoc.doc_project_id)
    pdoclb=ProjectDoclibraryies.objects.filter(doc_project_lb=pdoc.doc_project_id)
    pdocdot=ProjectDocother.objects.filter(doc_project_oth=pdoc.doc_project_id)
    devp=project_taskassign.objects.filter(project=pdoc.doc_project_id).values('developer').distinct()
    doc_user = user_registration.objects.all()
   
   

    template_path = 'pm_project_document_codepdf.html'
    context = {'proj':proj,'pdoc':pdoc,
                               'pdocd':pdocd,'pdocm':pdocm,'pdocv':pdocv,'pdochp':pdochp,'pdoclb':pdoclb,'pdocdot':pdocdot,
                                'devp':devp,'doc_user':doc_user,'date':date,'path':settings.NEWPATH,}
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-Code-Document.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def pm_doc_pdf(request,fulldoc_pdf):
    date = datetime.now()  
    if request.method =="POST":
        p1=request.POST.get('pdin_date')
        p2=request.POST.get('pd_corre')
        p3=request.POST.get('pdwdays')
        p4=request.POST.get('pddev')
        
  
    else:
        return redirect('projectManager_project_document')
    try:
        project_datils=PM_ProjectDocument.objects.get(id=fulldoc_pdf)

    except PM_ProjectDocument.DoesNotExist:
        project_datils=None
        return redirect('projectManager_project_document')
    projects=project.objects.get(id=project_datils.doc_project_id.id)
    project_module=project_module_assign.objects.filter(project_name=projects)
    project_doc=PM_ProjectDocument.objects.get(doc_project_id=projects)
    project_correction=ProjectCorrectionUpdation.objects.filter(project_cu_id=projects , project_cu_status='correction' )
    project_updation=ProjectCorrectionUpdation.objects.filter(project_cu_id=projects , project_cu_status='updation' )
    devp=project_taskassign.objects.filter(project=projects).values('developer').distinct()
    doc_user = user_registration.objects.all()
    work_days=project_doc.doc_project_enddate - project_doc.doc_project_startdate
    work_days=work_days.days

    template_path = 'pm_project_document_pdf.html'
    context = {'projects':projects,
    'project_module':project_module,
    'project_correction':project_correction,
    'p1':p1,
    'p2':p2,
    'p3':p3,
    'p4':p4,
    'project_updation':project_updation,
    'date':date,
    'project_doc':project_doc,
    'devp':devp,
    'doc_user':doc_user,
    'work_days':work_days,
    'path':settings.NEWPATH,
    }
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-Document.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Document desecription pdf
def pm_doc_des_pdf(request,desedoc_pdf):
    date = datetime.now()  
    try:
        project_datils=PM_ProjectDocument.objects.get(id=desedoc_pdf)
    except PM_ProjectDocument.DoesNotExist:
        project_datils=None
        return redirect('projectManager_project_document')
    projects=project.objects.get(id=project_datils.doc_project_id.id)
    prodoc=PM_ProjectDocument.objects.get(doc_project_id=projects)
    project_module=project_module_assign.objects.filter(project_name=projects)
    proj_table=project_table.objects.filter(project=projects)
    
   
    template_path = 'pm_project_document_dese_pdf.html'
    context = {'projects':projects,
    'project_module':project_module,
    'date':date,
    'prodoc':prodoc,
    'proj_table':proj_table,
    'path':settings.NEWPATH,

    }
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-desecription.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# document correction pdf  

def pm_doc_corr_pdf(request,corredoc_pdf):
    date = datetime.now()  
    try:
        project_datils=PM_ProjectDocument.objects.get(id=corredoc_pdf)
    except PM_ProjectDocument.DoesNotExist:
        project_datils=None
        return redirect('projectManager_project_document')
    projects=project.objects.get(id=project_datils.doc_project_id.id)
    prodoc=PM_ProjectDocument.objects.get(doc_project_id=projects)
    
   
    project_correction=ProjectCorrectionUpdation.objects.filter(project_cu_id=projects , project_cu_status='correction' )
    
   
    template_path = 'pm_project_document_corre_pdf.html'
    context = {'projects':projects,
    'project_correction':project_correction,
    'date':date,
    'prodoc':prodoc,
    'path':settings.NEWPATH,
    }
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-correction.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

  
# document updation pdf 
def pm_doc_updt_pdf(request,updedoc_pdf):
    date = datetime.now()  
    try:
        project_datils=PM_ProjectDocument.objects.get(id=updedoc_pdf)
    except PM_ProjectDocument.DoesNotExist:
        project_datils=None
        return redirect('projectManager_project_document')
    projects=project.objects.get(id=project_datils.doc_project_id.id)
    prodoc=PM_ProjectDocument.objects.get(doc_project_id=projects)
    project_updation=ProjectCorrectionUpdation.objects.filter(project_cu_id=projects , project_cu_status='updation' )
    
   
    template_path = 'pm_project_document_updation_pdf.html'
    context = {'projects':projects,
    'project_updation':project_updation,
    'date':date,
    'prodoc':prodoc,
    'path':settings.NEWPATH,
    }
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-updation.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




    



    #******************************************************************************************************************************

def projectmanager_rejected_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        projects = project.objects.filter(status="rejected")
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        return render(request, 'projectManager_rejected_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')


#bibin #amal #abin #rohit
def manindex(request):
    return render(request, 'manager_index.html')

def projectmanEmp(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectman_emp.html', {'pro': pro})
    else:
        return redirect('/')

def projectmanDev(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_dep = user_registration.objects.get(id=prid)
        des_id = designation.objects.get(designation="developer")
        man = user_registration.objects.filter(designation_id=des_id.id).filter(department_id=pro_dep.department_id,status="active").order_by("-id")
        return render(request, 'projectman_dev.html',{'pro':pro,'man':man})
    else:
        return redirect('/')
def projectman_trainees(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_dep = user_registration.objects.get(id=prid)
        des_id = designation.objects.get(designation="trainee")
        man = user_registration.objects.filter(designation_id=des_id.id).filter(department_id=pro_dep.department_id,status="active").order_by("-id")
        return render(request, 'projectman_trainees.html',{'pro':pro,'man':man})
    else:
        return redirect('/')

def projectmanDevDashboard(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectman_dev_Dashboard.html',{'labels':labels,'data':data,'pro':pro,'man':man})
    else:
        return redirect('/')


def pro_allocatetl(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
            
        pro = user_registration.objects.filter(id=prid)
        des_tl = designation.objects.get(designation = "team leader")
        des_dev = designation.objects.get(designation = "developer ")
        devs = user_registration.objects.filter(designation_id=des_dev.id,status="active")
        tls = user_registration.objects.filter(designation_id=des_tl.id,status="active")
        
        tl_name = user_registration.objects.all()
        
        if request.method == "POST":
            emp_id = request.POST.get('id')
            tl_id = request.POST.get('team')
            
            alocate = user_registration.objects.get(id=emp_id)
            alocate.tl_id = tl_id
            alocate.save()
            return redirect('pro_allocatetl')
            
        return render(request, 'Pro_allocatetl.html', {'mem': tls, 'memm': devs,'pro':pro, 'tl_name':tl_name})
    else:
        return redirect('/')



def projectman_developer_attendance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectman_team_attendance.html',{'pro':pro})
    else:
        return redirect('/')

def projectman_team(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid) 
        teamid = user_registration.objects.filter(tl_id=id,status="active").order_by("-id") 
        return render(request, 'projectman_team.html',{'pro': pro,'teamid': teamid})
    else:
        return redirect('/')  

def projectman_team_profile(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)  
        ind = user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectman_team_profile.html',{'pro': pro,'ind': ind,'labels':labels,'data':data})
    else:
        return redirect('/')  

def projectman_team_attendance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.filter(id=id)  
        return render(request,'projectman_team_attendance.html',{'pro':pro,'man':man})
    else:
        return redirect('/')  
def projectman_team_attandance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = attendance.objects.filter(user_id=id)  
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id) .order_by('-id')
        return render(request, 'projectman_team_attandance.html', {'pro': pro,'mem1':mem1,'man':man})
    else:
        return redirect('/')
def projectMANattendance(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANattendance.html',{'pro':pro})
    else:
        return redirect('/')  
def projectMANattandance(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            prm1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=prid)
        return render(request, 'projectMANattendancesort.html',{'pro':pro,'prm1':prm1})
    else:
        return redirect('/')


# def projectMANreportsuccess(request):
#     if 'prid' in request.session:
#         if request.session.has_key('prid'):
#             prid = request.session['prid']
#         else:
#             return redirect('/')
#         pro = user_registration.objects.filter(id=prid)
#         if request.method == 'POST':
#             # uid=objects.GET.get('user_id')
#             vars = reported_issue()
#             vars.issue=request.POST.get('report')
#             vars.reported_date=datetime.datetime.now()
#             vars.reported_to_id=2
#             vars.reporter_id=prid
#             vars.status='pending'
#             vars.save()
#         return render(request, 'MANreportsuccess.html',{'pro':pro})
#     else:
#         return redirect('/')  

def projectMANleave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANleave.html',{'pro':pro})
    else:
        return redirect('/') 

def projectMANleavereq(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user_id = request.POST.get('pr_id')
            mem.status = "pending"
            
            start = datetime.strptime(mem.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(mem.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                mem.days = 1
            else:
                mem.days = diff - cnt
                
                
            mem.save()
        return render(request, 'projectMANleavereq.html',{'pro':pro})  
    else:
        return redirect('/')




def projectMANreqedleave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        var = leave.objects.filter(user_id=prid).order_by("-id")
        return render(request, 'projectMANreqedleave.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')

def Manager_employees(request):
    return render(request,'Manager_employees.html')

def projectManager_tl(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        dept_id = user_registration.objects.get(id=prid)
        p = designation.objects.get(designation="team leader")
        tlfil = user_registration.objects.filter(designation_id=p.id, department_id = dept_id.department_id, status="active").order_by("-id")
        return render(request, 'projectManager_tl.html', {'pro': pro, 'tlfil': tlfil})
    else:
        return redirect('/')


def projectManager_tl_dashboard(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        tls = user_registration.objects.filter(id=id) 
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectManager_tl_dashboard.html',{'labels':labels,'data':data,'pro': pro, 'tls': tls})
    else:
        return redirect('/')



def man_tl_attendance(request):
    return render(request,'man_tl_attendance.html')

def projectmanager_currentproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        proj = user_registration.objects.get(id=prid)
        pro = user_registration.objects.filter(id=prid)
        var=project.objects.filter(department_id=proj.department_id,status="assigned").order_by('-id')
        return render(request, 'projectmanager_currentproject.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')
        
def completepro(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        display = project.objects.get(id=id)
        if request.method == "POST":
            var =project.objects.get(id=id)
            var.status="completed"
            var.progress=100
            var.save()
            pro = user_registration.objects.filter(id=prid)
            display = project.objects.get(id=id)
            return render(request, 'projectmanager_currentdetail.html',{'pro':pro,'display':display})
        return render(request, 'projectmanager_currentdetail.html',{'pro':pro,'display':display})
    else:
        return redirect('/')
        
def projectmanager_currentdetail(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        display = project.objects.get(id=id)
        return render(request, 'projectmanager_currentdetail.html',{'pro':pro,'display':display})
    else:
        return redirect('/')

def projectmanager_currentteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        
        display = project_taskassign.objects.filter(project_id=id).values('tl_id').distinct()
        
        uniq = user_registration.objects.all()
      
        return render(request, 'projectmanager_currentteam.html',{'pro':pro,'display':display, 'uniq':uniq})
    else:
        return redirect('/')

def projectmanager_completeteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        display = project_taskassign.objects.filter(project_id=id)
        return render(request, 'projectmanager_completeteam.html',{'pro':pro,'display':display})
    else:
        return redirect('/')


def projectmanager_currenttl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')

        pro = user_registration.objects.filter(id=prid)
        display2 = user_registration.objects.all()
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        
        return render(request, 'projectmanager_currenttl.html',{'pro':pro,'display':display,'display2':display2})
    else:
        return redirect('/')

    
def projectmanager_completeproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        asus = project.objects.filter(status="completed")
        return render(request, 'projectmanager_completeproject.html',{'pro':pro,'asus':asus})
    else:
        return redirect('/')

def projectmanager_completedetail(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        val = project.objects.filter(id=id)
        return render(request, 'projectmanager_completedetail.html',{'pro':pro,'val':val})
    else:
        return redirect('/')



def projectmanager_teaminvolved(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pri = project_taskassign.objects.filter(developer_id=id).order_by("-id")
        return render(request, 'projectmanager_teaminvolved.html',{'pro': pro, 'pri': pri})
    else:
        return redirect('/')


def projectmanager_devteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.filter(tl_id = id).order_by("-id")
        return render(request, 'projectmanager_devteam.html',{'pro':pro,'man':man})
    else:
        return redirect('/')



def projectmanager_completetl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        com = project.objects.filter(status = "completed")
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        user = user_registration.objects.all()

        return render(request, 'projectmanager_completetl.html',{'pro':pro,'com':com,'display':display,'user':user})
    else:
        return redirect('/')


# Project Manager complete document - project complete -- 2/11/22 -shebin shaji
def projectmanager_completedoc(request,pm_comp_doc):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        com = project.objects.filter(status = "completed")
        proj_doc = PM_ProjectDocument.objects.filter(doc_project_id_id=pm_comp_doc,doc_status='completed')

        return render(request, 'projectmanager_completetdoc.html',{'pro':pro,'com':com,'proj_doc':proj_doc})
    else:
        return redirect('/')



def projectMANreportedissue(request):
    if 'prid' in request.session:
        if request.session.has_key('devdes'):
            devdes = request.session['devdes']
        if request.session.has_key('devdep'):
            devdep = request.session['devdep']
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        var=reported_issue.objects.filter(reporter=prid).order_by("-id")
    
        return render(request, 'projectMANreportedissue.html',{'var':var,'pro':pro})
    else:
        return redirect('/')
def projectMANreportissue(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANreportissue.html',{'pro':pro})
    else:
        return redirect('/')

def projectmanagerreportedissue2(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var,'pro':pro})
    else:
        return redirect('/')

def projectmanagerreportedissue3(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var,'pro':pro})
    else:
        return redirect('/')


def currentperformance(request, id):
    if 'prid' in request.session:
   
        
        if request.session.has_key('prid'):
            prid = request.session['prid']
        
        pro = user_registration.objects.filter(id=prid)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem.attitude = request.POST['sele1']
            mem.creativity = request.POST['sele2']
            mem.workperformance = request.POST['sele3']
            mem.save()
            return render(request, 'currentperformance.html', {'mem': mem, 'pro': pro})
        return render(request, 'currentperformance.html', {'mem': mem, 'pro': pro})
    else:
        return render('/')

def MANreportsuccess(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro1 = user_registration.objects.get(id=prid)
        design=designation.objects.get(designation="manager")
        man = user_registration.objects.get(branch_id=pro1.branch_id,designation_id=design.id)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('MANreportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=man.id
            vars.reporter_id=prid
            vars.status='pending'
            vars.save()
        return render(request, 'projectMANreportedissues.html',{'pro':pro})
    else:
        return redirect('/')


def projectmanager_tlreported(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
    
        else:
           return redirect('/')
        desi = designation.objects.get(designation="team leader")
        pro = user_registration.objects.filter(id=prid)
        vars=user_registration.objects.filter(designation=1)
        var=reported_issue.objects.filter(designation_id=desi.id)
        # vars=user_registration.objects.filter(designation_id=2).filter(id=devid)
        return render(request, 'projectmanager_tlreported.html',{'var':var,'vars':vars,'pro':pro})
    else:
        return redirect('/')

def projectreply(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            
            vars = reported_issue.objects.get(id=id)
            vars.reply=request.POST.get('reply')
            vars.save()
        return redirect('projectmanager_tlreported')
    else:
        return redirect('/')

def projectreplytl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('tlid'):
            prid = request.session['tlid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
        return redirect('devtlreported')
    else:
        return redirect('/')

def projectMANreportedissues(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)
        return render(request,'projectMANreportedissues.html',{'pro':pro})
    else:
        return redirect('/')


#-------------------------------------------------------------------------------------------------------------------------------------

#TL module

def TLdashboard(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')

        user_id = user_registration.objects.get(id=tlid)
        conf_sal = user_id.confirm_salary
        if conf_sal == "":
            conf_sal = 0
        else:
            conf_sal = int(user_id.confirm_salary)

        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
        start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

        start_day_of_this_month = date.today().replace(day=1)

        def last_day_of_month(any_day):
            # get close to the end of the month for any day, and add 4 days 'over'
            next_month = any_day.replace(day=28) + timedelta(days=4)
            # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
            return next_month - timedelta(days=next_month.day)

        last_day_of_this_month = last_day_of_month(date.today())

        previous_sal_main = 0
        this_month_sal_main = 0

        if conf_sal > 0:
            

            last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
            start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)


            prev_holly_day = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()
            working_days_pre = ((last_day_of_prev_month - start_day_of_prev_month).days - prev_holly_day) + 1
            
            one_day_sal_pre = round((conf_sal / working_days_pre), 2)
           

            evntlst = []

            event_days = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).values('start_time')
            for event_days in event_days:
                evntlst.append(event_days['start_time'])

            pre_event_lst_cnt = len(evntlst)
            


            pre_month_leave_count = leave.objects.filter(from_date__gte = start_day_of_prev_month, to_date__lte = last_day_of_prev_month, user_id = tlid).count()
            pre_month_leave_count_sub = leave.objects.filter(from_date__range=(start_day_of_prev_month,last_day_of_prev_month),to_date__range=(start_day_of_prev_month,last_day_of_prev_month), user_id = tlid).values('from_date','to_date')
            leave_lst = []

            if pre_month_leave_count >= 1:

                for pre_month_leave_count_sub in pre_month_leave_count_sub:

                    from_date = (pre_month_leave_count_sub['from_date'])
                    to_date =  (pre_month_leave_count_sub['to_date'])

                    delta = to_date - from_date
                    for i in range(delta.days + 1):
                        day = from_date + timedelta(days=i)
                        leave_lst.append(day)
                        if day in evntlst:
                            evntlst.remove(day)

            def pre_remove_days(from_day, end_day):
                pre_leaves = leave.objects.filter(from_date__range=(from_day,end_day),to_date__range=(from_day,end_day), user_id = tlid).values('from_date','to_date')
                
                for pre_leaves in pre_leaves:

                    from_date = (pre_leaves['from_date'])
                    to_date =  (pre_leaves['to_date'])

                    delta = to_date - from_date
                    for i in range(delta.days + 1):
                        day = from_date + timedelta(days=i)
                       
                        if day in leave_lst:
                            leave_lst.remove(day)
                        if day in evntlst:
                            evntlst.remove(day)

            



            pre_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pre_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= tlid).values('startdate','enddate','submitted_date')
            pre_start_current_sub_other = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(~Q(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(developer_id= tlid).values('startdate','enddate','submitted_date')
            pre_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pre_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= tlid).values('startdate','enddate','submitted_date')

            
            pre_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= tlid).values('submitted_date')
            pre_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)),submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')



            prev_current_delay = 0
            prev_current_delay = 0
            print("TL From date and todate are in previous month it does not have submission date  :", pre_current.count())
            for pre_current in pre_current:
                start_date =  (pre_current['enddate'])
                end_date =  (pre_current['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                delay_days = (last_day_of_prev_month - end_date).days
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay +  work_days

                pre_remove_days(start_date,last_day_of_prev_month)

            print("TL From date and to date are in previous month it does have submission date :", pre_start_current.count())
            for pre_start_current in pre_start_current:
                start_date =  (pre_start_current['startdate'])
                end_date =  (pre_start_current['enddate'])
                submitted_date =  (pre_start_current['submitted_date'])

                if submitted_date <= end_date:
                    work_days = 0
                    prev_current_delay = prev_current_delay +  work_days
                else:
                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy
                    
                    prev_current_delay = prev_current_delay +  work_days

                    pre_remove_days(start_date,submitted_date)

            print("TL Start and End date seleted month it does have submission date other month :", pre_start_current_sub_other.count())
            for pre_start_current_sub_other in pre_start_current_sub_other:
                start_date =  (pre_start_current_sub_other['startdate'])
                end_date =  (pre_start_current_sub_other['enddate'])
                submission_date = (pre_start_current_sub_other['submitted_date'])
                if submission_date is not None:
                    if last_day_of_prev_month < submission_date:

                        holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                        delay_days = (last_day_of_prev_month - end_date).days
                        work_days = delay_days - holy

                        prev_current_delay = prev_current_delay +  work_days

                        pre_remove_days(start_date,last_day_of_prev_month)

            print("TL End date previous month it does not have submission date  :", pre_current_sub.count())
            for pre_current_sub in pre_current_sub:
                end_date =  (pre_current_sub['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                delay_days = (last_day_of_prev_month - end_date).days
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay +  work_days

                pre_remove_days(start_day_of_prev_month,last_day_of_prev_month)

                
                
            print("TL End date previous month it have submission date is previous month :", pre_start_current_sub.count())
            for pre_start_current_sub in pre_start_current_sub:
                end_date =  (pre_start_current_sub['enddate'])
                submitted_date =  (pre_start_current_sub['submitted_date'])

                if submitted_date <= end_date:
                    work_days = 0
                    prev_current_delay = prev_current_delay +  work_days
                else:
                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay +  work_days

                    pre_remove_days(start_day_of_prev_month,submitted_date)

                


            print("TL End date and start date not in previous month but submission date in previous month :", pre_this_month_have_submission.count())
            for pre_this_month_have_submission in pre_this_month_have_submission:
                submitted_date =  (pre_this_month_have_submission['submitted_date'])
                if start_day_of_prev_month <= submitted_date:

                    holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,submitted_date )).count()
                    delay_days = (submitted_date - start_day_of_prev_month).days + 1
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay + work_days

                    pre_remove_days(start_day_of_prev_month,submitted_date)


        


            print("TL From date and to date are not in previous month it does not have submission date :", pre_this_month_have_not_submission.count())
            for pre_this_month_have_not_submission in pre_this_month_have_not_submission:
                end_date = (pre_this_month_have_not_submission['enddate'])

                if end_date <= last_day_of_prev_month:

                    holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()
                    delay_days = (last_day_of_prev_month - start_day_of_prev_month).days  + 1
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay + work_days

                    pre_remove_days(start_day_of_prev_month,last_day_of_prev_month)

            
            pre_event_lst_cnt_rm = len(evntlst)
            pre_total_event_leave = pre_event_lst_cnt - pre_event_lst_cnt_rm
            print("Total holiday remove from leave", pre_total_event_leave )
            print("previous month leave count", len(leave_lst) )
            print("previous month event list count when counted", len(evntlst) )
            if pre_total_event_leave <= 0:
                pre_total_event_leave = 0
            pre_grand_tot_leave = len(leave_lst) - pre_total_event_leave
            print("previous month grand total leave ", pre_grand_tot_leave )
            print("prev_current_delay", prev_current_delay)
            if pre_grand_tot_leave <= 0:
                pre_grand_tot_leave = 0
            prev_current_delay = prev_current_delay + pre_grand_tot_leave
            delay_sal_previous = round((one_day_sal_pre * prev_current_delay), 2)
            print("Delay salary Cut previous month", delay_sal_previous)
            previous_sal_main = round((conf_sal - delay_sal_previous), 2)
            print("Previous month total salary",previous_sal_main)

            if previous_sal_main <= 0:
                previous_sal_main = 0


           

            start_day_of_this_month = date.today().replace(day=1)

            def last_day_of_month(any_day):
                # get close to the end of the month for any day, and add 4 days 'over'
                next_month = any_day.replace(day=28) + timedelta(days=4)
                # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
                return next_month - timedelta(days=next_month.day)

            last_day_of_this_month = last_day_of_month(date.today())

            holly_day_current = Event.objects.filter(start_time__range=(start_day_of_this_month,last_day_of_this_month)).count()
           
            working_days_current = ((last_day_of_this_month - start_day_of_this_month).days - holly_day_current) + 1
            
            one_day_sal_current = round((conf_sal / working_days_current), 2)









            this_evntlst = []

            this_event_days = Event.objects.filter(start_time__range=(start_day_of_this_month,last_day_of_this_month)).values('start_time')
            for this_event_days in this_event_days:
                this_evntlst.append(this_event_days['start_time'])

            this_event_lst_cnt = len(this_evntlst)
            

            
            this_leave_lst= []

            def this_remove_days(from_day, end_day):
                this_leaves = leave.objects.filter(from_date__range=(from_day,end_day),to_date__range=(from_day,end_day), user_id = tlid).values('from_date','to_date')
                
                for this_leaves in this_leaves:

                    from_date = (this_leaves['from_date'])
                    to_date =  (this_leaves['to_date'])

                    delta = to_date - from_date
                    for i in range(delta.days + 1):
                        day = from_date + timedelta(days=i)
                       
                        if day in this_leave_lst:
                            this_leave_lst.remove(day)
                        if day in this_evntlst:
                            this_evntlst.remove(day)



            

            


            pro_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pro_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today())).filter(submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= tlid).values('startdate','enddate','submitted_date')
            pro_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pro_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= tlid).values('startdate','enddate','submitted_date')

            
            pro_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= tlid).values('submitted_date')
            pro_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')

            yes_current = 0
            print("From date and to date are in this month it does not have submission date  :", pro_current.count())
            for pro_current in pro_current:
                start_date =  (pro_current['startdate'])
                end_date =  (pro_current['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
                delay_days = (date.today() - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current +  work_days

                this_remove_days(start_date, date.today())



            print("From date and to date are in this month it does have submission date :", pro_start_current.count())
            for pro_start_current in pro_start_current:
                start_date =  (pro_start_current['startdate'])
                end_date =  (pro_start_current['enddate'])
                submitted_date =  (pro_start_current['submitted_date'])
                if submitted_date <= end_date:
                    work_days = 0
                    yes_current = yes_current + work_days
                else:
                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy

                    yes_current = yes_current + work_days

                    this_remove_days(start_date, submitted_date)



  
            print("End date this month it does not have submission date  :", pro_current_sub.count())
            for pro_current_sub in pro_current_sub:
                end_date =  (pro_current_sub['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
                delay_days = (date.today() - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current +  work_days

                this_remove_days(start_day_of_this_month, date.today())

                


           
                
            print("End date this month it have submission date :", pro_start_current_sub.count())
            for pro_start_current_sub in pro_start_current_sub:
                end_date =  (pro_start_current_sub['enddate'])
                submitted_date =  (pro_start_current_sub['submitted_date'])

                if submitted_date <= end_date:
                    work_days = 0
                    yes_current = yes_current + work_days
                else:

                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy

                    yes_current = yes_current + work_days

                    this_remove_days(start_day_of_this_month, submitted_date)




            print("End date and start date not in this month but  submission date in this :", pro_this_month_have_submission.count())
            for pro_this_month_have_submission in pro_this_month_have_submission:

            
                submitted_date =  (pro_this_month_have_submission['submitted_date'])
                holy = Event.objects.filter(start_time__range=(start_day_of_this_month,submitted_date )).count()
                delay_days = (submitted_date - start_day_of_this_month).days + 1
                work_days = delay_days - holy

                yes_current = yes_current + work_days

                this_remove_days(start_day_of_this_month, submitted_date)





            print("From date and to date are not in this month it does not have submission date :", pro_this_month_have_not_submission.count())
            for pro_this_month_have_not_submission in pro_this_month_have_not_submission:
                end_date = (pro_this_month_have_not_submission['enddate'])

                if end_date <= date.today():

                    holy = Event.objects.filter(start_time__range=(start_day_of_this_month,date.today())).count()
                    delay_days = (date.today() - start_day_of_this_month).days + 1
                    work_days = delay_days - holy

                    yes_current = yes_current + work_days

                    this_remove_days(start_day_of_this_month, date.today())

            
            this_month_leave_count = leave.objects.filter(from_date__gte = start_day_of_this_month, to_date__lte = last_day_of_this_month, user_id = tlid).count()
            this_month_leave_count_sub = leave.objects.filter(from_date__range=(start_day_of_this_month,last_day_of_this_month),to_date__range=(start_day_of_this_month,last_day_of_this_month), user_id = tlid).values('from_date','to_date')
            

            if this_month_leave_count >= 1:

                for this_month_leave_count_sub in this_month_leave_count_sub:

                    from_date = (this_month_leave_count_sub['from_date'])
                    to_date =  (this_month_leave_count_sub['to_date'])

                    delta = to_date - from_date
                    for i in range(delta.days + 1):
                        day = from_date + timedelta(days=i)
                        this_leave_lst.append(day)
                        if day in this_evntlst:
                            this_evntlst.remove(day)


    


            this_event_lst_cnt_rm = len(this_evntlst)
            this_total_event_leave = this_event_lst_cnt - this_event_lst_cnt_rm
            print("Total holiday remove from leave", this_total_event_leave )
            print("This month leave count", len(this_leave_lst) )
            print("This month event list count when counted", len(this_evntlst) )
            if this_total_event_leave <= 0:
                this_total_event_leave = 0
            this_grand_tot_leave = len(this_leave_lst) - this_total_event_leave
            print("This month grand total leave ", this_grand_tot_leave )
            if this_grand_tot_leave <= 0:
                this_grand_tot_leave = 0
            yes_current = yes_current + this_grand_tot_leave
            print("Total Current Month Delay", yes_current)
            delay_sal_current = round((one_day_sal_current * yes_current), 2)
            print("Delay salary Cut", delay_sal_current)
            this_month_sal_main = round((conf_sal - delay_sal_current), 2)
            print("This month total salary",this_month_sal_main)

            if this_month_sal_main <= 0:
                this_month_sal_main = 0

            
        else:
            previous_sal_main = 0
            this_month_sal_main = 0







        mem = user_registration.objects.filter(id=tlid)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=tlid)
        dev = user_registration.objects.filter(tl_id=tlid)
        ids = dev.values_list('id', flat="true")
        des = designation.objects.get(designation="developer")
        le = leave.objects.filter(user_id__in=ids.all(
        ), designation_id=des.id, leaveapprovedstatus=0)

        

        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]

        l=leave.objects.filter(to_date__gte=date.today())
       
        
        count=user_registration.objects.filter(~Q(id__in=l.values_list('user_id', flat=True)),tl_id=user_id.id,status="active",work_status='0').count()
        return render(request, 'TLdashboard.html', {'labels': labels, 'data': data, 'mem': mem, 'le': le,'count':count,
         'previous_sal_main':previous_sal_main, 'this_month_sal_main':this_month_sal_main, 'last_day_of_prev_month':last_day_of_prev_month, 'start_day_of_prev_month':start_day_of_prev_month })
    else:
        return redirect('/')
        
def tldevview(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        rid=request.GET.get('rid')
        mem1=reported_issue.objects.filter(id=id)
        
        return render(request, 'tldevview.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')


def dev_Work_not_assign(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        tli =user_registration.objects.get(id=tlid)
        tl=user_registration.objects.filter(id=tli.id)
        pm=tli.projectmanager_id
        pman = user_registration.objects.filter(id=pm)
      
        l=leave.objects.filter(to_date__gte=date.today())
       
        dev=user_registration.objects.filter(~Q(id__in=l.values_list('user_id', flat=True)),tl_id=tli.id,status="active",work_status='0')
        req=WorkRequest.objects.filter(wrkreq_tl_id=tlid,wrkreq_date=date.today())
        return render(request, 'tl_worknot_assign.html',{'mem':mem,'tl':tl,'dev':dev,'req':req,'pman':pman})
    else:
        return redirect('/')


        
def TLprojects(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        display1 = project.objects.all()
        notific=project_taskassign.objects.filter(tl_id=tlid,delay__gt='4').count()
       
        display=project_taskassign.objects.filter(developer_id=tlid).values('project_id').distinct()
        return render(request, 'TLprojects.html',{'display':display,'mem':mem,'display1':display1,'notific':notific})
    else:
        return redirect('/')

def tlprojecttasks(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
            
        
        if request.method == 'POST':
            uid = request.POST.get('id')
            mems = project_taskassign.objects.get(id=uid)
            task = test_status()
            task.date = datetime.now()
            task.workdone = request.POST['workdone']
            task.git_commit = request.POST['gitcommit']
            task.git_link = request.POST['gitlink']
            task.user_id = tlid
            task.subtask_id = mems.id
            task.project_id = mems.project_id
            
            dct_file = dict(request.FILES)
            lst_screenshot = dct_file['filed']
            lst_file = []
            for ins_screenshot in lst_screenshot:
                str_img_path = ""
                if ins_screenshot:
                    img_emp = ins_screenshot
                    fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                    str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                    str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                    lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                    task.json_testerscreenshot = lst_file
            task.save()
            proj=project.objects.get(id=id)
           
            msg_success = "Task added successfully"
            return render(request, 'TLprojecttasks.html', {'msg_success':msg_success,'proj':proj})
        else:
            
            request.session['splitid']=id
            mem = user_registration.objects.filter(id=tlid)
            mem1 = test_status.objects.filter(subtask_id=id)
            mem2 = tester_status.objects.filter(user_id=tlid)
            time=datetime.now()
            taskstatus = test_status.objects.all()
            proj=project.objects.get(id=id)
            display = project_taskassign.objects.filter(developer_id=tlid).filter(project_id=id)
            tasks = project_taskassign.objects.filter(project_id=id,developer_id = tlid)
            mem3 = user_registration.objects.get(id=tlid)
            display1=mem3.fullname
           
            return render(request, 'TLprojecttasks.html',{'display1':display1,'time':time,'display':display,'mem':mem,'mem1':mem1,'mem2':mem2,'taskstatus':taskstatus,'tasks':tasks,'proj':proj})
    else:
        return redirect('/')


#*********************************** Tl project document section shebin shaji 28-101-22

    
def Tl_ptoject_doc(request,tlproj_id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        tl = user_registration.objects.get(id=tlid)
        spa = user_registration.objects.filter(tl_id=tl.id, status="active")
        pro_corr=ProjectCorrectionUpdation.objects.filter(project_cu_id_id=tlproj_id,ptl_name=tl.fullname,project_cu_status='correction').order_by('-id')
        pro__up=ProjectCorrectionUpdation.objects.filter(project_cu_id_id=tlproj_id,ptl_name=tl.fullname,project_cu_status='updation')
        return render(request, 'TLproject_doc.html',{'mem':mem,'pro_corr':pro_corr,'pro__up':pro__up,'spa':spa})
    else:
        return redirect('/')
    
def TLproject_doc_emp_save(request,TLprj_docemp):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        if request.method == 'POST':
            empname = request.POST['doc_empname']
            docemp=user_registration.objects.get(id=int(empname))
            doc_assdate = request.POST['doc_start_date']
            doc=ProjectCorrectionUpdation.objects.get(id=TLprj_docemp)
            doc.pdev_name=docemp.fullname
            doc.project_cu_start=doc_assdate
            prid=doc.project_cu_id.id
            doc.save()
        return redirect('Tl_ptoject_doc',prid)
    else:
        return redirect('/')
            





#******************************************************************************************

def extensionsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.extension = request.POST['days']
        task.reason = request.POST['reason']
        task.extension_date = datetime.now()
        task.extension_status = "submitted"
        task.save()
        base_url = reverse('tlprojecttasks', kwargs={'id': task.project_id})
        query_string = urlencode({'id': task.project_id})
        url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
    
 
def tlprojectsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.progress= request.POST['progress']
        task.projectstatus = request.POST['prostatus']
        task.save()
        base_url = reverse('tlsplittask', kwargs={'id':id})
        query_string = urlencode({'id':id})
        url = '{}?{}'.format(base_url, query_string)
    return redirect(url)

def pdetailsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.progress= request.POST['progress']
        task.project_status = request.POST.get('status')
        task.save()
        base_url = reverse('tlprojecttasks', kwargs={'id': task.project_id})
        query_string = urlencode({'id': task.project_id})
        url = '{}?{}'.format(base_url, query_string)
    return redirect(url)

def extensionapprove(request,id):

    task = project_taskassign.objects.get(id=id)
    task.extension_status = "Approved"
    task.extension_date = datetime.now()
    task.save()
    base_url = reverse('tlsplittask', kwargs={'id': id})
    query_string =  urlencode({'id': id})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
    
    

def extensionreject(request,id):
  
    task = project_taskassign.objects.get(id=id)
    task.extension_status = "Rejected"
    task.extension_date = datetime.now()
    task.save()
    base_url = reverse('tlsplittask', kwargs={'id': id})
    query_string =  urlencode({'id': id})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
    
 

def tltaskstatus(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
       
        
            
    else:
        return redirect('/')
    
def tlsplittask(request,id):
        if 'tlid' in request.session:
            if request.session.has_key('tlid'):
                tlid = request.session['tlid']
            else:
                return redirect('/')
            wtype=project_taskassign.objects.get(id=id)
            
            if wtype.worktype == '0':
                splitid = request.session['splitid']
                sub1 = project_taskassign.objects.get(id=id)
                test = test_status.objects.all()
                tester = tester_status.objects.all()
                mem = user_registration.objects.filter(id=tlid)
                sub = project_taskassign.objects.filter(~Q(developer_id=tlid)).filter(project_id=splitid,tl_id=tlid) 
                return render(request, 'TLsplittask.html',{'mem':mem,'sub':sub,'sub1':sub1,'test':test,'tester':tester})
            else:
                prj=wtype.project.id
                return redirect('tlprojecttasks',prj) 
        else:
            return redirect('/') 

def tlgivetask(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        splitid = request.session['splitid']
      
        mem = user_registration.objects.filter(id=tlid)
        dept_id = user_registration.objects.get(id=tlid)
       
        e = designation.objects.get(designation="tester")
        dev_id = designation.objects.get(designation="developer")
        e1 = e.id
        spa = user_registration.objects.filter(tl_id=dept_id.id, status="active")
        spa1 = user_registration.objects.filter(designation_id=e1, status="active")
        time=datetime.now().date()
        tasks = project_taskassign.objects.filter(developer_id=tlid,project_id=splitid).values('task').distinct()
        new = project.objects.get(id=splitid)
        
        if request.method =='POST':
            
            var = project_taskassign()
           
            var.developer_id =  request.POST['ename']
            var.tl_id = tlid
            var.tester_id = request.POST['tname']
            var.tl_description=request.POST.get('description')
            var.subtask=request.POST.get('subtask')
            var.task = request.POST.get('task')
            var.startdate= request.POST.get('start_date')
            var.enddate= request.POST.get('date')
            var.files=request.FILES['files']
            var.extension=0
            var.project_id = splitid
            var.description = new.description
            var.worktype='1'
            var.save()
            v = request.POST.get('ename')
            em=user_registration.objects.get(id=v)
            em.projectmanager_id=dept_id.projectmanager_id
            em.save()

            user=user_registration.objects.get(id=request.POST['ename']) #developer work status change
            user.work_status='1'
            user.save()

            # print(em.email)
            # subject = 'Greetings from iNFOX TECHNOLOGIES'
            # message = 'Congratulations,\n' \
            # 'You are assigned new project from iNFOX TECHNOLOGIES.\n' \
            # 'following is your Project Details\n'\
            # 'Project :'+str(var.project.project)+'\n' 'Task : '+str(var.task) +'\n' 'Description : '+str(var.tl_description)+'\n' 'SubTask : '+str(var.subtask)+'\n''Start Date : '+str(var.startdate)+'\n' 'End Date : '+str(var.enddate)+'\n'\
            # '\n' 'Complete your project on or before Enddate \n'\
            #     'NOTE : THIS IS A SYSTEM GENETATED MAIL PLEASE DO NOT REPLY' 
            # recepient = str(em.email)
            # send_mail(subject, message, settings.EMAIL_HOST_USER,
            #       [recepient], fail_silently=False)
            msg_success = "Task split successfully"
            return render(request, 'TLgivetask.html',{'msg_success':msg_success})
        else:
            return render(request, 'TLgivetask.html',{'mem':mem,'spa':spa,'spa1':spa1,'time':time,'tasks':tasks,'dept_id':dept_id})
    else:
        return redirect('/')

def TLattendance(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLattendance.html',{'mem':mem})
    else:
        return redirect('/')

def TLattendancesort(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=tlid)
        return render(request, 'TLattendancesort.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')   

def TLreportissues(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLreportissues.html',{'mem':mem})
    else:
        return redirect('/') 

def TLreportissues(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLreportissues.html',{'mem':mem})
    else:
        return redirect('/')   

def TLreportedissue1(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(reporter_id=tlid).order_by("-id")
        return render(request, 'TLreportedissue1.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   

def TLreportedissue2(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(id=id)
        return render(request, 'TLreportedissue2.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   
   
def TLreport1(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')  
        mem1 = user_registration.objects.get(id=tlid)
        
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.reported_to_id=mem1.projectmanager_id
            vars.reporter_id=tlid
            vars.status='pending'
            vars.save()
            return redirect('TLreport1')
        else:
            mem = user_registration.objects.filter(id=tlid)
            return render(request, 'TLreport1.html',{'mem':mem})
    else:
        return redirect('/')

def devtlreported(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(reported_to_id=tlid).order_by("-id")
        return render(request, 'devtlreported.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   
 
def TLreportsuccess(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')    
        mem = user_registration.objects.filter(id=tlid)
        mem1 = user_registration.objects.get(id=tlid)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.designation_id=mem1.designation_id
            vars.reporter_id=tlid
            vars.status='pending'
            vars.save()
        return render(request, 'TLreportsuccess.html',{'mem':mem})
    else:
        return redirect('/')


def TLtasks(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        task = tasks.objects.filter(user_id=tlid).order_by("-id")
        return render(request, 'TLtasks.html',{'mem':mem,'task':task})
    else:
        return redirect('/')
        
def TLtasksub(request,id):
    task = tasks.objects.get(id=id)
    task.status = "1"
    task.save()
    return redirect('TLtasks')

def TLtaskformsubmit(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        dev1 = user_registration.objects.get(id=tlid)
        if request.method == "POST":
            var = datetime.now().date()
            task = project_taskassign.objects.get(id=id)
            task.employee_description = request.POST['description']
            task.git_link = request.POST['gitlink']
            task.employee_files = request.FILES['scn']
            task.submitted_date = var
          
            x = task.enddate
            y = var
            event = Event.objects.filter(start_time__range=(task.enddate,datetime.now().date())).count()
            event1 = Event.objects.filter(start_time__range=(task.startdate,datetime.now().date())).count()
            
            d1=datetime.now().date() - task.startdate
            w=d1.days - event1
            if w <= 0:
                task.tsakworkdays=1
            else:
                task.tsakworkdays=w 


          
            if task.status == 'correction':
            
                test=TSproject_Task_verify.objects.filter(ts_tester=task.tester, ts_project_task=task).last()
            
                events = Event.objects.filter(start_time__range=(test.ts_task_verify_date,datetime.now().date())).count()

            
                delta=datetime.now().date() - test.ts_task_verify_date
            
                delay=delta.days - events
                wrk=delay
                if delay > 0:
                    total= delay + int(task.delay)
                    task.delay = total
                    task.status = 'Verification'
                    task.submitted_date = datetime.now().date()
                    task.save()
                

                else:
                    delay=0
                    total= delay + int(task.delay)
                    task.delay = total
                    task.status = 'Verification'
                    task.submitted_date = datetime.now().date()
                    task.save()
                
                
                if request.method == 'POST':  
                
                    corre_up=ProjectCorrectionUpdation.objects.get(id=int(request.POST.get('ptid')))
                    corre_up.project_cu_olddescrip=request.POST.get('doc_privios')
                    corre_up.project_oldui= request.FILES.get('doc_privios_img')
                    corre_up.project_cu_newdescrip=request.POST.get('doc_new')
                    corre_up.project_cu_newui= request.FILES.get('doc_new_img')
                    corre_up.project_cu_start=test.ts_task_verify_date
                    corre_up.project_cu_end=datetime.now().date()
                    if wrk == 0:
                        wrk=1
                    corre_up.project_cu_wdays=int(wrk)
                    corre_up.save()
                
                msg_success = "Task submitted successfully"
                return render(request, 'TLgivetasks.html', {'mem': mem, 'msg_success': msg_success})
            
            else:
                dev1.work_status='0'
                dev1.save()
                task.submitted_date = datetime.now().date()
                if task.worktype == '0':
                     task.status = 'submitted'
                else:
                    task.status = 'Verification'
                delta = datetime.now().date() - task.enddate
                delay = delta.days - event
                if delay > 0:
                    task.delay = delay
                    task.save()
                else:
                    task.delay = 0
                    task.save()
                msg_success = "Task submitted successfully"
                return render(request, 'TLgivetasks.html', {'mem': mem, 'msg_success': msg_success})

        return render(request, 'TLsuccess.html', {'mem': mem, 'task': task})
    else:
        return redirect('/')

           

def TLleavereq(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLleavereq.html',{'mem':mem})
    else:
        return redirect('/')


def TLreqedleave(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var = leave.objects.filter(user_id=tlid)
        return render(request, 'TLreqedleave.html',{'var': var,'mem':mem})
    else:
        return redirect('/')

def tl_leave_form(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        des1 = designation.objects.get(designation='team leader')
        if request.method == "POST":
            leaves = leave()
            leaves.from_date = request.POST['from']
            leaves.to_date = request.POST['to']
            leaves.leave_status = request.POST['haful']
            leaves.reason = request.POST['reason']
            leaves.user_id = tlid
            leaves.status = "submitted"
            leaves.designation_id = des1.id
            leaves.leaveapprovedstatus=0
            
            start = datetime.strptime(leaves.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(leaves.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                leaves.days = 1
            else:
                leaves.days = diff - cnt
                
                
            leaves.save()
        return render(request, 'TLleavereq.html',{'mem':mem})   
    else:
        return redirect('/')


def TLgivetasks(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        time = datetime.now()
        task = project_taskassign.objects.filter(developer_id=tlid).filter(id=id)
        corr = ProjectCorrectionUpdation.objects.filter(project_tsak_id_id=id).last()
        return render(request, 'TLgivetasks.html', {'mem': mem, 'task': task, 'time': time,'corr':corr})
    else:
        return redirect('/')

def TLgavetask(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        task = project_taskassign.objects.filter(developer_id=tlid).filter(id=id)
        return render(request, 'TLgavetask.html', {'mem': mem, 'task': task})
    else:
        return redirect('/')

def TLleave(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLleave.html',{'mem':mem})
    else:
        return redirect('/')


#------------------------------------------------------------------------------------------------------

#tester module

def TSdashboard(request):
    if 'usernametsid' in request.session:
       
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets).filter(fullname=usernamets1)
        return render(request,'TSdashboard.html',{'mem':mem})
    else:
        return redirect('/')

def TStask(request):
    if 'usernametsid' in request.session:

        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
            return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets).filter(fullname=usernamets1)
        task = tasks.objects.filter(user_id=usertsid).order_by("-id")
        return render(request,'TStask.html',{'mem':mem,'tasks':task})
    else:
        return redirect('/')


def testasksub(request,id):
    
    task = tasks.objects.get(id=id)
    task.status = "1"
    task.save()
    return redirect('TStask')
        
def TSproject(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        pros = project_taskassign.objects.filter(tester=usertsid).values('project').distinct()
        verify_count=project_taskassign.objects.filter(status='verification',tester=usertsid).values('project').distinct()
        new = project.objects.all()  
        return render(request,'TSproject.html',{'mem':mem,'pros':pros,'new':new,'verify_count':verify_count})
    else:
        return redirect('/')

def TSprojectdetails(request,pid):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
           return redirect('/')
    

        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        var = project_taskassign.objects.filter(project=pid,tester_id=usertsid,worktype='1').order_by('-status')
        data = tester_status.objects.filter(project_id=pid)
        data1 = test_status.objects.filter(project_id=pid)
        deg=designation.objects.filter(Q(designation='developer')| Q(designation='team leader'))
        
        verify_count=project_taskassign.objects.filter(status='verification', project=pid, tester=usertsid,worktype='1').count()


        date1= datetime.now()
        return render(request,'TSprojectdetails.html',{'date1':date1,'mem':mem,'var':var,'data':data,'data1':data1,'deg':deg,'verify_count':verify_count})
    else:
        return redirect('/')
    

def TSproject_verifiy(request,ts_task_verify):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        pts=project_taskassign.objects.get(id=ts_task_verify)
        proj=project_module_assign.objects.filter(project_name=pts.project)
        c_date=date.today()
       
        if c_date == pts.submitted_date:
            num=1
        else:
            num=0
        return render(request,'TSproject_verify.html',{'mem':mem,'pts':pts,'num':num,'proj':proj})
    else:
        return redirect('/')


def TSproject_status_confirm(request,ts_prj_task_verify):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
           return redirect('/')
       
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        if request.method == 'POST':
            task_verify=request.POST['verify_status']
            delay_reson=request.POST['tsdelay_reson']
           
           
    
        prj_task=project_taskassign.objects.get(id=ts_prj_task_verify)
        prj_task.status=task_verify
        prj_task.save()
        c_date=date.today()


        if task_verify == 'correction':
            t=tester_status()
            t.tester=user_registration.objects.get(id=usertsid) 
            t.project=prj_task.project
            t.task=prj_task
            t.subtask=prj_task
            t.date=date.today()
            t.workdone=request.POST['doc_pm_cumodule_dese']
            t.files= request.FILES.get('files')
            t.progress=0
            t.save()
            
            proj_doc_cu=ProjectCorrectionUpdation()
            proj_doc_cu.project_tsak_id=prj_task
            proj_doc_cu.project_cu_module=prj_task.task
            proj_doc_cu.project_cu_descrip=request.POST['doc_pm_cumodule_dese']
            proj_doc_cu.pdev_name=prj_task.developer.fullname
            proj_doc_cu.ptl_name=prj_task.tl.fullname
          
            proj_doc_cu.project_cu_id=prj_task.project
            proj_doc_cu.project_date=date.today()
            proj_doc_cu.project_cu_status='correction'
            proj_doc_cu.save()


        event = Event.objects.filter(start_time__range=(prj_task.submitted_date,datetime.now().date())).count()
        delys=c_date - prj_task.submitted_date
        delys=delys.days - event
      
        if delys > 0:
            verify_task=TSproject_Task_verify(ts_project_task=prj_task,ts_reson_dely=delay_reson,
                                                ts_delay=delys,ts_tester=prj_task.tester,ts_task_status=task_verify,ts_task_sub_date=prj_task.submitted_date)
            verify_task.save()
        else:
            verify_task=TSproject_Task_verify(ts_project_task=prj_task,ts_reson_dely=delay_reson,
                                                ts_delay=0,ts_tester=prj_task.tester,ts_task_status=task_verify,ts_task_sub_date=prj_task.submitted_date)
            verify_task.save()
        pts=project_taskassign.objects.get(id=ts_prj_task_verify)
        prj_id=prj_task.project.id
        return redirect('TSprojectdetails', prj_id)
    else:
        return redirect('/')

        


def testersave(request,uid,pid):

    if request.session.has_key('usernametsid'):
        usertsid = request.session['usernametsid']
    else:
        return redirect('/')
    pr = project_taskassign.objects.get(id=pid)
    user = user_registration.objects.get(id=uid)
    if request.method == 'POST':
        test = tester_status()
        test.tester_id = usertsid
        test.date = datetime.now()
        test.project_id = pr.project_id
        test.user_id = user.id
        test.progress = pr.progress
        test.subtask_id = pid
        test.workdone = request.POST.get('workdone')
        test.files = request.FILES['files']
        test.task=pr
        test.save()
        base_url = reverse('TSprojectdetails', kwargs={'pid': test.project_id})
        query_string = urlencode({'pid': test.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)



def projectdetailsave(request,uid,pid):
    if request.session.has_key('usernametsid'):
        usertsid = request.session['usernametsid']
    else:
       return redirect('/')
    if request.method == 'POST':
        
        user = project_taskassign.objects.get(developer_id=uid,id=pid)
        user.progress = request.POST.get('dprogress')
        user.projectstatus = request.POST.get('sp')
        user.save()
        base_url = reverse('TSprojectdetails', kwargs={'pid': user.project_id})
        query_string = urlencode({'pid': user.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)


def TSassigned(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        
        data = project_taskassign.objects.get(id=id)
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSassigned.html',{'mem':mem,'data':data})
    else:
        return redirect('/')

def TSsubmitted(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        
        var = project_taskassign.objects.get(id=id)
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSsubmitted.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def TSsubmittedsave(request,id):
    if 'usernametsid' in request.session:
        if request.method =='POST':
            
            a = project_taskassign.objects.get(id=id)
            a.employee_description = request.POST.get('empdescription')
            a.employee_files = request.FILES.get('empfile')
            a.submitted_date = datetime.now()
            a.status = "submitted"
            a.save()
            return redirect('TStask')
        else:
            pass
    else:
        return redirect('/')


def TSsucess(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSsucess.html',{'mem':mem})
    else:
        return redirect('/')

#-----------------------------------------------------------------------------------------------------------------------------------------

#developer module

def devindex(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devindex.html', {'dev': dev})


def devdashboard(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    


    user_id = user_registration.objects.get(id=devid)
    conf_sal = user_id.confirm_salary
    if conf_sal == "":
        conf_sal = 0
    else:
        conf_sal = int(user_id.confirm_salary)

    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

    start_day_of_this_month = date.today().replace(day=1)

    def last_day_of_month(any_day):
        # get close to the end of the month for any day, and add 4 days 'over'
        next_month = any_day.replace(day=28) + timedelta(days=4)
        # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
        return next_month - timedelta(days=next_month.day)

    last_day_of_this_month = last_day_of_month(date.today())

    previous_sal_main = 0
    this_month_sal_main = 0

    if conf_sal > 0:
        

        


        prev_holly_day = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()

        # print("Previous Month Holly day:", prev_holly_day)
        working_days_pre = ((last_day_of_prev_month - start_day_of_prev_month).days - prev_holly_day) + 1
        # print("Previous Month working days:", working_days_pre)
        one_day_sal_pre = round((conf_sal / working_days_pre), 2)
        # print("Previous Month one day salary:", one_day_sal_pre)

        # print("First day of prev month:", start_day_of_prev_month)
        # print("Last day of prev month:", last_day_of_prev_month)


        pre_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pre_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= devid).values('startdate','enddate','submitted_date')
        pre_start_current_sub_other = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(~Q(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(developer_id= devid).values('startdate','enddate','submitted_date')
        pre_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pre_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= devid).values('startdate','enddate','submitted_date')

        
        pre_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= devid).values('submitted_date')
        pre_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)),submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')



        pre_month_leave_count = Event.objects.filter(start_time__gte = "2022-05-01", start_time__lte = "2022-05-27").count()   
        print("pre hollyday in gte lte", pre_month_leave_count)
        pre_month_leave_count_sub = Event.objects.filter(start_time__range=("2022-05-01", "2022-05-27")).count()
        print("pre hollyday in range", pre_month_leave_count_sub)    


        prev_current_delay = 0
        print("dev From date and to date are in previous month it does not have submission date  :", pre_current.count())
        for pre_current in pre_current:
            end_date =  (pre_current['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
            delay_days = (last_day_of_prev_month - end_date).days
            work_days = delay_days - holy

            prev_current_delay = prev_current_delay +  work_days


        print("dev From date and to date are in previous month it does have submission date :", pre_start_current.count())
        for pre_start_current in pre_start_current:
            end_date =  (pre_start_current['enddate'])
            submitted_date =  (pre_start_current['submitted_date'])

            delay_days = (submitted_date - end_date).days
            if delay_days <= 0:
                work_days = 0
                prev_current_delay = prev_current_delay +  work_days
            else:
                delay_days = (submitted_date - end_date).days
                holy = Event.objects.filter(start_time__gte=end_date,start_time__lte = submitted_date).count()
                work_days = delay_days - holy
                prev_current_delay = prev_current_delay +  work_days
                
        
        print("dev Start and End date seleted month it does have submission date other month :", pre_start_current_sub_other.count())
        for pre_start_current_sub_other in pre_start_current_sub_other:
            end_date =  (pre_start_current_sub_other['enddate'])
            submission_date = (pre_start_current_sub_other['submitted_date'])
            if submission_date is not None:
                if last_day_of_prev_month < submission_date:

                    holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                    delay_days = (last_day_of_prev_month - end_date).days
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay +  work_days

        print("dev End date previous month it does not have submission date  :", pre_current_sub.count())
        for pre_current_sub in pre_current_sub:
            end_date =  (pre_current_sub['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
            delay_days = (last_day_of_prev_month - end_date).days
            work_days = delay_days - holy

            prev_current_delay = prev_current_delay +  work_days

            
            
        print("dev End date previous month it have submission date is previous month :", pre_start_current_sub.count())
        for pre_start_current_sub in pre_start_current_sub:
            end_date =  (pre_start_current_sub['enddate'])
            submitted_date =  (pre_start_current_sub['submitted_date'])

            if submitted_date <= end_date:
                work_days = 0
                prev_current_delay = prev_current_delay +  work_days
            else:
                holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                delay_days = (submitted_date - end_date).days
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay +  work_days

            


        print("dev End date and start date not in previous month but submission date in previous month :", pre_this_month_have_submission.count())
        for pre_this_month_have_submission in pre_this_month_have_submission:
            submitted_date =  (pre_this_month_have_submission['submitted_date'])
            if start_day_of_prev_month <= submitted_date:

                holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,submitted_date )).count()
                delay_days = (submitted_date - start_day_of_prev_month).days + 1
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay + work_days


    


        print("dev From date and to date are not in previous month it does not have submission date :", pre_this_month_have_not_submission.count())
        for pre_this_month_have_not_submission in pre_this_month_have_not_submission:
            end_date = (pre_this_month_have_not_submission['enddate'])

            if end_date <= last_day_of_prev_month:

                holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()
                delay_days = (last_day_of_prev_month - start_day_of_prev_month).days  + 1
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay + work_days


        previous_sal_main
        print("prev_current_delay", prev_current_delay)
        delay_sal_previous = one_day_sal_pre * prev_current_delay
        print("Delay salary Cut previous month", delay_sal_previous)
        previous_sal_main = round((conf_sal - delay_sal_previous), 2)
        print("Previous month total salary",previous_sal_main)

        if previous_sal_main <= 0:
            previous_sal_main = 0


        

        
        # print("First day of This  month:", start_day_of_this_month)
        # print("Last day of This month:", last_day_of_this_month)

        holly_day_current = Event.objects.filter(start_time__range=(start_day_of_this_month,last_day_of_this_month)).count()
        # print("Holly day:", holly_day_current)
        working_days_current = ((last_day_of_this_month - start_day_of_this_month).days - holly_day_current) + 1
        # print("Current Month day:", working_days_current)
        one_day_sal_current = round((conf_sal / working_days_current), 2)
        # print("One Day:", one_day_sal_current)

        tot_day = 0
        work_del = 0
        this_month_leave = leave.objects.filter(from_date__range=(start_day_of_this_month,date.today()),to_date__range=(start_day_of_this_month,date.today()), user_id  = devid).values('from_date','to_date')

        for x in this_month_leave:
            from_date = x['from_date']
            to_date = x['to_date']
            diff_days = ((to_date - from_date).days ) + 1
            if diff_days == 0:
                main_days = 0
                tot_day = tot_day + main_days
            else:
                hol= Event.objects.filter(start_time__gte=from_date,start_time__lte=to_date).count()
                main_days = (diff_days - hol)
                tot_day = tot_day + main_days

        print("This month Leave",tot_day )

        def delay_leave_ext(start,end):
            this_month_leave = leave.objects.filter(from_date__range=(start_day_of_this_month,date.today()),to_date__range=(start_day_of_this_month,date.today()), user_id  = devid).values('from_date','to_date')

            for x in this_month_leave:
                from_date = x['from_date']
                to_date = x['to_date']
                diff_days = ((to_date - from_date).days ) + 1
                if diff_days == 0:
                    main_days = 0
                    tot_day = tot_day + main_days
                else:
                    hol= Event.objects.filter(start_time__gte=from_date,start_time__lte=to_date).count()
                    main_days = (diff_days - hol)
                    tot_day = tot_day + main_days



        pro_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pro_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today())).filter(submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= devid).values('startdate','enddate','submitted_date')
        pro_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pro_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= devid).values('startdate','enddate','submitted_date')

        
        pro_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= devid).values('submitted_date')
        pro_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')

        yes_current = 0
        print("dev From date and to date are in this month it does not have submission date  :", pro_current.count())
        for pro_current in pro_current:
            end_date =  (pro_current['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
            delay_days = (date.today() - end_date).days
            work_days = delay_days - holy

            yes_current = yes_current +  work_days


        print("dev From date and to date are in this month it does have submission date :", pro_start_current.count())
        for pro_start_current in pro_start_current:
            end_date =  (pro_start_current['enddate'])
            submitted_date =  (pro_start_current['submitted_date'])
            if submitted_date <= end_date:
                work_days = 0
                yes_current = yes_current + work_days
            else:
                holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                delay_days = (submitted_date - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current + work_days


    

        print("dev End date this month it does not have submission date  :", pro_current_sub.count())
        for pro_current_sub in pro_current_sub:
            end_date =  (pro_current_sub['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
            delay_days = (date.today() - end_date).days
            work_days = delay_days - holy

            yes_current = yes_current +  work_days

          
        

        
            
        print("dev End date this month it have submission date :", pro_start_current_sub.count())
        for pro_start_current_sub in pro_start_current_sub:
            end_date =  (pro_start_current_sub['enddate'])
            submitted_date =  (pro_start_current_sub['submitted_date'])

            if submitted_date <= end_date:
                work_days = 0
                yes_current = yes_current + work_days
            else:

                holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                delay_days = (submitted_date - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current + work_days

         


        print("dev End date and start date not in this month but submission date in this :", pro_this_month_have_submission.count())
        for pro_this_month_have_submission in pro_this_month_have_submission:
            
            if start_day_of_this_month <= submitted_date:
                submitted_date =  (pro_this_month_have_submission['submitted_date'])
                holy = Event.objects.filter(start_time__range=(submitted_date,start_day_of_this_month)).count()
                delay_days = (submitted_date - start_day_of_this_month ).days + 1
                work_days = delay_days - holy

                yes_current = yes_current + work_days


        


        print("dev From date and to date are not in this month it does not have submission date :", pro_this_month_have_not_submission.count())
        for pro_this_month_have_not_submission in pro_this_month_have_not_submission:
            end_date = (pro_this_month_have_not_submission['enddate'])

            if end_date <= date.today():

                holy = Event.objects.filter(start_time__range=(start_day_of_this_month,date.today())).count()
                delay_days = (date.today() - start_day_of_this_month).days + 1
                work_days = delay_days - holy

                yes_current = yes_current + work_days


        print("Current Month Delay", yes_current)
        delay_sal_current = round((one_day_sal_current * yes_current), 2)
        print("Delay salary Cut", delay_sal_current)
        this_month_sal_main = round((conf_sal - delay_sal_current), 2)
        print("This month total salary",this_month_sal_main)

        if this_month_sal_main <= 0:
            this_month_sal_main = 0

        
    else:
        previous_sal_main = 0
        this_month_sal_main = 0



    dev = user_registration.objects.filter(id=devid)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=devid)
    for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
    work_check=user_registration.objects.get(id=devid)
    wreq=WorkRequest.objects.filter(wrk_develp_id=devid,wrkreq_date=date.today()).exists()
    if wreq :
         work_req=WorkRequest.objects.get(wrk_develp_id=devid,wrkreq_date=date.today())
    else:
        work_req=NULL

    return render(request, 'devdashboard.html', {'labels':labels,'data':data,'dev': dev,  'previous_sal_main':previous_sal_main, 'this_month_sal_main':this_month_sal_main, 'last_day_of_prev_month':last_day_of_prev_month,
     'start_day_of_prev_month':start_day_of_prev_month,'work_check':work_check,'work_req':work_req})


def devReportedissues(request):
    if 'devid' in request.session:    
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        return render(request,'devReportedissues.html',{'dev':dev})
    else:
        return redirect('/')

# work request by developer
def Dev_workrequest(request,dev_wrequest):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
           return redirect('/')
        dev = user_registration.objects.get(id=dev_wrequest)
        tl = user_registration.objects.get(id=dev.tl_id)
        work_req=WorkRequest()
        work_req.wrk_develp=dev
        work_req.wrkreq_tl=tl
        work_req.wrk_status='requested'
        work_req.save()
        return redirect('devdashboard')
    else:
        return redirect('/')
        

def devreportissue(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        var=reported_issue.objects.filter(reporter_id=devid).order_by("-id")    
        return render(request,'devreportissue.html',{'var':var,'dev':dev})
    else:
        return redirect('/')


def devreportedissue(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
           return redirect('/')
        
        var=reported_issue.objects.filter(reporter_id=devid)  
        dev = user_registration.objects.filter(id=devid)  
        return render(request,'devreportedissue.html',{'var':var,'dev':dev})
    else:
        return redirect('/')


def devsuccess(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        
        dev = user_registration.objects.filter(id=devid)
        tl = user_registration.objects.get(id=devid)
        if request.method == 'POST':           
            vars = reported_issue()
            vars.issue=request.POST.get('reportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=tl.tl_id
            vars.reporter_id=devid
            vars.status='pending'
            vars.save()
        return render(request,'devsuccess.html',{'dev':dev})
    else:
        return redirect('/')


def devissues(request,id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    man = reported_issue.objects.filter(id=id)
    return render(request, 'devissues.html', {'dev': dev,'man':man})


def devsample(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devsample.html', {'dev': dev})


# *********************praveesh*********************


def Devapplyleav(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav.html', {'dev': dev})


def dev_leave_form(request):
    des1 = designation.objects.get(designation='developer')
    if request.method == "POST":
        leaves = leave()
        leaves.from_date = request.POST['from']
        leaves.to_date = request.POST['to']
        leaves.leave_status = request.POST['haful']
        leaves.reason = request.POST['reason']
        leaves.leaveapprovedstatus=0
        leaves.user_id = request.POST['dev_id']
        leaves.designation_id = des1.id
        
        start = datetime.strptime(leaves.from_date, '%Y-%m-%d').date() 
        end = datetime.strptime(leaves.to_date, '%Y-%m-%d').date()

        diff = (end  - start).days
        
        cnt =  Event.objects.filter(start_time__range=(start,end)).count()
        
        if diff == 0:
            leaves.days = 1
        else:
            leaves.days = diff - cnt
            
        leaves.save()
        return render(request, 'Devapplyleav.html')
    else:
        return render(request, 'Devapplyleav1.html')


def Devapplyleav1(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav1.html', {'dev': dev})


def Devapplyleav2(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav2.html', {'dev': dev})


def Devleaverequiest(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    devl = leave.objects.filter(user_id=devid)
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devleaverequiest.html', {'dev': dev, 'devl': devl})

def Devattendance(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        return render(request, 'Devattendance.html', {'dev': dev})
    else:
        return redirect('/')

def Devattendancesort(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=devid)          
        return render(request, 'Devattendancesort.html',{'dev':dev,'mem1':mem1})
        
    else:
        return redirect('/')


def Tattend(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Tattend.html', {'dev': dev})


def Devapplyleav3(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav3.html', {'dev': dev})


# **************************maneesh*******************************


def DEVprojects(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    pros = project.objects.all()
    devp = project_taskassign.objects.filter(developer_id=devid).values('project_id').distinct()
    return render(request, 'DEVprojects.html', {'dev': dev, 'devp': devp, 'pros': pros})


def DEVtable(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    devp = project_taskassign.objects.filter(project_id=id).filter(developer_id=devid).order_by("-id")
    teststatus = test_status.objects.all()
    proj=project.objects.get(id=id)
    testerstatus = tester_status.objects.filter(project_id=id)
    time = datetime.now()
   
    return render(request, 'DEVtable.html', {'dev': dev, 'devp': devp, 'time': time, 'teststatus': teststatus,'testerstatus': testerstatus,'proj':proj})


#******************Developer Project Document section **********************

def DEV_projrect_doc(request,dev_prjdoc_id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    dev1 = user_registration.objects.get(id=devid)
    proj=project.objects.get(id=dev_prjdoc_id)
    task=project_taskassign.objects.filter(project=proj,developer=dev1).last()

    if task.status == 'submitted':
        prj_module=project_module_assign.objects.filter(project_name=proj)
        dev = user_registration.objects.filter(id=devid)
        try:
            prj_doc=PM_ProjectDocument.objects.get(doc_project_id=proj)
        except PM_ProjectDocument.DoesNotExist:
            return redirect('DEVprojects')
        prj_doc_crr_up=ProjectCorrectionUpdation.objects.filter(project_cu_id=proj,pdev_name=dev1.fullname).order_by('-id')
        return render(request, 'DEV_project_doc.html', {'dev': dev,'proj':proj,'prj_module':prj_module,'prj_doc':prj_doc,'prj_doc_crr_up':prj_doc_crr_up})
    else:
       return redirect('DEVprojects')


def docrequirements(request,dev_prjredoc_id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    prj=project.objects.get(id=dev_prjredoc_id)
    proj_md=project_module_assign.objects.filter(project_name=prj)
    proj_table=project_table.objects.filter(project=prj)
    proj_other=project_other_assign.objects.filter(othproject_name=prj)
    return render(request, 'DEV_docrequirements.html', {'dev': dev,'prj':prj,'proj_md':proj_md,'proj_table':proj_table,'proj_other':proj_other})
    



def DEV_project_FB(request,dev_prj_fb):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    proj=project.objects.get(id=dev_prj_fb)
    doc=PM_ProjectDocument.objects.get(doc_project_id=proj)
    if request.method == 'POST':  
        fend = request.POST.get('fend')
        bend = request.POST.get('bend')
        doc.doc_project_frontend=fend
        doc.doc_project_backend=bend
        doc.save()
    return redirect('DEV_projrect_doc',dev_prj_fb)


def DEV_corr_up(request,dev_prj_cu_id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    if request.method == 'POST':  
        pre = request.POST.get('doc_privios')
        pre_img = request.FILES.get('doc_privios_img')
        new = request.POST.get('doc_new')
        new_img = request.FILES.get('doc_new_img')
        p1=request.POST.get('doc_sdate')
        p2=request.POST['doc_edate']
        sdate=parse_date(p1)
        edate=parse_date(p2)
        work_days=edate - sdate
        work_days=work_days.days
        if work_days == 0:
            work_days=1
       

    corre_up=ProjectCorrectionUpdation.objects.get(id=dev_prj_cu_id)
    corre_up.project_cu_olddescrip=pre
    corre_up.project_oldui=pre_img
    corre_up.project_cu_newdescrip=new
    corre_up.project_cu_newui=new_img
    corre_up.project_cu_start=sdate
    corre_up.project_cu_end=edate
    corre_up.project_cu_wdays=work_days
    corre_up.save()
   
    prj=corre_up.project_cu_id.id
    return redirect('DEV_projrect_doc',prj)


#developer project daily data entry

def DEV_project_doc_daily_doc_add(request,DEV_pdocdaily):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    dev1 = user_registration.objects.get(id=devid)
    proj=project.objects.get(id=DEV_pdocdaily)

    if request.method == 'POST':  
        check1 = request.POST.get('check1')
        check2 = request.POST.get('check2')
        check3 = request.POST.get('check3')
        check4 = request.POST.get('check4')
        check5 = request.POST.get('check5')
        check6 = request.POST.get('check6')
       
        if  check1 == '1':
            p1 = request.POST['pdname']
            p2 = request.POST['pddese']
            doc1=ProjectDocDetails()
            doc1.doc_project_d=proj
            doc1.doc_duser=dev1
            doc1.doc_project_mdname=p1
            doc1.doc_project_mddise_d=p2
            doc1.save()

        if  check2 == '1':
            p3 = request.POST['pmname']
            p4 = request.POST['pmdese']
            doc2=ProjectDocModels()
            doc2.doc_project_md=proj
            doc2.doc_mduser=dev1
            doc2.doc_project_mdname=p3
            doc2.doc_project_dise_md=p4
            doc2.save()

        if  check3 == '1':
            p5 = request.POST['pvname']
            p6 = request.POST['pvdese']
            doc3=ProjectDocViews()
            doc3.doc_project_v=proj
            doc3.doc_vuser=dev1
            doc3.doc_project_vname=p5
            doc3.doc_project_vdise=p6
            doc3.save()

        if  check4 == '1':
            p7 = request.POST['phpname']
            p8 = request.POST['phpdese']
            p13 = request.FILES.get('phpimg')
            p14= request.POST['phpmdname']
            doc4=ProjectDochtmlpages()
            doc4.doc_project_hp=proj
            doc4.doc_hpuser=dev1
            doc4.doc_project_hpname=p7
            doc4.doc_project_hpdise=p8
            doc4.doc_project_html_page=p13
            doc4.doc_project_hpmdname=p14
            doc4.save()

        if  check5 == '1':
            p9 = request.POST['plbname']
            p10 = request.POST['plbdese']
            doc5=ProjectDoclibraryies()
            doc5.doc_project_lb=proj
            doc5.doc_lbuser=dev1
            doc5.doc_project_lbname=p9
            doc5.doc_project_lbdise=p10
            doc5.save()

        if  check6 == '1':
            p11 = request.POST['podname']
            p12 = request.POST['poddese']
            doc6=ProjectDocother()
            doc6.doc_project_oth=proj
            doc6.doc_othuser=dev1
            doc6.doc_project_othname=p11
            doc6.doc_project_othdise=p12
            doc6.save()
   
    return redirect ('DEV_projrect_doc',DEV_pdocdaily)


  
   



#**********************************************************************************************
def DEVtaskstatus(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    mem = project_taskassign.objects.get(id=id)
    if request.method == 'POST':
        task = test_status()
        task.date = datetime.now()
        task.workdone = request.POST['workdone']
        task.git_commit = request.POST['gitcommit']
        task.git_link = request.POST['gitlink']
        task.user_id = devid
        task.subtask_id = mem.id
        task.project_id = mem.project_id
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['filed']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                task.json_testerscreenshot = lst_file
        task.save()
       
        base_url = reverse('DEVtable', kwargs={'id': task.project_id})
        query_string = urlencode({'id': task.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def DEVextension(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    mem = project_taskassign.objects.get(id=id)
    if request.method == 'POST':
        ext = project_taskassign.objects.get(id=id)
        ext.extension = request.POST['dayz']
        ext.reason = request.POST['reason']
        ext.extension_date = datetime.now()
        ext.extension_status = "submitted"
        ext.save()
        base_url = reverse('DEVtable', kwargs={'id': ext.project_id})
        query_string = urlencode({'id': ext.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
        
def devprjsave(request,id):
    if request.method == 'POST':
       
        ext = project_taskassign.objects.get(id=id)
        ext.progress = request.POST['devpro']
        ext.projectstatus = request.POST['devstat']
        ext.save()
        base_url = reverse('DEVtable', kwargs={'id': ext.project_id})
        query_string = urlencode({'id': ext.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
       


def DEVtaskmain(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
            return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        task = tasks.objects.filter(user_id=devid).order_by("-id")
        return render(request,'DEVtaskmain.html', {'dev':dev,'task':task})
    else:
        return redirect('/')


def devtasksub(request,id):
    
    task = tasks.objects.get(id=id)
    task.status = "1"
    task.save()
    return redirect('DEVtaskmain')


def DEVtaskform(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    time = datetime.now()
    dev = user_registration.objects.filter(id=devid)
    task = project_taskassign.objects.filter(developer_id=devid).filter(id=id)
    corr = ProjectCorrectionUpdation.objects.filter(project_tsak_id_id=id).last()
    return render(request, 'DEVtaskform.html', {'dev': dev, 'task': task, 'time': time,'corr':corr})

def DEVtaskformsubmit(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    dev1 = user_registration.objects.get(id=devid)
    if request.method == "POST":
        task = project_taskassign.objects.get(id=id)
        task.employee_description = request.POST['description']
        task.git_link = request.POST['gitlink']
        task.employee_files = request.FILES['scn']
        var = datetime.now().date()
        x = task.enddate
        y = var
        event = Event.objects.filter(start_time__range=(task.enddate,datetime.now().date())).count()
        event1 = Event.objects.filter(start_time__range=(task.startdate,datetime.now().date())).count()
        
        d1=datetime.now().date() - task.startdate
        w=d1.days - event1
        if w <= 0:
            task.tsakworkdays=1
        else:
            task.tsakworkdays=w 
        if task.status == 'correction':
          
            test=TSproject_Task_verify.objects.filter(ts_tester=task.tester, ts_project_task=task).last()
           
            events = Event.objects.filter(start_time__range=(test.ts_task_verify_date,datetime.now().date())).count()

           
            delta=datetime.now().date() - test.ts_task_verify_date
           
            delay=delta.days - events
            wrk=delay
          
            if delay > 0:
                total= delay + int(task.delay)
                task.delay = total
                task.status = 'Verification'
                task.submitted_date = datetime.now().date()
                task.save()
               

            else:
                delay = 0
                total = delay + int(task.delay)
                task.delay = total
                task.status = 'Verification'
                task.submitted_date = datetime.now().date()
                task.save()

            if request.method == 'POST':  
                
                corre_up=ProjectCorrectionUpdation.objects.get(id=int(request.POST.get('prtid')))
                corre_up.project_cu_olddescrip=request.POST.get('doc_privios')
                corre_up.project_oldui= request.FILES.get('doc_privios_img')
                corre_up.project_cu_newdescrip=request.POST.get('doc_new')
                corre_up.project_cu_newui= request.FILES.get('doc_new_img')
                corre_up.project_cu_start=test.ts_task_verify_date
                corre_up.project_cu_end=datetime.now().date()
                if wrk == 0:
                    wrk=1
                corre_up.project_cu_wdays=int(wrk)
                corre_up.save()

            msg_success = "Task submitted successfully"
            return render(request, 'DEVtaskform.html', {'dev': dev, 'msg_success': msg_success})
        
        else:
            dev1.work_status='0'
            dev1.save()
            task.submitted_date = datetime.now().date()
            task.status = 'Verification'
            delta = datetime.now().date() - task.enddate
            delay = delta.days - event
            if delay > 0:
                task.delay = delay
                task.save()
            else:
                task.delay = 0
                task.save()
            msg_success = "Task submitted successfully"
            return render(request, 'DEVtaskform.html', {'dev': dev, 'msg_success': msg_success})
    return render(request, 'DEVtasksumitted.html', {'dev': dev, 'task': task})

def DEVtask(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    task = project_taskassign.objects.filter(developer_id=devid).filter(id=id)
    return render(request, 'DEVtask.html', {'dev': dev, 'task': task})


def dev_task_submit(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    if request.method == "POST":
        dpid = request.POST.get('dpid')
        member = project_taskassign.objects.get(id=dpid)
        member.employee_description=request.POST['workdone']
        member.save()
        return redirect('DEVtable')


def DEVsuccess(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'DEVsuccess.html', {'dev': dev})

def DEVtasksumitted(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'DEVtasksumitted.html', {'dev': dev})
    
    
    
    
    
    
    
    #**********************internship****************
    
def man_internship_view(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'man_internship_view.html',{'mem':mem})
    
def BRadmin_internship_view(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_internship_view.html',{'Adm':Adm})

def registrationview(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,'registrationview.html',{'Adm':Adm})

def registrationviewman(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'registrationviewman.html',{'mem':mem})

def BRadmin_internship(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)

    var1=internship.objects.all().order_by("-id")
    return render(request,'BRadmin_internship.html',{'var1':var1,'Adm':Adm})
    
def man_internship(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id) 
    var1=internship.objects.all().order_by("-id")
    return render(request,'man_internship.html',{'var1':var1,'mem':mem})

def man_internship_date(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    newdata1 = internship.objects.all().values('reg_date').distinct()
    return render(request,'man_internship_date.html',{'mem':mem,'newdata':newdata1})
    
def man_internship_dateview(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    reg_date=request.GET.get('reg_date')
    empid1=internship.objects.filter(reg_date=reg_date)
    return render(request,'man_internship_dateview.html',{'mem':mem,'data':empid1})

def BRadmin_internship_date(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    newdata = internship.objects.all().values('reg_date').distinct()
    return render(request,'BRadmin_internship_date.html',{'Adm':Adm,'newdata':newdata})
    
def BRadmin_internship_dateview(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    reg_date=request.GET.get('date')
    empid=internship.objects.filter(reg_date=reg_date)
    return render(request,'BRadmin_internship_dateview.html',{'Adm':Adm,'data':empid})
    

def BRadmin_internship_update(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    return render(request,'BRadmin_internship_update.html',{'var':var,'Adm':Adm})
    
def render_pdf_view(request,id):

    date = datetime.now()   
    mem = internship.objects.get(id=id)
    template_path = 'pdf.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


    
def internshipupdatesave(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    var.fullname = request.POST['fullname']
    var.collegename = request.POST['college']
    var.reg_no = request.POST['regno']
    var.course = request.POST['course']
    var.stream = request.POST['stream']        
    var.platform = request.POST['platform']        
    #var.branch_id  =  request.POST['branch']        
    var.start_date =  request.POST['startdate']        
    var.end_date  =  request.POST['enddate']        
    var.mobile  =  request.POST['mobile']        
    var.alternative_no  =  request.POST['altmob']        
    var.email = request.POST['email']
    var.hrmanager = request.POST['hrmanager']
    var.guide = request.POST['guide']
    var.rating = request.POST['rating']
    
    if request.FILES.get('profile_pic') is not None:
         var.profile_pic  =  request.FILES['profile_pic']
    var.save()
    return redirect('BRadmin_internship')

def interndelete(request,id):
    man = internship.objects.get(id=id)
    man.delete()
    return redirect('BRadmin_internship')

def maninterndelete(request,id):
    man1 = internship.objects.get(id=id)
    man1.delete()
    return redirect('man_internship')


def certificate_intrn(request,id):

    date = datetime.now()   
    mem = internship.objects.get(id=id)
    mems = internship.objects.filter(id=id)
    template_path = 'certificate_intrn.html'
    context = {'mem': mem, 'mems': mems,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
       

#*****************************registration********


# def man_registration_update(request,id):
#     if 'Adm_id' in request.session:
#         if request.session.has_key('Adm_id'):
#             Adm_id = request.session['Adm_id']
#         else:
#             return redirect('/')    
#         Adm = user_registration.objects.filter(id=Adm_id)
        
#         mem4 = user_registration.objects.get(id=id)
#         con = conditions.objects.get(id=1)
#         xem = extracurricular.objects.get(user_id=id)
#         qem = qualification.objects.get(user_id=id)
#         des = designation.objects.filter(~Q(designation='admin'))
        
#         admins = user_registration.objects.get(id=Adm_id)
        
#         br_name = branch_registration.objects.get(id=admins.id)
        
#         return render(request,'man_registration_update.html',{'con':con,'mem4':mem4,'qem':qem,'xem':xem,'Adm':Adm, 'des':des, 'br_name':br_name})
#     else:
#         return redirect('/')

def man_registration_update(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        mem4 = user_registration.objects.get(id=id)
        con = conditions.objects.get(id=1)
        try:
            xem = extracurricular.objects.get(user_id=id)
        except extracurricular.DoesNotExist:
            xem = None
        try:
            qem = qualification.objects.get(user_id=id)
        except qualification.DoesNotExist:
            qem= None
        des = designation.objects.filter(~Q(designation='admin'))
        desig = designation.objects.all().exclude(designation = 'team leader').exclude(designation ='manager').exclude(designation ='trainee').exclude(designation ='project manager').exclude(designation ='tester').exclude(designation ='trainingmanager').exclude(designation ='account').exclude(designation ='trainer').exclude(designation ='developer')

        admins = user_registration.objects.get(id=Adm_id)

        br_name = branch_registration.objects.get(id=admins.id)

        return render(request, 'man_registration_update.html', {'con': con, 'mem4': mem4, 'qem': qem, 'xem': xem, 'Adm': Adm, 'des': des, 'br_name': br_name, 'desig':desig})
    else:
        return redirect('/')

def man_registration(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    mem1 = user_registration.objects.all().order_by("-id")
    return render(request,'man_registration.html',{'mem':mem,'mem1':mem1})
    
def BRadmin_registration(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')   
        
    if 'stop_status' in request.POST:
        uid = request.POST.get("His_id")
        user = user_registration.objects.get(id=uid)
        if user.status=="active":
            user.status="stop"
            user.save()
            return redirect("BRadmin_registration")
        else:
            user.status="active"
            user.save()
            return redirect("BRadmin_registration")
    else:    
        if  request.method=="POST":
            u_id = request.POST.get("id")
            dept_id = request.POST.get("dept")
            desi_id = request.POST.get("des")
            emp_ty = request.POST.get("emp_type")
            res = request.POST.get("stat")

            user = user_registration.objects.get(id=u_id)
            user.department_id = dept_id 
            user.status = res
            user.employee_type=emp_ty
            user.designation_id = desi_id
            if desi_id == '6' or desi_id == '4':
                user.work_status='0'
            user.save()
            return redirect("BRadmin_registration")
        
        Adm = user_registration.objects.filter(id=Adm_id)
        mem1 = user_registration.objects.filter(~Q(status="resigned")).order_by("-id")
        mem2 = designation.objects.filter(~Q(designation="admin"))
        mem3 = department.objects.all()
        return render(request,'BRadmin_registration.html',{'mem3':mem3,'mem2':mem2,'Adm':Adm,'mem1':mem1})

def BRadmin_resign(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    if request.method=="POST":
        u_id = request.POST.get("id")
        dept_id = request.POST.get("dept")
        desi_id = request.POST.get("des")
        user = user_registration.objects.get(id=u_id)
        user.department_id = dept_id 
        
        user.designation_id = desi_id
        user.save()
        return redirect("BRadmin_registration")
    Adm = user_registration.objects.filter(id=Adm_id)
    mem1 = user_registration.objects.filter(status="resigned").order_by("-id")
    mem2 = designation.objects.all()
    mem3 = department.objects.all()
    return render(request,'BRadmin_resign.html',{'mem3':mem3,'mem2':mem2,'Adm':Adm,'mem1':mem1})
    
def man_resign(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    if request.method=="POST":
        u_id = request.POST.get("id")
        dept_id = request.POST.get("dept")
        desi_id = request.POST.get("des")
        user = user_registration.objects.get(id=u_id)
        user.department_id = dept_id 
        
        user.designation_id = desi_id
        user.save()
        return redirect("BRadmin_registration")
    mem = user_registration.objects.filter(id=m_id)
    mem1 = user_registration.objects.filter(status="resigned").order_by("-id")
    mem2 = designation.objects.all()
    mem3 = department.objects.all()
    return render(request,'man_resign.html',{'mem3':mem3,'mem2':mem2,'mem':mem,'mem1':mem1})


def registrationupdatesave(request, id):
    a = user_registration.objects.get(id=id)
    b = qualification.objects.get(user_id=id)
    try:
        c = extracurricular.objects.get(user_id=id)
    except extracurricular.DoesNotExist:
        c = None

    d = conditions.objects.get(id=1)
    if request.method == 'POST':
        a.fullname = request.POST['name']
        a.fathername = request.POST['fathersname']
        a.mothername = request.POST['mothersname']
        a.presentaddress1 = request.POST['presentaddress1']
        a.presentaddress2 = request.POST['presentaddress2']
        a.presentaddress3 = request.POST['presentaddress3']
        a.pincode = request.POST['pincode']
        a.district = request.POST['district']
        a.state = request.POST['state']
        a.permanentaddress1 = request.POST['permanentaddress1']
        a.permanentaddress2 = request.POST['permanentaddress2']
        a.permanentaddress3 = request.POST['permanentaddress3']
        a.permanentpincode = request.POST['permanentpincode']
        a.permanentdistrict = request.POST['permanentdistrict']
        a.permanentstate = request.POST['permanentstate']
        a.designation_id = request.POST['designation']
        a.desig_input = request.POST['desg']
        a.department_input = request.POST['department_current']
        a.mobile = request.POST['mobile']
        a.alternativeno = request.POST['altmobile1']
        a.email = request.POST['email']
        a.hrmanager = request.POST['hrname']
        a.joiningdate = request.POST['dateofjoin']
        a.startdate = request.POST['startdate']
        a.enddate = request.POST['enddate']
        a.workperformance = request.POST['performance']
        a.hr_designation = request.POST['hrdesignation']
        if request.FILES.get('signature') is not None:
            a.signature = request.FILES['signature']
        a.save()

        b.user_id = a.id
        b.school = request.POST['school']
        b.schoolaggregate = request.POST['aggregate']
        b.ugdegree = request.POST['degree']
        b.ugstream = request.POST['stream']
        b.ugpassoutyr = request.POST['passoutyear']
        b.ugaggregrate = request.POST['aggregate1']
        b.pg = request.POST['pg']
        b.save()
        
        if c :
            c.user_id = a.id
            c.internshipdetails = request.POST['details']
            c.internshipduration = request.POST['duration1']
            c.internshipcertificate = request.POST['certification']
            c.onlinetrainingdetails = request.POST['details1']
            c.onlinetrainingduration = request.POST['duration2']
            c.onlinetrainingcertificate = request.POST['certification1']
            c.projecttitle = request.POST['title']
            c.projectduration = request.POST['duration3']
            c.projectdescription = request.POST['description']
            c.projecturl = request.POST['url']
            c.skill1 = request.POST['skill1']
            c.skill2 = request.POST['skill2']
            c.skill3 = request.POST['skill3']
            c.save()
            
        d.condition1 = request.POST.get("condition1")
        d.condition2 = request.POST.get("condition2")
        d.condition3 = request.POST.get("condition3")
        d.condition4 = request.POST.get("condition4")
        d.condition5 = request.POST.get("condition5")
        d.condition6 = request.POST.get("condition6")
        d.save()
        return redirect('BRadmin_registration')
        
def registrationdelete(request,id):
    man = user_registration.objects.get(id=id)
  
    man1 = extracurricular.objects.get(user_id=man.id)
    man2 = qualification.objects.get(user_id=man.id)
    man2.delete()
    man1.delete()
    man.delete()
    os.remove(man.idproof.path)
    os.remove(man.photo.path)
    return redirect('BRadmin_registration')
    
#########################  trainee Payment New ######################

def trainee_payment(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainee_payment.html',{'z':z})
    else:
        return redirect('/')

def trainee_payment_addpayment(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        z = user_registration.objects.filter(id=usernametrns2)
        mem1 = user_registration.objects.get(id=usernametrns2)
        if request.method=="POST":
            ad=paymentlist()
            ad.amount_pay=request.POST['amount']
            ad.amount_date=request.POST['paymentdate']
            ad.amount_downlod=request.FILES['files']
            ad.current_date = datetime.now()
            ad.user_id=mem1
            ad.amount_status=0
            member = user_registration.objects.get(id=usernametrns2)
            co = course.objects.get(id = member.course_id)
            member.total_pay=int(request.POST['amount'])+member.total_pay
            member.payment_balance = co.total_fee - member.total_pay
            member.save()
            ad.save()
            return redirect('/trainee_payment')
        return render(request,'trainee_payment_addpayment.html',{'z':z})
    else:
        return redirect('/')

def trainee_payment_viewpayment(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        mem=paymentlist.objects.filter(user_id = usernametrns2).order_by('-id')
        return render(request,'trainee_payment_viewpayment.html',{'z':z,'mem':mem})
                
    else:
        return redirect('/')




def pm_leavestatus(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        dept  = user_registration.objects.get(id=prid)

        dep = department.objects.filter(id=dept.department_id)
        des = designation.objects.all()
        emp = user_registration.objects.all()
        return render(request,'pm_leavestatus.html',{'pro':pro,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')
        
@csrf_exempt
def pm_leave(request):
    
    emp = request.GET.get('emp')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')
    leaves = leave.objects.filter(user_id=emp,from_date__gte=fdate,to_date__lte=tdate)
    return render(request,'pm_leave.html', {'names':leaves})

#########################  Accounts New ##########################################################################################################

# def accounts_leavehistory(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         d = department.objects.all()
#         return render(request,'accounts_leavehistory.html',{'z' : z,'d':d})
#     else:
#         return redirect('/')

@csrf_exempt
def accounts_leave(request):
    
    emp = request.GET.get('emp')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')
    leaves = leave.objects.filter(user_id=emp,from_date__gte=fdate,to_date__lte=tdate)
    return render(request,'accounts_leave.html', {'names':leaves})
    
def accounts_leavehistory(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        d = department.objects.all()
        return render(request, 'accounts_leavehistory.html', {'z': z, 'd': d})
    else:
        return redirect('/')

        
# def accounts_leavehistory_department(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         var = department.objects.get(id=id)
#         de = designation.objects.filter(~Q(designation='account'))
#         return render(request,'accounts_leavehistory_department.html',{'z' : z,'de':de,'var':var})
#     else:
#         return redirect('/')

def accounts_leavehistory_department(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var = department.objects.get(id=id)
        de = designation.objects.filter(~Q(designation='account'))
        return render(request, 'accounts_leavehistory_department.html', {'z': z, 'de': de, 'var': var})
    else:
        return redirect('/')

# def accounts_leavehistory_employees(request,id,id1):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         var=user_registration.objects.filter(designation_id=id,department_id=id1)
#         return render(request,'accounts_leavehistory_employees.html',{'z' : z,'var':var})
#     else:
#         return redirect('/')
    
def accounts_leavehistory_employees(request, id, id1):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var = user_registration.objects.filter(
            designation_id=id, department_id=id1, status="active")
        return render(request, 'accounts_leavehistory_employees.html', {'z': z, 'var': var})
    else:
        return redirect('/')
        
# def accounts_emp_leavehistory(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         var = leave.objects.filter(user=id)
#         return render(request,'accounts_emp_leavehistory.html',{'z' : z,'var':var})
#     else:
#         return redirect('/')

def accounts_emp_leavehistory(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var = leave.objects.filter(user=id)
        return render(request, 'accounts_emp_leavehistory.html', {'z': z, 'var': var})
    else:
        return redirect('/')


# def accounts_Dashboard(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         year = date.today().year
#         month = date.today().month
#         vars = vars = acntspayslip.objects.filter(~Q(fromdate__year=year,
#                                           fromdate__month=month)).count()
#         vars1 = user_registration.objects.filter(confirm_salary_status=1).count()
#         des2 = designation.objects.get(designation='trainee')
#         Adm1 = designation.objects.get(designation="Admin")
#         vars2 = user_registration.objects.exclude(designation=des2.id).exclude(designation=Adm1.id).count()
#         vars3 = acntspayslip.objects.filter(fromdate__year=year,
#                                           fromdate__month=month).count()
#         deta = user_registration.objects.filter(designation=des2.id,payment_status=0).count()
#         deta2 = user_registration.objects.filter(designation=des2.id).count()
#         deta2 = user_registration.objects.filter(designation=des2.id,).count()
#         icount=internship.objects.all().count()
#         return render(request, 'accounts_Dashboard.html', {'z': z,'vars':vars,'vars1':vars1,'vars2':vars2,'vars3':vars3,'deta':deta,'deta2':deta2,'icount':icount})
#     else:
#         return redirect('/')

def accounts_Dashboard(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        year = date.today().year
        month = date.today().month
        vars = vars = acntspayslip.objects.filter(~Q(fromdate__year=year,
                                          fromdate__month=month)).count()
        vars1 = user_registration.objects.filter(confirm_salary_status=1).count()
        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars2 = user_registration.objects.exclude(designation=des2.id).exclude(designation=Adm1.id).count()
        vars3 = acntspayslip.objects.filter(fromdate__year=year,
                                          fromdate__month=month).count()
        deta = user_registration.objects.filter(designation=des2.id,payment_status=0).count()
        deta2 = user_registration.objects.filter(designation=des2.id).count()
        deta2 = user_registration.objects.filter(designation=des2.id,).count()
        icount=internship.objects.all().count()
        return render(request, 'accounts_Dashboard.html', {'z': z,'vars':vars,'vars1':vars1,'vars2':vars2,'vars3':vars3,'deta':deta,'deta2':deta2,'icount':icount})
    else:
        return redirect('/')

# def account_accounts(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id= usernameacnt2)
#         return render(request,'account_accounts.html', {'z': z})
#     else:
#         return redirect('/')

def account_accounts(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request, 'account_accounts.html', {'z': z})
    else:
        return redirect('/')

# def imagechange_accounts(request):
#     if 'usernameacnt2' in request.session:
#         if request.method == 'POST':
#             id = request.GET.get('id')
#             abc = user_registration.objects.get(id=id)
#             abc.photo = request.FILES['filenamees']
#             abc.save()
#             return redirect('account_accounts')
#         return render(request,'account_accounts.html' )
#     else:
#         return redirect('/')

def imagechange_accounts(request):
    if 'usernameacnt2' in request.session:
        if request.method == 'POST':
            id = request.GET.get('id')
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filenamees']
            abc.save()
            return redirect('account_accounts')
        return render(request, 'account_accounts.html')
    else:
        return redirect('/')
        
def changepassword_accounts(request):
    if 'usernameacnt2' in request.session:
            if request.session.has_key('usernameacnt2'):
                usernameacnt2 = request.session['usernameacnt2']
            z = user_registration.objects.filter(id=usernameacnt2)
            if request.method == 'POST':
                abc = user_registration.objects.get(id=usernameacnt2)
                oldps = request.POST['currentPassword']
                newps = request.POST['newPassword']
                cmps = request.POST.get('confirmPassword')
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request,'accounts_Dashboard.html', {'z': z})
                    return render(request,'changepassword_accounts.html', {'z': z})
                return render(request,'changepassword_accounts.html', {'z': z})
    else:
        return redirect('/')

def accounts_employee(request): 
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2) 
        des = department.objects.all()
        return render(request,'accounts_employee.html',{'des':des,'z' : z})
    else:
        return redirect('/')

def accounts_emp_dep(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = department.objects.get(id=id)
        des=designation.objects.all()
        context = {'mem':mem,'des':des,'z' : z,}
        return render(request,'accounts_emp_dep.html', context)
    else:
        return redirect('/')

def accounts_emp_list(request,id,pk): 
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)  
        mem = department.objects.get(id=id)
        mem1 = designation.objects.get(pk=pk)
        use=user_registration.objects.filter(department_id=mem.id,designation=mem1, status="active")
        context = {'use':use,'z' : z,}
        return render(request,'accounts_emp_list.html', context)
    else:
        return redirect('/')

def accounts_emp_details(request,id):  
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)  
        vars=user_registration.objects.get(id=id)
        context = {'vars':vars,'z' : z,}
        return render(request,'accounts_emp_details.html', context)
    else:
        return redirect('/')

def accounts_payment(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = department.objects.all()
        return render(request,'accounts_payment.html', {'des' : des ,'z' : z,})
    else:
        return redirect('/')

def accounts_payment_dep(request,id): 
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = course.objects.get(id=id)
        des = designation.objects.all()
        context = {'mem':mem,'des':des,'z' : z,}
        return render(request,'accounts_payment_dep.html', context)
    else:
        return redirect('/')

def accounts_payment_list(request,id,pk):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2) 
        mem = department.objects.get(id=id)
        mem1 = designation.objects.get(pk=pk)
        use=user_registration.objects.filter(department_id=mem.id,designation=mem1,status="active")
        context = {'use':use,'z' : z,}
        return render(request,'accounts_payment_list.html', context)
    else:
        return redirect('/')

def accounts_coursefee(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem=course.objects.all()
        return render(request,'accounts_coursefee.html',{'mem':mem,'z' : z,})
    else:
        return redirect('/')

def accounts_coursefee_addnew(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem=course()
        if request.method=="POST":
            mem.name=request.POST['coursename']
            mem.total_fee=request.POST['totalfee']
            try:
                user= course.objects.get(name=mem.name)
                context = {'msg': 'Course already exists!!!....  Try to add another course','z':z}
                return render(request,'accounts_coursefee_addnew.html',context)
            except :
                mem.save()
                return redirect('/accounts_coursefee')
        return render(request,'accounts_coursefee_addnew.html',{'z':z})
    else:
        return redirect('/')  

def coursefeeupdate(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method=="POST":
            abc=course.objects.get(id=id)
            abc.total_fee=request.POST['totalfee']
            abc.save()
            return redirect('accounts_coursefee')
        return render(request,'accounts_coursefee_addnew.html',{'z' : z,})
    else:
        return redirect('/')

def coursedelete(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        abc=course.objects.get(id=id)
        abc.delete()
        return redirect('accounts_coursefee')
    else:
        return redirect('/')

def accounts_registration_details(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id).order_by('-id')
        vars = paymentlist.objects.all()
        return render(request,'accounts_registration_details.html', { 'z' : z, 'deta':deta , 'vars':vars})
    else:
        return redirect('/')

def accounts_payment_detail_list(request, id):
    if 'usernameacnt2' in request.session:
        
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        
        else:
            return redirect('/')

        z = user_registration.objects.filter(id=usernameacnt2)

        a = user_registration.objects.get(id=id)
        
        pay = paymentlist.objects.filter(user_id_id = a.id).order_by('-id')
        
        return render(request,'accounts_payment_detail_list.html',{ 'z' : z, 'pay': pay , 'a':a })
    else:
        return redirect('/')

def verify(request,id):
    rem = paymentlist.objects.get(id=id)
    rem.amount_status = 1
    rem.save()
    return redirect('/accounts_registration_details')
    
def reminder(request,id):
    rem = user_registration.objects.get(id=id)
    rem.payment_status = 1
    rem.save()
    return redirect('/accounts_registration_details')

def accounts_expenses(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars=acntexpensest.objects.all()
        return render(request,'accounts_expenses.html',{'z':z, 'vars':vars})
    else:
        return redirect('/')

def accounts_expenses_viewEdit(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var=acntexpensest.objects.filter(id=id)
        return render(request,'accounts_expenses_viewEdit.html',{'z':z, 'var':var})
    else:
        return redirect('/')

def accounts_expenses_viewEdit_Update(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method == 'POST':
            emps = acntexpensest.objects.get(id=id)
            emps.payee = request.POST['payee']
            emps.payacnt = request.POST['payacnt']
            emps.paymethod = request.POST['paymod']
            emps.paydate = request.POST['paydt']
            emps.category = request.POST['category']
            emps.description = request.POST['description']
            emps.refno = request.POST['ref']
            emps.amount = request.POST['amount']
            emps.tax = request.POST['tax']
            emps.total = request.POST['total']                
            emps.save() 
            return redirect('/accounts_expenses')
        return render(request,'accounts_expenses_viewEdit.html',{'z':z})
    else:
        return redirect('/')

def accounts_expense_newTransaction(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem=acntexpensest()
        if request.method == 'POST':
            mem.payee = request.POST['payee']
            mem.payacnt = request.POST['payacnt']
            mem.paymethod = request.POST['paymod']
            mem.paydate = request.POST['paydt']
            mem.category = request.POST['category']
            mem.description = request.POST['description']
            mem.refno = request.POST['ref']
            mem.amount = request.POST['amount']
            mem.tax = request.POST['tax']
            mem.total = request.POST['total']                
            mem.save()
            return redirect('/accounts_expenses')
        else:
            return render(request,'accounts_expense_newTransaction.html',{'z':z})
    else:
        return redirect('/')

def account_report(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request,'account_report.html',{'z':z})
    else:
        return redirect('/')
        
def account_reportt_issue(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = reported_issue()
        if request.method == 'POST':
            vars.issue=request.POST['issue']
            vars.reporter_id=usernameacnt2
            vars.reported_date=datetime.now()
            vars.issuestatus=0
            vars.save()
            return redirect('account_report')
        return render(request,'account_report_issue.html',{'z':z})
    else:
        return redirect('/')
    
def account_reported_issue(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        n = reported_issue.objects.filter(reporter_id=usernameacnt2).order_by('-id')
        return render(request,'account_reported_issue.html',{'z':z,'n':n})
    else:
        return redirect('/')

def account_payment_details(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars=user_registration.objects.get(id=id)
        context = {'vars':vars,'z' : z,}
        return render(request,'account_payment_details.html', context)
    else:
        return redirect('/')

def account_payment_salary(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        vars=user_registration.objects.get(id=id)
        if request.method == "POST":
            abc = acntspayslip()
            abc.basic_salary = request.POST["salary"]
            abc.hra = request.POST["hra"]
            abc.conveyns = request.POST["ca"]
            abc.pf_tax = request.POST["pt"]
            abc.incentives = request.POST["ins"]
            abc.delay = request.POST["leaves"]
            abc.net_salary = request.POST["net_salary"]
            abc.leavesno= request.POST["commonleaves"]
            abc.fromdate= request.POST["efdate"]
            abc.tax = 0
            abc.da = request.POST['DA']
            abc.pf = request.POST["pf"]
            abc.incometax = 0
            abc.other_allovance = request.POST["other_allowance"]
            abc.other_allovancetype = request.POST["other_allowance_type"]
            abc.basictype = request.POST["basictype"]
            abc.pftype = request.POST["pftype"]
            abc.esitype = request.POST["esitype"]
            abc.hratype = request.POST["hratype"]
            abc.contype = request.POST["contype"]
            abc.protype = request.POST["protype"]
            abc.instype = request.POST["instype"]
            abc.deltype = request.POST["deltype"]
            abc.leatype = request.POST["leatype"]
            abc.esi = request.POST["esi"] 
            abc.user_id_id = vars.id
            abc.department_id = vars.department.id
            abc.designation_id = vars.designation.id
            
            abc.account_no = vars.account_no
            abc.bank_branch = vars.bank_branch
            abc.bank_name = vars.bank_name
            abc.ifsc = vars.ifsc
            
            
            
            
            abc.save()
            msg = "Salary payslip generated"
            return render(request, 'account_payment_salary.html',{'msg':msg, 'vars':vars,'z' : z})
        return render(request, 'account_payment_salary.html',{'vars':vars,'z' : z})
    else:
        return redirect('/')

def account_payment_view(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        reg =user_registration.objects.get(id=id)
        use=acntspayslip.objects.filter(user_id_id=id)
        return render(request,'account_payment_view.html',{'reg':reg,'use':use,'z' : z,})
    else:
        return redirect('/')

def accounts_bank_acnt_details(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.filter(id=id)
        return render(request,'accounts_bank_acnt_details.html',{ 'mem1':mem1,'z': z})
    else:
        return redirect('/')

def accounts_add_bank_acnt(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.filter(id=id)
        if request.method == 'POST':
            vars = user_registration.objects.get(id=id)
            vars.account_no = request.POST['account_no']
            vars.ifsc = request.POST['ifsc']
            vars.bank_branch = request.POST['bank_branch']
            vars.bank_name= request.POST['bank_name']
            vars.save()
        return render(request,'accounts_add_bank_acnt.html',{'mem1':mem1,'z': z})
    else:
        return redirect('/')

def accounts_salary_details(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.get(id=id)
        usk=acntspayslip.objects.filter(user_id=id)
        return render(request,'accounts_salary_details.html',{ 'mem1':mem1,'usk':usk,'z': z})
    else:
        return redirect('/')

def logout5(request):
    if 'usernameacnt2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

@csrf_exempt
def accounts_acntpay(request):
    if 'usernameacnt2' in request.session:
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        dept_id = int(request.POST['depmt'])
        desig_id = int(request.POST['desi'])  
        names = acntspayslip.objects.filter(fromdate__range=(fdate,tdate),designation_id= desig_id, department_id= dept_id)
       
                
        return render(request,'accounts_acntpay.html', {'names':names})
    else:
        return redirect('/')

def accounts_payslip(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)   
        dept = department.objects.all()
        des = designation.objects.all()
        return render(request,'accounts_payslip.html', {'dept':dept, 'des':des,'z':z})      
    else:
        return redirect('/')
def accounts_paydetails(request,id,tid):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        names = acntspayslip.objects.all()
        return render(request,'accounts_paydetails.html', {'acc':acc, 'user':user,'z':z})
    else:
        return redirect('/')
def accounts_print(request,id,tid):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        return render(request,'accounts_print.html', {'acc':acc, 'user':user,'z':z})
    else:
        return redirect('/')

def acntpaypdf(request, id, tid):
    date = datetime.now()
    user = user_registration.objects.get(id=tid)
    acc = acntspayslip.objects.get(id=id)
    
    f_date = acc.fromdate
    year = f_date.year
    month = f_date.month

    leave = acnt_monthdays.objects.get(month_fromdate__year__gte=year,
                                       month_fromdate__month__gte=month,
                                       month_todate__year__lte=year,
                                       month_todate__month__lte=month)
    mm = leave.month_workingdays
    m = leave.month_holidays
    
    abc = int(user.confirm_salary)
    
    c = abc - acc.net_salary
    if c == 0:
        c=0
    v = acc.leavesno
    z = v-m
    mem = mm-z
    leaves_tot = acc.delay+acc.leavesno
    wrk_days = mm -leaves_tot
    if mem == '-':
        mem = 0
        conf = abc-acc.net_salary
        if conf == 0:
            conf=abc
        words = num2words(conf)
        template_path = 'acntpaypdf.html'
        context = {'acc': acc, 'user': user, 'c': c, 'mm': mm, 'mem': mem, 'conf': conf, 'words': words,
                   'media_url': settings.MEDIA_URL,
                   'date': date, 'leaves_tot':leaves_tot, 'wrk_days':wrk_days
                   }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="Payslip.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    else:

        conf = abc-c
        words = num2words(conf)
        template_path = 'acntpaypdf.html'
        context = {'acc': acc, 'user': user, 'c': c, 'mm': mm, 'mem': mem, 'conf': conf, 'words': words,
                   'media_url': settings.MEDIA_URL,
                   'date': date, 'leaves_tot':leaves_tot, "wrk_days":wrk_days
                   }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="Payslip.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response      
        
        
    #************************Reset password*****************************
def reset_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.get(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)

            _user.password = password
            subject = 'iNFOX Technologies your authentication data updated'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email_id) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details\n\nNote: This is a system generated email, do not reply to this email id'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)

            _user.save()
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'Reset_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist iNFOX Technologies "
            return render(request, 'Reset_password.html', {'msg_error': msg_error})

    return render(request,'Reset_password.html')
    
    
    
#**************************christin account settings and change password**************************
def tlaccountset(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'tlaccountset.html', {'mem': mem})

def devaccountset(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devaccountset.html', {'dev': dev})

def testaccountset(request):
    if request.session.has_key('usernametsid'):
        usernametsid = request.session['usernametsid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=usernametsid)
    mems = user_registration.objects.filter(id=usernametsid)
    return render(request, 'testaccountset.html', {'mem': mem, 'mems': mems})

def pmaccountset(request):
    if request.session.has_key('prid'):
        prid = request.session['prid']
    else:
        return redirect('/')
    pro = user_registration.objects.filter(id=prid)
    return render(request, 'pmaccountset.html', {'pro': pro})


def imagechange_tl(request, id):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=tlid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('tlaccountset')
    return render(request, 'tlaccountset.html',{'mem': mem})

def imagechange_dev(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('devaccountset')
    return render(request, 'devaccountset.html',{'dev': dev})

def imagechange_test(request, id):
    if request.session.has_key('usernametsid'):
        usernametsid = request.session['usernametsid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=usernametsid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('testaccountset')
    return render(request, 'testaccountset.html',{'mem': mem})

def imagechange_pm(request, id):
    if request.session.has_key('prid'):
        prid = request.session['prid']
    else:
        return redirect('/')
    pro = user_registration.objects.filter(id=prid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('pmaccountset')
    return render(request, 'pmaccountset.html',{'pro': pro})


def tlchangepass(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=tlid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=tlid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'TLdashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'tlchangepass.html', {'mem': mem})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'tlchangepass.html', {'mem': mem})
    return render(request, 'tlchangepass.html', {'mem': mem})

def devchangepass(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=devid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'devdashboard.html', {'dev': dev})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'devchangepass.html', {'dev': dev})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'devchangepass.html', {'dev': dev})
    return render(request, 'devchangepass.html', {'dev': dev})

def testchangepass(request):
    if request.session.has_key('usernametsid'):
        usernametsid = request.session['usernametsid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=usernametsid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=usernametsid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'TLdashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'testchangepass.html', {'mem': mem})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'testchangepass.html', {'mem': mem})
    return render(request, 'testchangepass.html', {'mem': mem})

def prchangepass(request):
    if request.session.has_key('prid'):
        prid = request.session['prid']
    else:
        return redirect('/')
    pro = user_registration.objects.filter(id=prid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=prid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if newps == cmps:
                abc.password = request.POST.get('confirmPassword')
                abc.save()
                return render(request, 'pmanager_dash.html', {'pro': pro})
            elif oldps == newps:
                messages.info(request,  'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
                return render(request, 'TSdashboard.html', {'pro': pro})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'prchangepass.html', {'pro': pro})
    return render(request, 'prchangepass.html', {'pro': pro})
    
    
    
    
    
    
#super admin views #
def superadmin_changepwd(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'superadmin_changepwd.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'superadmin_changepwd.html', {'msg_error': msg_error})
        return render(request,'superadmin_changepwd.html',{'users':users})
    else:
        return redirect('/')
    
    

def superadmin_index(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_index.html',{'users':users})
    else:
        return redirect('/')

def superadmin_logout(request):
    request.session.flush()
    return redirect("/")



#**************************Anandhu Super-Admin Dashboard section**************************

def SuperAdmin_index(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     mem = user_registration.objects.filter(id=Adm_id)
    #     return render(request,'SuperAdmin_index.html',{'mem':mem})
    # else:
    #     return redirect('/')
    return render(request, 'SuperAdmin_index.html')


def SuperAdmin_dashboard(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branch = branch_registration.objects.all()
        
        return render(request, 'SuperAdmin_dashboard.html',{'branch_registration':branch,'users':users}) 
    else:
        return redirect('/')


def SuperAdmin_profile(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branch = branch_registration.objects.get(id = id)
        Num1 = project.objects.filter(branch_id=id).count()
        Num = user_registration.objects.filter(branch_id=id).count()
        Trainer = designation.objects.get(designation='trainer')
        trcount=user_registration.objects.filter(designation=Trainer,branch_id=id).count()
        return render(request, 'SuperAdmin_profile.html',{'users':users,'br':branch,'Num1':Num1,'Num':Num,'trcount':trcount}) 
    else:
        return redirect('/')


def SuperAdmin_trainersdepartment(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Dept = department.objects.filter(branch = id)
        return render(request,'SuperAdmin_trainersdepartment.html',{'users':users,'Dept':Dept})
    else:
        return redirect('/')


def SuperAdmin_trainerstable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        Trainer = designation.objects.get(designation='Trainer')
            
        trainers_data=user_registration.objects.filter(designation=Trainer).filter(department=id)
        topics=topic.objects.all()
        return render(request,'SuperAdmin_trainerstable.html',{'users':users,'trainers_data':trainers_data,'topics':topics})
    else:
        return redirect('/')

def SuperAdmin_trainerteams(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'SuperAdmin_trainerteams.html',{'users':users,'team':team,'user':user})
    else:
        return redirect('/')

def  SuperAdmin_trainerteam(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'SuperAdmin_trainerteam.html',{'users':users,'id':id,'num':num,'num1':num1})
    else:
        return redirect('/')

def SuperAdmin_topictable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        topics=topic.objects.filter(team=id).order_by("-id")
        return render(request,'SuperAdmin_topictable.html',{'users':users,'topics':topics})
    else:
        return redirect('/')
        
def SuperAdmin_traineestable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
        return render(request,'SuperAdmin_traineestable.html',{'users':users,'trainees_data':trainees_data}) 
    else:
        return redirect('/')

        
def SuperAdmin_traineeprofile(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        trainees_data=user_registration.objects.get(id=id)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(task_status='1').count()
        return render(request,'SuperAdmin_traineeprofile.html',{'users':users,'trainees_data':trainees_data,'num':num})
    else:
        return redirect('/')

def SuperAdmin_completedtasktable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'SuperAdmin_completedtasktable.html',{'users':users,'task_data':task})   
    else:
        return redirect('/')
   

#**************************subeesh akhil sharon  Super-Admin Dashboard-project section**************************


# current projects- sharon
def SuperAdmin_pythons(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.all()
        return render(request,'SuperAdmin_projects.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     Adm = user_registration.objects.filter(id=Adm_id)
        
    # else:
    #     return redirect('/')

def SuperAdmin_dept(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)    
        project_details = project.objects.all()
        depart =department.objects.filter(branch=id)
        
        return render(request,'SuperAdmin_dept.html',{'users':users,'proj_det':project_details,'department':depart})
    else:
        return redirect('/')
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     Adm = user_registration.objects.filter(id=Adm_id)
    
    # else:
    #     return redirect('/')

    
# def SuperAdmin_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'SuperAdmin_profiledash.html',{'proj_det':project_details,'num':Num})

def SuperAdmin_projects(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Num= project.objects.filter(status='accepted').filter(department=id).count()
        num= project.objects.filter(status='completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'SuperAdmin_projects.html',{'users':users,'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id})
    else:
        return redirect('/')
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     Adm = user_registration.objects.filter(id=Adm_id)
    
    # else:
    #     return redirect('/')
 
def SuperAdmin_proj_list(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.filter(department=id)
        
        return render(request,'SuperAdmin_proj_list.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_proj_det(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_det.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_proj_mngrs(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_mngrs.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')

# def SuperAdmin_proj_mangrs1(request,id):
#     if request.session.has_key('Adm_id'):
#         Adm_id = request.session['Adm_id']
 
#     mem = user_registration.objects.filter(id=Adm_id)
#     project_details = project.objects.get(id=id) 
#     return render(request,'SuperAdmin_proj_mangrs1.html',{'proj_det':project_details,'mem':mem})
def SuperAdmin_proj_mangrs1(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'SuperAdmin_proj_mangrs1.html',{'users':users,'proj1':proj1,'user_det':user_det,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_proj_mangrs2(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        
        return render(request,'SuperAdmin_proj_mangrs2.html',{'users':users,'proj1':proj1,'user_det':user_det,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_daily_report(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)


        proj_name =  project_taskassign.objects.all()
        tester_name = user_registration.objects.all()
        tester = tester_status.objects.filter(user_id=id)
        return render(request,'SuperAdmin_daily_report.html',{'users':users,'test':tester, 'tester_name':tester_name, 'proj_name':proj_name})
    else:
        return redirect('/')
        
def SuperAdmin_developers(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        proj2=request.session['proj2']
        
    
        project_details = project.objects.get(id=proj2) 
        project_task = project_taskassign.objects.filter(project_id = project_details).filter(tl_id=id)
        user_det=user_registration.objects.filter(tl_id=id).order_by("-id")
        progress_bar= tester_status.objects.all()
        
        return render(request,'SuperAdmin_developers.html',{'users':users,'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'user_det':user_det})
    else:
        return redirect('/')


# completed projects- subeesh
 
def SuperAdmin_proj_cmpltd_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details=project.objects.filter(department=id)
        
        return render(request,'SuperAdmin_proj_cmpltd_show.html',{'users':users,'project': project_details})
    else:
        return redirect('/')


def SuperAdmin_cmpltd_proj_det_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_cmpltd_proj_det_show.html',{'users':users,'project': project_details})
    else:
        return redirect('/')
        
def SuperAdmin_proj_mngrs_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_mngrs_show.html', {'users':users,'project': project_details})
    else:
        return redirect('/')

# def SuperAdmin_proj_mangrs1_new(request,id):
#     if request.session.has_key('Adm_id'):
#         Adm_id = request.session['Adm_id']
 
#     mem = user_registration.objects.filter(id=Adm_id)
#     project_details = project.objects.get(id=id)
#     return render(request,'SuperAdmin_proj_mangrs1_show.html', {'project': project_details,'mem':mem})
def SuperAdmin_proj_mangrs1_new(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'SuperAdmin_proj_mangrs1_show.html',{'users':users,'proj1':proj1,'user_det':user_det,'proj_det':project_details})
    else:
        return redirect('/')
        
def SuperAdmin_proj_mangrs2_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.all()
        return render(request,'SuperAdmin_proj_mangrs2_show.html', {'users':users,'project':project_details,'project_taskassign':project_task})
    else:
        return redirect('/')

def SuperAdmin_developers_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'SuperAdmin_developers_show.html', {'users':users,'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar})
    else:
        return redirect('/')

def SuperAdmin_daily_report_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'SuperAdmin_daily_report_show.html', {'users':users,'project':project_task,'tester_status':tester})
    else:
        return redirect('/')


    #**************************meenu nimisha  Super-Admin Dashboard-employee section**************************

def SuperAdmin_employees(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Dept = department.objects.filter(branch=id)
        return render(request,'SuperAdmin_Employees1.html',{'users':users,'Dept':Dept})
    else:
        return redirect('/')

        
def SuperAdmin_edepartments(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Dept = department.objects.get(id = id)
        deptid=id        
        Desig = designation.objects.all()
        return render(request,'SuperAdmin_edpartments.html',{'users':users,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')

def SuperAdmin_projectman(request,id,did):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did).order_by("-id")
        return render(request,'SuperAdmin_projectman.html',{'users':users,'pro_man_data':Project_man_data,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
    

def SuperAdmin_ViewTrainers(request,id,did):  
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
        return render(request,'SuperAdmin_ViewTrainers.html', {'users':users,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')


def SuperAdmin_View_Trainerprofile(request,id):  
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        userreg=user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_View_Trainerprofile.html', {'users':users,'user_registration':userreg,'labels':labels,'data':data})
    else:
        return redirect('/')


def SuperAdmin_View_Currenttraineesoftrainer(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'SuperAdmin_View_Currenttraineesoftrainer.html',{'users':users,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
   
def SuperAdmin_View_Currenttraineeprofile(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        userreg=user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_View_Currenttraineeprofile.html', {'users':users,'user_registration':userreg,'labels':labels,'data':data})
    else:
        return redirect('/')
   
       
def SuperAdmin_View_Currenttraineetasks(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'SuperAdmin_View_Currenttraineetasks.html',{'users':users,'trainer_task':tasks})
    else:
        return redirect('/')
    
       
def SuperAdmin_View_Currenttraineeattendance(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'SuperAdmin_View_Currenttraineeattendance.html', {'users':users,'user_registration':usr})
    else:
        return redirect('/')


def SuperAdmin_ViewCurrenttraineeattendancesort(request,id): 
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'SuperAdmin_View_Currenttraineeattendancesort.html',{'users':users,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')
    
        
def SuperAdmin_View_Previoustraineesoftrainer(request,id): 
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'SuperAdmin_View_Previoustraineesoftrainer.html',{'users':users,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')

def SuperAdmin_View_Previoustraineetasks(request,id):   
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)        
        return render(request,'SuperAdmin_View_Previoustraineetasks.html',{'users':users,'trainer_task':tasks})
    else:
        return redirect('/')


def SuperAdmin_View_Previoustraineeattendance(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'SuperAdmin_View_Previoustraineeattendance.html', {'users':users,'user_registration':usr})
    else:
        return redirect('/')


def SuperAdmin_ViewPrevioustraineeattendancesort(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'SuperAdmin_ViewPrevioustraineeattendancesort.html',{'users':users,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')
    
   
def SuperAdmin_View_Trainerattendance(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'SuperAdmin_View_Trainerattendance.html', {'users':users,'user_registration':usr})
    else:
        return redirect('/')


def SuperAdmin_ViewTrainerattendancesort(request,id):  
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'SuperAdmin_ViewTrainerattendancesort.html',{'users':users,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')
    

def SuperAdmin_View_Previoustraineeprofile(request,id):   
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_View_Previoustraineeprofile.html', {'users':users,'user_registration':usr,'labels':labels,'data':data})
    else:
        return redirect('/')
    
    
def SuperAdmin_proname(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Project_man_data = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_proname.html',{'users':users,'pro_man_data':Project_man_data,'labels':labels,'data':data})
    else:
        return redirect('/')
    

def SuperAdmin_proinvolve(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
        return render(request,'SuperAdmin_proinvolve.html',{'users':users,'pro_data':Pro_data})
    else:
        return redirect('/')
    
def SuperAdmin_promanatten(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        id = id
        return render(request, 'SuperAdmin_promanatten.html',{'users':users,'id':id})
    else:
        return redirect('/')

def SuperAdmin_promanattendsort(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
                # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'SuperAdmin_promanattensort.html',{'users':users,'mem1':mem1,'id':id})
    else:
        return redirect('/')
    

def SuperAdmin_admin_registration(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_admin_registration.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_registration(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branches=branch_registration.objects.all()
        
        return render(request,'SuperAdmin_registration.html',{'users':users,'branches':branches,})
    else:
        return redirect('/')

def SuperAdmin_Add(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        des=designation.objects.get(designation="admin")
        if request.method == 'POST':
            fn1 = request.POST['fname']
            fn2 = request.POST['faname']
            fn3 = request.POST['adob']
            fn4 = request.POST['agender']
            fn5 = request.POST['amobile']
            fn6 = request.POST['aemail']
            fn7 = request.POST['aalternative']
            fn8 = request.POST['Adminbranch']
            fn9 = request.FILES['aproof']
            fn10 = request.FILES['cphoto']
            
           
            
            new2 = user_registration(fullname=fn1, fathername=fn2, dateofbirth=fn3, gender=fn4, mobile=fn5, email=fn6, alternativeno=fn7,branch_id=fn8,
                                    idproof=fn9, photo=fn10,designation_id=des.id)
            new2.save()
            return render(request,'SuperAdmin_registration.html',{'users':users})
        else:
            return redirect('SuperAdmin_registration')
    else:
        return redirect('/')




def SuperAdmin_admin_view(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        designations=designation.objects.get(designation='Admin')
        user=user_registration.objects.filter(designation=designations)
        return render(request,'SuperAdmin_view_admin.html',{'users':users,'user_registration':user,'designation':designations})
    else:
        return redirect('/')

def admindelete(request, id):
    
    user = user_registration.objects.get(id=id)
    try:
        user.delete()
        return redirect('SuperAdmin_admin_view')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('SuperAdmin_admin_view')


def SuperAdmin_admin_update(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.get(id=id)
        branchs=branch_registration.objects.all()

        return render(request,'SuperAdmin_update_admin.html',{'users':users,'user_registration':user,'branch_registration':branchs})
    else:
        return redirect('/')

def SuperAdmin_updatesave(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            usr = user_registration.objects.get(id=id)
            usr.fullname = request.POST.get('aname')
            usr.fathername = request.POST.get('fname')
            usr.dateofbirth = request.POST.get('date')
            usr.gender = request.POST.get('gen')
            usr.mobile = request.POST.get('mob')
            usr.email = request.POST.get('mail')
            usr.alternativeno = request.POST.get('alternative')
            try:
                usr.idproof = request.FILES['idp']
                usr.photo = request.FILES['pic']
            except:
                pass
            
            br_id = request.POST.get("Adminbranch")
            usr.branch_id = br_id
            usr.save()
            return redirect('SuperAdmin_admin_view')
        else:
            return render(request,'SuperAdmin_update_admin.html',{'users':users})

    else:
        return redirect('/')






def SuperAdmin_Branch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_Branch.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_AddBranch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            br1 = request.POST['Brname']
            br2 = request.POST['location']
            br3 = request.POST['Brtype']
            br4 = request.POST['Bradmin']
            br5 = request.POST['Bremail']
            br6 = request.POST['Brcontact']
            br7 = request.FILES['img[]']
    
            new1 = branch_registration(branch_name=br1,location=br2,
                                      branch_type=br3, branch_admin=br4,logo = br7,
                                      email= br5,mobile =br6)
            new1.save()
    
        return render(request,'SuperAdmin_AddBranch.html',{'users':users})
    else:
        return redirect('/')


def SuperAdmin_Viewbranch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        branch=branch_registration.objects.all()
        return render(request,'SuperAdmin_Viewbranch.html',{'users':users,'branch_registration':branch})
    else:
        return redirect('/')

def SuperAdmin_Updatebranch(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        branch=branch_registration.objects.get(id=id)
       
        return render(request,'SuperAdmin_Updatebranch.html',{'users':users,'branch_registration':branch})
    else:
        return redirect('/')

def SuperAdmin_branchupdate(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method=="POST":
            br=branch_registration.objects.get(id=id)
            br.branch_name=request.POST['brname']
            br.location=request.POST['brlocation']
            br.branch_type=request.POST['brtype']
            br.branch_admin=request.POST['bradmin']
            br.email=request.POST['bremail']
            br.mobile=request.POST['brmobile']
            br.save()
            
            lg=branch_registration.objects.get(id=id)
            try: 
                lg.logo = request.FILES['photo']
                lg.save()
            except:
                br.save()
        
            return redirect('SuperAdmin_Viewbranch')
        else:
            return render(request,'SuperAdmin_Viewbranch.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_Branchdelete(request,id):
    branch=branch_registration.objects.get(id=id)
    try:
        
        branch.delete()
        return redirect('SuperAdmin_Viewbranch')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('SuperAdmin_Viewbranch')


def SuperAdmin_ReportedissueShow(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        ad_id = designation.objects.get(designation="admin")
        admin_id = ad_id.id
        reported_issues=reported_issue.objects.all()
        user1=user_registration.objects.all()
        return render(request,'SuperAdmin_ReportedissueShow.html',{'users':users,'reported_issue':reported_issues,'user1':user1, 'admin_id':admin_id})
    else:
        return redirect('/')

def SuperAdmin_Reportedissue_department(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branch=branch_registration.objects.all()
        file = user_registration.objects.all()
        return render(request, 'SuperAdmin_Reportedissue_department.html',{'users':users,'branches':branch,'files':file})
    else:
        return redirect('/')

def SuperAdminreply(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
            return redirect('SuperAdmin_Reportedissue_department')
        else:
            return render(request,'SuperAdmin_ReportedissueShow.html',{'users':users})
    else:
        return redirect('/')
        
def trainer_currentprogress(request,id):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        var = user_registration.objects.get(id=id)
        
        
        
        if request.method == 'POST':
            mm = previousTeam.objects.get(user=id,teamname=var.team_id)
            
            mm.progress = request.POST['sele1']
            mm.save()
            
            msg_success = "Progress submitted"
            return render(request, 'trainer_currentprogress.html', {'z': z,'msg_success':msg_success,'var':var})
        return render(request, 'trainer_currentprogress.html', {'z': z,'var':var, 'old_pr':old_pr})
    else:
        return render('/')
        
def trainer_currentprogress(request,id):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        var = user_registration.objects.get(id=id)
       
        old_pr = previousTeam.objects.get(user=id,teamname_id=var.team_id)
        
        if request.method == 'POST':
            mm = previousTeam.objects.get(user=id,teamname=var.team_id)
            
            mm.progress = request.POST['sele1']
            mm.save()
            
            msg_success = "Progress submitted"
            return render(request, 'trainer_currentprogress.html', {'z': z,'msg_success':msg_success,'var':var})
        return render(request, 'trainer_currentprogress.html', {'z': z,'var':var, 'old_pr':old_pr})
    else:
        return render('/')



def BRadmin_new_registration(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')
    if request.method == "POST":
        u_id = request.POST.get("id")
        dept_id = request.POST.get("dept")
        desi_id = request.POST.get("des")
        res = request.POST.get("stat")

        user = user_registration.objects.get(id=u_id)
        user.department_id = dept_id
        user.status = res
        user.designation_id = desi_id
        user.save()
        return redirect("BRadmin_new_registration")
    Adm = user_registration.objects.filter(id=Adm_id)
    mem1 = user_registration.objects.filter(~Q(status="resigned"),reg_status=0).order_by("-id")
    mem2 = designation.objects.filter(~Q(designation="admin"))
    mem3 = department.objects.all()
    return render(request, 'BRadmin_new_registration.html', {'mem3': mem3, 'mem2': mem2, 'Adm': Adm, 'mem1': mem1})


def registrationstatus(request, id):
    man = user_registration.objects.get(id=id)
    man.reg_status = "1"    
    man.save()
    return redirect('BRadmin_new_registration')

def BRadmin_internship_pending(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=Adm_id)

    data=internship.objects.filter(complete_status='0')
    use=internship_type.objects.all()
   
    return render(request, 'BRadmin_internship_pending.html', {'data': data,'use': use,'Adm':Adm})

def BRadmin_internship_acc_approved(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=Adm_id)
    data=internship.objects.filter(verify_status='1')
    use=internship_type.objects.all()

    return render(request, 'BRadmin_internship_acc_approved.html', {'data': data ,'use':use, 'Adm':Adm})



def BRadmin_accounts(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        year = date.today().year
        month = date.today().month
        vars = acntspayslip.objects.filter(~Q(fromdate__year=year,
                                          fromdate__month=month)).count()
        vars1 = user_registration.objects.filter(confirm_salary_status=1).count()
        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars2 = user_registration.objects.exclude(designation=des2.id).exclude(designation=Adm1.id).count()
        vars3 = acntspayslip.objects.filter(fromdate__year=year,
                                          fromdate__month=month).count()
        deta = user_registration.objects.filter(designation=des2.id,payment_status=0).count()
        deta2 = user_registration.objects.filter(designation=des2.id).count()
        deta2 = user_registration.objects.filter(designation=des2.id,).count()
        icount=internship.objects.all().count()
        return render(request, 'BRadmin_accounts.html', {'Adm': Adm,'vars':vars,'vars1':vars1,'vars2':vars2,'vars3':vars3,'deta':deta,'deta2':deta2,'icount':icount})
    else:
        return redirect('/')

def BRadmin_accounts_traineepayment_notverified(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request,'BRadmin_accounts_traineepayment_notverified.html', { 'Adm': Adm, 'deta':deta})
    else:
        return redirect('/')

def BRadmin_accounts_traineepayment_pending(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request,'BRadmin_accounts_traineepayment_pending.html', { 'Adm': Adm, 'deta': deta })
    else:
        return redirect('/')

def BRadmin_accounts_newtrainees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id).order_by('-id')
        return render(request,'BRadmin_accounts_newtrainees.html', { 'Adm': Adm, 'deta':deta })
    else:
        return redirect('/')

def BRadmin_accounts_salaried_employees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        vars = user_registration.objects.filter(confirm_salary_status=1).order_by("-id")
        return render(request,'BRadmin_accounts_salaried_employees.html', {'Adm': Adm,'vars':vars})
    else:
        return redirect('/')

def BRadmin_accounts_salary_employees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars = user_registration.objects.exclude(designation=des2.id).exclude(designation=Adm1.id, status="active").order_by("-id")
        return render(request,'BRadmin_accounts_salary_employees.html', {'Adm': Adm,'vars':vars})
    else:
        return redirect('/')   

def BRadmin_accounts_internship(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
   
        return render(request, 'BRadmin_accounts_internship.html', {'Adm': Adm})
    else:
        return redirect('/')   


def BRadmin_accounts_internship_viewall(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        data=internship.objects.filter(complete_status='1')
        use=internship_type.objects.all()
    
        return render(request, 'BRadmin_accounts_internship_viewall.html', {'Adm': Adm,'data': data,'use': use})
    else:
        return redirect('/')   
    
def BRadmin_accounts_internship_payment_pending(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        data=internship.objects.filter(complete_status='0')
        use=internship_type.objects.all()
    
        return render(request, 'BRadmin_accounts_internship_payment_pending.html', {'Adm': Adm,'data': data,'use': use})
    else:
        return redirect('/')   

def BRadmin_accounts_intrenship_viewbydate(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)

    newdata = internship.objects.filter(verify_status=1)
    return render(request, 'BRadmin_accounts_internship_viewbydate.html', {'Adm': Adm,'newdata':newdata})

def BRadmin_accounts_internship_dateview(request):  
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
    reg_date = request.GET.get('date')  
    #empid = internship.objects.get(id=id)  
    empid = internship.objects.filter(reg_date=reg_date)  
    return render(request, 'BRadmin_accounts_internship_dateview.html',{'Adm': Adm, 'empid':empid})  

def BRadmin_accounts_internship_update(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    return render (request, 'BRadmin_accounts_internship_update.html', {'Adm': Adm,'var': var})


def BRadmin_accounts_interndelete(request, id):
    man = internship.objects.get(id=id)
    man.delete()
    return redirect('BRadmin_accounts_internship')

def BRadmin_accounts_internshipupdatesave(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id) 
  
        
        Adm = user_registration.objects.filter(id=Adm_id)
        var = internship.objects.get(id=id)
        var.fullname = request.POST['fullname']
        var.collegename = request.POST['college']
        var.reg_no = request.POST['regno']
        var.course = request.POST['course']
        var.stream = request.POST['stream']
        var.platform = request.POST['platform']
        #var.branch_id  =  request.POST['branch']
        var.start_date = request.POST['startdate']
        var.end_date = request.POST['enddate']
        var.mobile = request.POST['mobile']
        var.alternative_no = request.POST['altmob']
        var.email = request.POST['email']
        var.hrmanager = request.POST['hrmanager']
        var.guide = request.POST['guide']
        var.rating = request.POST['rating']
        var.save()
        return redirect('BRadmin_accounts_internship')

def BRadmin_monthdays(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_monthdays.html', {'Adm': Adm})
    else:
        return redirect('/')
        
def BRadmin_viewdays(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        mem = acnt_monthdays.objects.all()
        return render(request,'BRadmin_viewdays.html', {'Adm': Adm,'mem':mem})
    else:
        return redirect('/')
        
# def BRadmin_salary_given(request):
#     if 'Adm_id' in request.session:
#         if request.session.has_key('Adm_id'):
#             Adm_id = request.session['Adm_id']
#         Adm = user_registration.objects.filter(id=Adm_id)
#         mem = user_registration.objects.filter(salary_status=1)
#         return render(request,'BRadmin_salary_given.html', {'Adm': Adm,'mem':mem})
#     else:
#         return redirect('/')

def BRadmin_salary_given(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        year = date.today().year
        month = date.today().month
        mem = acntspayslip.objects.filter(fromdate__year=year,
                                          fromdate__month=month)
        return render(request,'BRadmin_salary_given.html', {'Adm': Adm,'mem':mem})
    else:
        return redirect('/')


def BRadmin_project_dept(request):
     if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        depart = department.objects.all()
        return render(request, 'BRadmin_project_dept.html', {'proj_det': project_details, 'department': depart, 'Adm': Adm})
     else:
        return redirect('/')

     
# Admin project documents view
def BRadmin_project_document(request,Bradmin_dep_id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        projects = project.objects.filter(department_id=Bradmin_dep_id).order_by("-id")
        proj_doc=PM_ProjectDocument.objects.filter(doc_project_id__in=projects.values_list('id'))
        return render(request, 'BRadmin_project_docview.html', {'Adm': Adm,'projects':projects,'proj_doc':proj_doc})
    else:
        return redirect('/')


         
# Admin project document  details view
def BRadmin_project_doc_detail(request,BRadmin_pdocv_id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
       
        pdoc= PM_ProjectDocument.objects.get(id=BRadmin_pdocv_id)
        proj=project_module_assign.objects.filter(project_name=pdoc.doc_project_id)
        corre=ProjectCorrectionUpdation.objects.filter(project_cu_id=pdoc.doc_project_id,project_cu_status='correction')
        updte=ProjectCorrectionUpdation.objects.filter(project_cu_id=pdoc.doc_project_id,project_cu_status='updation')

        return render(request, 'BRadmin_project_doc_detail_view.html', {'Adm': Adm,'proj':proj,'pdoc':pdoc,'corre':corre,'updte':updte})
    else:
        return redirect('/')
    
    

def BRadmin_project_list(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(
            ~Q(status='Rejected'), department_id=id).order_by('-id')
        dep=department.objects.get(id=id)
        return render(request, 'BRadmin_project_list.html', {'proj_det': project_details, 'Adm': Adm,'dep':dep})
    else:
        return redirect('/')


def BRadmin_project_table(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation="team leader")
        dev = designation.objects.get(designation="developer")
        var = project_taskassign.objects.filter(project_id=id,worktype='1').order_by('-id')
        data = test_status.objects.filter(project_id=id,).order_by('-id')
        data1 = tester_status.objects.filter(project_id=id).order_by('-id')
        newdata = project_taskassign.objects.filter(
            project_id=id, subtask__isnull=False).order_by('-id')
        return render(request, 'BRadmin_project_table.html', {'Adm': Adm, 'var': var, 'data': data, 'data1': data1, 'newdata': newdata})
    else:
        return redirect('/')


def BRadmin_project_tester(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        deg=designation.objects.get(designation='tester')
        proj_tester=user_registration.objects.filter(designation=deg)
      
        return render(request, 'BRadmin_project_tester.html', {'Adm': Adm,'proj_tester':proj_tester})
    else:
        return redirect('/')

def BRadmin_tester_project_list(request,BRadmin_prj_list):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        proj_list=project_taskassign.objects.filter(tester_id=BRadmin_prj_list).order_by('-submitted_date')

        verify_num=project_taskassign.objects.filter(tester_id=BRadmin_prj_list, status='submitted').count()
        pending_verify_num=project_taskassign.objects.filter(tester_id=BRadmin_prj_list, status='Verification').count()
        correction_num=project_taskassign.objects.filter(tester_id=BRadmin_prj_list, status='correction').count()
        tester_dely=TSproject_Task_verify.objects.filter(ts_tester_id=BRadmin_prj_list).order_by('-id')
        delay_num=0
        for i in tester_dely:
            delay_num=delay_num+int(i.ts_delay)
       
        return render(request, 'BRadmin_tester_project_list.html', {'Adm': Adm,'proj_list':proj_list,'verify_num':verify_num,'pending_verify_num':pending_verify_num,'correction_num':correction_num,'tester_dely':tester_dely,'delay_num':delay_num})
    else:
        return redirect('/')

def BRadmin_dev_project_task(request,BRadmin_dev_prj_task):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        print(BRadmin_dev_prj_task)
        Adm = user_registration.objects.filter(id=Adm_id)
        tas=project_taskassign.objects.get(id=BRadmin_dev_prj_task)
        data1 = tester_status.objects.filter(task=tas).order_by('-id')
        print(data1)
        return render(request, 'BRadmin_dev_project_task.html', {'Adm': Adm,'tas':tas,'data1':data1})
    else:
        return redirect('/')


# def BRadmin_salary_pending(request):
#     if 'Adm_id' in request.session:
#         if request.session.has_key('Adm_id'):
#             Adm_id = request.session['Adm_id']
#         else:
#             return redirect('/')
#         Adm = user_registration.objects.filter(id=Adm_id)
#         mem = user_registration.objects.filter(salary_status=0)
#         return render(request,'BRadmin_salary_pending.html', {'Adm': Adm,'mem':mem})
#     else:
#         return redirect('/')

def BRadmin_salary_pending(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        year = date.today().year
        month = date.today().month
        mem = acntspayslip.objects.filter(~Q(fromdate__year=year,
                                          fromdate__month=month))
        return render(request,'BRadmin_salary_pending.html', {'Adm': Adm,'mem':mem})
    else:
        return redirect('/')


# def accounts_intrenship_viewbydate(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
        
#     newdata = internship.objects.filter(verify_status=1)
#     return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})

# def accounts_internship(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         ipcount=internship.objects.filter(complete_status='0').count()
#         ivacount=internship.objects.filter(complete_status=1).count()
#         ivdcount=internship.objects.filter(verify_status=1).count()
#         return render(request,'accounts_internship.html',{'z': z,'ipcount':ipcount,'ivacount':ivacount,'ivdcount':ivdcount})
#     else:
#         return redirect('/')

# def accounts_internship_update(request, id):
#     if 'usernameacnt2' in request.session:  
#         if request.session.has_key('usernameacnt2'):  
#             usernameacnt2 = request.session['usernameacnt2']  
#         z = user_registration.objects.filter(id=usernameacnt2) 
#     var = internship.objects.get(id=id)
#     return render (request,'accounts_internship_update.html', {'z': z,'var': var})


# def accounts_interndelete(request, id):
#     man = internship.objects.get(id=id)
#     man.delete()
#     return redirect('accounts_internship')

# def accounts_internshipupdatesave(request, id):
#     if 'usernameacnt2' in request.session:  
#         if request.session.has_key('usernameacnt2'):  
#             usernameacnt2 = request.session['usernameacnt2']  
  
#         else:
#             return redirect('/')
#         Adm = user_registration.objects.filter(id=usernameacnt2)
#         var = internship.objects.get(id=id)
#         var.fullname = request.POST['fullname']
#         var.collegename = request.POST['college']
#         var.reg_no = request.POST['regno']
#         var.course = request.POST['course']
#         var.stream = request.POST['stream']
#         var.platform = request.POST['platform']
#         #var.branch_id  =  request.POST['branch']
#         var.start_date = request.POST['startdate']
#         var.end_date = request.POST['enddate']
#         var.mobile = request.POST['mobile']
#         var.alternative_no = request.POST['altmob']
#         var.email = request.POST['email']
#         var.hrmanager = request.POST['hrmanager']
#         var.guide = request.POST['guide']
#         var.rating = request.POST['rating']
#         var.save()
#         return redirect('accounts_internship')

def accounts_intrenship_viewbydate(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    newdata = internship.objects.all().values('reg_date').distinct()
    # newdata = internship.objects.filter(verify_status=1)
    return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})

def accounts_internship(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        ipcount=internship.objects.filter(complete_status='0').count()
        ivacount=internship.objects.filter(complete_status=1).count()
        ivdcount=internship.objects.filter(verify_status=1).count()
        return render(request,'accounts_internship.html',{'z': z,'ipcount':ipcount,'ivacount':ivacount,'ivdcount':ivdcount})
    else:
        return redirect('/')

def accounts_internship_update(request, id):
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
        z = user_registration.objects.filter(id=usernameacnt2) 
    var = internship.objects.get(id=id)
    return render (request,'accounts_internship_update.html', {'z': z,'var': var})
    
def accounts_internship_dateview(request):  
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
        z = user_registration.objects.filter(id=usernameacnt2)  

    reg_date = request.GET.get('date')    
    empid = internship.objects.filter(reg_date=reg_date)  
    return render(request, 'accounts_internship_dateview.html',{'z':z, 'empid':empid})  

def accounts_interndelete(request, id):
    man = internship.objects.get(id=id)
    man.delete()
    return redirect('accounts_internship')

def accounts_internshipupdatesave(request, id):
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
  
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=usernameacnt2)
        var = internship.objects.get(id=id)
        var.fullname = request.POST['fullname']
        var.collegename = request.POST['college']
        var.reg_no = request.POST['regno']
        var.course = request.POST['course']
        var.stream = request.POST['stream']
        var.platform = request.POST['platform']
        #var.branch_id  =  request.POST['branch']
        var.start_date = request.POST['startdate']
        var.end_date = request.POST['enddate']
        var.mobile = request.POST['mobile']
        var.alternative_no = request.POST['altmob']
        var.email = request.POST['email']
        var.hrmanager = request.POST['hrmanager']
        var.guide = request.POST['guide']
        var.rating = request.POST['rating']
        var.save()
        return redirect('accounts_internship')
 
def trainer_save(request,id):  
    var = user_registration.objects.get(id=id)  
    var.trainer_level = request.POST['tr_level']  
    var.save()  
    msg_success="Added succesfully"
    return render(request, 'trainer.html', {'msg_success':msg_success})

# def accounts_internship_viewbydate(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
        
#     newdata = internship.objects.all().values('reg_date').distinct()
#     return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})
    
# #################Emil
# def accounts_internship_dateview(request):  
#     if 'usernameacnt2' in request.session:  
#         if request.session.has_key('usernameacnt2'):  
#             usernameacnt2 = request.session['usernameacnt2']  
#         z = user_registration.objects.filter(id=usernameacnt2)  

#     reg_date = request.GET.get('date')    
#     empid = internship.objects.filter(reg_date=reg_date)  
#     return render(request, 'accounts_internship_dateview.html',{'z':z, 'empid':empid})  

# def accounts_internship_payment_pending(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.filter(complete_status='0')
#     use=internship_type.objects.all()
   
#     return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'use': use})

# def accounts_internship_type_sel(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#     data=internship.objects.all()
#     ab=internship.objects.get(id=id)
#     ab.internshiptype_id=request.POST['inter']    
#     use=internship_type.objects.get(id=int(request.POST['inter']))
#     ab.total_fee=use.fee
#     ab.save()
#     msg_success = "Add Succesfully"
   
   
#     return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'msg_success': msg_success})

# def addamount(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         if request.method == "POST":
            
#             abc = internship.objects.get(id=id)
           
#             abc.pay_date = request.POST['date']
#             abc.amount = request.POST['amount']
#             abc.total_pay= int(request.POST['amount'])+abc.total_pay
#             abc.balance = abc.total_fee - abc.total_pay

#             # member.total_pay = int(request.POST['amount'])+member.total_pay
#             # member.payment_balance = member.total_amount - member.total_pay


            
#             abc.save()
#             abcd = internship_paydata()
#             abcd.internship_user=abc
#             abcd.date = request.POST['date']
#             abcd.amount = request.POST['amount']
#             abcd.save()
#             msg_success = "Add Succesfully"
#             return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})
#         return render(request, 'internship_payment_pending.html', {'z': z,})
#     else:
#         return redirect('/')
    
# def accounts_internship_verify(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.get(id=id)
#     data.verify_status=1
#     data.save()
#     msg_success = "Verifyed Succesfully"
#     return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

# def accounts_internship_complete(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.get(id=id)
#     data.complete_status=1
#     data.save()
#     msg_success = "Verifyed Succesfully"
#     return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

# def accounts_internship_viewall(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.filter(complete_status='1')
#     use=internship_type.objects.all()
   
#     return render(request, 'accounts_internship_viewall.html', {'z': z,'data': data,'use': use})
   
    


# #########################   jishnu   ##############################

# def accounts_intrenship_type(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         mem = internship_type.objects.all()
        
#     return render(request, 'accounts_intrenship_type.html', {'z': z,'mem':mem,})

# def accounts_intrenship_add(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#         if request.method == 'POST':
#             vars = internship_type()
#             vars.type = request.POST['type']
#             vars.duration = request.POST['duration']
#             vars.fee = request.POST['fees']
#             vars.save()
#             msg_success = "Add Succesfully"
#             return render(request, 'accounts_intrenship_add.html', {'z': z,'msg_success':msg_success})

#     return render(request, 'accounts_intrenship_add.html', {'z': z,})

# def internshiptypeupdate(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         if request.method == "POST":
#             vars = internship_type.objects.get(id=id)
#             vars.type = request.POST['types']
#             vars.duration = request.POST['durations']
#             vars.fee = request.POST['fees']
#             vars.save()
#             msg_success = "Updated Succesfully"
#             return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
#         return render(request, 'accounts_intrenship_type.html', {'z': z, })
#     else:
#         return redirect('/')

# def internshiptypedelete(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         vars = internship_type.objects.get(id=id)
#         vars.delete()
#         msg_success = "Deleted Succesfully"
#         return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
#     else:
#         return redirect('/')
        
def accounts_internship_viewbydate(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
    newdata = internship.objects.all().values('reg_date').distinct()
    return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})
    
#################Emil
def accounts_internship_dateview(request):  
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
        z = user_registration.objects.filter(id=usernameacnt2)  

    reg_date = request.GET.get('date')    
    empid = internship.objects.filter(reg_date=reg_date)  
    return render(request, 'accounts_internship_dateview.html',{'z':z, 'empid':empid})  

def accounts_internship_payment_pending(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.filter(complete_status='0')
    use=internship_type.objects.all()
   
    return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'use': use})

def accounts_internship_type_sel(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    data=internship.objects.all()
    ab=internship.objects.get(id=id)
    ab.internshiptype_id=request.POST['inter']    
    use=internship_type.objects.get(id=int(request.POST['inter']))
    ab.total_fee=use.fee
    ab.save()
    msg_success = "Add Succesfully"
   
   
    return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'msg_success': msg_success})

def addamount(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method == "POST":
            
            abc = internship.objects.get(id=id)
           
            abc.pay_date = request.POST['date']
            abc.amount = request.POST['amount']
            abc.total_pay= int(request.POST['amount'])+abc.total_pay
            abc.balance = abc.total_fee - abc.total_pay

            # member.total_pay = int(request.POST['amount'])+member.total_pay
            # member.payment_balance = member.total_amount - member.total_pay


            
            abc.save()
            abcd = internship_paydata()
            abcd.internship_user=abc
            abcd.date = request.POST['date']
            abcd.amount = request.POST['amount']
            abcd.save()
            msg_success = "Add Succesfully"
            return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})
        return render(request, 'internship_payment_pending.html', {'z': z,})
    else:
        return redirect('/')
    
def accounts_internship_verify(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.get(id=id)
    data.verify_status=1
    data.save()
    msg_success = "Verifyed Succesfully"
    return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

def accounts_internship_complete(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.get(id=id)
    data.complete_status=1
    data.save()
    msg_success = "Verifyed Succesfully"
    return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

def accounts_internship_viewall(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.filter(complete_status='1')
    use=internship_type.objects.all()
   
    return render(request, 'accounts_internship_viewall.html', {'z': z,'data': data,'use': use})
   
    


#########################   jishnu   ##############################

def accounts_intrenship_type(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = internship_type.objects.all()
        
    return render(request, 'accounts_intrenship_type.html', {'z': z,'mem':mem,})

def accounts_intrenship_add(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        if request.method == 'POST':
            vars = internship_type()
            vars.type = request.POST['type']
            vars.duration = request.POST['duration']
            vars.fee = request.POST['fees']
            vars.save()
            msg_success = "Add Succesfully"
            return render(request, 'accounts_intrenship_add.html', {'z': z,'msg_success':msg_success})

    return render(request, 'accounts_intrenship_add.html', {'z': z,})

def internshiptypeupdate(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method == "POST":
            vars = internship_type.objects.get(id=id)
            vars.type = request.POST['types']
            vars.duration = request.POST['durations']
            vars.fee = request.POST['fees']
            vars.save()
            msg_success = "Updated Succesfully"
            return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
        return render(request, 'accounts_intrenship_type.html', {'z': z, })
    else:
        return redirect('/')

def internshiptypedelete(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = internship_type.objects.get(id=id)
        vars.delete()
        msg_success = "Deleted Succesfully"
        return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
    else:
        return redirect('/')        

def projectmanager_workstatus(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        dept  = user_registration.objects.get(id=prid)

        cous = course.objects.all()
        dep = department.objects.filter(id=dept.department_id)
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'projectmanager_workstatus.html',{'pro':pro, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')


@csrf_exempt
def projectmanager_designation(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="manager"),~Q(designation="project manager"),~Q(designation="trainingmanager"),~Q(designation="trainer"),~Q(designation="trainee"),~Q(designation="account"), ~Q(designation="hr")).filter(branch_id=br_id.branch_id)
        return render(request,'projectmanager_designation.html',{'pro':pro,'Desig': Desig, })
    else:
        return redirect('/')


@csrf_exempt
def projectmanager_emp_ajax(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        Desig = user_registration.objects.filter(department_id=dept_id, designation_id=desigId, status="active")

        return render(request,'projectmanager_emp_ajax.html',{'pro':pro,'Desig': Desig,})
    else:
        return redirect('/')

@csrf_exempt
def projectmanager_projects_details(request):
    if 'prid' in request.session:
        emp = request.POST['emp']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        names = project_taskassign.objects.filter(developer=emp,startdate__gte=fdate, enddate__lte=tdate).order_by('-id')
        
        year = date.today().year
        month = date.today().month

        leave = project_taskassign.objects.filter(developer=emp,startdate__year__gte=year,
                                          startdate__month__gte=month,
                                          submitted_date__year__lte=year,
                                          submitted_date__month__lte=month)
        mm = leave.values_list('delay', flat='true')

        a=0
        for i in mm:
            
            a=a+int(i)

        teststatus = test_status.objects.all()
        print(teststatus)
        return render(request,'projectmanager_projects_details.html', {'names':names,'mm':mm,'a':a ,'teststatus':teststatus})
    else:
        return redirect('/')

# Error fix:

# def accounts_traineepayment_notverified(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des = designation.objects.get(designation='trainee')
#         deta = user_registration.objects.filter(designation=des.id)
#         return render(request, 'accounts_traineepayment_notverified.html', {'z': z, 'deta': deta})
#     else:
#         return redirect('/')


# def verified(request, id):
#     rem = user_registration.objects.get(id=id)
#     rem.payment_status = 2
#     rem.save()
#     return redirect('/accounts_traineepayment_notverified')


# def accounts_traineepayment_pending(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des = designation.objects.get(designation='trainee')
#         deta = user_registration.objects.filter(designation=des.id)

#         return render(request, 'accounts_traineepayment_pending.html', {'z': z, 'deta': deta})
#     else:
#         return redirect('/')


# def accounts_newtrainees(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des = designation.objects.get(designation='trainee')
#         deta = user_registration.objects.filter(designation=des.id)
#         return render(request, 'accounts_newtrainees.html', {'z': z, 'deta': deta})
#     else:
#         return redirect('/')


# def accounts_salary_employees(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des2 = designation.objects.get(designation='trainee')
#         Adm1 = designation.objects.get(designation="Admin")
#         vars = user_registration.objects.exclude(
#             designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
#         return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')


# def accounts_salaryconfirm(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#         des2 = designation.objects.get(designation='trainee')
#         Adm1 = designation.objects.get(designation="Admin")
#         vars = user_registration.objects.exclude(
#             designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
#         if request.method == 'POST':
#             var = user_registration.objects.get(id=id)
#             var.confirm_salary = request.POST['salary']
#             var.confirm_salary_status = 1
#             var.save()
#             msg_success = "submitted successfully"
#             return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars, 'msg_success': msg_success})
#         return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')


# def accounts_salaried_employees(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         vars = user_registration.objects.filter(
#             confirm_salary_status=1).order_by("-id")
#         return render(request, 'accounts_salaried_employees.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')


# def accounts_monthdays_cards(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         return render(request, 'accounts_monthdays_cards.html', {'z': z})
#     else:
#         return redirect('/')


# def accounts_month_adddays_form(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         mem = acnt_monthdays()
#         if request.method == 'POST':
#             mem.month_fromdate = request.POST['fromdate']
#             mem.month_todate = request.POST['todate']
#             mem.month_workingdays = request.POST['workingdays']
#             mem.month_holidays = request.POST['holidays']
#             mem.save()
#             msg_success = 'submitted succesfully'
#             return render(request, 'accounts_month_adddays_form.html', {'z': z, 'msg_success': msg_success})

#         return render(request, 'accounts_month_adddays_form.html', {'z': z})
#     else:
#         return redirect('/')


# def accounts_month_viewdays(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         mem = acnt_monthdays.objects.all()

#         return render(request, 'accounts_month_viewdays.html', {'z': z, 'mem': mem})
#     else:
#         return redirect('/')

def accounts_traineepayment_notverified(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request, 'accounts_traineepayment_notverified.html', {'z': z, 'deta': deta})
    else:
        return redirect('/')


def verified(request, id):
    rem = user_registration.objects.get(id=id)
    rem.payment_status = 2
    rem.save()
    return redirect('/accounts_traineepayment_notverified')


def accounts_traineepayment_pending(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)

        return render(request, 'accounts_traineepayment_pending.html', {'z': z, 'deta': deta})
    else:
        return redirect('/')


def accounts_newtrainees(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request, 'accounts_newtrainees.html', {'z': z, 'deta': deta})
    else:
        return redirect('/')


def accounts_salary_employees(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars = user_registration.objects.exclude(
            designation=des2.id).exclude(designation=Adm1.id).filter(status="active").order_by("-id")
        return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def accounts_salaryconfirm(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars = user_registration.objects.exclude(
            designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
        if request.method == 'POST':
            var = user_registration.objects.get(id=id)
            var.confirm_salary = request.POST['salary']
            var.confirm_salary_status = 1
            var.save()
            msg_success = "submitted successfully"
            return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars, 'msg_success': msg_success})
        return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def accounts_salaried_employees(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = user_registration.objects.filter(
            confirm_salary_status=1).order_by("-id")
        return render(request, 'accounts_salaried_employees.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')

def accounts_monthdays_cards(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = acnt_monthdays.objects.all().count()
        return render(request, 'accounts_monthdays_cards.html', {'mem':mem,'z': z})
    else:
        return redirect('/')


def accounts_month_adddays_form(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = acnt_monthdays()
        if request.method == 'POST':
            mem.month_fromdate = request.POST['fromdate']
            mem.month_todate = request.POST['todate']
            mem.month_workingdays = request.POST['workingdays']
            mem.month_holidays = request.POST['holidays']
            mem.save()
            msg_success = 'submitted succesfully'
            return render(request, 'accounts_month_adddays_form.html', {'z': z, 'msg_success': msg_success})

        return render(request, 'accounts_month_adddays_form.html', {'z': z})
    else:
        return redirect('/')


def accounts_month_viewdays(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = acnt_monthdays.objects.all()

        return render(request, 'accounts_month_viewdays.html', {'z': z, 'mem': mem})
    else:
        return redirect('/')
        
def accounts_month_viewdays_delete(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = acnt_monthdays.objects.get(id=id)
        mem.delete()
        msg_success = "Month days deleted Successfully"

        return render(request, 'accounts_month_viewdays.html', {'z': z, 'msg_success': msg_success})
    else:
        return redirect('/')

def SuperAdmin_leavehistory(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr = user_registration.objects.all()
        des = designation.objects.get(designation="trainee")
        le = leave.objects.filter(leaveapprovedstatus=0).exclude(
            designation_id=des.id).order_by('-id')
        return render(request, 'SuperAdmin_leavehistory.html', {'users': users, 'le': le})
    else:
        return redirect('/')


def SuperAdmin_leaveapprovedstatus(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr = user_registration.objects.all()

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave Approved Successfully"
        return render(request, 'SuperAdmin_leavehistory.html', {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def SuperAdmin_rejectedstatus(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr = user_registration.objects.all()

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'SuperAdmin_leavehistory.html', {'users': users, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def projectMAN_leavehistory(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation="team leader")
        des1 = designation.objects.get(designation="developer")

        dev = user_registration.objects.filter(projectmanager_id=prid)
        ids = dev.values_list('id', flat="true")
        le = leave.objects.filter(user_id__in=ids.all()).filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0).order_by('-id')
        return render(request, 'projectMAN_leavehistory.html', {'pro': pro, 'le': le})
    else:
        return redirect('/')


def projectMAN_leaveapprovedstatus(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave aprroved Successfully"
        return render(request, 'projectMAN_leavehistory.html', {'pro': pro, 'msg_success': msg_success})
    else:
        return redirect('/')


def projectMAN_rejectedstatus(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'projectMAN_leavehistory.html', {'pro': pro, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def TL_leavehistory(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        if request.session.has_key('tlteam'):
            tlteam = request.session['tlteam']

        else:
            return redirect('/')

        mem = user_registration.objects.filter(id=tlid)

        dev = user_registration.objects.filter(tl_id=tlid)
        ids = dev.values_list('id', flat="true")

        des = designation.objects.get(designation="developer")
        le = leave.objects.filter(user_id__in=ids.all(
        ), designation_id=des.id, leaveapprovedstatus=0).order_by('-id')
        return render(request, 'TL_leavehistory.html', {'mem': mem, 'le': le})
    else:
        return redirect('/')


def TL_leaveapprovedstatus(request, id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave aprroved Successfully"
        return render(request, 'TL_leavehistory.html', {'mem': mem, 'msg_success': msg_success})
    else:
        return redirect('/')


def TL_rejectedstatus(request, id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'TL_leavehistory.html', {'mem': mem, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def trainer_leavehistory(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        if request.session.has_key('usernametrnr3'):
            usernametrnr3 = request.session['usernametrnr3']

        mem = user_registration.objects.filter(id=usernametrnr2)
        tr = user_registration.objects.filter(team_id=usernametrnr3)
        ids = tr.values_list('id', flat="true")
        des = designation.objects.get(designation='trainee')
        le = leave.objects.filter(
            designation_id=des.id, leaveapprovedstatus=0).all().order_by('-id')
        return render(request, 'trainer_leavehistory.html', {'le': le, 'mem': mem})

    else:
        return redirect('/')


def trainer_leaveapprovedstatus(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        if request.session.has_key('usernametrnr3'):
            usernametrnr3 = request.session['usernametrnr3']

        mem = user_registration.objects.filter(id=usernametrnr2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave Approved successfully"
        return render(request, 'trainer_leavehistory.html', {'mem': mem, 'msg_success': msg_success})
    else:
        return redirect('/')


def trainer_rejectedstatus(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        if request.session.has_key('usernametrnr3'):
            usernametrnr3 = request.session['usernametrnr3']

        mem = user_registration.objects.filter(id=usernametrnr2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'trainer_leavehistory.html', {'mem': mem, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def tm_leavehistory(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametm2)
        des = designation.objects.get(designation="trainer")
        des1 = designation.objects.get(designation="trainee")
        le = leave.objects.filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0).order_by('-id')

        return render(request, 'tm_leavehistory.html', {'mem': mem, 'le': le})
    else:
        return redirect('/')


def tm_leaveapprovedstatus(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametm2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave Approved successfully"
        return render(request, 'tm_leavehistory.html', {'mem': mem, 'msg_success': msg_success})

    else:
        return redirect('/')


def tm_rejectedstatus(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametm2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'tm_leavehistory.html', {'mem': mem, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def BRadmin_leavehistory(request):
    if 'Adm_id' in request.session:

        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']

        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation="trainee")
        le = leave.objects.filter(leaveapprovedstatus=0).exclude(
            designation_id=des.id).order_by('-id')
        return render(request, 'BRadmin_leavehistory.html', {'Adm': Adm, 'le': le})
    else:
        return redirect('/')


def BRadmin_leaveapprovedstatus(request, id):
    if 'Adm_id' in request.session:

        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']

        Adm = user_registration.objects.filter(id=Adm_id)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave approved Successfully"
        return render(request, 'BRadmin_leavehistory.html', {'Adm': Adm, 'msg_success': msg_success})
    else:
        return redirect('/')


def BRadmin_rejectedstatus(request, id):
    if 'Adm_id' in request.session:

        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']

        Adm = user_registration.objects.filter(id=Adm_id)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'BRadmin_leavehistory.html', {'Adm': Adm, 'msg_warning': msg_warning})
    else:
        return redirect('/')

# def accounts_account_salary(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)          
#         mem1 = user_registration.objects.get(id=usernameacnt2)
#         var = acntspayslip.objects.filter(user_id=usernameacnt2)
#         return render(request, 'accounts_account_salary.html', {'z': z,'mem1': mem1, 'var': var })
#     else:
#         return redirect('/')



# def accounts_accout_salary_slip(request, id):
#     date = datetime.now()
#     user = user_registration.objects.get(id=id)
#     acc = acntspayslip.objects.get(user_id=id)
#     print(acc)
#     year = date.today().year
#     month = date.today().month

#     leave = acnt_monthdays.objects.get(month_fromdate__year__gte=year, month_fromdate__month__gte=month,
#                                       month_todate__year__lte=year, month_todate__month__lte=month)
#     mm = leave.month_workingdays
#     print(mm)
#     abc = int(user.confirm_salary)
#     print(abc)
#     c = abc/mm
#     v = acc.leavesno
#     mem = mm-v
#     print(v)
#     conf = abc-c
#     template_path = 'accounts_accout_salary_slip.html'
#     context = {'acc': acc, 'user': user, 'c': c, 'mm': mm, 'mem': mem, 'conf': conf, 'media_url': settings.MEDIA_URL, 'date': date,
#               }
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="Payslip.pdf"'
#     template = get_template(template_path)
#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response



# def accounts_salary_pending(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         year = date.today().year
#         month = date.today().month
#         vars = acntspayslip.objects.filter(~Q(fromdate__year=year,
#                                           fromdate__month=month))

#         return render(request, 'accounts_salary_pending.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')


# def salarysubmit(request, id):
#     if request.method == 'POST':
#         m = user_registration.objects.get(id=id)
#         m.salary_status = 1
#         m.save()
#         return redirect('/accounts_salary_pending')
#     return redirect('/accounts_salary_pending')



# def accounts_salary_given(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         year = date.today().year
#         month = date.today().month

#         vars = acntspayslip.objects.filter(fromdate__year=year,
#                                           fromdate__month=month)
        
#         return render(request, 'accounts_salary_given.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')

# def accounts_promissory(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         user = user_registration.objects.get(id=id)

#     return render(request, 'accounts_promissory.html', {'z': z, 'user': user})


# def accounts_download_promissory(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         user = user_registration.objects.get(id=id)
        
        
#         try:
#           c = Promissory.objects.filter(user_id=id).latest('id')
#         except Promissory.DoesNotExist:
#           c = None
#           msg_success="No Data in Database Pleace Add Promissory"
#           return render(request, 'accounts_promissory.html', {'z': z,'msg_success':msg_success})
#         print(c)
#     return render(request, 'accounts_download_promissory.html', {'z': z, 'user': user, 'c': c})


# def accounts_promissory_complete_pfd(request, id):
#     date = datetime.now()
#     mem = Promissory.objects.filter(user_id=id).latest('id')
#     template_path = 'accounts_promissory_complete_pfd.html'
#     context = {'mem': mem,
#               'media_url': settings.MEDIA_URL,
#               'date': date
#               }
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
#     response['Content-Disposition'] = 'filename="PROMISSORY.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#         html, dest=response)

#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response
#     # return render(request,'accounts_promissory_complete_pfd.html')


# def accounts_promissory_notcomplete_pfd(request, id):
#     date = datetime.now()
#     mem = Promissory.objects.filter(user_id=id).latest('id')
#     a = num2words(mem.user_id.total_pay)
#     b = (u'u20B9')

#     template_path = 'accounts_promissory_notcomplete_pfd.html'
#     context = {'mem': mem, 'a': a, 'b': b,
#               'media_url': settings.MEDIA_URL,
#               'date': date
#               }
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
#     response['Content-Disposition'] = 'filename="PROMISSORY.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#         html, dest=response)

#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response


# def accounts_promissory_add(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#     mem = user_registration.objects.get(id=id)

#     print(mem)
#     if request.method == "POST":

#         user = Promissory()
#         user.user_id = user_registration.objects.get(id=id)
#         user.inital_amount = request.POST['in_amt']
#         user.inital_paid_on = request.POST['in_paid_on']
#         user.inital_paid_amount = request.POST['in_paid_amt']
#         user.inital_paid_date = request.POST['in_paid_date']
#         user.inital_balance_amount = request.POST['in_bal_amt']
#         user.inital_due_date = request.POST['in_due_date']
#         user.inital_total_payment = request.POST['in_tot_pay']

#         user.second_amount = request.POST['sec_amt']
#         user.second_due_on = request.POST['sec_paid_on']
#         user.second_paid_amount = request.POST['sec_paid_amt']
#         user.second_paid_date = request.POST['sec_paid_date']
#         user.second_balance_amount = request.POST['sec_bal_amt']
#         user.second_due_date = request.POST['sec_due_date']
#         user.second_total_payment = request.POST['sec_tot_pay']

#         user.final_amount = request.POST['fnl_amt']
#         user.final_due_on = request.POST['fnl_paid_on']
#         user.final_paid_amount = request.POST['fnl_paid_amt']
#         user.final_paid_date = request.POST['fnl_paid_date']
#         user.final_balance_amount = request.POST['fnl_bal_amt']
#         user.final_due_date = request.POST['fnl_due_date']
#         user.final_total_payment = request.POST['fnl_tot_pay']
#         user.save()
#         msg_success = "Add Successfully"
#         return render(request, 'accounts_promissory_add.html', {'z': z, 'msg_success': msg_success})

#     return render(request, 'accounts_promissory_add.html', {'z': z})


# def test(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#     user = user_registration.objects.get(id=id)
#     c = Promissory.objects.filter(user_id=id).latest('id')

#     user = Promissory.objects.filter(user_id=id).latest('id')
#     user.complete_status = 1
#     user.save()
#     msg_success = "Status Change To Completed"

#     return render(request, 'accounts_download_promissory.html', {'z': z, 'user': user, 'c': c, 'msg_success': msg_success, })


# def accounts_workstatus(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         cous = course.objects.all()
#         dep = department.objects.all()
#         des = designation.objects.all()
#         emp = user_registration.objects.all()

#         return render(request,'accounts_workstatus.html',{'z':z, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
#     else:
#         return redirect('/')

# @csrf_exempt
# def accounts_designation(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#         dept_id = request.GET.get('dept_id')
#         Desig = designation.objects.filter(department = dept_id).exclude(designation = 'admin').exclude(designation ='manager').exclude(designation ='trainee').exclude(designation ='project manager').exclude(designation ='tester').exclude(designation ='trainingmanager').exclude(designation ='account').exclude(designation ='trainer')
       
#         return render(request,'accounts_designation.html',{'z':z,'Desig': Desig, })
#     else:
#         return redirect('/')

# @csrf_exempt
# def accounts_emp_ajax(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#         dept_id = request.GET.get('dept_id')
#         courseId = request.GET.get('courseId')
#         desigId = request.GET.get('desigId')
#         Desig = user_registration.objects.filter(course=courseId, department=dept_id, designation=desigId)

#         return render(request,'accounts_emp_ajax.html',{'z':z,'Desig': Desig,})
#     else:
#         return redirect('/')

# @csrf_exempt
# def accounts_project_details(request):
#     if 'usernameacnt2' in request.session:
#         emp = request.POST['emp']
#         names = user_registration.objects.get(id=emp) 

#         year = date.today().year
#         month = date.today().month

#         leave = project_taskassign.objects.filter(tl_id=emp,startdate__year__gte=year,
#                                           startdate__month__gte=month,
#                                           submitted_date__year__lte=year,
#                                           submitted_date__month__lte=month)
#         mm = leave.values_list('delay', flat='true')
#         a=0
#         for i in mm:
            
#             a=a+int(i)
#         print(emp)
#         return render(request,'accounts_project_details.html', {'names':names,'mm':mm,'a':a})
#     else:
#         return redirect('/')


# def accounts_add_bank_acnt_update(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         mem1=user_registration.objects.filter(id=id)
#         if request.method == 'POST':
#             vars = user_registration.objects.get(id=id)
#             vars.account_no = request.POST['account_no']
#             vars.ifsc = request.POST['ifsc']
#             vars.bank_branch = request.POST['bank_branch']
#             vars.bank_name= request.POST['bank_name']
#             vars.save()
#             msg_success = "Updated"
#             return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z,'msg_success':msg_success})
#         return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z})
#     else:
        
#         return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z})

def accounts_account_salary(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)          
        mem1 = user_registration.objects.get(id=usernameacnt2)
        var = acntspayslip.objects.filter(user_id=usernameacnt2)
        return render(request, 'accounts_account_salary.html', {'z': z,'mem1': mem1, 'var': var })
    else:
        return redirect('/')



def accounts_accout_salary_slip(request, id):
    date = datetime.now()
    user = user_registration.objects.get(id=id)
    acc = acntspayslip.objects.get(user_id=id)
    
    year = date.today().year
    month = date.today().month

    leave = acnt_monthdays.objects.get(month_fromdate__year__gte=year, month_fromdate__month__gte=month,
                                       month_todate__year__lte=year, month_todate__month__lte=month)
    mm = leave.month_workingdays
   
    abc = int(user.confirm_salary)
    
    c = abc/mm
    v = acc.leavesno
    mem = mm-v
    
    conf = abc-c
    template_path = 'accounts_accout_salary_slip.html'
    context = {'acc': acc, 'user': user, 'c': c, 'mm': mm, 'mem': mem, 'conf': conf, 'media_url': settings.MEDIA_URL, 'date': date,
               }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Payslip.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def accounts_salary_pending(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        year = date.today().year
        month = date.today().month
        vars = acntspayslip.objects.filter(~Q(fromdate__year=year,
                                          fromdate__month=month))

        return render(request, 'accounts_salary_pending.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def salarysubmit(request, id):
    if request.method == 'POST':
        m = user_registration.objects.get(id=id)
        m.salary_status = 1
        m.save()
        return redirect('/accounts_salary_pending')
    return redirect('/accounts_salary_pending')


def accounts_salary_given(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        year = date.today().year
        month = date.today().month

        vars = acntspayslip.objects.filter(fromdate__year=year,
                                          fromdate__month=month)
        
        return render(request, 'accounts_salary_given.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def accounts_promissory(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        user = user_registration.objects.get(id=id)

    return render(request, 'accounts_promissory.html', {'z': z, 'user': user})

def accounts_download_promissory(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        user = user_registration.objects.get(id=id)
        
        
        try:
           c = Promissory.objects.filter(user_id=id).latest('id')
        except Promissory.DoesNotExist:
           c = None
           msg_success="No Data in Database Pleace Add Promissory"
           return render(request, 'accounts_promissory.html', {'z': z,'msg_success':msg_success})
        
    return render(request, 'accounts_download_promissory.html', {'z': z, 'user': user, 'c': c})

def accounts_promissory_delete(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        user = user_registration.objects.get(id=id)
        
        del_id = Promissory.objects.get(user_id_id =id)
        del_id.delete()
        msg_success="Promissory deleted Successfully"
        return render(request, 'accounts_promissory.html', {'z': z,'msg_success':msg_success})
        
    return render(request, 'accounts_download_promissory.html', {'z': z, 'user': user})

def accounts_promissory_complete_pfd(request, id):
    date = datetime.now()
    mem = Promissory.objects.filter(user_id=id).latest('id')
    template_path = 'accounts_promissory_complete_pfd.html'
    context = {'mem': mem,
               'media_url': settings.MEDIA_URL,
               'date': date
               }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="PROMISSORY.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return render(request,'accounts_promissory_complete_pfd.html')


def accounts_promissory_notcomplete_pfd(request, id):
    date = datetime.now()
    mem = Promissory.objects.filter(user_id=id).latest('id')
    a = num2words(30000)
    b = (u'u20B9')

    template_path = 'accounts_promissory_notcomplete_pfd.html'
    context = {'mem': mem, 'a': a, 'b': b,
               'media_url': settings.MEDIA_URL,
               'date': date
               }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="PROMISSORY.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

import re
def accounts_promissory_add(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    mem = user_registration.objects.get(id=id)

    
    if request.method == "POST":
        def change_date_format(dt):
            return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

        user = Promissory()
        user.user_id = user_registration.objects.get(id=id)
        user.inital_amount = request.POST['in_amt']
        if request.POST['in_paid_on'] is not None:
            user.inital_paid_on = change_date_format(request.POST['in_paid_on'])

        user.inital_paid_amount = request.POST['in_paid_amt']

        if request.POST['in_paid_date'] is not None:
            user.inital_paid_date = change_date_format(request.POST['in_paid_date'])

        user.inital_balance_amount = request.POST['in_bal_amt']
        
        if request.POST['in_due_date'] is not None:
            user.inital_due_date = change_date_format(request.POST['in_due_date'])

        user.inital_total_payment = request.POST['in_tot_pay']
        user.second_amount = request.POST['sec_amt']

        if request.POST['sec_paid_on'] is not None:
            user.second_due_on = change_date_format(request.POST['sec_paid_on'])

        user.second_paid_amount = request.POST['sec_paid_amt']

        if request.POST['sec_paid_date'] is not None:
            user.second_paid_date = change_date_format(request.POST['sec_paid_date'])

  
        user.second_balance_amount = request.POST['sec_bal_amt']

        if request.POST['sec_due_date'] is not None:
            user.second_due_date = change_date_format(request.POST['sec_due_date'])

        
        user.second_total_payment = request.POST['sec_tot_pay']


        if request.POST['second_due_date_on'] is not None:
            user.second_due_date_on = change_date_format(request.POST['second_due_date_on'])

        user.final_amount = request.POST['fnl_amt']

        if request.POST['fnl_paid_on'] is not None:
            user.final_due_on = change_date_format(request.POST['fnl_paid_on'])

 
        user.final_paid_amount = request.POST['fnl_paid_amt']

        if request.POST['fnl_paid_date'] is not None:
            user.final_paid_date = change_date_format(request.POST['fnl_paid_date'])

        user.final_balance_amount = request.POST['fnl_bal_amt']

        if request.POST['fnl_due_date'] is not None:
            user.final_due_date = change_date_format(request.POST['fnl_due_date'])

        user.final_total_payment = request.POST['fnl_tot_pay']

        if request.POST['fnl_due_date_on'] is not None:
            user.final_due_date_on = change_date_format(request.POST['fnl_due_date_on'])
        user.save()

        user_pay = user_registration.objects.get(id=id)
        
        user_pay.total_pay = user.final_total_payment + user.second_total_payment + user.inital_total_payment
        user_pay.save() 
        user.save()

        msg_success = "Add Successfully"
        return render(request, 'accounts_promissory_add.html', {'z': z, 'msg_success': msg_success})

    return render(request, 'accounts_promissory_add.html', {'z': z, 'mem':mem})

def accounts_promissory_update(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    mem = user_registration.objects.get(id=id)

    prom_data = Promissory.objects.get(user_id = id)

    
    if request.method == "POST":

        def change_date_format(dt):
            return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

        user = Promissory.objects.get(user_id = id)
        user.user_id = user_registration.objects.get(id=id)
        user.inital_amount = request.POST['in_amt']
        if request.POST['in_paid_on'] is not None:
            user.inital_paid_on = change_date_format(request.POST['in_paid_on'])

        user.inital_paid_amount = request.POST['in_paid_amt']

        if request.POST['in_paid_date'] is not None:
            user.inital_paid_date = change_date_format(request.POST['in_paid_date'])

        user.inital_balance_amount = request.POST['in_bal_amt']
        
        if request.POST['in_due_date'] is not None:
            user.inital_due_date = change_date_format(request.POST['in_due_date'])

        user.inital_total_payment = request.POST['in_tot_pay']
        user.second_amount = request.POST['sec_amt']

        if request.POST['sec_paid_on'] is not None:
            user.second_due_on = change_date_format(request.POST['sec_paid_on'])

        user.second_paid_amount = request.POST['sec_paid_amt']

        if request.POST['sec_paid_date'] is not None:
            user.second_paid_date = change_date_format(request.POST['sec_paid_date'])

  
        user.second_balance_amount = request.POST['sec_bal_amt']

        if request.POST['sec_due_date'] is not None:
            user.second_due_date = change_date_format(request.POST['sec_due_date'])

        
        user.second_total_payment = request.POST['sec_tot_pay']


        if request.POST['second_due_date_on'] is not None:
            user.second_due_date_on = change_date_format(request.POST['second_due_date_on'])

        user.final_amount = request.POST['fnl_amt']

        if request.POST['fnl_paid_on'] is not None:
            user.final_due_on = change_date_format(request.POST['fnl_paid_on'])

 
        user.final_paid_amount = request.POST['fnl_paid_amt']

        if request.POST['fnl_paid_date'] is not None:
            user.final_paid_date = change_date_format(request.POST['fnl_paid_date'])

        user.final_balance_amount = request.POST['fnl_bal_amt']

        if request.POST['fnl_due_date'] is not None:
            user.final_due_date = change_date_format(request.POST['fnl_due_date'])

        user.final_total_payment = request.POST['fnl_tot_pay']

        if request.POST['fnl_due_date_on'] is not None:
            user.final_due_date_on = change_date_format(request.POST['fnl_due_date_on'])
       

        user_pay = user_registration.objects.get(id=id)
        user_pay.total_pay = int(user.final_total_payment) + int(user.second_total_payment) + int(user.inital_total_payment)
        user_pay.save()
        user.save()

        msg_success = "Update Successfully"
        return render(request, 'accounts_promissory_update.html', {'z': z, 'msg_success': msg_success, 'prom_data':prom_data})

    return render(request, 'accounts_promissory_update.html', {'z': z, 'prom_data':prom_data, })


def test(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    user = user_registration.objects.get(id=id)
    c = Promissory.objects.filter(user_id=id).latest('id')

    user = Promissory.objects.filter(user_id=id).latest('id')
    user.complete_status = 1
    user.save()
    msg_success = "Status Change To Completed"

    return render(request, 'accounts_download_promissory.html', {'z': z, 'user': user, 'c': c, 'msg_success': msg_success, })


def accounts_workstatus(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'accounts_workstatus.html',{'z':z, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')

@csrf_exempt
def accounts_designation(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="manager"),~Q(designation="project manager"),~Q(designation="tester"),~Q(designation="trainingmanager"),~Q(designation="trainer"),~Q(designation="trainee"),~Q(designation="account"),~Q(designation="hr"))
       
        return render(request,'accounts_designation.html',{'z':z,'Desig': Desig, })
    else:
        return redirect('/')

@csrf_exempt
def accounts_emp_ajax(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        dept_id = request.GET.get('dept_id')
        courseId = request.GET.get('courseId')
        desigId = request.GET.get('desigId')
        Desig = user_registration.objects.filter(course=courseId, department=dept_id, designation=desigId, status="active")

        return render(request,'accounts_emp_ajax.html',{'z':z,'Desig': Desig,})
    else:
        return redirect('/')

@csrf_exempt
def accounts_project_details(request):
    if 'usernameacnt2' in request.session:
        emp = request.POST['emp']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        names = project_taskassign.objects.filter(developer=emp,startdate__gte=fdate, enddate__lte=tdate).order_by('-id')

        year = date.today().year
        month = date.today().month

        leave = project_taskassign.objects.filter(developer=emp,startdate__year__gte=year,
                                          startdate__month__gte=month,
                                          submitted_date__year__lte=year,
                                          submitted_date__month__lte=month)
        
        start = datetime.strptime(fdate, '%Y-%m-%d').date()
        end = datetime.strptime(tdate, '%Y-%m-%d').date()
        pro = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = False).filter(developer_id= emp, ).values('startdate','enddate','submitted_date', 'delay')
        pro_false = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= emp).values('startdate','enddate')
        tot = 0
        tot1 = 0
        xx=0
        xx1 = 0
        for i in pro:
            d_end = (i['enddate'])
            d_submitted = (i['submitted_date'])
            differ = (d_submitted - d_end).days
            if differ == 0:
                tot=0
            else:

                if d_submitted <= end:
                    diff = (d_submitted - d_end).days
                    cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=d_submitted).values('start_time').count()
                    xx = diff - cnt
                else:
                    diff = (end - d_end).days
                    cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
                    xx = diff - cnt
            tot = tot + xx
                

        for x in pro_false:
            d_end = (x['enddate'])
            diff =  (end - d_end).days
            if diff <= 0:
                tot1=0
            cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
            xx1 = diff- cnt
            tot1 = tot1 + xx1

        a = tot + tot1

        return render(request,'accounts_project_details.html', {'names':names,'a':a })
    else:
        return redirect('/')


def accounts_add_bank_acnt_update(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.filter(id=id)
        if request.method == 'POST':
            vars = user_registration.objects.get(id=id)
            vars.account_no = request.POST['account_no']
            vars.ifsc = request.POST['ifsc']
            vars.bank_branch = request.POST['bank_branch']
            vars.bank_name= request.POST['bank_name']
            vars.save()
            msg_success = "Updated"
            return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z,'msg_success':msg_success})
        return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z})
    else:
        
        return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z})

def DEVpayments(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    mem1 = user_registration.objects.get(id=devid)
    var = acntspayslip.objects.filter(user_id =devid)
    return render(request, 'DEVpayments.html', {'dev': dev, 'var': var,'mem1':mem1})
    
    
def TLpayment(request):
   if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        mem1 = user_registration.objects.get(id=tlid)
        var = acntspayslip.objects.filter(user_id =tlid)
        return render(request, 'TLpayment.html', {'mem': mem, 'var': var,'mem1':mem1})
   else:
        return redirect('/')

def projectmanager_payment_list(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        var = acntspayslip.objects.filter(user_id = prid)
        b = user_registration.objects.get(id=prid)
        return render(request, 'projectmanager_payment_list.html', {'pro': pro, 'var': var, 'b':b })
    else:
        return redirect('/')

############### training manager ###################################

def trainingmanager_payment_list(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
       
        mem = user_registration.objects.filter(id=usernametm2)
        var = acntspayslip.objects.filter(user_id = usernametm2)
        return render(request, 'trainingmanager_payment_list.html', {'mem': mem, 'var': var })
    else:
        return redirect('/')

########################### pdf #########################

def paypdf(request,id,tid):
    date = datetime.now()  
    user = user_registration.objects.get(id=tid)
    acc = acntspayslip.objects.get(id=id)
    
    # year = date.today().year
    # month = date.today().month

    year = acc.fromdate.year
    month = acc.fromdate.month

    leave = acnt_monthdays.objects.get(month_fromdate__year__gte=year,month_fromdate__month__gte=month,month_todate__year__lte=year,month_todate__month__lte=month)
    
    mm = leave.month_workingdays
    mem = leave.month_holidays
    v = acc.leavesno
    mam = mm-v
    leaves_tot = acc.delay+acc.leavesno
    wrk_days = mm -leaves_tot
    
    abc = int(user.confirm_salary)
    
    c = abc - acc.net_salary
    
   
    
    
    
    add = acc.basic_salary+ int(acc.conveyns)+acc.hra+acc.pf_tax+acc.pf+int(acc.esi)+acc.delay+acc.leavesno+acc.incentives
    conf = add-c
    words = num2words(acc.net_salary)
    template_path = 'paypdf.html'
    context = {'acc':acc, 'user':user,'c':c,'mm':mm,'mam':mam,'conf':conf,'words':words, 'add':add,
    'media_url':settings.MEDIA_URL,
    'date':date, 'leaves_tot':leaves_tot, 'wrk_days':wrk_days
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Payslip.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


########################### manager ######################


def MAN_payment_list(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        var = acntspayslip.objects.filter(user_id = m_id)
        return render(request, 'MAN_payment_list.html', {'mem': mem, 'var': var })
    else:
        return redirect('/')


############################### trainer #############################

def trainer_payment_list(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        var = acntspayslip.objects.filter(user_id = usernametrnr2)
        return render(request, 'trainer_payment_list.html', {'z': z, 'var': var })
    else:
        return redirect('/')

def TSpayment(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernametsid'):
            usernametsid = request.session['usernametsid']
        else:
            return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets).filter(id=usernametsid)
        mem1 = user_registration.objects.get(id=usernametsid)
        var = acntspayslip.objects.filter(user_id = usernametsid)
        return render(request, 'TSpayment.html', {'mem': mem,'mem1': mem1, 'var': var })
    else:
        return redirect('/')
        
        
        
def project_reset(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        x = project_taskassign.objects.get(id = id)
        x.submitted_date ="0101-01-01"
        x.employee_files =""
        x.projectstatus = "in progress"
        x.status=''
        x.delay=0
        x.progress=50
        x.save()
        
        msg_success="success"
        return render(request, 'projectmanager_projectstatus.html', {'pro': pro,'msg_success':msg_success})
    else:
        return redirect('/')
        

def projectmanager_trainee_status(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        
        des = designation.objects.get(designation="trainee")
        des1 = designation.objects.get(designation="developer")
        var=user_registration.objects.filter(designation_id=des.id, status="active")
        var1=user_registration.objects.filter(designation_id=des1.id, status="active")
        return render(request, 'projectmanager_trainee_status.html', {'pro': pro,'var':var,'var1':var1})
    else:
        return redirect('/')
        
@csrf_exempt
def projectmanager_trainee_details(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        emp = request.POST['emp']
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'projectmanager_trainee_details.html', {'pro': pro,'names':names,'a':a})
    else:
        return redirect('/')

# ------------------------------- HR   ------------------------------- #

def HR_Dashboard(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        return render(request, 'hr_module/HR_Dashboard.html', {'mem': mem})
    else:
        return redirect('/')

def HR_leave(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        return render(request, 'hr_module/HR_leave.html', {'mem': mem})
    else:
        return redirect('/')

def HR_leaveapply(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_des_id'):
            hr_des_id = request.session['hr_des_id']
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=hr_des_id).filter(id=hr_id)
        
        if request.method == 'POST':
            apply_leave = leave()
            apply_leave.from_date = request.POST['from']
            apply_leave.to_date = request.POST['to']
            apply_leave.leave_status = request.POST['haful']
            apply_leave.reason = request.POST['reason']
            apply_leave.user =user_registration.objects.get(id=hr_id)
            apply_leave.designation_id =hr_des_id
            apply_leave.leaveapprovedstatus = 0
            
            start = datetime.strptime(apply_leave.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(apply_leave.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                apply_leave.days = 1
            else:
                apply_leave.days = diff - cnt
                
                
            apply_leave.save()
            msg_success = "leave applied"
            return render(request, 'hr_module/HR_leaveapply.html',{"msg_success":msg_success})
        else:
            pass
        return render(request, 'hr_module/HR_leaveapply.html',{'mem':mem})
    else:
        return redirect('/')

def HR_appliedleave(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id= request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        hr_leave = leave.objects.filter(user=hr_id).order_by('-id')
        return render(request, 'hr_module/HR_appliedleave.html', {'mem': mem,'hr':hr_leave})
    else:
        return redirect('/')

def HR_issue(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        return render(request, 'hr_module/HR_issue.html', {'mem': mem})
    else:
        return redirect('/')

def HR_reportissue(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_des_id'):
            hr_des_id = request.session['hr_des_id']
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=hr_des_id).filter(id=hr_id)
        issue = reported_issue()
        des = designation.objects.get(designation='admin')
        if request.method == "POST":
            issue.issue = request.POST['issues']
            issue.reported_date = datetime.now()
            issue.reported_to = user_registration.objects.get(designation_id=des.id)
            issue.reporter = user_registration.objects.get(id=hr_id)
            issue.designation_id = hr_des_id
            issue.issuestatus = 0
            issue.save()
            msg_success = "Issue Reported"
            return render(request, 'hr_module/HR_reportissue.html',{'mem':mem,'msg_success':msg_success})
        else:
            pass
        return render(request, 'hr_module/HR_reportissue.html',{'mem':mem})
    else:
        return redirect('/')

def HR_reportedissue(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        hr_issue = reported_issue.objects.filter(reporter=hr_id) .order_by('-id')
        return render(request, 'hr_module/HR_reportedissue.html', {'mem': mem,'hr_issue':hr_issue})
    else:
        return redirect('/')

def HR_trainingdepartment(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.all()
        Desig = designation.objects.all()
        return render(request, 'hr_module/HR_trainingdepartment.html', {'mem': mem,'Dept':Dept,'Desig':Desig})
    else:
        return redirect('/')

def HR_trainerslist(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.get(id=id)
        deptid = id
        Trainer = designation.objects.get(designation='Trainer')
        trainers_data = user_registration.objects.filter(designation=Trainer).filter(department=id)
        topics = topic.objects.all()
        return render(request, 'hr_module/HR_trainerslist.html', {'mem': mem,'trainers_data': trainers_data, 'topics': topics, 'Dept': Dept, 'deptid': deptid})
    else:
        return redirect('/')

def HR_trainersteam(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        user = user_registration.objects.filter(id=id)
        team = create_team.objects.filter(trainer_id=id).order_by('-id')
        return render(request, 'hr_module/HR_trainersteam.html', {'mem': mem,'user': user, 'team': team})
    else:
        return redirect('/')

def HR_trainersteamdetails(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        id = id
        num = previousTeam.objects.filter(teamname=id).count()
        num1 = topic.objects.filter(team=id).count()
        return render(request, 'hr_module/HR_trainersteamdetails.html', {'mem': mem,'num':num, 'num1':num1,'id': id})
    else:
        return redirect('/')

def HR_trainees(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        trainees_data = previousTeam.objects.filter(teamname=id).order_by('-id')
        return render(request, 'hr_module/HR_trainees.html', {'trainees_data': trainees_data, 'mem': mem})
    else:
        return redirect('/')

def HR_traineestopic(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        topics = topic.objects.filter(team=id).order_by("-id")
        return render(request, 'hr_module/HR_traineestopics.html', {'topics': topics, 'mem': mem})
    else:
        return redirect('/')

def HR_traineeprofile(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        trainees_data = user_registration.objects.get(id=id)
        user = user_registration.objects.get(id=id)
        num = trainer_task.objects.filter(user=user).filter(task_status='1').count()
        progress = user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'hr_module/HR_traineesprofile.html', {'trainees_data': trainees_data, 'mem': mem,'num':num,'labels':labels,'data':data,'progress':progress})
    else:
        return redirect('/')

def HR_traineecompletedtask(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        user = user_registration.objects.get(id=id)
        
        task = trainer_task.objects.filter(user=user).filter(task_status='1')
        return render(request, 'hr_module/HR_traineecompletedtask.html', {'mem': mem,'task':task})
    else:
        return redirect('/')

def HR_employeesdepartment(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.all()
        return render(request, 'hr_module/HR_employeesdepartment.html', {'mem': mem,'Dept':Dept})
    else:
        return redirect('/')

def HR_employeeslist(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.get(id=id)
        deptid = id
        Desig = designation.objects.filter(branch_id=Dept.branch_id).exclude(designation='admin').exclude(designation='manager')
        return render(request, 'hr_module/HR_employeeslist.html', {'mem': mem,'Dept':Dept,'Desig':Desig,'deptid':deptid})
    else:
        return redirect('/')

def HR_viewtrainers(request, id, did):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        userreg = user_registration.objects.filter(designation=id).filter(department=did).order_by("-id")
        return render(request, 'hr_module/HR_viewtrainers.html', {'mem': mem,'userreg':userreg})
    else:
        return redirect('/')

def HR_trainerprofile(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        userreg = user_registration.objects.get(id=id)
        return render(request, 'hr_module/HR_trainerprofile.html', {'mem': mem,'userreg':userreg})
    else:
        return redirect('/')

def HR_trainercurrenttrainees(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        team= create_team.objects.filter(trainer_id=id,team_status="0").values_list('id', flat=True)
        user = previousTeam.objects.filter(teamname_id__in=team).values_list('user', flat=True)
        trainees = user_registration.objects.filter(id__in=user)
        return render(request, 'hr_module/HR_trainercurrenttrainees.html', {'mem': mem,'trainees':trainees,'user':user})
    else:
        return redirect('/')

def HR_trainerprevioustrainees(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        team= create_team.objects.filter(trainer_id=id,team_status="1").values_list('id', flat=True)
        user = previousTeam.objects.filter(teamname_id__in=team).values_list('user', flat=True)
        trainees = user_registration.objects.filter(id__in=user)
        return render(request, 'hr_module/HR_trainerprevioustrainees.html', {'mem': mem,'trainees':trainees,'user':user})
    else:
        return redirect('/')

def HR_trainersattendance(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        usr = user_registration.objects.get(id=id)
        return render(request, 'hr_module/HR_trainersattendance.html', {'mem': mem,'usr':usr})
    else:
        return redirect('/')

def HR_trainersattendanceview(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        usr = user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            adata = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id)
            return render(request, 'hr_module/HR_trainersattendancesort.html', {'mem': mem,'usr':usr,'adata':adata})
    else:
        return redirect('/')

def HR_employeedetails(request,id,did):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        emp_data = user_registration.objects.filter(designation_id=id,department=did, status="active")
        return render(request, 'hr_module/HR_employeedetails.html', {'mem': mem,'emp_data':emp_data})
    else:
        return redirect('/')

def HR_employeesprofile(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        emp_data = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'hr_module/HR_employeesprofile.html', {'mem': mem,'emp_data':emp_data,'labels': labels, 'data': data})
    else:
        return redirect('/')


def HR_employeesinvolvedprojects(request,id,did):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        mem1 = user_registration.objects.filter(id__in=id,designation_id__in=did).values_list('id', flat=True)
        mem2 = designation.objects.get(designation="project manager")
        mem3 = designation.objects.get(designation="team leader")
        mem4 = designation.objects.get(designation="developer")
        des_id = mem2.id
        des1_id=mem3.id
        des2_id=mem4.id
        x_id=int(did)
        if x_id==des_id:
            Pro_data = project.objects.filter(projectmanager_id=id).order_by("-id")
            return render(request, 'hr_module/HR_employeesinvolvedprojects.html', {'mem': mem,'Pro_data': Pro_data})
        elif x_id==des1_id or x_id==des2_id:
            Pro_data = project_taskassign.objects.filter(developer=id).order_by("-id")
            return render(request, 'hr_module/HR_employeesinvolvedprojects.html', {'mem': mem,'Pro_data': Pro_data})
        else:
            return render(request, 'hr_module/HR_employeesinvolvedprojects.html', {'mem': mem})
    else:
        return redirect('/')

def HR_employeesattendance(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        id = id
        return render(request, 'hr_module/HR_employeesattendance.html', {'mem': mem,'id': id})
    else:
        return redirect('/')

def HR_employeesattendancesort(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id).order_by('-id')
            return render(request, 'hr_module/HR_employeesattendancesort.html', {'mem1': mem1,'id': id,'mem':mem})
    else:
        return redirect('/')

def HR_changepassword(request):
    if 'hr_id' in request.session:

        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=hr_id)
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    msg_success= "password changed"
                    return render(request, 'hr_module/HR_changepassword.html', {'mem': mem,'msg_success':msg_success})
            elif oldps == newps:
                    msg_warning= " current password and new  password are same"
                    return render(request, 'hr_module/HR_changepassword.html', {'mem': mem,'msg_warning':msg_warning})
            elif newps == cmps:
                msg_warning= " new password and confirm same password not matching"
                return render(request, 'hr_module/HR_changepassword.html', {'mem': mem,'msg_warning':msg_warning})
            # return render(request, 'hr_module/HR_changepassword.html', {'mem': mem})
        return render(request, 'hr_module/HR_changepassword.html', {'mem': mem})
    else:
        return redirect('/')

def HR_accountsettings(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        if request.method == 'POST':
            id = request.GET.get('id')
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filenamees']
            abc.save()
            msg_success= "image changed"
            return render(request, 'hr_module/HR_accountsettings.html', {'msg_success':msg_success,'mem':mem})
        return render(request, 'hr_module/HR_accountsettings.html',{'mem':mem})
    else:
        return redirect('/')

def HR_imagesettings(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        
        return render(request,'hr_module/HR_accountsettings.html', {'mem': mem})
    else:
        return redirect('/')


    
#============== 24/02/2023  New Upadation =============


def HR_training_leads(request):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        
        return render(request,'hr_module/HR_training_leads.html', {'mem': mem})
    else:
        return redirect('/')
    
    
def HR_upcoming_leads(request):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        leads=Leads_Register.objects.filter(r_status=0,r_assing_id=hr_id)
        return render(request,'hr_module/HR_upcoming_leads.html', {'mem': mem,'leads':leads})
    else:
        return redirect('/')


def HR_current_leads(request):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        leads=Leads_Register.objects.filter(Q(r_type_status='') | Q(r_type_status=1),r_status=3,r_refference=hr_id)
        return render(request,'hr_module/HR_current_leads.html', {'mem': mem,'leads':leads})
    else:
        return redirect('/')
    
def HR_Waiting_leads(request):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        leads=Leads_Register.objects.filter(r_type_status=2,r_refference=hr_id)
        cur_date=date.today()
       
        return render(request,'hr_module/HR_wating_leads.html', {'mem': mem,'leads':leads,'cur_date':cur_date})
    else:
        return redirect('/')

def HR_leads_expfre(request,pk):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        if pk == 1:
            leads=Leads_Register.objects.filter(r_type_status=2,r_refference=hr_id, r_fre_exp='Fresher')
            print(leads)
        else:
            leads=Leads_Register.objects.filter(r_type_status=2,r_refference=hr_id, r_fre_exp='Experienced')
            print(leads)

        cur_date=date.today()
       
        return render(request,'hr_module/HR_wating_leads.html', {'mem': mem,'leads':leads,'cur_date':cur_date})
    else:
        return redirect('/')
    
    
def HR_Joined(request):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        leads=Leads_Register.objects.filter(r_status=1,r_refference=hr_id)
        return render(request,'hr_module/HR_joined.html', {'mem': mem,'leads':leads})
    else:
        return redirect('/')
    
        
def HR_add_leads(request):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
       
        return render(request,'hr_module/HR_add_lead.html', {'mem': mem})
    else:
        return redirect('/')
    
def HR_register_lead(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
      
        
        if request.method == 'POST':

            email_check = Leads_Register.objects.filter(r_email__iexact=request.POST['remail']).exists()
            phno_check = Leads_Register.objects.filter(r_phno__iexact=request.POST['rphno']).exists()
            
            if email_check or phno_check :
                msg_success="Lead Registration Not Successfull, Email Id Or Phone Number Already Exists"
                leads=Leads_Register.objects.filter(r_status=0,r_refference=hr_id)
                return render(request,'hr_module/HR_add_lead.html', {'mem': mem,'msg_success':msg_success,'leads':leads})
            
            else:
                reg = Leads_Register()
                reg.r_fullname = request.POST['rname']
                reg.r_email = request.POST['remail']
                reg.r_phno = request.POST['rphno']
                reg.r_place = request.POST['rplace']
                reg.r_qulific = request.POST['rquli']
                reg.r_pass_out_year = request.POST['ryear']
                reg.r_fre_exp = request.POST['rfr_exp']
                reg.r_lead_source = request.POST['l_source']
                reg.r_refference = user_registration.objects.get(id=request.POST['rreffer'])
                reg.r_dese = request.POST['rdesc']
                msg_success="Lead Registration Successfull"
                reg.save()
                leads=Leads_Register.objects.filter(r_status=0,r_refference=hr_id)

        return render(request,'hr_module/HR_add_lead.html', {'mem': mem,'msg_success':msg_success,'leads':leads})
    
    else:
        return redirect('/')
    

def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Leads_Register.objects.filter(r_email__iexact=email).exists()
    }
   
    return JsonResponse(data)

def check_phone(request):
    phno = request.GET.get('phno', None)
    data = {
        'is_taken': Leads_Register.objects.filter(r_phno__iexact=phno).exists()
    }
   
    return JsonResponse(data)

def HR_lead_accept(request,pk):

    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        reg = Leads_Register.objects.get(id=pk)
        reg.r_status=3
        reg.save()
        leads=Leads_Register.objects.filter(r_status=0,r_refference=hr_id)
        return render(request,'hr_module/HR_upcoming_leads.html', {'mem': mem,'leads':leads})
    else:
        return redirect('/')

    
def HR_lead_reject(request,pk):
 
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        reg = Leads_Register.objects.get(id=pk)
        reg.r_status=2
        reg.save()
        leads=Leads_Register.objects.filter(r_status=0,r_refference=hr_id)
        return render(request,'hr_module/HR_upcoming_leads.html', {'mem': mem,'leads':leads})
    else:
        return redirect('/')


def HR_update_lead_status(request,pk):
     
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        leads = Leads_Register.objects.get(id=pk,r_refference=hr_id)
        
        return render(request,'hr_module/HR_update_lead_status.html', {'mem': mem,'leads':leads})
    else:
        return redirect('/')
    
def HR_update_lead_data(request,pk):
     
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        leads = Leads_Register.objects.get(id=pk)
         
        if request.method == 'POST':

            leads.r_fullname = request.POST['rname']
            leads.r_email = request.POST['remail']
            leads.r_phno = request.POST['rphno']
            leads.r_place = request.POST['rplace']
            leads.r_qulific = request.POST['rquli']
            leads.r_refference = user_registration.objects.get(id=request.POST['rreffer'])
            leads.r_dese = request.POST['rdesc']
            leads.r_type = request.POST['rtype']

            leads.r_pass_out_year = request.POST['ryear']
            leads.r_fre_exp = request.POST['rfr_exp']
            leads.r_lead_source = request.POST['l_source']

            if request.POST['wdate']:
                leads.r_wating_date =  request.POST['wdate']
            else:
                leads.r_wating_date =  leads.r_wating_date 

            leads.r_type_status = request.POST['rstatus']
            leads.save()

        return redirect('HR_Waiting_leads')
    else:
        return redirect('/')


def HR_update_lead_confirm(request,pk):
 
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        leads = Leads_Register.objects.get(id=pk,r_refference=hr_id)
        leads.r_status=1
        leads.r_completed_date=date.today()
        leads.save()
        
        return redirect('HR_current_leads')
    else:
        return redirect('/')

#============== 24/02/2023  End Upadation =============

def HR_logout(request):
    if 'hr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')




#*******new******************************

def completedteam(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        var = create_team.objects.filter(team_status=1).order_by('-id')
        des = designation.objects.get(designation='trainer')
        var1 = user_registration.objects.filter(designation_id=des.id)
        return render(request,'completedteam.html',{'mem':mem,'var':var,'var1':var1})
    return redirect('/')

def completed_team_trainees(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        var = previousTeam.objects.filter(teamname=id)
       
        return render(request,'completed_team_trainees.html',{'mem':mem,'var':var})
    return redirect('/')

def completed_team_task(request,id,tid):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        var =trainer_task.objects.filter(user=id,team_name=tid).order_by('-id')
      
        return render(request,'completed_team_task.html',{'mem':mem,'var':var})
    return redirect('/')

def probations(request):
    
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        des= designation.objects.get(designation='trainee')
        var =user_registration.objects.filter(designation_id=des.id).order_by('-id')
        team=create_team.objects.filter(team_status=0)
        pb=probation()
        if request.method == 'POST':
            pb.team=create_team.objects.get(id=int(request.POST['team']))
            ut=create_team.objects.get(id=int(request.POST['team']))
            pb.trainer_id=ut.trainer_id
            
            pb.reason=request.POST['extend_reason']
            pb.startdate=request.POST['startdate']
            pb.enddate=request.POST['enddate']
            id = request.GET.get('tid')
            pb.user_id=id
            pb.save()
            msg_success="probation extended"
            return render(request,'probation.html',{'mem':mem,'var':var,'team':team,'msg_success':msg_success})
        
        return render(request,'probation.html',{'mem':mem,'var':var,'team':team})


# def probation_stop(request):  
#     id = request.GET.get('id')
#     var = probation.objects.filter(status=0,user_id=id).latest()   
#     var.stop_reason = request.POST['stop_reason'] 
#     var.status= 1
#     var.stopdate=datetime.now()
#     var.user_id=id 
#     var.save()  
#     print(var)
#     msg_success="stoped succesfully"
#     return render(request, 'probation.html', {'msg_success':msg_success})

# def probation_renew(request):  
#     id = request.GET.get('id')
#     var = probation.objects.filter(status=1,user_id=id).latest() 
    
#     alt = var.stopdate
    
#     print(alt)
#     akm = datetime.now().date()
#     v= (akm-alt).days
#     var.extension = (akm-alt).days
#     var.status= 0
#     var.renewdate=datetime.now() 
#     var.user_id=id
#     var.save()  
#     x=user_registration.objects.get(id=id)
#     del_add = x.trainee_delay
#     x.trainee_delay=del_add+v
#     x.save()
#     msg_success="renew succesfully"
#     return render(request, 'probation.html', {'msg_success':msg_success})


def probation_stop(request):  
    id = request.GET.get('id')
    var = probation() 
    var.stop_reason = request.POST['stop_reason'] 
    var.status= 1
    var.stopdate=datetime.now()
    var.user_id=id 
    var.save()  
    x=user_registration.objects.get(id=id)
    x.status="resigned"
    x.save()
    msg_success="stoped succesfully"
    return render(request, 'probation.html', {'msg_success':msg_success})

def probation_renew(request):  
    id = request.GET.get('id')
    var = probation.objects.filter(status=1,user_id=id).latest() 
    alt = var.stopdate
    akm = datetime.now().date()
    v= (akm-alt).days
    z= (akm-alt).days
    var.extension = (akm-alt).days
    var.status= 0
    var.renewdate=datetime.now()
    var.user_id=id
    var.save()  
    x=user_registration.objects.get(id=id)
    delta =  x.enddate+timedelta(z)
    x.enddate =delta
    del_add = x.trainee_delay
    x.trainee_delay=del_add+v
    x.status='active'
    x.save()
    msg_success="renew succesfully"
    return render(request, 'probation.html', {'msg_success':msg_success})
    
def task_perform(request):
    if request.method == 'POST':
        id = request.POST['uid']
        abc = trainer_task.objects.get(id=id)
        abc.task_progress = request.POST['sele']
        abc.save()
        msg_success = "progress added"
        return render(request,'trainer_taskgiven.html',{'msg_success':msg_success})
    else:
        pass

def tm_trainee_status(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        
        des = designation.objects.get(designation="trainee")
        var=user_registration.objects.filter(designation_id=des.id)
        return render(request, 'tm_trainee_status.html', {'mem': mem,'var':var})
    else:
        return redirect('/')
        
        

def tm_trainee_details(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        emp = request.GET.get('emp')
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'tm_trainee_details.html', {'mem': mem,'names':names,'a':a})
    else:
        return redirect('/')


def manager_trainee_status(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dep=department.objects.all()
        des = designation.objects.get(designation="trainee")
        var=user_registration.objects.filter(designation_id=des.id)
        return render(request, 'manager_trainee_status.html', {'mem': mem,'var':var,'dep':dep})
    else:
        return redirect('/')


@csrf_exempt
def manager_trainess(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        des = designation.objects.get(designation="trainee")
        Desig = user_registration.objects.filter(department_id=dept_id,designation_id=des.id)
       
        return render(request,'manager_trainess.html',{'mem': mem,'Desig': Desig, })
    else:
        return redirect('/')

@csrf_exempt
def manager_trainee_details(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        emp = request.POST['emp']
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'manager_trainee_details.html', {'mem': mem,'names':names,'a':a})
    else:
        return redirect('/')



def BRadmin_trainee_status(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dep=department.objects.all()
        des = designation.objects.get(designation="trainee")
        var=user_registration.objects.filter(designation_id=des.id)
        return render(request, 'BRadmin_trainee_status.html', {'Adm': Adm,'var':var,'dep':dep})
    else:
        return redirect('/')


@csrf_exempt
def BRadmin_trainess(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dept_id = request.GET.get('dept_id')
        des = designation.objects.get(designation="trainee")
        des1 = designation.objects.get(designation="developer")
        Desig = user_registration.objects.filter(department_id=dept_id,designation_id=des.id, status="active")
        Desig1 = user_registration.objects.filter(department_id=dept_id,designation_id=des1.id, status="active")
       
        return render(request,'BRadmin_trainess.html',{'Adm': Adm,'Desig': Desig, 'Desig1':Desig1 })
    else:
        return redirect('/')

@csrf_exempt
def BRadmin_trainee_details(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        emp = request.POST['emp']
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'BRadmin_trainee_details.html', {'Adm': Adm,'names':names,'a':a})
    else:
        return redirect('/')

def BRadmin_leavestatus(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'BRadmin_leavestatus.html',{'Adm': Adm, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')

@csrf_exempt
def BRadmin_leavedesgn(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        
        Desig = designation.objects.filter(~Q(designation="admin")).filter(branch_id=br_id.branch_id)
        return render(request,'BRadmin_leavedesgn.html',{'Adm': Adm,'Desig': Desig})
    else:
        return redirect('/')

@csrf_exempt
def BRadmin_leave_details(request):
    
    emp = request.GET.get('emp')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')
    leaves = leave.objects.filter(user_id=emp,from_date__gte=fdate,to_date__lte=tdate)
    return render(request,'BRadmin_leave_details.html',{'names':leaves})


def BRadmin_workstatus(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'BRadmin_workstatus.html',{'Adm': Adm, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')



@csrf_exempt
def BRadmin_projects_details(request):
    if 'Adm_id' in request.session:
        emp = request.POST['emp']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        names = project_taskassign.objects.filter(developer=emp,startdate__gte=fdate, enddate__lte=tdate).order_by('-id')

        tot_delay = 0
        start = datetime.strptime(fdate, '%Y-%m-%d').date()
        end = datetime.strptime(tdate, '%Y-%m-%d').date()
        pro_sub = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = False).filter(developer_id= emp, ).values('startdate','enddate','submitted_date', 'delay')
        pro_sub_false = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= emp).values('startdate','enddate')

        pro_sub_selected = project_taskassign.objects.filter(~Q(startdate__range=(start,end))).filter(enddate__range=(start,end), submitted_date__isnull = False).filter(developer_id= emp).values('startdate','enddate', 'submitted_date')
        pro_sub_selected_false = project_taskassign.objects.filter(~Q(startdate__range=(start,end))).filter(enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= emp).values('startdate','enddate')

        pro_sub_not_this =  project_taskassign.objects.filter(~Q(startdate__range=(start,end)), ~Q(enddate__range=(start,end))).filter(submitted_date__isnull = True).filter(developer_id= emp).values('startdate','enddate')
        pro_sub_sub_this =  project_taskassign.objects.filter(~Q(startdate__range=(start,end)), ~Q(enddate__range=(start,end))).filter(submitted_date__isnull = False).filter(developer_id= emp).values('startdate','enddate', 'submitted_date')
       

        for x in pro_sub:
            end_date = x['enddate']
            sub_date = x['submitted_date']
            if sub_date <= end:
                holy =  Event.objects.filter(start_time__gte=end_date,start_time__lte=sub_date).values('start_time').count()
                diff = ((sub_date - end_date ).days) - holy

                tot_delay = tot_delay + diff
            else:
                holy =  Event.objects.filter(start_time__gte=end_date,start_time__lte=end).values('start_time').count()
                diff = ((end - end_date ).days) - holy

                tot_delay = tot_delay + diff


        for x in pro_sub_false:
            end_date = x['enddate']
            if end_date <= end:
                holy =  Event.objects.filter(start_time__gte=end_date,start_time__lte=end).values('start_time').count()
                diff = ((end - end_date ).days) - holy

                tot_delay = tot_delay + diff
        
        for x in pro_sub_selected:
            end_date = x['enddate']
            sub_date = x['submitted_date']
            holy =  Event.objects.filter(start_time__gte=end_date,start_time__lte=sub_date).values('start_time').count()
            diff = ((sub_date - end_date ).days) - holy

            tot_delay = tot_delay + diff

        for x in pro_sub_selected_false:
            end_date = x['enddate']
            holy =  Event.objects.filter(start_time__gte=end_date,start_time__lte=end).values('start_time').count()
            diff = ((end - end_date ).days) - holy

            tot_delay = tot_delay + diff


        for x in pro_sub_not_this:
            end_date = x['enddate']
            if end_date <= start:
                holy =  Event.objects.filter(start_time__gte=start,start_time__lte=end).values('start_time').count()
                diff = (((end - start ).days) - holy) + 1

                tot_delay = tot_delay + diff

        

        for x in pro_sub_sub_this:
            end_date = x['enddate']
            sub_date = x['submitted_date']
            if start <= sub_date and sub_date <=end:
                holy =  Event.objects.filter(start_time__gte=start,start_time__lte=sub_date).values('start_time').count()
                diff = (((sub_date - start ).days) - holy) + 1
                tot_delay = tot_delay + diff

        a = tot_delay


        return render(request,'BRadmin_projects_details.html', {'names':names,'a':a })
    else:
        return redirect('/')







# @csrf_exempt
# def BRadmin_projects_details(request):
#     if 'Adm_id' in request.session:
#         emp = request.POST['emp']
#         fdate = request.POST['fdate']
#         tdate = request.POST['tdate']
#         names = project_taskassign.objects.filter(developer=emp,startdate__gte=fdate, enddate__lte=tdate).order_by('-id')
#         year = date.today().year
#         month = date.today().month

#         leave = project_taskassign.objects.filter(developer=emp,startdate__year__gte=year,
#                                           startdate__month__gte=month,
#                                           submitted_date__year__lte=year,
#                                           submitted_date__month__lte=month).order_by('-id')


#         start = datetime.strptime(fdate, '%Y-%m-%d').date()
#         end = datetime.strptime(tdate, '%Y-%m-%d').date()
#         pro = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = False).filter(developer_id= emp, ).values('startdate','enddate','submitted_date', 'delay')
#         pro_false = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= emp).values('startdate','enddate')
#         tot = 0
#         tot1 = 0
#         xx=0
#         xx1 = 0
#         for i in pro:
#             d_end = (i['enddate'])
#             d_submitted = (i['submitted_date'])
#             differ = (d_submitted - d_end).days
#             if differ == 0:
#                 tot=0
#             else:

#                 if d_submitted <= end:
#                     diff = (d_submitted - d_end).days
#                     cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=d_submitted).values('start_time').count()
#                     xx = diff - cnt
#                 else:
#                     diff = (end - d_end).days
#                     cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
#                     xx = diff - cnt
#             tot = tot + xx
                

#         for x in pro_false:
#             d_end = (x['enddate'])
#             diff =  (end - d_end).days
#             if diff <= 0:
#                 tot1=0
#             cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
#             xx1 = diff- cnt
#             tot1 = tot1 + xx1

#         a = tot + tot1


#         return render(request,'BRadmin_projects_details.html', {'names':names,'a':a })
#     else:
#         return redirect('/')
#---------------------PM updates------------------------------------------------

def pm_projectcards(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'pm_projectcards.html',{'pro':pro})
    else:
        return redirect('/')

def pm_createmodule(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        project_data = project.objects.filter(projectmanager_id=prid)
        # return render(request, 'pm_createmodule.html',{'pro':pro,'project_data':project_data})
        
        if request.method =='POST':
            var = project_module_assign()
            var.project_name = project.objects.get(id=int(request.POST['project_id']))
            var.module = request.POST['module']
            var.description = request.POST['moduledescription']
            var.save()
            msg_success = "Module created"
            return render(request, 'pm_createmodule.html',{'pro':pro,'project_data':project_data,'msg_success':msg_success})
        return render(request, 'pm_createmodule.html',{'pro':pro,'project_data':project_data})
    else:
        return redirect('/')


def pm_createother(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        project_data = project.objects.filter(projectmanager_id=prid)
       
        
        if request.method =='POST':
            var = project_other_assign()
            var.othproject_name = project.objects.get(id=int(request.POST['project_id']))
            var.other_name = request.POST['other']
            var.other_description = request.POST['otherdescription']
            var.save()
            msg_success = "Other Details created"
            return render(request, 'pm_createother.html',{'pro':pro,'project_data':project_data,'msg_success':msg_success})
        return render(request, 'pm_createother.html',{'pro':pro,'project_data':project_data})
    else:
        return redirect('/')


def pm_createtable(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        project_data = project.objects.filter(projectmanager_id = prid)
        var = project_table()
        if request.method == 'POST':
            var.project = project.objects.get(id=int(request.POST['project']))
            var.module_name_id = request.POST['emp']
            var.description = request.POST['table']
            var.save()
            msg_success = "table created"
            return render(request, 'pm_createtables.html',{'pro':pro,'project_data':project_data,'msg_success':msg_success})
        return render(request, 'pm_createtables.html',{'pro':pro,'project_data':project_data})
    else:
        return redirect('/')

@csrf_exempt
def pm_module_data(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('dept_id')
        Desig = project_module_assign.objects.filter(project_name=pro_id)
        
        return render(request,'pm_module_data.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')

def pm_projectview(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_data = project.objects.filter(projectmanager_id=prid)
        return render(request,'pm_projectview.html',{'pro': pro,'pro_data':pro_data})
    else:
        return redirect('/')

def pm_prodata(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_data = project.objects.get(id=id)
        return render(request,'pm_prodata.html',{'pro': pro,'pro_data':pro_data})
    else:
        return redirect('/')

def pm_project_assigned(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_data = project.objects.get (id = id)
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        user = user_registration.objects.all()
        com = project.objects.filter(status = "completed")
        return render(request,'pm_project_assigned.html',{'pro': pro,'pro_data':pro_data,'display':display,'user':user,'com':com})
    else:
        return redirect('/')
#-------------------------------TM ------------------------------------------------
def trainer_progress_add(request,id):
    mem = user_registration.objects.get(id=id)
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametm2)
        var = user_registration.objects.get(id=id)
        if request.method == 'POST':
            var.attitude = request.POST['sele1']
            var.creativity = request.POST['sele2']
            var.workperformance = request.POST['sele3']
            var.save()
            msg_success = "progress added"
            return render(request, 'trainer_progress_add.html', {'mem': mem,'msg_success':msg_success})
        return render(request, 'trainer_progress_add.html', {'mem': mem})
    else:
        return redirect('/')

#-----------------------------------tester-----------------------------

def tester_leave(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid = request.session['usernametsid']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(id=usernametsid)
        return render(request, 'tester_leave.html', {'mem': mem})
    else:
        return redirect('/')

def tester_apply_leave(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid = request.session['usernametsid']
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernamets).filter(id=usernametsid)
        if request.method == 'POST':
            apply_leave = leave()
            apply_leave.from_date = request.POST['from']
            apply_leave.to_date = request.POST['to']
            apply_leave.leave_status = request.POST['haful']
            apply_leave.reason = request.POST['reason']
            apply_leave.user =user_registration.objects.get(id=usernametsid)
            apply_leave.designation_id =usernamets
            apply_leave.leaveapprovedstatus = 0
            
            start = datetime.strptime(apply_leave.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(apply_leave.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                apply_leave.days = 1
            else:
                apply_leave.days = diff - cnt
                
                
            apply_leave.save()
            msg_success = "leave applied"
            return render(request, 'tester_apply_leave.html',{'mem':mem,"msg_success":msg_success})
        else:
            pass
        return render(request, 'tester_apply_leave.html',{'mem':mem})
    else:
        return redirect('/')

def tester_appliedleave(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        hr_leave = leave.objects.filter(user=usernametsid).order_by('-id')
        return render(request, 'tester_appliedleave.html', {'mem': mem,'hr':hr_leave})
    else:
        return redirect('/')

def tester_employees(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        return render(request, 'tester_employees.html', {'mem': mem})
    else:
        return redirect('/')

def tester_tllist(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        p = designation.objects.get(designation="team leader")
        tlfil = user_registration.objects.filter(designation_id=p.id,status="active").order_by("-id")
        return render(request, 'tester_tllist.html', {'mem': mem,'tlfil':tlfil})
    else:
        return redirect('/')

def tester_tldashboard(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        tls = user_registration.objects.filter(id=id) 
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'tester_tldashboard.html',{'labels':labels,'data':data,'mem': mem, 'tls': tls})
    else:
        return redirect('/') 

def ts_ltteaminvolved(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        pri = project_taskassign.objects.filter(developer_id=id).order_by("-id")
        return render(request, 'ts_ltteaminvolved.html',{'mem': mem, 'pri': pri})
    else:
        return redirect('/') 

def tl_currentperformance(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        mem1 = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem1.attitude = request.POST['sele1']
            mem1.creativity = request.POST['sele2']
            mem1.workperformance = request.POST['sele3']
            mem1.save()
            msg_success="performance added"
            return render(request, 'tl_currentperformanace.html',{'mem': mem,'mem1':mem1,'msg_success':msg_success})
        return render(request, 'tl_currentperformanace.html',{'mem': mem,'mem1':mem1})
    else:
        return redirect('/')

def ts_allocatetl(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        des_tl = designation.objects.get(designation = "team leader")
        des_dev = designation.objects.get(designation = "developer ")
        devs = user_registration.objects.filter(designation_id=des_dev.id,status="active")
        tls = user_registration.objects.filter(designation_id=des_tl.id,status="active")
        tl_name = user_registration.objects.all()
        if request.method == "POST":
            emp_id = request.POST.get('id')
            tl_id = request.POST.get('team')
            alocate = user_registration.objects.get(id=emp_id)
            alocate.tl_id = tl_id
            alocate.save()
            msg_success="tl added"
            return render(request, 'ts_allocatetl.html',{'mem': mem,'devs':devs,'tls':tls,'tl_name':tl_name,'msg_success':msg_success})
        return render(request, 'ts_allocatetl.html',{'mem': mem,'devs':devs,'tls':tls,'tl_name':tl_name})
    else:
        return redirect('/')

def ts_tl_attandance(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        man = attendance.objects.filter(user_id=id) 
        return render(request, 'ts_tl_attandance.html',{'mem': mem,'man':man})
    else:
        return redirect('/')

def ts_tl_attendance(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        man = user_registration.objects.get(id=id)  
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id)
            return render(request, 'ts_tl_attandance.html',{'mem': mem,'man':man,'mem1':mem1}) 
        return render(request, 'ts_tl_attendance.html',{'mem': mem,'man':man})
    else:
        return redirect('/')

def ts_dev_team(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        teamid = user_registration.objects.filter(tl_id=id,status="active").order_by("-id") 
        return render(request, 'ts_dev_team.html',{'mem': mem,'teamid': teamid})
    else:
        return redirect('/')  

def ts_dev_team_profile(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid) 
        ind = user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'ts_dev_team_profile.html',{'mem': mem,'ind': ind,'labels':labels,'data':data})
    else:
        return redirect('/')  

def ts_tl_dev_teaminvolved(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        pri = project_taskassign.objects.filter(developer_id=id).order_by("-id")
        return render(request, 'ts_tl_dev_teaminvolved.html',{'mem': mem, 'pri': pri})
    else:
        return redirect('/')

def ts_Devlists(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        pro_dep = user_registration.objects.get(id=usernametsid)
        des_id = designation.objects.get(designation="developer")
        man = user_registration.objects.filter(designation_id=des_id.id).filter(department_id=pro_dep.department_id,status="active").order_by("-id")
        return render(request, 'ts_Devlists.html',{'mem':mem,'man':man})
    else:
        return redirect('/')

def ts_DevDashboard(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        man = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'ts_DevDashboard.html',{'labels':labels,'data':data,'mem':mem,'man':man})
    else:
        return redirect('/')

#-----------------pm_attendence-----------------------
def projectman_search(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation = "team leader")
        des1 = designation.objects.get(designation = "tester")
        x = des.id
        x1 = des1.id
        tl_data = user_registration.objects.filter(Q(designation_id = x,status = 'active'))
        
        return render(request, 'projectman_search.html', {'pro': pro,'tl_data':tl_data})
    else:
        return redirect('/')

@csrf_exempt
def pm_employees_att(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('dept_id')
        Desig = user_registration.objects.get(id=pro_id)
        return render(request,'pm_employees_att.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')


def pm_attendanceview(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        project_data = designation.objects.filter(Q(designation = "developer")|Q (designation="team leader"))
        return render(request, 'pm_attendanceview.html',{'pro':pro,'project_data':project_data})
    else:
        return redirect('/')

@csrf_exempt
def pm_employeelist(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('dept_id')

        Desig = user_registration.objects.filter(designation_id=pro_id,status = "active")
        
        return render(request,'pm_employeelist.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')

@csrf_exempt
def pm_employees_attendance_view(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('des_id')
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        
        Desig = attendance.objects.filter(date__gte=from_date,date__lte=to_date, user_id= pro_id).order_by('-id')
        return render(request,'pm_employees_attendance_view.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')

def tl_attendanceview(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        Desig = attendance.objects.filter(user_id = tlid).order_by('-id')
        return render(request,'tl_attendanceview.html',{'mem': mem,'Desig': Desig})
    else:
        return redirect('/')

def tl_devattendsearch(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        des = designation.objects.get(designation = "developer")
        x = des.id
        tl_data = user_registration.objects.filter(designation_id = x,status = 'active',tl_id=tlid)
        return render(request,'tl_devattendsearch.html',{'mem': mem,'tl_data': tl_data})
    else:
        return redirect('/')
@csrf_exempt
def tl_devattendanceview(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        pro_id = request.GET.get('dept_id')
        x=int(pro_id)
        
        
        Desig = attendance.objects.filter(user_id= x).order_by('-id')
        
        return render(request,'tl_devattendenceview.html',{'mem': mem,'Desig':Desig})
    else:
        return redirect('/')

def tl_devattendanceadd(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        des = designation.objects.get(designation = "developer")
        x = des.id
        tl_data = user_registration.objects.filter(designation_id = x,status = 'active',tl_id=tlid)
        return render(request,'tl_devattendanceadd.html',{'mem': mem,'tl_data': tl_data})
    else:
        return redirect('/')

@csrf_exempt
def tl_employees_att(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        pro_id = request.GET.get('dept_id')
        Desig = user_registration.objects.get(id=pro_id)
        return render(request,'tl_employees_att.html',{'mem': mem,'Desig': Desig})
    else:
        return redirect('/')

def tl_add_attendance(request,id):
    if request.method == 'POST':
        var=attendance()
        var.date=request.POST['date']
        var.user = user_registration.objects.get(id=id)
        var.attendance_status = request.POST['pres']
        var.save()
        msg_success = "attendance added"
        return render(request,'tl_devattendanceadd.html',{'msg_success':msg_success})
    else:
        pass

def pm_add_attendance(request,id):
    if request.method == 'POST':
        var=attendance()
        var.date=request.POST['date']
        var.user = user_registration.objects.get(id=id)
        var.attendance_status = request.POST['pres']
        var.save()
        msg_success = "attendance added"
        return render(request,'projectman_search.html',{'msg_success':msg_success})
    else:
        pass

def current_modules(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        data = project_module_assign.objects.filter(project_name=id)
        tab = project_table.objects.filter(project=id)
        other = project_other_assign.objects.filter(othproject_name=id)
        devtab = ProjectDocModels.objects.filter(doc_project_md_id=id)
        devview = ProjectDocViews.objects.filter(doc_project_v=id)
        devlb = ProjectDoclibraryies.objects.filter(doc_project_lb=id)
        devoth = ProjectDocother.objects.filter(doc_project_oth=id)
        devpage = ProjectDochtmlpages.objects.filter(doc_project_hp=id)
        return render(request,'current_modules.html',{'pro': pro,'data': data,'tab':tab,'other':other,
        'devtab':devtab,'devview':devview,'devlb':devlb,'devoth':devoth,'devpage':devpage})
    else:
        return redirect('/')
        
        
        
# @csrf_exempt
# def accounts_salary_leave(request):
#         fdate = request.GET.get('fdate')
#         tdate = request.GET.get('tdate')
#         his_id = request.GET.get('his_id')
#         global k1
#         global d14
#         global d13,d15,d16,d17,d18,d19,d20,d21
#         try:
#             date_exe = acnt_monthdays.objects.get(month_fromdate__gte=fdate,month_todate__lte=tdate)
#             if date_exe:
#                 work_day = date_exe.month_workingdays
#                 start = datetime.strptime(fdate, '%Y-%m-%d').date()
#                 end = datetime.strptime(tdate, '%Y-%m-%d').date()
#                 pro = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= his_id, ).values('startdate','enddate')
#                 pro_start = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end),submitted_date__isnull = False).filter(developer_id= his_id, ).values('startdate','enddate','submitted_date')
                
                
#                 leave_emp = leave.objects.filter(user_id = his_id,from_date__gte = start,to_date__lte = end).values('from_date','to_date')
#                 k1=0
#                 for k in leave_emp:
#                     k2 = (k['to_date']-k['from_date']).days
#                     if k2 == 0:
#                         k2 = 1
#                     k1 = k1 + k2
                
#                 d14 =0
#                 d21 = 0
#                 d17 = 0
#                 d20 = 0
#                 for i in pro:
#                     d_start = (i['startdate'])
#                     d_end = (i['enddate'])
#                     if d_start == d_end:
                       
#                         d14 = 0
#                     else :

#                         diff = (end - d_end).days
#                         cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
#                         d14 = diff - cnt
                    
#                     d20 = d20 + d14
                
                
#                 d18 = 0
#                 d19 = 0
#                 for i in pro_start:
#                     d10 = (i['enddate'])
#                     d11 = (i['submitted_date'])
#                     diff_date = (d11 - d10).days
#                     if diff_date <= 0:
#                         d18 = 0
#                     else:
                        
#                         if d11 <= end:
#                             diff = (d11 - d10).days
                            
#                             cnt =  Event.objects.filter(start_time__gte=d10,start_time__lte=d11).values('start_time').count()
#                             d18 = diff - cnt
                            
#                         else:
#                             diff = (end - d10).days
#                             cnt =  Event.objects.filter(start_time__gte=d10,start_time__lte=end).values('start_time').count()
#                             d18 = diff - cnt
                            
#                     d19 = d19 + d18
                    
                  
                  
#                 delay_total = d19+d20 
#                 total_delay =delay_total+k1
#                 conf = user_registration.objects.get(id=his_id)
#                 conf_salary = conf.confirm_salary
#                 if conf_salary == "":
#                     conf_salary = 0
#                 one_day_sal = int(conf_salary) / int(work_day)
#                 total_delay_amt = float(one_day_sal) * float(total_delay)
#                 net_salary = float(conf_salary) - float(total_delay_amt)
#                 if net_salary <= 0:
#                     net_salary = 0
#                 return HttpResponse(json.dumps({'net_salary':net_salary, 'delay_total':delay_total,'k1':k1,'work_day':work_day,'conf_salary':conf_salary}))
#             else:
#                 msg = "please add month days"
#                 return HttpResponse(json.dumps({'msg':msg}))
#         except acnt_monthdays.DoesNotExist:
#             msg = "please add month days"
#             return HttpResponse(json.dumps({'msg':msg}))


@csrf_exempt
def accounts_salary_leave(request):
        fdate = request.GET.get('fdate')
        tdate = request.GET.get('tdate')
        his_id = request.GET.get('his_id')
        global k1
        global d14
        global d13,d15,d16,d17,d18,d19,d20,d21
        try:
            date_exe = acnt_monthdays.objects.get(month_fromdate__gte=fdate,month_todate__lte=tdate)
            if date_exe:
                work_day = date_exe.month_workingdays
                start = datetime.strptime(fdate, '%Y-%m-%d').date()
                end = datetime.strptime(tdate, '%Y-%m-%d').date()



                pre_current = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= his_id).values('startdate','enddate')
                pre_start_current = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end)).filter(submitted_date__range=(start,end)).filter(developer_id= his_id).values('startdate','enddate','submitted_date')
                pre_start_current_sub_other = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end)).filter(~Q(submitted_date__range=(start,end))).filter(developer_id= his_id).values('startdate','enddate','submitted_date')
                pre_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start,end))).filter(enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= his_id).values('startdate','enddate')
                pre_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start,end))).filter(enddate__range=(start,end)).filter(submitted_date__range=(start,end)).filter(developer_id= his_id).values('startdate','enddate','submitted_date')

            
                pre_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start,end)), ~Q(enddate__range=(start,end))).filter(submitted_date__range=(start,end)).filter(developer_id= his_id).values('submitted_date')
                pre_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start,end)), ~Q(enddate__range=(start,end)),submitted_date__isnull = True).filter(developer_id= his_id).values('startdate','enddate')
                
                
                leave_emp = leave.objects.filter(user_id = his_id,from_date__gte = start,to_date__lte = end).values('from_date','to_date')
                k1=0
                for k in leave_emp:
                    k2 = (k['to_date']-k['from_date']).days
                    if k2 == 0:
                        k2 = 1
                    k1 = k1 + k2
                
                d14 =0
                d21 = 0
                d17 = 0
                d20 = 0

                prev_current_delay = 0
                prev_current_delay = 0

                print("From date and to date are in previous month it does not have submission date  :", pre_current.count())
                for pre_current in pre_current:
                    end_date =  (pre_current['enddate'])
                    holy = Event.objects.filter(start_time__range=(end_date,end)).count()
                    delay_days = (end - end_date).days
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay +  work_days

            

                print("From date and to date are in previous month it does have submission date :", pre_start_current.count())
                for pre_start_current in pre_start_current:
                    end_date =  (pre_start_current['enddate'])
                    submitted_date =  (pre_start_current['submitted_date'])

                    if submitted_date <= end_date:
                        work_days = 0
                        prev_current_delay = prev_current_delay +  work_days
                    else:
                        holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                        delay_days = (submitted_date - end_date).days
                        work_days = delay_days - holy
                        
                        prev_current_delay = prev_current_delay +  work_days

                print("Start and End date seleted month it does have submission date other month :", pre_start_current_sub_other.count())
                for pre_start_current_sub_other in pre_start_current_sub_other:
                    end_date =  (pre_start_current_sub_other['enddate'])
                    submission_date = (pre_start_current_sub_other['submitted_date'])
                    if submission_date is not None:
                        if end < submission_date:

                            holy = Event.objects.filter(start_time__range=(end_date,end)).count()
                            delay_days = (end - end_date).days
                            work_days = delay_days - holy

                            prev_current_delay = prev_current_delay +  work_days

                print("End date previous month it does not have submission date  :", pre_current_sub.count())
                for pre_current_sub in pre_current_sub:
                    end_date =  (pre_current_sub['enddate'])
                    holy = Event.objects.filter(start_time__range=(end_date,end)).count()
                    delay_days = (end - end_date).days
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay +  work_days

                

                    
                    
                print("End date previous month it have submission date is previous month :", pre_start_current_sub.count())
                for pre_start_current_sub in pre_start_current_sub:
                    end_date =  (pre_start_current_sub['enddate'])
                    submitted_date =  (pre_start_current_sub['submitted_date'])

                    if submitted_date <= end_date:
                        work_days = 0
                        prev_current_delay = prev_current_delay +  work_days
                    else:
                        holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                        delay_days = (submitted_date - end_date).days
                        work_days = delay_days - holy

                        prev_current_delay = prev_current_delay +  work_days

                    


                print("End date and start date not in previous month but submission date in previous month :", pre_this_month_have_submission.count())
                for pre_this_month_have_submission in pre_this_month_have_submission:
                    submitted_date =  (pre_this_month_have_submission['submitted_date'])
                    if start <= submitted_date:

                        holy = Event.objects.filter(start_time__range=(start,submitted_date )).count()
                        delay_days = (submitted_date - start).days + 1
                        work_days = delay_days - holy

                        prev_current_delay = prev_current_delay + work_days


            


                print("From date and to date are not in previous month it does not have submission date :", pre_this_month_have_not_submission.count())
                for pre_this_month_have_not_submission in pre_this_month_have_not_submission:
                    end_date = (pre_this_month_have_not_submission['enddate'])

                    if end_date <= end:

                        holy = Event.objects.filter(start_time__range=(start,end)).count()
                        delay_days = (start - end).days  + 1
                        work_days = delay_days - holy

                        prev_current_delay = prev_current_delay + work_days

                print("prev_current_delay", prev_current_delay)
                delay_total = prev_current_delay 
                total_delay =delay_total
                conf = user_registration.objects.get(id=his_id)
                conf_salary = conf.confirm_salary
                if conf_salary == "":
                    conf_salary = 0
                one_day_sal = int(conf_salary) / int(work_day)
                total_delay_amt = float(one_day_sal) * float(total_delay)
                net_salary = float(conf_salary) - float(total_delay_amt)
                if net_salary <= 0:
                    net_salary = 0
                return HttpResponse(json.dumps({'net_salary':net_salary, 'delay_total':delay_total,'k1':k1,'work_day':work_day,'conf_salary':conf_salary}))
            else:
                msg = "please add month days"
                return HttpResponse(json.dumps({'msg':msg}))
        except acnt_monthdays.DoesNotExist:
            msg = "please add month days"
            return HttpResponse(json.dumps({'msg':msg}))
            
            

# account payment head page
def accounts_paymenthead(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request, 'account_paymenthead.html', {'z': z})
    else:
        return redirect('/')

# add account payment head
def accounts_addpaymenthead(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        if request.method == "POST":
            pay_table = payment_head()
            pay_table.payment_head = request.POST.get('paymenthead')
            pay_table.description_paymenthead = request.POST.get('description')
            pay_table.save()
            msg_success = "paymenthead successfully created"
            return render(request, 'accounts_addpaymenthead.html', {'z': z, 'msg_success':msg_success})
        else:
            return render(request, 'accounts_addpaymenthead.html', {'z': z})
    else:
        return redirect('/')


# view account payment head
def accounts_viewpaymenthead(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = payment_head.objects.all().order_by('-id')
        if request.method == "POST":
            uid = request.POST.get('paymenthead')
            ext = payment_head.objects.get(id=uid)
            ext.delete()
            msg_success = "paymenthead deleted successfully"
            return render(request, 'accounts_viewpaymenthead.html', {'z': z, 'msg_success':msg_success})
        else:
            return render(request, 'accounts_viewpaymenthead.html', {'z': z, 'vars':vars})
    else:
        return redirect('/')

#  account income page
def accounts_income(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request, 'accounts_income.html', {'z': z})
    else:
        return redirect('/')

# add account income
def accounts_addincome(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        dep = department.objects.all()
        pay_head = payment_head.objects.all()
        if request.method == "POST":
            income_tab = income()
            income_tab.pay_date = request.POST.get('paydate')
            income_tab.party_name = request.POST.get('pay_name')
            income_tab.amount = request.POST.get('pay_amount')
            income_tab.pay_method = request.POST.get('pay_method')
            income_tab.pay_description = request.POST.get('pay_description')
            income_tab.department_id = request.POST.get('pay_department')
            income_tab.payment_head_id = request.POST.get('pay_type')
            income_tab.save()
            msg_success = "Income added successfully"
            return render(request, 'accounts_addincome.html', {'z': z, 'msg_success':msg_success})

        return render(request, 'accounts_addincome.html', {'z': z, 'pay_head':pay_head,'dep':dep })
    else:
        return redirect('/')

def accounts_updateincome(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        dep = department.objects.all()
        pay_head = payment_head.objects.all()
        income_tab = income.objects.get(id =id)
        if request.method == "POST":
            income_tab = income.objects.get(id =id)
            income_tab.pay_date = request.POST.get('paydate')
            income_tab.party_name = request.POST.get('pay_name')
            income_tab.amount = request.POST.get('pay_amount')
            income_tab.pay_method = request.POST.get('pay_method')
            income_tab.pay_description = request.POST.get('pay_description')
            income_tab.department_id = request.POST.get('pay_department')
            income_tab.payment_head_id = request.POST.get('pay_type')
            income_tab.save()
            msg_success = "Income Update successfully"
            return render(request, 'accounts_updateincome.html', {'z': z, 'msg_success':msg_success})
        else:
            return render(request, 'accounts_updateincome.html', {'z': z, 'pay_head':pay_head,'dep':dep,'income_tab':income_tab })
    else:
        return redirect('/')


# add account view all income
def accounts_viewallincome(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        if request.method == "POST":
            delete_id = request.POST.get('paymenthead')
            del_data = income.objects.get(id=delete_id)
            del_data.delete()
            msg_success = "Income deleted successfully"
            return render(request, 'accounts_viewallincome.html', {'z': z, 'msg_success':msg_success})

        inc = income.objects.all().order_by('-id')
        return render(request, 'accounts_viewallincome.html', {'z': z, 'inc':inc})
    else:
        return redirect('/')



# add account filter income
def accounts_filterincome(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        dep = department.objects.all()
        return render(request, 'accounts_filterincome.html', {'z': z, 'dep':dep})
    else:
        return redirect('/')



# add account filter income ajax
def accounts_filterincome_ajax(request):

        dept_id = request.GET.get('dept_id')
        fdate = request.GET.get('fdate')
        tdate = request.GET.get('tdate')

        start = datetime.strptime(fdate, '%Y-%m-%d').date()
        end = datetime.strptime(tdate, '%Y-%m-%d').date()
        inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id)
        
        
        tot = 0
        tot_inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id).values('amount')
        for x in tot_inc:
            tot = tot + int(x['amount'])

        return render(request, 'accounts_filterincome_ajax.html', {'inc':inc,'tot':tot })




# Bradmin_income
def BRadmin_income(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        inc_cont = income.objects.filter(pay_status=0).count()
        return render(request, 'BRadmin_income.html', {'Adm': Adm, 'inc_cont':inc_cont})
    else:
        return redirect('/')


# Bradmin view all income
def BRadmin_viewallincome(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        inc = income.objects.all().order_by('-id')
        return render(request, 'BRadmin_viewallincome.html', {'Adm': Adm, 'inc':inc})
    else:
        return redirect('/')


# Bradmin view all pending income
def BRadmin_pendingincome(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        if request.method=="POST":
            uid = request.POST.get('pay_verify')
            inc = income.objects.get(id=uid)
            inc.pay_status = 1
            inc.save()
            msg_success = "Payment verified"
            return render(request, 'accounts_viewpaymenthead.html', {'Adm': Adm, 'msg_success':msg_success})
            
        else:
            inc = income.objects.filter(pay_status=0)
            return render(request, 'BRadmin_pendingincome.html', {'Adm': Adm, 'inc':inc})
    else:
        return redirect('/')


# Bradmin search income
def BRadmin_searchincome(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dep = department.objects.all()
        return render(request, 'BRadmin_searchincome.html', {'Adm': Adm, 'dep':dep})
    else:
        return redirect('/')



# add account filter income ajax
def BRadmin_filterincome_ajax(request):
    dept_id = request.GET.get('dept_id')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')

    start = datetime.strptime(fdate, '%Y-%m-%d').date()
    end = datetime.strptime(tdate, '%Y-%m-%d').date()
    inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id)
    
    
    tot = 0
    tot_inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id).values('amount')
    for x in tot_inc:
        tot = tot + int(x['amount'])

    return render(request, 'BRadmin_searchincome_ajax.html', {'inc':inc,'tot':tot })


# accounts main expences
def accounts_mainexpenses(request):

    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        return render(request, 'accounts_mainexpenses.html', {'z': z})
    else:
        return redirect('/')



# add account filter income
def accounts_salaryexpense(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        dep = department.objects.all()
        return render(request, 'accounts_salaryexpense.html', {'z': z, 'dep':dep})
    else:
        return redirect('/')


def accounts_salaryexpense_ajax(request):

    dept_id = request.GET.get('dept_id')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')

    start = datetime.strptime(fdate, '%Y-%m-%d').date()
    end = datetime.strptime(tdate, '%Y-%m-%d').date()

    inc = acntspayslip.objects.filter(fromdate__range=(start,end)).filter(department_id=dept_id)
    
    
    conf = 0
    net_sal = 0
    tot_sum = 0
    tot_inc = acntspayslip.objects.filter(fromdate__range=(start,end)).filter(department_id=dept_id).values('basic_salary','net_salary','hra','incentives', 'conveyns', 'other_allovance')
    for x in tot_inc:
        conf = conf + int(x['basic_salary']) + int(x['hra']) + int(x['other_allovance']) + int(x['conveyns'])
        net_sal = net_sal + int(x['net_salary'])
        
    tot_sum = conf - net_sal

    return render(request, 'accounts_salaryexpense_ajax.html', {'inc':inc,'conf':conf, 'net_sal':net_sal, 'tot_sum':tot_sum })




# BRadmin main expences
def BRadmin_mainexpenses(request):

    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')

        Adm = user_registration.objects.filter(id=Adm_id)
        
        return render(request, 'BRadmin_mainexpenses.html', {'Adm': Adm})
    else:
        return redirect('/')



# BRadmin filter income
def BRadmin_salaryexpense(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')

        Adm = user_registration.objects.filter(id=Adm_id)
        
        dep = department.objects.all()
        return render(request, 'BRadmin_salaryexpense.html', {'Adm': Adm, 'dep':dep})
    else:
        return redirect('/')



def verify_all_income(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        ver = income.objects.filter(pay_status=0).update(pay_status=1)

        msg_success = "verify All Income successfully"
        return render(request, 'BRadmin_pendingincome.html', {'Adm': Adm, 'msg_success':msg_success})
    else:
        return redirect('/')


#Team leader view developers list
def TL_dev(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        man = user_registration.objects.filter(tl_id=tlid, status="active")
        return render(request, 'TL_dev.html', { 'mem': mem, 'man': man})
    else:
        return redirect('/')


#Team leader view indivigual developers 
def Teamdevelopers_dashboard(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        man = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'TL_dev_dashboard.html',{'labels':labels,'data':data,'mem':mem,'man':man})
    else:
        return redirect('/')

#Team leader add indivigual performance of a developers 
def TL_add_dev_performance(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        man = user_registration.objects.get(id=id)
        if request.method == 'POST':
            man.attitude = request.POST['sele1']
            man.creativity = request.POST['sele2']
            man.workperformance = request.POST['sele3']
            man.save()
            msg_success = "Performance added successfully"
            
            return render(request, 'TL_add_dev_performance.html', {'mem': mem, 'man':man, 'msg_success':msg_success})
        else:
            return render(request, 'TL_add_dev_performance.html',{'mem':mem,'man':man})
    else:
        return redirect('/')



# Training manager Leave status
def tm_leave_status(request):
    if 'usernametm2' in request.session:

        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']

        mem = user_registration.objects.filter(id=usernametm2)
        dept  = user_registration.objects.get(id=usernametm2)

        dep = department.objects.filter(id=dept.department_id)
        des = designation.objects.all()
        return render(request, 'tm_leave_status.html', {'mem': mem, 'dep':dep,'des':des})
    else:
        return redirect('/')


@csrf_exempt
def tm_designation(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametm2)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="manager"),~Q(designation="project manager"),~Q(designation="trainingmanager"),~Q(designation="developer"),~Q(designation="team leader"),~Q(designation="tester"),~Q(designation="account"), ~Q(designation="hr")).filter(branch_id=br_id.branch_id)
        return render(request,'tm_designation.html',{'mem':mem,'Desig': Desig, })
    else:
        return redirect('/')


@csrf_exempt
def tm_emp_ajax(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametm2)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        Desig = user_registration.objects.filter(department_id=dept_id, designation_id=desigId, status="active")

        return render(request,'tm_emp_ajax.html',{'mem':mem,'Desig': Desig,})
    else:
        return redirect('/')


@csrf_exempt
def tm_leave(request):
    
    emp = request.GET.get('emp')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')
    leaves = leave.objects.filter(user_id=emp,from_date__gte=fdate,to_date__lte=tdate)
    return render(request,'tm_leave.html', {'names':leaves})
    
#**********************Developer section new edit(10-09-2022)******* 

def DEVwork(request,id):
    if request.method == 'POST':
        new = project_taskassign.objects.get(id=id)
        new.workaccept = request.FILES['work']
       
        new.save()
        return redirect("DEVprojects")
        
#**********************TL section new edit(10-09-2022)******* 

def TLwork(request,id):
    if request.method == "POST":
        n = project_taskassign.objects.get(id=id)
        n.workaccept = request.FILES['work']
        n.save()
        return redirect("TLprojects")
        
#**********************Manager section new edit(10-09-2022)*******

def MAN_project_dept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.all()
        depart = department.objects.all()
        return render(request, 'MAN_project_dept.html', {'proj_det': project_details, 'department': depart, 'mem': mem})
    else:
        return redirect('/')

def MAN_project_list(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.filter(
            ~Q(status='Rejected'), department_id=id).order_by('-id')
        return render(request, 'MAN_project_list.html', {'proj_det': project_details, 'mem': mem})
    else:
        return redirect('/')


def MAN_project_table(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        des = designation.objects.get(designation="team leader")
        dev = designation.objects.get(designation="developer")
        var = project_taskassign.objects.filter(
            project_id=id).order_by('-id')
        data = test_status.objects.filter(project_id=id).order_by('-id')
        data1 = tester_status.objects.filter(project_id=id).order_by('-id')
        newdata = project_taskassign.objects.filter(
            project_id=id, subtask__isnull=False).order_by('-id')
        return render(request, 'MAN_project_table.html', {'mem': mem, 'var': var, 'data': data, 'data1': data1, 'newdata': newdata})
    else:
        return redirect('/')



##########################################################################################################

#********************************* Digital marketing - (15/10/22-shebin shaji) *********************#
def dmmanagerlogout(request):
    if 'pm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def dm_pmdashboard(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        try:
            desig=designation.objects.get(designation='Digital Developer')
            dmdeveloper=user_registration.objects.filter(designation=desig).count()
        except designation.DoesNotExist:
            desig=None
            dmdeveloper=None
        try:
            num1=DM_projects.objects.filter(dm_project_categ='In House Project').count()
        except DM_projects.DoesNotExist:
            num1=None
        try:
            num2=DM_projects.objects.filter(dm_project_categ='Client Project').count()
        except DM_projects.DoesNotExist:
            num2=None

       
        return render(request, 'DigitalMarketing/DM_projectmanager_dashboard.html', {'mem': mem,'dmdeveloper':dmdeveloper,'num1':num1,'num2':num2})
    else:
        return redirect('/')
    

def DM_project_works(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        desig=designation.objects.get(designation='Digital Developer')
        dmdeveloper=user_registration.objects.filter(designation=desig)
        projects=DM_projects.objects.filter(dm_project_status='Work Started')
        return render(request, 'DigitalMarketing/DM_project_work.html', {'mem': mem,'dmdeveloper':dmdeveloper,'projects':projects})
    else:
        return redirect('/')
    

def DM_inhouseproject(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        projects=DM_projects.objects.filter(dm_project_categ='In House Project').order_by('-id')
        pr_task=DM_project_dese.objects.all()
        prj=DM_projects.objects.all()
        return render(request, 'DigitalMarketing/DM_Inhouseproject.html', {'mem': mem,'projects':projects,'pr_task':pr_task,'prj':prj})
    else:
        return redirect('/')

    
def DM_Clientproject(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        projects=DM_projects.objects.filter(dm_project_categ='Client Project').order_by('-id')
        pr_task=DM_project_dese.objects.all()
        prj=DM_projects.objects.all()
        return render(request, 'DigitalMarketing/DM_clientproject.html', {'mem': mem,'projects':projects,'pr_task':pr_task,'prj':prj})
    else:
        return redirect('/')

    
def DM_project_save(request,project_save):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)

        if request.method == 'POST':
            project = request.POST['pro_name']

        if project_save == 0:
            projects=DM_projects(dm_project_name=project,dm_project_categ='In House Project')
            projects.save()
            return redirect('DM_inhouseproject')
        
        elif project_save == 1:
            projects=DM_projects(dm_project_name=project,dm_project_categ='Client Project')
            projects.save()
            return redirect('DM_Clientproject')
    else:
        return redirect('/')


def DM_ptoject_dese_add(request,prj_dese_id):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        projects=DM_projects(id=prj_dese_id)

        if request.method == 'POST':
            task_dese = request.POST['prj_taskdese']


           
            print()
            prj_task_des=DM_project_dese(dm_task_dese=task_dese,dm_task_project_id=projects)
            prj_task_des.save()
                
            if projects.dm_project_categ == 'In House Project':
                return redirect('DM_inhouseproject')
            else:
                return redirect('DM_Clientproject')
        else:
            pr_task=DM_project_dese.objects.filter(dm_task_project_id=projects).order_by('-id')
            return render(request, 'DigitalMarketing/DM_project_tash_dese.html',{'mem': mem,'projects':projects,'pr_task':pr_task})


    else:
        return redirect('/')





    

def DM_empolyees(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        desig=designation.objects.get(designation='Digital Developer')
        dmdeveloper=user_registration.objects.filter(designation=desig)
        return render(request, 'DigitalMarketing/DM_employees.html', {'mem': mem,'dmdeveloper':dmdeveloper})
    else:
        return redirect('/')


def Dm_project_start(request,proj_start):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        projects=DM_projects.objects.get(id=proj_start)
        projects.dm_project_status="Work Started"
        projects.dm_project_start=date.today()
        projects.save()
        return redirect('DM_project_works')
    else:
        return redirect('/')
    

def DM_project_tasks(request,proj_taskid):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        proj=DM_projects.objects.get(id=proj_taskid)
        tasks=Dm_project_Task.objects.filter(dm_project_id=proj)
        return render(request, 'DigitalMarketing/DM_project_task.html', {'mem': mem,'tasks':tasks})
    else:
        return redirect('/')

    
def DM_project_task_assign(request,proj_assign):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        
        if request.method == 'POST':
            dev_name = request.POST['dev_name']
            task_name = request.POST['task_name']
        projects=DM_projects.objects.get(id=proj_assign)
        dev=user_registration.objects.get(fullname=dev_name)
        today = date.today()
        try:

            leave_status=leave.objects.get(user=dev,from_date=today)
            msg=1
            mem = user_registration.objects.filter(id=pm_id)
            desig=designation.objects.get(designation='Digital Developer')
            dmdeveloper=user_registration.objects.filter(designation=desig)
            projects=DM_projects.objects.filter(dm_project_status='Work Started')
            return render(request, 'DigitalMarketing/DM_project_work.html', {'mem': mem,'dmdeveloper':dmdeveloper,'projects':projects,'msg':msg})

        except leave.DoesNotExist:

            task=Dm_project_Task(dm_project_id=projects,dm_user_name=dev,dm_task_name=task_name,dm_task_status="Assinged")
            task.save()
            msg=0
            mem = user_registration.objects.filter(id=pm_id)
            desig=designation.objects.get(designation='Digital Developer')
            dmdeveloper=user_registration.objects.filter(designation=desig)
            projects=DM_projects.objects.filter(dm_project_status='Work Started')
            return render(request, 'DigitalMarketing/DM_project_work.html', {'mem': mem,'dmdeveloper':dmdeveloper,'projects':projects,'msg':msg})
            
        
    else:
        return redirect('/')


# task data view related to Digital marketing developers/Workers

def DM_project_task_data(request,dmtask_id,dmuser_id):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        
        task=Dm_project_Task.objects.get(id=dmtask_id)
        user=user_registration.objects.get(id=dmuser_id)
        if task.dm_task_name == 'Data Collection':
            task_data=DataCollect.objects.filter(Project_name=task,Employeeid=user)
            rcount=DataCollect.objects.filter(Project_name=task,Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data':task_data,'rcount':rcount})
        
        elif task.dm_task_name == 'Backlink Details':
            task_data1=Backlinks.objects.filter(bd_taskid=task,bd_Employeeid=user)
            rcount=Backlinks.objects.filter(bd_taskid=task,bd_Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data1':task_data1,'rcount':rcount})
        
        elif task.dm_task_name == 'Webpage Content creation':
            task_data2=WebpageContent.objects.filter(web_taskid=task,web_Employeeid=user)
            rcount=WebpageContent.objects.filter(web_taskid=task,web_Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data2':task_data2,'rcount':rcount})
        
        elif task.dm_task_name == 'Competitor analysis/Website Audit':
            task_data3=CompanyAnalysis.objects.filter(analysis_taskid=task,analysis_Employeeid=user)
            rcount=CompanyAnalysis.objects.filter(analysis_taskid=task,analysis_Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data3':task_data3,'rcount':rcount})

        elif task.dm_task_name == 'Data collection - Client':
            task_data4=ClientData.objects.filter(cd_taskid=task,cd_Employeeid=user)
            rcount=ClientData.objects.filter(cd_taskid=task,cd_Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data4':task_data4,'rcount':rcount})
        
        elif task.dm_task_name == 'On page works':
            task_data5=OnPage.objects.filter(op_taskid=task,op_Employeeid=user)
            rcount=OnPage.objects.filter(op_taskid=task,op_Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data5':task_data5,'rcount':rcount})
        
        elif task.dm_task_name == 'Blog calender':
            task_data6=BlogCalander.objects.filter(blog_taskid=task,blog_Employeeid=user)
            rcount=BlogCalander.objects.filter(blog_taskid=task,blog_Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data6':task_data6,'rcount':rcount})
        
        elif task.dm_task_name == 'SMM Post Calender':
            task_data7=SmmPoster.objects.filter(smm_taskid=task,smm_Employeeid=user)
            rcount=SmmPoster.objects.filter(smm_taskid=task,smm_Employeeid=user).count()
            return render(request, 'DigitalMarketing/DM_project_task_data.html', {'mem': mem,'task_data7':task_data7,'rcount':rcount})
        
    else:
        return redirect('/')


# Full data related to each task
    
def DM_project_task_fulldata(request,task_full,task_pro):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        task=Dm_project_Task.objects.get(id=task_full)
        proj=DM_projects.objects.get(id=task_pro)

        if task.dm_task_name == 'Data Collection':
            task_data=DataCollect.objects.all()
            rcount=0
            for i in task_data:
                if i.Project_name.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data':task_data,'rcount':rcount,'proj':proj})
    
        if task.dm_task_name == 'Backlink Details':
            task_data1=Backlinks.objects.all()
            rcount=0
            for i in task_data1:
                if i.bd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data1':task_data1,'rcount':rcount,'proj':proj})
        
        if task.dm_task_name == 'Webpage Content creation':
            task_data2=WebpageContent.objects.all()
            rcount=0
            for i in task_data2:
                if i.web_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data2':task_data2,'rcount':rcount,'proj':proj})

        if task.dm_task_name == 'Competitor analysis/Website Audit':
            task_data3=CompanyAnalysis.objects.all()
            rcount=0
            for i in task_data3:
                if i.analysis_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data3':task_data3,'rcount':rcount,'proj':proj})
        
        if task.dm_task_name == 'Data collection - Client':
            task_data4=ClientData.objects.all()
            rcount=0
            for i in task_data4:
                if i.cd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data4':task_data4,'rcount':rcount,'proj':proj})
        
           
        if task.dm_task_name == 'On page works':
            task_data5=OnPage.objects.all()
            rcount=0
            for i in task_data5:
                if i.op_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data5':task_data5,'rcount':rcount,'proj':proj})
        
        if task.dm_task_name == 'Blog calender':
            task_data6=BlogCalander.objects.all()
            rcount=0
            for i in task_data6:
                if i.blog_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data6':task_data6,'rcount':rcount,'proj':proj})
        
        if task.dm_task_name == 'SMM Post Calender':
            task_data7=SmmPoster.objects.all()
            rcount=0
            for i in task_data7:
                if i.smm_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_project_task_fulldata.html',{'mem': mem,'task_data7':task_data7,'rcount':rcount,'proj':proj})
    
    else:
        return redirect('/')

# report Full Data
    
def DM_report_full_data(request,report_data_id,repoj_id):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        
        proj=DM_projects.objects.get(id=repoj_id)

        if 1 == report_data_id:
            task_data=DataCollect.objects.all()
            rcount=0
            for i in task_data:
                if i.Project_name.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data':task_data,'rcount':rcount,'proj':proj})
        elif 2 == report_data_id:
            task_data1=Backlinks.objects.all()
            rcount=0
            for i in task_data1:
                if i.bd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data1':task_data1,'rcount':rcount,'proj':proj})
        
        elif 3 == report_data_id:
            task_data6=BlogCalander.objects.all()
            rcount=0
            for i in task_data6:
                if i.blog_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data6':task_data6,'rcount':rcount,'proj':proj})
        
        elif 4 == report_data_id:
            task_data7=SmmPoster.objects.all()
            rcount=0
            for i in task_data7:
                if i.smm_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data7':task_data7,'rcount':rcount,'proj':proj})
        
        elif 5 == report_data_id:
            task_data2=WebpageContent.objects.all()
            rcount=0
            for i in task_data2:
                if i.web_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data2':task_data2,'rcount':rcount,'proj':proj})
        
        elif 6 == report_data_id:
            task_data5=OnPage.objects.all()
            rcount=0
            for i in task_data5:
                if i.op_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data5':task_data5,'rcount':rcount,'proj':proj})
        
        elif 7 == report_data_id:
            task_data3=CompanyAnalysis.objects.all()
            rcount=0
            for i in task_data3:
                if i.analysis_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data3':task_data3,'rcount':rcount,'proj':proj})
        
        elif 8 == report_data_id:
            task_data4=ClientData.objects.all()
            rcount=0
            for i in task_data4:
                if i.cd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data4':task_data4,'rcount':rcount,'proj':proj})
    else:
        return redirect('/')
    
    
# serach report date -Date Vice
    
def Dm_datereport_data(request,retask_id,repj_id):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        
        proj=DM_projects.objects.get(id=repj_id)

        if request.method == 'POST':
          fromdate = request.POST['report_from']
          todate = request.POST['report_to']


        if 1 == retask_id:
            task_data=DataCollect.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
           
            rcount=0
            for i in task_data:
                if i.Project_name.dm_project_id.id == proj.id :
                    rcount=rcount+1
           
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data':task_data,'rcount':rcount,'proj':proj})
        
        elif 2 == retask_id:
            task_data1=Backlinks.objects.filter(bd_date__gte=fromdate, bd_date__lte=todate)
            rcount=0
            for i in task_data1:
                if i.bd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data1':task_data1,'rcount':rcount,'proj':proj})
        
        elif 3 == retask_id:
            task_data6=BlogCalander.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data6:
                if i.blog_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data6':task_data6,'rcount':rcount,'proj':proj})
        
        elif 4 == retask_id:
            task_data7=SmmPoster.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data7:
                if i.smm_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data7':task_data7,'rcount':rcount,'proj':proj})
        
        elif 5 == retask_id:
            task_data2=WebpageContent.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data2:
                if i.web_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data2':task_data2,'rcount':rcount,'proj':proj})
        
        elif 6 == retask_id:
            task_data5=OnPage.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data5:
                if i.op_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data5':task_data5,'rcount':rcount,'proj':proj})
        
        elif 7 == retask_id:
            task_data3=CompanyAnalysis.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data3:
                if i.analysis_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data3':task_data3,'rcount':rcount,'proj':proj})
        
        elif 8 == retask_id:
            task_data4=ClientData.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data4:
                if i.cd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'task_data4':task_data4,'rcount':rcount,'proj':proj})
    else:
        return redirect('/')


# task data download based on date
    
def Dm_datereport_download_data(request,drep_task):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        
        proj=DM_projects.objects.get(id=drep_task)

        if request.method == 'POST':
          fromdate = request.POST['report_from']
          todate = request.POST['report_to']
          task_name=request.POST['task_name']


        if task_name == 'Data Collection':
            response=HttpResponse(content_type='text/csv')
            response['Content-Disposition']='attachment ; filename=Data.csv'

            writer=csv.writer(response)

            writer.writerow(['Date' ,'Name' ,'Email','Phone Number' ,'Internship', 'Location' ,'Status','Reason'])  
            data=DataCollect.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate) 
            for i in data:
                if i.Project_name.dm_project_id.id == proj.id:
                    writer.writerow([i.dc_date, i.dc_name, i.dc_email, i.dc_phone, i.dc_internship, i.dc_loc, i.dc_status, i.dc_reason])
            return response

    else:
        return redirect('/')

    

# Digital Marketing manager  Attendece
    
def DM_manager_attende(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        user1 = user_registration.objects.get(id=pm_id)
        attend=attendance.objects.filter(user=user1).order_by('-id')
        return render(request, 'DigitalMarketing/DM_manager_attend.html',{'mem': mem,'attend':attend})
    else:
        return redirect('/')


def DM_manager_leave(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        user1 = user_registration.objects.get(id=pm_id)
        leaves=leave.objects.filter(user=user1).order_by('-id')
        return render(request, 'DigitalMarketing/DM_manager_leave.html',{'mem': mem,'leaves':leaves})
    else:
        return redirect('/')
    

def DM_manager_leave_apply(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        user1 = user_registration.objects.get(id=pm_id)
        if request.method == 'POST':
            sdate = request.POST['fromdate']
            edate = request.POST['todate']
            day = request.POST['day']
            reson = request.POST['reson']
            apply=leave(from_date=sdate,to_date=edate,reason=reson,leave_status=day,user=user1,designation_id=user1.designation.id)
            apply.save()
            msg=1
            leaves=leave.objects.filter(user=user1).order_by('-id')
            return render(request, 'DigitalMarketing/DM_manager_leave.html',{'mem': mem,'leaves':leaves,'msg':msg})
    else:
        return redirect('/')
    
#payments

def DM_manager_payment(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        user1 = user_registration.objects.get(id=pm_id)
        var = acntspayslip.objects.filter(user_id =user1)
        return render(request, 'DigitalMarketing/DM_manager_payments.html',{'mem': mem,'var':var})
    else:
        return redirect('/')


    # Report Issue

def DM_manager_report_isssue(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        return render(request, 'DigitalMarketing/DM_manager_report_issue.html',{'mem': mem})
    else:
        return redirect('/')

    

def DM_manager_report(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        projects=DM_projects.objects.all()
        return render(request, 'DigitalMarketing/DM_manager_report.html',{'mem': mem,'projects':projects})
    else:
        return redirect('/')
    



def DM_project_full_tasks(request,full_task_id):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        proj=DM_projects.objects.get(id=full_task_id)
        return render(request, 'DigitalMarketing/DM_current_month_report.html',{'mem': mem,'tasks':tasks,'proj':proj})
    else:
        return redirect('/')

def DM_report_add(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        proj=DM_projects.objects.all()
        report=DM_Project_Report.objects.all()
        return render(request, 'DigitalMarketing/DM_report_add.html',{'mem': mem,'proj':proj,'report':report})
    else:
        return redirect('/')

# Report Upload

def DM_report_upload(request):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(id=pm_id)
        if request.method == 'POST':
            p_name = request.POST['Project_name']
            t_name = request.POST['task_name']
            fdate = request.POST['client_report_from']
            tdate = request.POST['client_report_to']
            t_dese = request.POST['client_dese']
            t_file = request.FILES.get('task_file')
            prj=DM_projects.objects.get(dm_project_name=p_name)
            report=DM_Project_Report(re_project_name=p_name,re_project_task=t_name,re_project_fromdate=fdate,re_project_todate=tdate,
                                   re_project_dese=t_dese,re_project_task_file=t_file,report_project_id=prj)
            report.save()
            msg=1
            proj=DM_projects.objects.all()
            report=DM_Project_Report.objects.all()
            return render(request, 'DigitalMarketing/DM_report_add.html',{'mem': mem,'proj':proj,'msg':msg,'report':report})
    else:
        return redirect('/')

    

def Dm_report_data(request,report_data):
    if 'pm_id' in request.session:
        if request.session.has_key('pm_id'):
            pm_id = request.session['pm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=pm_id)
        proj=DM_projects.objects.get(id=report_data)
        rcount=0
        task_data=DataCollect.objects.all()
        for i in task_data:
            if i.Project_name.dm_project_id.id == proj.id :
                rcount=rcount+1
        return render(request, 'DigitalMarketing/DM_report_data.html',{'mem': mem,'task_data':task_data,'proj':proj,'rcount':rcount})
    else:
        return redirect('/')





    #****************************** digital Marketing 8 Tasks (17/10/22 -Shebin Shaji) *************


def devstart_task(request,task_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        task=Dm_project_Task.objects.get(id=task_id)
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if task.dm_task_name == 'Data Collection':
            task.dm_task_status='pending'
            task.save()
            datacollect=DataCollect.objects.filter(Project_name=task, Employeeid=user)
            rcount=DataCollect.objects.filter(Project_name=task, Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Data-Collection.html',{'task':task,'dmdev':dmdev,'datacollect':datacollect,'rcount':rcount})

        # backlink Details

        elif task.dm_task_name == 'Backlink Details':
            task.dm_task_status='pending'
            task.save()
            backlink=Backlinks.objects.filter(bd_taskid=task, bd_Employeeid=user)
            rcount=Backlinks.objects.filter(bd_taskid=task, bd_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Backlins-Details.html',{'task':task,'dmdev':dmdev,'backlink':backlink,'rcount':rcount})

         # Webpage Content creatio
        
        elif task.dm_task_name == 'Webpage Content creation':
            task.dm_task_status='pending'
            task.save()
            webcontent=WebpageContent.objects.filter(web_taskid=task, web_Employeeid=user)
            rcount=WebpageContent.objects.filter(web_taskid=task, web_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Web-Page-Content.html',{'dmdev':dmdev ,'webcontent':webcontent,'task':task,'rcount':rcount})


        #Competitor analysis/Website Audit

        elif task.dm_task_name == 'Competitor analysis/Website Audit':
            task.dm_task_status='pending'
            task.save()
            comp_analysis=CompanyAnalysis.objects.filter(analysis_taskid=task, analysis_Employeeid=user)
            rcount=CompanyAnalysis.objects.filter(analysis_taskid=task, analysis_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_CompetitorAnalysis.html',{'task':task,'dmdev':dmdev ,'comp_analysis':comp_analysis,'rcount':rcount})

        #Data collection - Client
        elif task.dm_task_name == 'Data collection - Client':
            task.dm_task_status='pending'
            task.save()
            clientdata=ClientData.objects.filter(cd_taskid=task, cd_Employeeid=user)
            rcount=ClientData.objects.filter(cd_taskid=task, cd_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_DataCollection-Client.html',{'task':task,'dmdev':dmdev ,'clientdata':clientdata,'rcount':rcount})

        #On page works
        elif task.dm_task_name == 'On page works':
            task.dm_task_status='pending'
            task.save()
            onpage=OnPage.objects.filter(op_taskid=task, op_Employeeid=user)
            rcount=OnPage.objects.filter(op_taskid=task, op_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_On-Page-Works.html',{'task':task,'dmdev':dmdev ,'onpage':onpage,'rcount':rcount})
        
        # Blog Calander
        elif task.dm_task_name == 'Blog calender':
            task.dm_task_status='pending'
            task.save()
            blog=BlogCalander.objects.filter(blog_taskid=task, blog_Employeeid=user)
            rcount=BlogCalander.objects.filter(blog_taskid=task, blog_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Blog-calender.html',{'task':task,'dmdev':dmdev,'blog':blog,'rcount':rcount })

        # Smm Poster
        elif task.dm_task_name == 'SMM Post Calender':
            task.dm_task_status='pending'
            task.save()
            smm=SmmPoster.objects.filter(smm_taskid=task, smm_Employeeid=user)
            rcount=SmmPoster.objects.filter(smm_taskid=task, smm_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Smm-Post-Calender.html',{'task':task,'smm':smm,'dmdev':dmdev,'rcount':rcount })

    
    else:
        return redirect('/')

    
def devstart_task_submit(request,task_submit):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        task=Dm_project_Task.objects.get(id=task_submit)
        task.dm_task_status='Completed'
        task.save()
        dmdev = user_registration.objects.filter(id=dmdev_id)
        return redirect('DM_devprojects')
    else:
        return redirect('/')


#data colection

def data_collect_save(request,task_dcid):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            dcdate=request.POST['dcdate']
            dcname=request.POST['dcname']
            dcmail=request.POST['dcmail']
            dcphno=request.POST['dcphno']
            dcloc=request.POST['dcloc']
            dcinternship=request.POST['dcinternship']
            dcfrex=request.POST['dcfr_ex']
            dcstatus=request.POST['dcstatus']
            dcreason=request.POST['dcreason']
            task=Dm_project_Task.objects.get(id=task_dcid)
            
            datacollect=DataCollect(dc_date=dcdate,dc_name=dcname,dc_email=dcmail,dc_phone=dcphno,dc_loc=dcloc,
                                    dc_internship=dcinternship,dc_Fr_Ex=dcfrex,dc_status=dcstatus,dc_reason=dcreason,Employeeid=user,Project_name=task)
            datacollect.save()
            datacollect=DataCollect.objects.filter(Project_name=task, Employeeid=user)
            rcount=DataCollect.objects.filter(Project_name=task, Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Data-Collection.html',{'task':task,'dmdev':dmdev,'datacollect':datacollect,'rcount':rcount})
    else:
        return redirect('/')

# showing all the task data

def devdata_collect_view(request,dc_view):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        user = user_registration.objects.get(id=dmdev_id)
        dmdev = user_registration.objects.filter(id=dmdev_id)
        task=Dm_project_Task.objects.get(id=dc_view)
        if task.dm_task_name == 'Data Collection':
            datacollect=DataCollect.objects.filter(Project_name=task, Employeeid=user)
            rcount=DataCollect.objects.filter(Project_name=task, Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Data-Collection_view.html',{'datacollect':datacollect,'rcount':rcount,'dmdev':dmdev})
        
        #Backlink Details
        elif task.dm_task_name == 'Backlink Details':
            backlink=Backlinks.objects.filter(bd_taskid=task, bd_Employeeid=user)
            rcount=Backlinks.objects.filter(bd_taskid=task, bd_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Backlink_view.html',{'backlink':backlink,'rcount':rcount,'dmdev':dmdev})

        #Webpage Content creation
        elif task.dm_task_name == 'Webpage Content creation':
            webcontent=WebpageContent.objects.filter(web_taskid=task, web_Employeeid=user)
            rcount=WebpageContent.objects.filter(web_taskid=task, web_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Webpage_view.html',{'webcontent':webcontent,'rcount':rcount,'dmdev':dmdev})

        #Competitor analysis/Website Audit
        elif task.dm_task_name == 'Competitor analysis/Website Audit':
            comp_analysis=CompanyAnalysis.objects.filter(analysis_taskid=task, analysis_Employeeid=user)
            rcount=CompanyAnalysis.objects.filter(analysis_taskid=task, analysis_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_CompanyAnalysis_view.html',{'comp_analysis':comp_analysis,'rcount':rcount,'dmdev':dmdev})

        #Data collection - Client
        elif task.dm_task_name == 'Data collection - Client':
            clientdata=ClientData.objects.filter(cd_taskid=task, cd_Employeeid=user)
            rcount=ClientData.objects.filter(cd_taskid=task, cd_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Data-Collection-Client_view.html',{'clientdata':clientdata,'rcount':rcount,'dmdev':dmdev})

        #onpage
        elif task.dm_task_name == 'On page works':
            onpage=OnPage.objects.filter(op_taskid=task, op_Employeeid=user)
            rcount=OnPage.objects.filter(op_taskid=task, op_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Onpage_view.html',{'onpage':onpage,'rcount':rcount,'dmdev':dmdev})

        #Blog Calander
        elif task.dm_task_name == 'Blog calender':
            blog=BlogCalander.objects.filter(blog_taskid=task, blog_Employeeid=user)
            rcount=BlogCalander.objects.filter(blog_taskid=task, blog_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Blog_calander_view.html',{'blog':blog,'rcount':rcount,'dmdev':dmdev})

        #Smm Post Calander
        elif task.dm_task_name == 'SMM Post Calender':
            smm=SmmPoster.objects.filter(smm_taskid=task, smm_Employeeid=user)
            rcount=SmmPoster.objects.filter(smm_taskid=task, smm_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_SmmPost_view.html',{'smm':smm,'rcount':rcount,'dmdev':dmdev})
        

        
        
    else:
        return redirect('/')


# backlink collect
    
def dev_backlink_save(request,bd_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            bddate=request.POST['bd_date']
            bdurl=request.POST['bd_url']
            bdtype=request.POST['bd_type']
            bdstatus=request.POST['bd_status']

            task=Dm_project_Task.objects.get(id=bd_id)
            
            backlink=Backlinks(bd_date=bddate,bd_url=bdurl,bd_type=bdtype,bd_status=bdstatus,
                                    bd_Employeeid=user,bd_taskid=task)
            backlink.save()
            backlink=Backlinks.objects.filter(bd_taskid=task, bd_Employeeid=user)
            rcount=Backlinks.objects.filter(bd_taskid=task, bd_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Backlins-Details.html',{'task':task,'dmdev':dmdev,'backlink':backlink,'rcount':rcount})
    else:
        return redirect('/')


#web page content
    
def dev_webpagecontent_save(request,web_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            bddate=request.POST['web_date']
            bdurl=request.POST['web_url']
            bdtype=request.POST['web_dese']
            bdstatus=request.POST['web_key']

            task=Dm_project_Task.objects.get(id=web_id)
            
            webcontent=WebpageContent(web_date=bddate,web_url=bdurl,web_dese=bdtype,web_key=bdstatus,
                                    web_Employeeid=user,web_taskid=task)
            webcontent.save()
            webcontent=WebpageContent.objects.filter(web_taskid=task, web_Employeeid=user)
            rcount=WebpageContent.objects.filter(web_taskid=task, web_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Web-Page-Content.html',{'task':task,'dmdev':dmdev,'webcontent':webcontent,'rcount':rcount})
    else:
        return redirect('/')

    
#web analysi Audit

def dev_webanalysi_save(request,audit_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            bddate=request.POST['cawa_date']
            comp=request.POST['cawa_compname']
        
            task=Dm_project_Task.objects.get(id=audit_id)
            
            comp_analysis=CompanyAnalysis(analysis_date=bddate,analysis_compname=comp,analysis_Employeeid=user,analysis_taskid=task)
            comp_analysis.save()
            comp_analysis=CompanyAnalysis.objects.filter(analysis_taskid=task, analysis_Employeeid=user)
            rcount=CompanyAnalysis.objects.filter(analysis_taskid=task, analysis_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_CompetitorAnalysis.html',{'task':task,'dmdev':dmdev,'comp_analysis':comp_analysis,'rcount':rcount})
    else:
        return redirect('/')

# data collection client
 
def dev_datacollect_client_save(request,dcc_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            bddate=request.POST['dcc_date']
            name=request.POST['dcc_fullname']
            email=request.POST['dcc_email']
            phno=request.POST['dcc_number']
            bussines=request.POST['dcc_busines']
        
        
            task=Dm_project_Task.objects.get(id=dcc_id)
            
            clientdata=ClientData(cd_date=bddate,cd_name=name,cd_email=email,
                                  cd_phno=phno,cd_bussines=bussines,cd_Employeeid=user,cd_taskid=task)
            clientdata.save()
            clientdata=ClientData.objects.filter(cd_taskid=task, cd_Employeeid=user)
            rcount=ClientData.objects.filter(cd_taskid=task, cd_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_DataCollection-Client.html',{'task':task,'dmdev':dmdev,'clientdata':clientdata,'rcount':rcount})
    else:
        return redirect('/')


 #on page    
def dev_onpage_save(request,onpage_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            bddate=request.POST['op_date']
            op_url=request.POST['op_url']
            opwork=request.POST['op_work']
            opstatus=request.POST['op_status']
        
            task=Dm_project_Task.objects.get(id=onpage_id)
            
            onpage=OnPage(op_date=bddate,op_url=op_url,op_work=opwork,
                                  op_status=opstatus,op_Employeeid=user,op_taskid=task)
            onpage.save()
            onpage=OnPage.objects.filter(op_taskid=task, op_Employeeid=user)
            rcount=OnPage.objects.filter(op_taskid=task, op_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_On-Page-Works.html',{'task':task,'dmdev':dmdev,'onpage':onpage,'rcount':rcount})
    else:
        return redirect('/')
    

def dev_onpge_edit_save(request,onpage_edit):
    print(onpage_edit)
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        onpage=OnPage.objects.get(id=onpage_edit)
        onpage.op_status=request.POST.get('op_editstatus')
        onpage.save()
        on_id=onpage.op_taskid.id
        print(on_id)
        return redirect('devstart_task', on_id)
    else:
        return redirect('/')

#bloag calander

def dev_blog_calander_save(request,blog_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            bddate=request.POST['bc_date']
            title=request.POST['bc_blogt']
            keyw=request.POST['bc_key']
            blogstatus=request.POST['bc_status']
        
            task=Dm_project_Task.objects.get(id=blog_id)
            
            blog=BlogCalander(blog_date=bddate,blog_title=title,blog_key=keyw,
                                  blog_status=blogstatus,blog_Employeeid=user,blog_taskid=task)
            blog.save()
            blog=BlogCalander.objects.filter(blog_taskid=task, blog_Employeeid=user)
            rcount=BlogCalander.objects.filter(blog_taskid=task, blog_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Blog-calender.html',{'task':task,'dmdev':dmdev,'blog':blog,'rcount':rcount})
    else:
        return redirect('/')


# Smm Poster
def dev_smm_poster_save(request,smm_id):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user = user_registration.objects.get(id=dmdev_id)
        if request.method =="POST":
            date=request.POST['smm_date']
            sub=request.POST['smm_sub']
            types=request.POST['smm_pt']
            cont=request.POST['smm_con']
            dese=request.POST['smm_dese']
            status=request.POST['smm_status']
            files=request.FILES.get('smm_file')
        
            task=Dm_project_Task.objects.get(id=smm_id)
            
            smm=SmmPoster(smm_date=date,smm_sub=sub,smm_type=types,
                                  smm_content=cont,smm_dese=dese,smm_satus=status,
                                  smm_file=files,smm_Employeeid=user,smm_taskid=task)
            smm.save()
            smm=SmmPoster.objects.filter(smm_taskid=task, smm_Employeeid=user)
            rcount=SmmPoster.objects.filter(smm_taskid=task, smm_Employeeid=user).count()
            return render(request,'DigitalMarketing/DM_Smm-Post-Calender.html',{'task':task,'dmdev':dmdev,'smm':smm,'rcount':rcount})
    else:
        return redirect('/')


#********************************* Digital marketing - (15/10/22-shebin shaji) *********************
def dmdevlogout(request):
    if 'dmdev_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def dm_devdashboard(request):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        
        return render(request, 'DigitalMarketing/DM_devdasbord.html', {'dmdev': dmdev})
    else:
        return redirect('/') 
    

def DM_devprojects(request):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        project=DM_projects.objects.all()
        user = user_registration.objects.get(id=dmdev_id)
        tasks=Dm_project_Task.objects.filter(dm_user_name=user).values('dm_project_id').distinct()
      
        return render(request, 'DigitalMarketing/DM_devproject.html', {'dmdev': dmdev,'tasks':tasks,'project':project})
    else:
        return redirect('/') 


def Dm_devattends(request):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user1=user_registration.objects.get(id=dmdev_id)
        attend=attendance.objects.filter(user=user1).order_by('-id')
        return render(request, 'DigitalMarketing/DM_devproject_Attendence.html', {'dmdev': dmdev,'tasks':tasks,'attend':attend})
    else:
        return redirect('/')


def Dm_devleave(request):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user1=user_registration.objects.get(id=dmdev_id)
        leaves=leave.objects.filter(user=user1).order_by('-id')
        return render(request, 'DigitalMarketing/DM_devplor_leave.html',{'dmdev': dmdev,'leaves':leaves})
    else:
        return redirect('/')

def DM_developer_leave_apply(request):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        user1 = user_registration.objects.get(id=dmdev_id)
        if request.method == 'POST':
            sdate = request.POST['fromdate']
            edate = request.POST['todate']
            day = request.POST['day']
            reson = request.POST['reson']
            apply=leave(from_date=sdate,to_date=edate,reason=reson,leave_status=day,user=user1,designation_id=user1.designation.id)
            apply.save()
            msg=1
            leaves=leave.objects.filter(user=user1).order_by('-id')
            return render(request, 'DigitalMarketing/DM_devplor_leave.html',{'dmdev': dmdev,'leaves':leaves,'msg':msg})

    else:
        return redirect('/')




    

def DM_devproject_tasks(request,dev_prj_task):
    if 'dmdev_id' in request.session:
        if request.session.has_key('dmdev_id'):
            dmdev_id = request.session['dmdev_id']
        else:
            return redirect('/')
        dmdev = user_registration.objects.filter(id=dmdev_id)
        project=DM_projects.objects.get(id=dev_prj_task)
        tasks=Dm_project_Task.objects.filter(dm_project_id=project)
        return render(request, 'DigitalMarketing/DM_devproject_tasks.html', {'dmdev': dmdev,'tasks':tasks})
    else:
        return redirect('/')



#****************************************** Digital marketing in Admin Section (19/10/22)
    
def BRadmin_dmproject(request,br_dmproj_id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        proj=DM_projects.objects.get(id=br_dmproj_id)
        return render(request,'BRadmin_dmproject_show.html', {'proj':proj,'Adm':Adm})
    else:
        return redirect('/')


def BRadmin_dm_report_full_data(request,brtask_id, br_proj_id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        proj=DM_projects.objects.get(id=br_proj_id)

        if 1 == brtask_id:
            task_data=DataCollect.objects.all()
            rcount=0
            for i in task_data:
                if i.Project_name.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data':task_data,'rcount':rcount,'proj':proj})
        elif 2 == brtask_id:
            task_data1=Backlinks.objects.all()
            rcount=0
            for i in task_data1:
                if i.bd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data1':task_data1,'rcount':rcount,'proj':proj})
        
        elif 3 == brtask_id:
            task_data6=BlogCalander.objects.all()
            rcount=0
            for i in task_data6:
                if i.blog_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data6':task_data6,'rcount':rcount,'proj':proj})
        
        elif 4 == brtask_id:
            task_data7=SmmPoster.objects.all()
            rcount=0
            for i in task_data7:
                if i.smm_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data7':task_data7,'rcount':rcount,'proj':proj})
        
        elif 5 == brtask_id:
            task_data2=WebpageContent.objects.all()
            rcount=0
            for i in task_data2:
                if i.web_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data2':task_data2,'rcount':rcount,'proj':proj})
        
        elif 6 == brtask_id:
            task_data5=OnPage.objects.all()
            rcount=0
            for i in task_data5:
                if i.op_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data5':task_data5,'rcount':rcount,'proj':proj})
        
        elif 7 == brtask_id:
            task_data3=CompanyAnalysis.objects.all()
            rcount=0
            for i in task_data3:
                if i.analysis_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data3':task_data3,'rcount':rcount,'proj':proj})
        
        elif 8 == brtask_id:
            task_data4=ClientData.objects.all()
            rcount=0
            for i in task_data4:
                if i.cd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data4':task_data4,'rcount':rcount,'proj':proj})
    else:
        return redirect('/')


def BRadmin_dm_datereport_data(request,br_retask_id,br_repj_id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        proj=DM_projects.objects.get(id=br_repj_id)

        if request.method == 'POST':
            fromdate = request.POST['report_from']
            todate = request.POST['report_to']


        if 1 == br_retask_id:
            task_data=DataCollect.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
           
            rcount=0
            for i in task_data:
                if i.Project_name.dm_project_id.id == proj.id :
                    rcount=rcount+1
           
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data':task_data,'rcount':rcount,'proj':proj})
        
        elif 2 == br_retask_id:
            task_data1=Backlinks.objects.filter(bd_date__gte=fromdate, bd_date__lte=todate)
            rcount=0
            for i in task_data1:
                if i.bd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data1':task_data1,'rcount':rcount,'proj':proj})
        
        elif 3 == br_retask_id:
            task_data6=BlogCalander.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data6:
                if i.blog_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data6':task_data6,'rcount':rcount,'proj':proj})
        
        elif 4 == br_retask_id:
            task_data7=SmmPoster.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data7:
                if i.smm_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data7':task_data7,'rcount':rcount,'proj':proj})
        
        elif 5 == br_retask_id:
            task_data2=WebpageContent.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data2:
                if i.web_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data2':task_data2,'rcount':rcount,'proj':proj})
        
        elif 6 == br_retask_id:
            task_data5=OnPage.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data5:
                if i.op_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data5':task_data5,'rcount':rcount,'proj':proj})
        
        elif 7 == br_retask_id:
            task_data3=CompanyAnalysis.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data3:
                if i.analysis_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data3':task_data3,'rcount':rcount,'proj':proj})
        
        elif 8 == br_retask_id:
            task_data4=ClientData.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            rcount=0
            for i in task_data4:
                if i.cd_taskid.dm_project_id.id == proj.id :
                    rcount=rcount+1
            return render(request, 'BRadmin_dmproject_show.html',{'Adm': Adm,'task_data4':task_data4,'rcount':rcount,'proj':proj})
    else:
        return redirect('/')
    


    
# Excel File Download
def excel_file_download(request,dwl_task,dwd_prj_id):
    
    proj=DM_projects.objects.get(id=dwd_prj_id)
    if 1 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=Data.csv'

        writer=csv.writer(response)

        writer.writerow(['Date' ,'Name' ,'Email','Phone Number' ,'Internship', 'Location' ,'Status','Reason'])  
        data=DataCollect.objects.all() 
        for i in data:
            if i.Project_name.dm_project_id.id == proj.id:
                writer.writerow([i.dc_date, i.dc_name, i.dc_email, i.dc_phone, i.dc_internship, i.dc_loc, i.dc_status, i.dc_reason])
        return response
    
    elif 2 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=Backlins.csv'

        writer=csv.writer(response)
        
        writer.writerow(['Date' ,'Url' ,'Type', 'Status']) 
        data=Backlinks.objects.all() 
        for i in data:
            if i.bd_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.bd_date, i.bd_url, i.bd_type, i.bd_status])
        return response
    
    elif 3 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=BlogCalander.csv'

        writer=csv.writer(response)
        writer.writerow(['Date' ,'Title' ,'Key', 'Status']) 
        data=BlogCalander.objects.all() 
        for i in data:
            if i.blog_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.blog_date, i.blog_title, i.blog_key, i.blog_status])
        return response
    
    elif 4 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=SMMPoster.csv'

        writer=csv.writer(response)
        writer.writerow(['Date' ,'Subject' ,'Type', 'Content', 'Desecription','Status']) 
        data=SmmPoster.objects.all() 
        for i in data:
            if i.smm_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.smm_date, i.smm_sub, i.smm_type, i.smm_content, i.smm_dese, i.smm_satus])
        return response
    
    elif 5 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=Webcontent.csv'

        writer=csv.writer(response)
        writer.writerow(['Date' ,'Url' ,'Desecription', 'Key']) 
        data=WebpageContent.objects.all() 
        for i in data:
            if i.web_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.web_date, i.web_url, i.web_dese, i.web_key])
        return response
    
    elif 6 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=Onpage.csv'

        writer=csv.writer(response)
        writer.writerow(['Date' ,'Url' ,'Work', 'Status']) 
        data=OnPage.objects.all() 
        for i in data:
            if i.op_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.op_date, i.op_url, i.op_work, i.op_status])
        return response
    
    elif 7 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=CompanyAnalysis.csv'

        writer=csv.writer(response)
        writer.writerow(['Date' ,'Company Name']) 
        data=CompanyAnalysis.objects.all() 
        for i in data:
            if i.analysis_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.analysis_date, i.analysis_compname])
        return response
    
    elif 8 == dwl_task:
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=ClientData.csv'

        writer=csv.writer(response)
        writer.writerow(['Date' ,'Name' ,'Email', 'Phone Number', 'Bussines']) 
        data=ClientData.objects.all() 
        for i in data:
            if i.cd_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.cd_date, i.cd_name, i.cd_email, i.cd_phno, i.cd_bussines])
        return response


    

def Dm_project_report_download(request):
   if request.method == 'POST':
        p_name = request.POST['proj_name']
        fdate = request.POST['prj_from']
        tdate = request.POST['prj_to']
        proj=DM_projects.objects.get(dm_project_name=p_name)

        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment ; filename=Report.csv'
      
      
      
        data=DataCollect.objects.filter(dc_date__gte=fdate, dc_date__lte=tdate,)
        writer=csv.writer(response)
        
        writer.writerow(['Data Collect']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Name' ,'Email','Phone Number' ,'Internship', 'Location' ,'Status','Reason'])  

        for i in data:
            if i.Project_name.dm_project_id.id == proj.id:
                writer.writerow([i.dc_date, i.dc_name, i.dc_email, i.dc_phone, i.dc_internship, i.dc_loc, i.dc_status, i.dc_reason])
    

       
        
        data=Backlinks.objects.filter(bd_date__gte=fdate,bd_date__lte=tdate)
        
        writer=csv.writer(response)
        writer.writerow(['']) 
        writer.writerow(['Backlink Data']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Url' ,'Type', 'Status']) 
                
        for i in data:
            if i.bd_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.bd_date, i.bd_url, i.bd_type, i.bd_status])


           
        
        data=BlogCalander.objects.filter(blog_date__gte=fdate, blog_date__lte=tdate)

        writer=csv.writer(response)
        writer.writerow(['']) 
        writer.writerow(['Blog Calander Data']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Title' ,'Key', 'Status']) 
        for i in data:
            if i.blog_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.blog_date, i.blog_title, i.blog_key, i.blog_status])
        
       
       
        data=SmmPoster.objects.filter(smm_date__gte=fdate, smm_date__lte=tdate)
     
        writer=csv.writer(response)
        writer.writerow(['']) 
        writer.writerow(['SMM Poster Calander Data']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Subject' ,'Type', 'Content', 'Desecription','Status']) 

        for i in data:
            if i.smm_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.smm_date, i.smm_sub, i.smm_type, i.smm_content, i.smm_dese, i.smm_satus])

        
        
        data=WebpageContent.objects.filter(web_date__gte=fdate, web_date__lte=tdate)
     
        writer=csv.writer(response)
        writer.writerow(['']) 
        writer.writerow(['Web Page Content Data']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Url' ,'Desecription', 'Key']) 
        for i in data:
            if i.web_taskid.dm_project_id.id == proj.id:
                 writer.writerow([i.web_date, i.web_url, i.web_dese, i.web_key])

        
        
        data=OnPage.objects.filter(op_date__gte=fdate, op_date__lte=tdate)
     
        writer=csv.writer(response)
        writer.writerow(['']) 
        writer.writerow(['Onpage Data']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Url' ,'Work', 'Status'])  
        for i in data:
            if i.op_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.op_date, i.op_url, i.op_work, i.op_status])


       
        data=CompanyAnalysis.objects.filter(analysis_date__gte=fdate, analysis_date__lte=tdate)
       
        writer=csv.writer(response)
        writer.writerow(['']) 
        writer.writerow(['Company Analyis']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Company Name']) 
        for i in data:
            if i.analysis_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.analysis_date, i.analysis_compname])


        
        data=ClientData.objects.filter(cd_date__gte=fdate, cd_date__lte=tdate)
       
        writer=csv.writer(response)
        writer.writerow(['']) 
        writer.writerow(['Client Data']) 
        writer.writerow(['']) 
        writer.writerow(['Date' ,'Name' ,'Email', 'Phone Number', 'Bussines']) 
        for i in data:
            if i.cd_taskid.dm_project_id.id == proj.id:
                writer.writerow([i.cd_date, i.cd_name, i.cd_email, i.cd_phno, i.cd_bussines])


        return response



#************************ Admin Audit section Digital Marketing shebin shaji 25/10/22

def BRadmin_audit(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        depart = department.objects.all()
        return render(request,'BRadmin_audit.html', {'Adm':Adm,'depart':depart})
    else:
        return redirect('/')
    
# admin Department Audit page   
def BRadmin_audit_department(request,BRadmin_aut_dep):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        depart = department.objects.get(id=BRadmin_aut_dep)
        if depart.department == 'Digital Marketing':
            use = user_registration.objects.filter(department_id=BRadmin_aut_dep)
            return render(request,'BRadmin_audit_department.html', {'Adm':Adm,'depart':depart,'use':use})
        else:
            use = user_registration.objects.filter(department_id=BRadmin_aut_dep)
            return render(request,'BRadmin_audit_department.html', {'Adm':Adm,'depart':depart,'use':use})
           
    else:
        return redirect('/')

#admin audit work categeory page
def BRadmin_audit_Works(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        depart = department.objects.all()
        return render(request,'BRadmin_audit_work.html', {'Adm':Adm,'depart':depart})
    else:
        return redirect('/')

#admin audit work list page
def BRadmin_audit_Works_list(request,BRadmin_aud_w_list):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if BRadmin_aud_w_list == 0:
            works_list=DM_projects.objects.filter(dm_project_categ='In House Project')
        else:
            works_list=DM_projects.objects.filter(dm_project_categ='Client Project')
        works=DM_projects.objects.all()
        return render(request,'BRadmin_audit_work_list.html', {'Adm':Adm,'works_list':works_list,'works':works})
    else:
        return redirect('/')
    

#admin audit work view
def BRadmin_audit_Works_view(request,BRadmin_aud_w_view):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        work_view=DM_projects.objects.get(id=BRadmin_aud_w_view)
        return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view})
    else:
        return redirect('/')

#admin audit work data
def BRadmin_audit_Works_data(request,Bradmin_aud_w,BRadmin_aud_w_data):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        work_view=DM_projects.objects.get(id=Bradmin_aud_w)
       
       
        if BRadmin_aud_w_data == 1:
            rcount=0
            task_data=DataCollect.objects.all()
            for i in task_data:
                if i.Project_name.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data':task_data,'rcount':rcount})
        
        elif BRadmin_aud_w_data == 2:
            rcount=0
            task_data1=Backlinks.objects.all()
            for i in task_data1:
                if i.bd_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data1':task_data1,'rcount':rcount})
        
        elif BRadmin_aud_w_data == 3:
            rcount=0
            task_data2=WebpageContent.objects.all()
            for i in task_data2:
                if i.web_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data2':task_data2,'rcount':rcount})
    
        elif BRadmin_aud_w_data == 4:
            rcount=0
            task_data7=SmmPoster.objects.all()
            for i in task_data7:
                if i.smm_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data7':task_data7,'rcount':rcount})
        
        elif BRadmin_aud_w_data == 5:
            rcount=0
            task_data6=BlogCalander.objects.all()
            for i in task_data6:
                if i.blog_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data6':task_data6,'rcount':rcount})
        
        elif BRadmin_aud_w_data == 6:
            rcount=0
            task_data5=OnPage.objects.all()
            for i in task_data5:
                if i.op_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data5':task_data5,'rcount':rcount})
        
        elif BRadmin_aud_w_data == 7:
            rcount=0
            task_data3=CompanyAnalysis.objects.all()
            for i in task_data3:
                if i.analysis_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data3':task_data3,'rcount':rcount})

        elif BRadmin_aud_w_data == 8:
            rcount=0
            task_data4=ClientData.objects.all()
            for i in task_data4:
                if i.cd_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data4':task_data4,'rcount':rcount})
 
    else:
        return redirect('/')


#admin audit data filter based on date
def BRadmin_audit_search(request,BRadmin_aud_sw,BRadmin_aud_search):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        work_view=DM_projects.objects.get(id=BRadmin_aud_sw)
        if request.method == 'POST':
            fromdate = request.POST['report_from']
            todate = request.POST['report_to']
        else:
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view})


        if BRadmin_aud_search == 1:
            rcount=0
            task_data=DataCollect.objects.filter(dc_date__gte=fromdate, dc_date__lte=todate)
            for i in task_data:
                if i.Project_name.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data':task_data,'rcount':rcount})
        
        elif BRadmin_aud_search == 2:
            rcount=0
            task_data1=Backlinks.objects.filter(bd_date__gte=fromdate, bd_date__lte=todate)
            for i in task_data1:
                if i.bd_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data1':task_data1,'rcount':rcount})
        
        elif BRadmin_aud_search == 3:
            rcount=0
            task_data2=WebpageContent.objects.filter(web_date__gte=fromdate, web_date__lte=todate)
            for i in task_data2:
                if i.web_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data2':task_data2,'rcount':rcount})
    
        elif BRadmin_aud_search == 4:
            rcount=0
            task_data7=SmmPoster.objects.filter(smm_date__gte=fromdate, smm_date__lte=todate)
            for i in task_data7:
                if i.smm_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data7':task_data7,'rcount':rcount})
        
        elif BRadmin_aud_search == 5:
            rcount=0
            task_data6=BlogCalander.objects.filter(blog_date__gte=fromdate, blog_date__lte=todate)
            for i in task_data6:
                if i.blog_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data6':task_data6,'rcount':rcount})
        
        elif BRadmin_aud_search == 6:
            rcount=0
            task_data5=OnPage.objects.filter(op_date__gte=fromdate, op_date__lte=todate)
            for i in task_data5:
                if i.op_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data5':task_data5,'rcount':rcount})
        
        elif BRadmin_aud_search == 7:
            rcount=0
            task_data3=CompanyAnalysis.objects.filter(analysis_date__gte=fromdate, analysis_date__lte=todate)
            for i in task_data3:
                if i.analysis_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
           
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data3':task_data3,'rcount':rcount})


        elif BRadmin_aud_search == 8:
            rcount=0
            task_data4=ClientData.objects.filter(cd_date__gte=fromdate, cd_date__lte=todate)
            for i in task_data4:
                if i.cd_taskid.dm_project_id.id == work_view.id :
                    rcount=rcount+1
            return render(request,'BRadmin_audit_work_view.html', {'Adm':Adm,'work_view':work_view,'task_data4':task_data4,'rcount':rcount})
    else:
        return redirect('/')

    




#admin audit employee page   
def BRadmin_audit_employees(request,BRadmin_aud_dep_id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dep=department.objects.get(id=BRadmin_aud_dep_id)
       
        return render(request,'BRadmin_audit_employee.html', {'Adm':Adm,'dep':dep})
    else:
        return redirect('/')

#admin audit trained employee page
def BRadmin_audit_trained_employees(request,BRadmin_aud_emp,Brasmin_aud_et):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if Brasmin_aud_et == 1:
            dep=department.objects.get(id=BRadmin_aud_emp)
            emp=user_registration.objects.filter(department=dep,employee_type='1')
        else:
            dep=department.objects.get(id=BRadmin_aud_emp)
            emp=user_registration.objects.filter(department=dep,employee_type='0')
        return render(request,'BRadmin_audit_employee_list.html', {'Adm':Adm,'emp':emp})
        
    else:
        return redirect('/')

#admin audit Emplyoee dashboard page
def BRadmin_auditdm_emp(request,BRadmin_aud_dmemp):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        emp=user_registration.objects.filter(id=BRadmin_aud_dmemp)
        
        return render(request,'BRadmin_audit_employee_page.html', {'Adm':Adm,'emp':emp})
    else:
        return redirect('/')

#admin audit employee attendance page
def BRadmin_audit_dmem_attend(request,Bradmin_aud_dmatte):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        emp=user_registration.objects.get(id=Bradmin_aud_dmatte)
        firstday=date.today().replace(day=1)
        attend=attendance.objects.filter(user_id=Bradmin_aud_dmatte,date__gte=firstday,date__lte=date.today())
        
        return render(request,'BRadmin_audit_dmemployee_ttend.html', {'Adm':Adm,'attend':attend,'emp':emp})
    else:
        return redirect('/')

#admin audit emloyee attendance search
def BRadmin_audit_dm_attendsearch(request,BRadmin_aud_emp_sattend):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        if request.method == 'POST':
            fdate = request.POST['d_from']
            tdate = request.POST['d_to']

        emp=user_registration.objects.get(id=BRadmin_aud_emp_sattend)
        attend=attendance.objects.filter(user_id=BRadmin_aud_emp_sattend,date__gte=fdate,date__lte=tdate)
        return render(request,'BRadmin_audit_dmemployee_ttend.html', {'Adm':Adm,'attend':attend,'emp':emp})
    else:
        return redirect('/')
    
# admin audit Digital marketing manager task assing search
def BRadmin_audit_dm_tasksearch(request,BRadmin_aud_stask):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        if request.method == 'POST':
            fdate = request.POST['task_from']
            tdate = request.POST['task_to']
        emp=user_registration.objects.get(id=BRadmin_aud_stask)
        task_ass=Dm_project_Task.objects.filter(dm_task_assigndate__gte=fdate,dm_task_assigndate__lte=tdate)
        return render(request,'BRadmin_audit_dmhead_works.html', {'Adm':Adm,'task_ass':task_ass,'emp':emp})
    else:
        return redirect('/')



# admin audit salary page
def BRadmin_audit_dmemp_salary(request,BRadmin_aud_dmemp_sal):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        emp=user_registration.objects.get(id=BRadmin_aud_dmemp_sal)
        salary=acntspayslip.objects.filter(user_id_id=BRadmin_aud_dmemp_sal).order_by('-fromdate')
        return render(request,'BRadmin_audit_dmemployee_salary.html', {'Adm':Adm,'emp':emp,'salary':salary})
    else:
        return redirect('/')
    
#admin audit salary search in date vice 
def BRadmin_audit_dm_salarysearch(request,BRadmin_aud_dmemp_ssalry):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            fdate = request.POST['sal_from']
            tdate = request.POST['sal_to']

        emp=user_registration.objects.get(id=BRadmin_aud_dmemp_ssalry)
        salary=acntspayslip.objects.filter(user_id_id=BRadmin_aud_dmemp_ssalry,fromdate__gte=fdate,fromdate__lte=tdate).order_by('-fromdate')
        return render(request,'BRadmin_audit_dmemployee_salary.html', {'Adm':Adm,'emp':emp,'salary':salary})
    else:
        return redirect('/')

#admin audit emloyee works
def BRadmin_audit_dmemp_works(request,BRadmin_aud_dmemp_work):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            fdate = request.POST['sal_from']
            tdate = request.POST['sal_to']
        deg=designation.objects.get(designation='Digital manager')
        emp=user_registration.objects.get(id=BRadmin_aud_dmemp_work)
        if emp.designation == deg:
           task_ass=Dm_project_Task.objects.all()
           return render(request,'BRadmin_audit_dmhead_works.html', {'Adm':Adm,'task_ass':task_ass,'emp':emp})
        
        else:
            works=DM_projects.objects.all()
            tasks=Dm_project_Task.objects.filter(dm_user_name_id=BRadmin_aud_dmemp_work).values('dm_project_id').distinct()
    
            return render(request,'BRadmin_audit_dmemployee_works.html', {'Adm':Adm,'emp':emp,'tasks':tasks,'works':works})
    else:
        return redirect('/')

#aduit admin work tasks
def BRadmin_audit_Works_tasks(request,BRadmin_adu_dmwt,BRadmin_aud_dmw):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
      
        work_view=DM_projects.objects.get(id=BRadmin_aud_dmw)
        task_data=DataCollect.objects.filter(Employeeid_id=BRadmin_adu_dmwt)
        task_data1=Backlinks.objects.filter(bd_Employeeid_id=BRadmin_adu_dmwt)
        task_data2=WebpageContent.objects.filter(web_Employeeid_id=BRadmin_adu_dmwt)
        task_data3=CompanyAnalysis.objects.filter(analysis_Employeeid=BRadmin_adu_dmwt)
        task_data4=ClientData.objects.filter(cd_Employeeid=BRadmin_adu_dmwt)
        task_data5=OnPage.objects.filter(op_Employeeid=BRadmin_adu_dmwt)
        task_data6=BlogCalander.objects.filter(blog_Employeeid=BRadmin_adu_dmwt)
        task_data7=SmmPoster.objects.filter(smm_Employeeid=BRadmin_adu_dmwt)
        
        return render(request,'BRadmin_audit_dmwork_task.html', {'Adm':Adm,'task_data':task_data,'task_data1':task_data1,'task_data2':task_data2,'task_data3':task_data3,'task_data4':task_data4,'task_data5':task_data5,'task_data6':task_data6,'task_data7':task_data7,'work_view':work_view})
    else:
        return redirect('/')

    
def get_instances(request):


    # unpack request:
    instance_id = request.POST.get('instanceID')
    print(instance_id)
   
    # get instance:
    instance = project.objects.get(id=instance_id)
    print(instance)

    
    response = {
        'is_taken':project_module_assign.objects.filter(project_name = instance)
    }
    return JsonResponse(response)
  

# team leader project task delay warning message 

def TLproject_task_delay(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        display1 = project.objects.all()
        display=project_taskassign.objects.filter(tl_id=tlid,delay__gte='4')
        war=wrdata.objects.all()
        return render(request, 'TLprojects_task_delay.html',{'display':display,'mem':mem,'display1':display1,'war':war,'tlid':tlid})
    else:
        return redirect('/')
    
    
def TL_warning(request,Tltask_id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        tl = user_registration.objects.get(id=tlid)

        if request.method == 'POST':
            remark = request.POST['remarks']
        prjtask=project_taskassign.objects.get(id=Tltask_id)
        warningdata=wrdata()
        warningdata.wrn_develp=prjtask.developer
        warningdata.wrn_user_name=tl
        warningdata.wrn_task=prjtask
        warningdata.wrn_reason=remark
        warningdata.save()
        war=wrdata.objects.all()

        display1 = project.objects.all()
        display=project_taskassign.objects.filter(tl_id=tlid,delay__gte='4')
        return render(request, 'TLprojects_task_delay.html',{'display':display,'mem':mem,'display1':display1,'war':war})
    else:
        return redirect('/')

# project manager delay section
def projectManager_project_delay(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pr_manager = user_registration.objects.get(id=prid)

        cur_date=date.today()
       
        year = cur_date.year
    
        first_date = datetime(year, 1, 1).strftime('%Y-%m-%d')
        display=project_taskassign.objects.filter(~Q(status='submitted'),enddate__lt=cur_date,enddate__gte=first_date).order_by('-id')
        for i in display:
           days=(cur_date - i.enddate).days
           
           i.tsakdelaydays= int(days)
           i.save()
        war=wrdata.objects.all()
        return render(request, 'projectmanager_projects_delay.html',{'pro':pro,'display':display,'war':war})
    else:
        return redirect('/')

    
def projectManager_warning(request,pmtaskwr_id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pr_manager = user_registration.objects.get(id=prid)

        if request.method == 'POST':
            remark = request.POST['pmremarks']
        prjtask=project_taskassign.objects.get(id=pmtaskwr_id)
        warningdata=wrdata()
        warningdata.wrn_develp=prjtask.developer
        warningdata.wrn_user_name=pr_manager
        warningdata.wrn_task=prjtask
        warningdata.wrn_reason=remark
        warningdata.save()
        
        return redirect('projectManager_project_delay')
    else:
        return redirect('/')

# admin project document delay action
    
def BRadmin_project_delay_action(request,BRadmin_dep_dely):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        projects = project.objects.filter(department_id=BRadmin_dep_dely)
        display=project_taskassign.objects.filter(delay__gte='4',project__in=projects.values_list('id')).order_by('-id')
        war=wrdata.objects.all()
        return render(request, 'BRadmin_project_delay_list.html', {'Adm': Adm,'display':display,'war':war})
    else:
        return redirect('/')

    
def BRadmin_project_budgect(request,BRadmin_bud):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        projects = project.objects.filter(department_id=BRadmin_bud).order_by('-id')
        prjbug = ProjectBudgect.objects.all()
        l= {}
        
       
        for i in projects:
            sum=0
            for j in prjbug:
                if j.pb.id == i.id:
                 
                  sum = sum + j.pb_amount
            
            l[i.id] = sum
      
        return render(request, 'BRadmin_project_budgect_list.html', {'Adm': Adm,'projects':projects,'prjbug':prjbug,'l':l.items()})
    else:
        return redirect('/')


def BRadmin_budgect_add(request,BRadmin_pb):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        projects = project.objects.get(id=BRadmin_pb)

        if request.method == 'POST':
            bud=ProjectBudgect()
            bud.pb=projects
            bud.pb_date=date.today()
            bud.pb_title=request.POST['pb_title']
            bud.pb_amount= request.POST['pb_amt']
            bud.pb_status='0'
            bud.save()

            return redirect('BRadmin_project_budgect',bud.pb.department.id)
    else:
        return redirect('/')

def BRAdmin_section_complete(request,BRadmin_sect_id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        pbug = ProjectBudgect.objects.get(id=BRadmin_sect_id)
        pbug.pb_status='1'
        pbug.pb_compdate=date.today()
        pbug.save()
        return redirect('BRadmin_project_budgect',pbug.pb.department.id)
    else:
        return redirect('/')




#************************* Audit Module ************************************4/11/22

#Auditor logout
def Auditlogout(request):
    if 'aud_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

# auaditor Dashboard
def Auditdashboard(request):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        return render(request, 'audit_module/audit_dasboard.html', {'Aud': Aud})
    else:
        return redirect('/')


# Training Section---------auaditor Training page load
def Audit_training(request):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        traines=user_registration.objects.filter(Q(trainee_status=0) | Q(trainee_status=2),designation_id=9,status='active')
        alltraines =user_registration.objects.filter(designation_id=9,status='active')
        trainers=user_registration.objects.filter(designation_id=8,status='active')
        return render(request, 'audit_module/audit_taining.html', {'Aud': Aud,'traines':traines,'trainers':trainers,'alltraines':alltraines})
    else:
        return redirect('/')

#Trainee Section ---->

def Audit_trainee_trainer_dashboard(request,audit_traine_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
      
        traine_tainer_db=user_registration.objects.get(id=audit_traine_id)
       
        deg=traine_tainer_db.designation.id
        if deg == 9:
            tnr=previousTeam.objects.filter(user_id=audit_traine_id)
            attend=attendance.objects.filter(user_id=audit_traine_id).order_by('-id')
            tran_proj=trainer_task.objects.filter(user_id=audit_traine_id,task_type='1')
            t_payments=paymentlist.objects.filter(user_id_id=audit_traine_id)
            t_leave=leave.objects.filter(user_id=audit_traine_id).order_by('-id')
            t_prob=probation.objects.filter(user_id=audit_traine_id)
            t_rep_issue=reported_issue.objects.filter(reporter_id=audit_traine_id)
            trainer_status= trainer_task_test.objects.filter(test_task_type='0')
            fbfrom=Feedbacks.objects.filter(fb_from=audit_traine_id)
            fbto=Feedbacks.objects.filter(fb_to=audit_traine_id)
            tm=previousTeam.objects.filter(user_id=audit_traine_id)
            return render(request, 'audit_module/audit_tainee_dashbord.html', {'Aud': Aud,'traine_tainer_db':traine_tainer_db,'tnr':tnr,'tm':tm,
                                                                                'attend':attend,'tran_proj':tran_proj,'t_payments':t_payments,
                                                                                't_leave':t_leave,'t_prob':t_prob,'t_rep_issue':t_rep_issue,'trainer_status':trainer_status,'fbfrom':fbfrom,'fbto':fbto})
        if deg == 8:
            trainer_team=create_team.objects.filter(trainer_id=str(audit_traine_id))
            fbfrom=Feedbacks.objects.filter(fb_to=audit_traine_id)
            fbto=Feedbacks.objects.filter(fb_from=audit_traine_id)
           
            return render(request, 'audit_module/audit_tainer_dashbord.html', {'Aud': Aud,'traine_tainer_db':traine_tainer_db,
                                                                                'trainer_team':trainer_team,'fbto':fbto,'fbfrom':fbfrom})
    else:
        return redirect('/')

# Traine's trainer details
def Audit_trainee_trainer_details(request,audit_ttrainer_id,audit_tm_id,audit_trn_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
      
        Aud = user_registration.objects.filter(id=Aud_id)
        trainer=user_registration.objects.get(id=audit_ttrainer_id)
       
        topics=topic.objects.filter(trainer_id=audit_ttrainer_id,team_id=audit_tm_id)
        tasks=trainer_task.objects.filter(team_name_id=audit_tm_id,user_id=audit_trn_id,task_type='0')
        trainer_status= trainer_task_test.objects.filter(test_task_type='0')
      
        return render(request, 'audit_module/audit_traine_tainer_details.html', {'Aud': Aud,'trainer':trainer,'topics':topics,'tasks':tasks,'trainer_status':trainer_status})
    else:
        return redirect('/')

# Trainee porobation Deatails
def audit_probation(request,audit_tr_prob):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
      
        Aud = user_registration.objects.filter(id=Aud_id)
        trainees= user_registration.objects.get(id=audit_tr_prob)
        t_prob=probation.objects.filter(user_id=audit_tr_prob)
        return render(request, 'audit_module/audit_traine_probation.html', {'Aud': Aud,'t_prob':t_prob,'trainees':trainees})
    else:
        return redirect('/')


# Trainer team view details
def audit_trainer_teamview(request,audit_trainer_tmid):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
      
        Aud = user_registration.objects.filter(id=Aud_id)
        team_memb=previousTeam.objects.filter(teamname_id=audit_trainer_tmid)
        team_topic=topic.objects.filter(team_id=audit_trainer_tmid)
        team_task=trainer_task.objects.filter(team_name_id=audit_trainer_tmid,task_status='0')
        return render(request, 'audit_module/audit_trainer_teamview.html', {'Aud': Aud,'team_memb':team_memb,
                                                    'team_topic':team_topic,'team_task':team_task})
    else:
        return redirect('/')





#Employee  Section ---------------auditor Employee page load

def Audit_employees(request):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        emp= user_registration.objects.filter(~Q(designation_id=9))
        des = department.objects.all()
        return render(request, 'audit_module/audit_employee.html', {'Aud': Aud,'emp':emp,'des':des})
    else:
        return redirect('/')

def Audit_department(request,audit_dep_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        mem = department.objects.get(id=audit_dep_id)
        des=designation.objects.filter(~Q(designation='admin'),~Q(designation='manager'),~Q(designation='account'),~Q(designation='auditor'),~Q(designation='Digital manager'),~Q(designation='Digital Developer'),~Q(designation='trainee'))
        context = {'mem':mem,'des':des,'Aud' : Aud,}
        return render(request, 'audit_module/audit_depart_designations.html',context)
    else:
        return redirect('/')


def Audit_emp_list(request,audit_depart_id,audit_des_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        mem = department.objects.get(id=audit_depart_id)
        mem1 = designation.objects.get(pk=audit_des_id)

        if mem1.designation == 'tester':

            use=user_registration.objects.filter(department_id=mem.id,designation=mem1, status="active")
            context = {'mem':mem,'use':use,'Aud' : Aud}

            return render(request, 'audit_module/audit_tester.html',context)
        

        use=user_registration.objects.filter(department_id=mem.id,designation=mem1, status="active")
        context = {'mem':mem,'use':use,'Aud' : Aud,}
        return render(request, 'audit_module/audit_depart_designations_emp.html',context)
    else:
        return redirect('/')
    

def Audit_tester_works(request,pk):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        proj_list=project_taskassign.objects.filter(tester_id=pk).order_by('-submitted_date')
        verify_num=project_taskassign.objects.filter(tester_id=pk, status='submitted').count()
        pending_verify_num=project_taskassign.objects.filter(tester_id=pk, status='Verification').count()
        correction_num=project_taskassign.objects.filter(tester_id=pk, status='correction').count()
        tester_dely=TSproject_Task_verify.objects.filter(ts_tester_id=pk).order_by('-id')
        delay_num=0
        for i in tester_dely:
            delay_num=delay_num+int(i.ts_delay)
       
        return render(request, 'audit_module/audit_tester_works.html', {'Aud': Aud,'proj_list':proj_list,'verify_num':verify_num,'pending_verify_num':pending_verify_num,'correction_num':correction_num,'tester_dely':tester_dely,'delay_num':delay_num})


def Audit_tester_works_view(request,pk):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        tas=project_taskassign.objects.get(id=pk)
        data1 = tester_status.objects.filter(task=tas).order_by('-id')
        print(data1)
        return render(request, 'audit_module/audit_tester_works_view.html', {'Aud': Aud,'tas':tas,'data1':data1})


#Employee Report Pdf


def Audit_empdaily_reportpdf(request,audit_rep_id):
    date = datetime.now()  
    if request.method =="POST":
        
        formdate=request.POST.get('emp_form')
        todate=request.POST.get('emp_to')
        user= user_registration.objects.get(id=audit_rep_id)
       
        
        task = project_taskassign.objects.filter(developer_id=audit_rep_id,startdate__gte=formdate, enddate__lte=todate)
       
        #tsk = trainer_task.objects.filter(user_id=audit_rep_id,startdate__gte=formdate ,startdate__lte=todate)
       
       
        lev = leave.objects.filter(user_id=audit_rep_id,from_date__gte=formdate,from_date__lte=todate)
        event1 = Event.objects.filter(start_time__range=(formdate,todate))
       
        if user.designation.designation == 'project manager':
            proj = project.objects.filter(projectmanager_id=audit_rep_id,startdate__gte=formdate,startdate__lte=todate)
            ptask = project_taskassign.objects.filter(project__in=proj,startdate__gte=formdate, enddate__lte=todate).order_by('startdate')
          
        else:
            proj=None
     
       
        tlev=0
        for i in lev:
            tlev=tlev + int(i.days)






    template_path = 'audit_module/audit_emp_dailyreport_pdf.html'
    context = {
    
    
    'task':task,
    'ptask':ptask,
    
    'date':date,
    
    'lev':lev,
    
    'tlev':tlev,
    'event1':event1,
    'user':user,
    'formdate':formdate,
    'todate':todate,
   
    'path':settings.NEWPATH,
    }
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-Document.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def Audit_emp_reportpdf(request,audit_rep_id):
    date = datetime.now()  
    if request.method =="POST":
        p1=request.POST.get('emp_training')
        p2=request.POST.get('emp_proj')
        p3=request.POST.get('emp_proj_corr')
        p4=request.POST.get('emp_proj_up')
        p5=request.POST.get('emp_salary')
        p6=request.POST.get('emp_leatd')
        p7=request.POST.get('emp_issue')
        formdate=request.POST.get('emp_form')
        todate=request.POST.get('emp_to')
        user= user_registration.objects.get(id=audit_rep_id)
        pros = project.objects.all()
        devp = project_taskassign.objects.filter(developer_id=audit_rep_id,startdate__gte=formdate, enddate__lte=todate).values('project_id').distinct()
        task = project_taskassign.objects.filter(developer_id=audit_rep_id,startdate__gte=formdate, enddate__lte=todate)
        corre = ProjectCorrectionUpdation.objects.filter(pdev_name=user.fullname,project_date__gte=formdate,project_date__lte=todate)
        tm = previousTeam.objects.filter(user_id=audit_rep_id,tr_start_date__gte=formdate,tr_start_date__lte=todate)
        tm1 = previousTeam.objects.filter(user_id=audit_rep_id,tr_start_date__gte=formdate,tr_start_date__lte=todate).values('teamname').distinct()
        pr = probation.objects.filter(user_id=audit_rep_id)
        tsk = trainer_task.objects.filter(user_id=audit_rep_id,startdate__gte=formdate ,startdate__lte=todate)
        top = topic.objects.filter(startdate__gte=formdate,startdate__lte=todate,team_id__in=tm1.values_list('teamname'))
        att = attendance.objects.filter(user_id=audit_rep_id,date__gte=formdate,date__lte=todate,attendance_status='1')
        lev = leave.objects.filter(user_id=audit_rep_id,from_date__gte=formdate,from_date__lte=todate)
        act = Action_Taken.objects.filter(atemp_id=audit_rep_id,at_date__gte=formdate,at_date__lte=todate)
        sal = acntspayslip.objects.filter(user_id_id=audit_rep_id,fromdate__gte=formdate,fromdate__lte=todate)
        proj = project.objects.filter(projectmanager_id=audit_rep_id,startdate__gte=formdate,startdate__lte=todate)
        


        tlev=0
        for i in lev:
            tlev=tlev + int(i.days)




    template_path = 'audit_module/audit_emp_report_pdf.html'
    context = {
    'p1':p1,
    'p2':p2,
    'pros':pros,
    'devp':devp,
    'task':task,
    'p3':p3,
    'p4':p4,
    'p5':p5,
    'p6':p6,
    'p7':p7,
    'date':date,
    'corre':corre,
    'tm':tm,
    'pr':pr,
    'tsk':tsk,
    'top':top,
    'lev':lev,
    'att':att,
    'tlev':tlev,
    'act':act,
    'sal':sal,
    'user':user,
    'formdate':formdate,
    'todate':todate,
    'proj':proj,
    'path':settings.NEWPATH,
    }
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="Project-Document.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
        
    

# Employee dashboard

def Audit_employee_dashbord(request,audit_emp_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        emp= user_registration.objects.get(id=audit_emp_id)
        pros = project.objects.all()
       
        if emp.designation.designation == 'project manager':
            devp = project.objects.filter(projectmanager_id=audit_emp_id,).order_by('-id')

        elif emp.designation.designation == 'team leader':
            devp = project_taskassign.objects.filter(developer_id=audit_emp_id,worktype='1').values('project_id').distinct()

        elif  emp.designation.designation == 'tester':
            devp = project_taskassign.objects.filter(tester_id=audit_emp_id).values('project_id').distinct()
        else:
            devp = project_taskassign.objects.filter(developer_id=audit_emp_id).values('project_id').distinct()

        firstday=date.today().replace(day=1)
        today=date.today()
       
        count=0
        leaves=0
        leve_count= leave.objects.filter(user_id=audit_emp_id,from_date__gte=firstday,from_date__lte=today)
        lev=leave.objects.filter(user_id=audit_emp_id).order_by('-id')
        attend=attendance.objects.filter(user_id=audit_emp_id).order_by('-id')
        sala=acntspayslip.objects.filter(user_id_id=audit_emp_id).order_by('-id')
        rep=reported_issue.objects.filter(reporter_id=audit_emp_id).order_by('-id')
        hld= Salary_hold.objects.filter(sal_id__in=sala.values_list('id', flat=True))
        act= Action_Taken.objects.filter(Q(atemp_id=audit_emp_id) | Q(atby_id=audit_emp_id))
        for j in leve_count:
            leaves=leaves+int(j.days)

        if emp.designation.designation == 'team leader':
            delya_count=project_taskassign.objects.filter(developer_id=audit_emp_id,submitted_date__gte=firstday,submitted_date__lte=date.today(),worktype='1')
            count=0
            for i in delya_count:
               
                count= count + int(i.delay)

        elif emp.designation.designation == 'tester':
            delya_count=TSproject_Task_verify.objects.filter(ts_tester_id=audit_emp_id,ts_task_verify_date__gte=firstday,ts_task_verify_date__lte=date.today())
            for i in delya_count:
                count=count+int(i.ts_delay)

        else:

            delya_count=project_taskassign.objects.filter(developer_id=audit_emp_id,submitted_date__gte=firstday,submitted_date__lte=date.today())
       
            for i in delya_count:
                count=count+int(i.delay)

        return render(request, 'audit_module/audit_employee_dasboard.html', {'Aud': Aud,'emp':emp,'pros':pros,'devp':devp,'count':count,
        'leaves':leaves,'lev':lev,'attend':attend,'sala':sala,'rep':rep,'hld':hld,'act':act})
    else:
        return redirect('/')

def Audit_salary_hold(request,holdid):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
                Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        display2 = user_registration.objects.all()
        sal=acntspayslip.objects.get(id=holdid)
        if request.method == 'POST':
            hld = request.POST['rea_hold']
            amount = request.POST['amount_hold']
            hd=Salary_hold()
            hd.sal_id=sal
            hd.sal_reason=hld
            if amount:
                hd.sal_amount=amount
                sal.net_salary=sal.net_salary - int(amount)
                sal.save()
            else:
                hd.sal_amount=0
            hd.sal_status='Hold'
            hd.save()
            return redirect('Audit_employee_dashbord',sal.user_id.id)
    else:
        return redirect('/')


def Audit_project_tl(request,audit_protls):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        display2 = user_registration.objects.all()
        display = project_taskassign.objects.filter(project_id=audit_protls).values('project_id','tl_id').distinct()
        return render(request, 'audit_module/audit_project_tl.html', {'Aud': Aud,'display2':display2,'display':display})

    else:
        return redirect('/')

        

def Audit_project_tlteam(request,audit_protlsdev,adev_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
       
        display = project_taskassign.objects.filter(project_id=audit_protlsdev).values('tl_id').distinct()
        display2 = project_taskassign.objects.filter(project_id=audit_protlsdev,developer_id=adev_id)
        uniq = user_registration.objects.all()
        return render(request, 'audit_module/audit_project_tlteam.html', {'Aud': Aud,'display2':display2,'display':display,'uniq':uniq})

    else:
        return redirect('/')




def Audit_trainee_dashboard(request,audit_emp_tr):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
      
        traine_tainer_db=user_registration.objects.get(id=audit_emp_tr)
        tnr=previousTeam.objects.filter(user_id=audit_emp_tr)
        attend=attendance.objects.filter(user_id=audit_emp_tr).order_by('-id')
        tran_proj=trainer_task.objects.filter(user_id=audit_emp_tr,task_type='1')
        t_payments=paymentlist.objects.filter(user_id_id=audit_emp_tr)
        t_leave=leave.objects.filter(user_id=audit_emp_tr).order_by('-id')
        t_prob=probation.objects.filter(user_id=audit_emp_tr)
        t_rep_issue=reported_issue.objects.filter(reporter_id=audit_emp_tr)
        trainer_status= trainer_task_test.objects.filter(test_task_type='0')
        fbfrom=Feedbacks.objects.filter(fb_from=audit_emp_tr)
        fbto=Feedbacks.objects.filter(fb_to=audit_emp_tr)
        return render(request, 'audit_module/audit_tainee_dashbord.html', {'Aud': Aud,'traine_tainer_db':traine_tainer_db,'tnr':tnr,
                                                                                'attend':attend,'tran_proj':tran_proj,'t_payments':t_payments,
                                                                                't_leave':t_leave,'t_prob':t_prob,'t_rep_issue':t_rep_issue,'trainer_status':trainer_status})
    else:
        return redirect('/')

def Audit_tl(request,Audit_tl):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        deg=designation.objects.get(designation='developer')
        dev_tl=user_registration.objects.filter(tl_id=int(Audit_tl),designation=deg)
        
        pros = project.objects.all()
        devp = project_taskassign.objects.filter(tl_id=Audit_tl,worktype='0').values('project_id').distinct()
        warn= wrdata.objects.filter(wrn_user_name_id=Audit_tl)

        return render(request, 'audit_module/audit_emp_tl.html', {'Aud': Aud,'dev_tl':dev_tl,'pros':pros,'devp':devp,'warn':warn,'Audit_tl':Audit_tl})
    else:
        return redirect('/')


def Audit_tlproject_split(request,audit_pid,audit_ptlid):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        devp = project_taskassign.objects.filter(tl_id=audit_ptlid,project_id=audit_pid,worktype='0').order_by('-id')
        return render(request, 'audit_module/audit_tl_project_split.html', {'Aud': Aud,'devp':devp})
    else:
        return redirect('/')


def Audit_DEVtable(request,audit_emp_prtask,audit_empid):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        
        Aud = user_registration.objects.filter(id=Aud_id)
        emp=user_registration.objects.get(id=audit_empid)
        task_verify = TSproject_Task_verify.objects.all()

        if emp.designation.designation == 'tester':
            devp= TSproject_Task_verify.objects.filter(ts_tester_id=audit_empid)
            ptask= project_taskassign.objects.filter(project_id=audit_emp_prtask,).filter(tester_id=audit_empid)
            testerstatus = tester_status.objects.filter(project_id=audit_emp_prtask)
            return render(request, 'audit_module/audit_tester_project.html', {'Aud': Aud,'devp':devp,'ptask':ptask,'testerstatus':testerstatus})

        elif emp.designation.designation == 'team leader':
            devp = project_taskassign.objects.filter(project_id=audit_emp_prtask,worktype='1').filter(developer_id=audit_empid).order_by("-id")
        else:
               devp = project_taskassign.objects.filter(project_id=audit_emp_prtask).filter(developer_id=audit_empid).order_by("-id")
        teststatus = test_status.objects.all()
        proj=project.objects.get(id=audit_emp_prtask)
        testerstatus = tester_status.objects.filter(project_id=audit_emp_prtask)
        
        time = datetime.now()
        action_take=wrdata.objects.all()
        return render(request, 'audit_module/audit_dev_project.html', {'Aud': Aud,'devp':devp,'teststatus':teststatus,'proj':proj,
                                                                       'testerstatus':testerstatus,'time':time,'action_take':action_take,'task_verify':task_verify})

    else:   
        return redirect('/')

    




#Project Section ------------------ audit Project page load

def Audit_project(request):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        proj= project.objects.all().order_by('-id')
        return render(request, 'audit_module/audit_projects.html', {'Aud': Aud,'proj':proj})
    else:
        return redirect('/')

def Audit_project_details(request,audit_pro_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        try:
            proj_doc = PM_ProjectDocument.objects.get(doc_project_id_id=audit_pro_id)
        except PM_ProjectDocument.DoesNotExist:
           return redirect('Audit_project')
        proj_task = project_taskassign.objects.filter(project_id=audit_pro_id)
        return render(request, 'audit_module/audit_project_details.html', {'Aud': Aud,'proj_doc':proj_doc,'proj_task':proj_task})
    else:
        return redirect('/')

def Audit_project_doc(request,prdoc_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        proj_doc = PM_ProjectDocument.objects.filter(id=prdoc_id)
        return render(request, 'audit_module/audit_project_doc_details.html', {'Aud': Aud,'proj_doc':proj_doc})
    else:
        return redirect('/')

def Audit_project_user_requirement(request,ur_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        prj=project.objects.get(id=ur_id)
        prjmodule=project_module_assign.objects.filter(project_name=prj)
        um=UserManuvel.objects.filter(user_project=prj)
        ump=UserManuvelPoints.objects.filter(userp_project=prj)
        return render(request, 'audit_module/audit_project_user_requirement.html', {'Aud': Aud,'prj':prj,'prjmodule':prjmodule,'um':um,'ump':ump})
    else:
        return redirect('/')

def Audit_project_Budgect(request,budgect_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        counts=0
        tsum=0
        pr=project.objects.get(id=budgect_id)
        event1 = Event.objects.filter(start_time__range=(pr.startdate,datetime.now().date())).count()
        prjbug = ProjectBudgect.objects.filter(pb=pr)
        ptask= project_taskassign.objects.filter(project=pr,worktype='1')
        dl= project_taskassign.objects.filter(project=pr).values('developer').distinct()
        tls=project_taskassign.objects.filter(project=pr,worktype='2').values('tl').distinct()
       
        users=user_registration.objects.all()
        for i in prjbug:
            tsum= tsum + i.pb_amount
        for i in ptask:
            counts=counts + int(i.tsakworkdays)
        devamount=counts * 400
        pdays=date.today() - pr.startdate
        pdays=pdays.days - event1
        project_days=date.today() - pr.startdate
        project_days = project_days.days - event1
        pm_salary = (project_days * 250)

        tlsal=0
        tltask= project_taskassign.objects.filter(project=pr,worktype='2')
       
        for i in tls:
            for j in tltask:
                if j.tl.id == i:
                    tlsal=tlsal + (j.tsakworkdays * 370)

        total_ex=pm_salary+tlsal+devamount
        return render(request, 'audit_module/audit_project_budgect.html', {'Aud': Aud,'prjbug':prjbug,'pr':pr,'tsum':tsum,'project_days':project_days,
            'ptask':ptask,'counts':counts,'dl':dl,'tls':tls,'users':users,'tlsal':tlsal,'devamount':devamount,'pm_salary':pm_salary,'total_ex':total_ex})
    else:
        return redirect('/')

#User manuvel pdf
    
def usermauvel_pdf(request,um_pdf):
    date = datetime.now()  
    
    projects=project.objects.get(id=um_pdf)
    um=UserManuvel.objects.filter(user_project=projects)
    ump=UserManuvelPoints.objects.filter(userp_project=projects)
    
    
   
    template_path = 'usermanuvel_pdf.html'
    context = {'projects':projects,
    'date':date,
    'um':um,
    'ump':ump,
    'settings.NEWPATH':settings.NEWPATH,
    }
        
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="User_Manuvel.pdf"'
     # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




    

def Audit_detail_project(request,pd_id):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        prj=project.objects.get(id=pd_id)
        prjmodule=project_module_assign.objects.filter(project_name=prj)
        prjtable=project_table.objects.filter(project=prj)
        prj_other= project_other_assign.objects.filter(othproject_name=prj)
        proj_task_ts= project_taskassign.objects.filter(project_id=pd_id).values('tester').distinct()
        proj_task_tl= project_taskassign.objects.filter(project_id=pd_id).values('tl').distinct()
        proj_task_dev= project_taskassign.objects.filter(project_id=pd_id).values('developer').distinct()
        user= user_registration.objects.all()
        proj_task=project_taskassign.objects.filter(project_id=pd_id)
        ts=tester_status.objects.filter(project_id=pd_id)
        ts_verify=TSproject_Task_verify.objects.all()
      
        return render(request, 'audit_module/audit_Detail_project.html', {'Aud': Aud,'prj':prj,'prjmodule':prjmodule,'prjtable':prjtable,
        'prj_other':prj_other,'proj_task_ts':proj_task_ts,'proj_task_tl':proj_task_tl,'proj_task_dev':proj_task_dev,'user':user,'proj_task':proj_task,'ts':ts,'ts_verify':ts_verify})
    else:
        return redirect('/')



# Audit Action Taken 
def Audit_action_taken(request):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)
        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()
       

        if request.method == 'POST':
            
            var=Action_Taken()
            var.atby=user_registration.objects.get(id=Aud_id)
            var.atdep=department.objects.get(id=int(request.POST['Department']))
            var.atdesig=designation.objects.get(id=int(request.POST['designation']))
            var.atemp=user_registration.objects.get(id=int(request.POST['emp']))
            var.at_remark=request.POST['reason']
            var.at_status='1'
            var.save()

        act=Action_Taken.objects.all().order_by('-id')
        return render(request, 'audit_module/audit_action_taken.html', {'Aud': Aud,'cous':cous,'dep':dep,'des':des,'emp':emp,'act':act})
    else:
        return redirect('/')


@csrf_exempt
def Audit_designation_list(request):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        
        Desig = designation.objects.filter(~Q(designation="admin")).filter(branch_id=br_id.branch_id)
        return render(request,'audit_module/audit_desig_list.html',{'Aud': Aud,'Desig': Desig})
    else:
        return redirect('/')


@csrf_exempt
def Audit_designationemp_list(request):
    if 'aud_id' in request.session:
        if request.session.has_key('aud_id'):
            Aud_id = request.session['aud_id']
        else:
            return redirect('/')
        Aud = user_registration.objects.filter(id=Aud_id)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        br_id = department.objects.get(id=dept_id)
        emps = user_registration.objects.filter(branch_id=br_id.branch_id,department=br_id, designation=desigId, status="active")

        return render(request,'audit_module/audit_desig_list.html',{'Aud': Aud,'emps': emps})
    else:
        return redirect('/')


# Tl Action Taken 
def TL_action_taken(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(id=tlid)
        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()
       

        if request.method == 'POST':
            
            var=Action_Taken()
            var.atby=user_registration.objects.get(id=tlid)
            var.atdep=department.objects.get(id=int(request.POST['Department']))
            var.atdesig=designation.objects.get(id=int(request.POST['designation']))
            var.atemp=user_registration.objects.get(id=int(request.POST['emp']))
            var.at_remark=request.POST['reason']
            var.at_status='1'
            var.save()

        act=Action_Taken.objects.filter(atby_id=tlid).order_by('-id')
        return render(request, 'TLactions_taken.html', {'mem': mem,'cous':cous,'dep':dep,'des':des,'emp':emp,'act':act})
    else:
        return redirect('/')



# Project Manager Action Taken 
def Projectmanager_action_taken(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()
       

        if request.method == 'POST':
            
            var=Action_Taken()
            var.atby=user_registration.objects.get(id=prid)
            var.atdep=department.objects.get(id=int(request.POST['Department']))
            var.atdesig=designation.objects.get(id=int(request.POST['designation']))
            var.atemp=user_registration.objects.get(id=int(request.POST['emp']))
            var.at_remark=request.POST['reason']
            var.at_status='1'
            var.save()

        act=Action_Taken.objects.filter(Q(atby_id=prid) | Q(atemp_id=prid)).order_by('-id')
        return render(request, 'Projectmanageractions_taken.html', {'pro': pro,'cous':cous,'dep':dep,'des':des,'emp':emp,'act':act})
    else:
        return redirect('/')

# Admin Action Taken
def BRadmin_action_taken(request):
    if 'Adm_id' in request.session:

        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']

        Adm = user_registration.objects.filter(id=Adm_id)
        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()
       

        if request.method == 'POST':
            
            var=Action_Taken()
            var.atby=user_registration.objects.get(id=Adm_id)
            var.atdep=department.objects.get(id=int(request.POST['Department']))
            var.atdesig=designation.objects.get(id=int(request.POST['designation']))
            var.atemp=user_registration.objects.get(id=int(request.POST['emp']))
            var.at_remark=request.POST['reason']
            var.at_status='1'
            var.save()

        act=Action_Taken.objects.all().order_by('-id')
        return render(request, 'BRadminactions_taken.html', {'Adm': Adm,'cous':cous,'dep':dep,'des':des,'emp':emp,'act':act})
    else:
        return redirect('/')

# acations taken to developer 
def DEVaction(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    devp = user_registration.objects.get(id=devid)
    action_take=wrdata.objects.filter(wrn_develp=devp)
    return render(request, 'DEVaction.html', {'dev': dev, 'devp': devp,  'action_take':action_take})



#project manager action


@csrf_exempt
def pm_leavedesgn(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="project manager"),~Q(designation="auditor"),~Q(designation="hr")).filter(branch_id=br_id.branch_id)
        return render(request,'BRadmin_leavedesgn.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')
    

@csrf_exempt
def pm_emp_ajax(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        br_id = department.objects.get(id=dept_id)
        Desig = user_registration.objects.filter(branch_id=br_id.branch_id, designation=desigId, status="active")

        return render(request,'BRadmin_emp_ajax.html',{'pro': pro,'Desig': Desig,})
    else:
        return redirect('/')







#Tl action 
@csrf_exempt
def tl_leavedesgn(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(id=tlid)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="team leader"),~Q(designation="project manager"),~Q(designation="auditor"),~Q(designation="hr")).filter(branch_id=br_id.branch_id)
        return render(request,'BRadmin_leavedesgn.html',{'mem': mem,'Desig': Desig})
    else:
        return redirect('/')


@csrf_exempt
def tl_emp_ajax(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(id=tlid)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        br_id = department.objects.get(id=dept_id)
        Desig = user_registration.objects.filter(branch_id=br_id.branch_id, designation=desigId, status="active")

        return render(request,'BRadmin_emp_ajax.html',{'mem': mem,'Desig': Desig,})
    else:
        return redirect('/')



#======================= Start Data Colletor Section ==========================================================================


# Data Collector  Dashboard created on 17-03-2023
def DatacollectorDashboard(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        return render(request, 'data_collection/data_dashboard.html', {'data_collect': data_collect,'ldcount':ldcount})
    else:
        return redirect('/')



 
# Data Collector password Change

def Datacollector_changepwd(request):
    
    if 'datacollector_id' in request.session:
        
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']     
        data_collect = user_registration.objects.filter(id=data_colletor_id)     
        if request.method == 'POST':
            abc = user_registration.objects.get(id=data_colletor_id)
            cur = abc.password
            oldps = request.POST["currentPassword"]
            newps = request.POST["newPassword"]
            cmps = request.POST["confirmPassword"]
            if oldps == cur:
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request, 'data_collection/data_dashboard.html', {'data_collect': data_collect})
                elif oldps == newps:
                    messages.add_message(request, messages.INFO, 'Current and New password same')
                else:
                    messages.info(request, 'Incorrect password same')

                return render(request, 'data_collection/data_dashboard.html', {'data_collect': data_collect})
            else:
                messages.add_message(request, messages.INFO, 'old password wrong')
                return render(request, 'data_collection/datacolltor_change.html', {'data_collect': data_collect})
        return render(request, 'data_collection/datacolltor_change.html', {'data_collect': data_collect})         
    else:
        return redirect('/')



#******************** Data Colletor account setting****************************
def Datacollector_accsetting(request):
    if 'datacollector_id' in request.session:
        
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        return render(request,'data_collection/data_accsetting.html', {'data_collect': data_collect})
    else:
        return redirect('/')

def Datacollector_accsettingimagechange(request,id):
    if 'datacollector_id' in request.session:
        
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('Datacollector_accsetting')
        return render(request,'data_collection/data_accsetting.html', {'data_collect': data_collect})
    else:
        return redirect('/')



# Data Collector  logout
def Datacollectorlogout(request):
    if 'datacollector_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


def datacollector_leads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        cur_date=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ldassign = Leads_Register.objects.filter(r_assign_status = 1).count()
        ldpending = Leads_Register.objects.filter(r_assign_status = 0).count()
        ldcomplete = Leads_Register.objects.filter(r_status = 1).count()
        tdldcount = Leads_Register.objects.filter(r_date=cur_date).count()
        tdassingedldcount = Leads_Register.objects.filter(r_assign_status = 1,r_date=cur_date).count()
        tdassingldcount = Leads_Register.objects.filter(r_assign_status = 0,r_date=cur_date ).count()
        content= {'tdldcount':tdldcount,'tdassingldcount':tdassingldcount,'tdassingedldcount':tdassingedldcount}
        return render(request, 'data_collection/datacollector_leads.html', {'data_collect': data_collect,'ldcount':ldcount,'ldcomplete':ldcomplete,'content':content,'ldassign':ldassign,'ldpending':ldpending})
    else:
        return redirect('/')



def datacollector_registerleads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ld = Leads_Register.objects.all()
        return render(request, 'data_collection/datacollector_registerleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')


def datacollector_Registered_search(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)

        if request.method == 'POST':

            ld = Leads_Register.objects.filter(r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate'])
       
        return render(request, 'data_collection/datacollector_registerleads.html', {'data_collect': data_collect,'ld':ld})
    else:
        return redirect('/')



        

def datacollector_assingnedleads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ld = Leads_Register.objects.filter(r_assign_status = 1)
        return render(request, 'data_collection/datacollector_assignedleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')


def datacollector_assingnedleads_search(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)

        if request.method == 'POST':

            ld = Leads_Register.objects.filter(r_assign_status = 1,r_assign_date__gte=request.POST['assing_stdate'], r_assign_date__lte=request.POST['assing_enddate'])
         
        return render(request, 'data_collection/datacollector_assignedleads.html', {'data_collect': data_collect,'ld':ld})
    else:
        return redirect('/')


    

def datacollector_pendingleads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ld = Leads_Register.objects.filter(r_assign_status = 0)
        return render(request, 'data_collection/datacollector_pendingleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')

def datacollector_completed_leads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ld = Leads_Register.objects.filter(r_status = 1)
        return render(request, 'data_collection/datacollector_completedleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')


    


def datacollector_assignleads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        desig= designation.objects.filter(designation='hr')
        user_details= user_registration.objects.filter(designation__in=desig)
        ld = Leads_Register.objects.filter(r_assing_id__isnull=True)
        return render(request, 'data_collection/datacollector_assignleads.html', {'data_collect': data_collect,'ldcount':ldcount,'user_details':user_details,'desig':desig,'ld':ld})
    else:
        return redirect('/')
    

# current day details

def datacollector_todyregisterleads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        today=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.filter(r_date=today).count()
        ld = Leads_Register.objects.filter(r_date=today) 
        return render(request, 'data_collection/datacollector_registerleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')


def datacollector_todyassignedleads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        today=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.filter(r_assign_date=today,r_assign_status = 1).count()
        ld= Leads_Register.objects.filter(r_assign_date=today,r_assign_status = 1)
        return render(request, 'data_collection/datacollector_assignedleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')

def datacollector_todypendingleads(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        today=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.filter(r_date=today,r_assign_status = 0).count()
        ld = Leads_Register.objects.filter(r_date=today,r_assign_status = 0)
        return render(request, 'data_collection/datacollector_pendingleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')


def data_assign_collector(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        
        if request.method == 'POST':
            collector_id = user_registration.objects.get(id=int(request.POST['data_colector']))
           
            checked_data = request.POST.getlist('select_check_id')
            if checked_data:
                for i in checked_data:
                    ld = Leads_Register.objects.get(id=i)
                    ld.r_assing_id = user_registration.objects.get(id=collector_id.id)
                    ld.r_assign_status=1
                    ld.save()
                    return redirect('datacollector_assignleads')

            else:
                    print('No data selected')
                    messages.warning(request, 'No data selected. Please  check  Atlest  one  data  from  the  table  to  assign')
                    return redirect('datacollector_assignleads')
                   

            # data_collect = user_registration.objects.filter(id=data_colletor_id)
            # ldcount = Leads_Register.objects.all().count()
           
    else:
        return redirect('/')


def data_collector_register_save(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')

        if request.method == 'POST':
            if  Leads_Register.objects.filter(r_email=request.POST['dc_email']).exists() or Leads_Register.objects.filter(r_phno=request.POST['dc_phno']).exists():
                
                print('Duplicate Data Found')

            else:

                ld = Leads_Register()
                ld.r_fullname = request.POST['dc_name']
                ld.r_email = request.POST['dc_email']
                ld.r_phno = request.POST['dc_phno']
                ld.r_place = request.POST['dc_place']
                ld.r_dese = request.POST['dc_other']
                ld.r_refference = user_registration.objects.get(id=data_colletor_id)
                ld.r_assign_date = date.today()
                ld.save()

        else:
            print('Error, No data')


        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ld = Leads_Register.objects.all()
        return render(request, 'data_collection/datacollector_registerleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')



#data collector Employeee section

def datacollector_employees(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        today=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.filter(r_date=today,r_assign_status = 0).count()
        ld = Leads_Register.objects.filter(r_assign_status = 1).values_list('r_assing_id', flat=True).distinct()
       
        lddata =  user_registration.objects.all()
       
        return render(request, 'data_collection/datacollector_employee.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld,'lddata':lddata})
    else:
        return redirect('/')


def data_collector_datas(request,pk):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        today=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        data_collector = user_registration.objects.get(id=pk)
        ldregcount = Leads_Register.objects.filter(r_refference=pk).count()
        ldassignedcount = Leads_Register.objects.filter(r_assing_id=pk).count()
        ldpencount = Leads_Register.objects.filter(Q(r_status=3) | Q(r_status=0),r_assing_id=pk).count()
        ldcompletecount = Leads_Register.objects.filter(r_status=1,r_assing_id=pk).count()
        ld = Leads_Register.objects.filter(r_refference=pk)
 
        return render(request, 'data_collection/datacollector_employee_datas.html', {'data_collect': data_collect,'data_collector':data_collector,
        'ldregcount':ldregcount,'ld':ld,'ldassignedcount':ldassignedcount,'ldpencount':ldpencount,'ldcompletecount':ldcompletecount})
    else:
        return redirect('/')




def data_collector_datas_serach(request,pk):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        today=date.today()
        data_collector = user_registration.objects.get(id=pk)
        if request.method == 'POST':
            data_collect = user_registration.objects.filter(id=data_colletor_id)

            if request.POST['check_id']:
                check=int(request.POST['check_id'])
            else:
                 check=1
            print(check)

            ldregcount = Leads_Register.objects.filter(r_refference=pk,r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate']).count()
            ldassignedcount = Leads_Register.objects.filter(r_assing_id=pk,r_assign_date__gte=request.POST['register_stdate'], r_assign_date__lte=request.POST['register_enddate'],r_assign_status = 1).count()
            ldpencount = Leads_Register.objects.filter(Q(r_status=3) | Q(r_status=0),r_assing_id=pk,r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate']).count()
            ldcompletecount = Leads_Register.objects.filter(r_status=1,r_assing_id=pk,r_completed_date__gte=request.POST['register_stdate'], r_completed_date__lte=request.POST['register_enddate']).count()
            ld = Leads_Register.objects.filter(r_refference=pk,r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate'])


            if check == 1:
                ld = Leads_Register.objects.filter(r_refference=pk,r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate'])
            elif check == 2:
                ld = Leads_Register.objects.filter(r_assing_id=pk,r_assign_date__gte=request.POST['register_stdate'], r_assign_date__lte=request.POST['register_enddate'],r_assign_status = 1)
            elif check == 3:
                ld = Leads_Register.objects.filter(Q(r_status=3) | Q(r_status=0),r_assing_id=pk,r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate'])
            else:
                check=4
                ld = Leads_Register.objects.filter(r_status=1,r_assing_id=pk,r_completed_date__gte=request.POST['register_stdate'], r_completed_date__lte=request.POST['register_enddate'])



            return render(request, 'data_collection/datacollector_employee_datas.html', {'data_collect': data_collect,'data_collector':data_collector,
            'ldregcount':ldregcount,'ld':ld,'ldassignedcount':ldassignedcount,'ldpencount':ldpencount,'ldcompletecount':ldcompletecount,'check':check})
        else:
            return redirect('data_collector_datas',data_collector.id)
    else:
        return redirect('/')



def datacollector_datas_check(request,pk,check):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
                data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        today=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        data_collector = user_registration.objects.get(id=pk)
        ldregcount = Leads_Register.objects.filter(r_refference=pk).count()
        ldassignedcount = Leads_Register.objects.filter(r_assing_id=pk).count()
        ldpencount = Leads_Register.objects.filter(Q(r_status=3) | Q(r_status=0),r_assing_id=pk).count()
        ldcompletecount = Leads_Register.objects.filter(r_status=1,r_assing_id=pk).count()

        if check == 1:
            ld = Leads_Register.objects.filter(r_refference=pk)
        elif check == 2:
            ld = Leads_Register.objects.filter(r_assing_id=pk)
        elif check == 3:
             ld = Leads_Register.objects.filter(Q(r_status=3) | Q(r_status=0),r_assing_id=pk)
        else:
            check=4
            ld = Leads_Register.objects.filter(r_status=1,r_assing_id=pk)

    
        return render(request, 'data_collection/datacollector_employee_datas.html', {'data_collect': data_collect,'data_collector':data_collector,
            'ldregcount':ldregcount,'ld':ld,'ldassignedcount':ldassignedcount,'ldpencount':ldpencount,'ldcompletecount':ldcompletecount,'check':check})
    else:
        return redirect('/')




#Data Collector Analiyis Section
def datacollector_analiyis(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        cur_date=date.today()
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ldassign = Leads_Register.objects.filter(r_assign_status = 1).count()
        ldpending = Leads_Register.objects.filter(r_assign_status = 0).count()
        tdldcount = Leads_Register.objects.filter(r_date=cur_date).count()
        tdassingedldcount = Leads_Register.objects.filter(r_assign_status = 1,r_date=cur_date).count()
        tdassingldcount = Leads_Register.objects.filter(r_assign_status = 0,r_date=cur_date ).count()
        tdcomplete = Leads_Register.objects.filter(r_status = 1 ).count()

        return render(request, 'data_collection/datacollector_analiyis.html', {'data_collect': data_collect,'ldcount':ldcount,'ldassign':ldassign,'ldpending':ldpending,'tdcomplete':tdcomplete})
    else:
        return redirect('/')



def datacollector_lead_analiyisearch(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        cur_date=date.today()

        if request.method == 'POST':

           
            ldcount = Leads_Register.objects.filter(r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate']).count()
            ldassign = Leads_Register.objects.filter(r_assign_date__gte=request.POST['register_stdate'], r_assign_date__lte=request.POST['register_enddate'],r_assign_status = 1).count()
            ldpending = Leads_Register.objects.filter(r_date__gte=request.POST['register_stdate'], r_date__lte=request.POST['register_enddate'],r_assign_status = 0).count()
           
            tdcomplete = Leads_Register.objects.filter(r_completed_date__gte=request.POST['register_stdate'], r_completed_date__lte=request.POST['register_enddate'],r_status = 1 ).count()

        return render(request, 'data_collection/datacollector_analiyis.html', {'data_collect': data_collect,'ldcount':ldcount,'ldassign':ldassign,'ldpending':ldpending,'tdcomplete':tdcomplete})
       
       
    else:
        return redirect('/')




def lead_fileupload(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        ldcount = Leads_Register.objects.all().count()
        ld = Leads_Register.objects.all()
        if request.method == 'POST':
            file_up=request.FILES.get('leadfile')
            
            df = pd.read_excel(file_up)
            for _, row in df.iterrows():
                if Leads_Register.objects.filter(Q(r_email=row['email'])| Q(r_phno=row['phno'])).exists():

                    print('Duplicate Data Found')
                else:

                    obj = Leads_Register()
                    obj.r_fullname=row['Name']
                    obj.r_email=row['email']
                    obj.r_phno=row['phno']
                    obj.r_place=row['place']
                    obj.r_dese=row['details']
                    obj.r_refference=  user_registration.objects.get(id=data_colletor_id)
                    obj.save()


        return render(request, 'data_collection/datacollector_registerleads.html', {'data_collect': data_collect,'ldcount':ldcount,'ld':ld})
    else:
        return redirect('/')


#leave Section
def data_leave(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        
        data_collect = user_registration.objects.filter(id=data_colletor_id)

        return render(request, 'data_collection/data_leave.html', {'data_collect': data_collect})
    else:
        return redirect('/')



def data_leave_form(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        
        data_collect = user_registration.objects.filter(id=data_colletor_id)
       

        return render(request, 'data_collection/data_leave_form.html', {'data_collect': data_collect})
    else:
        return redirect('/')


def data_leave_apply(request):
    if 'datacollector_id' in request.session:
        if request.session.has_key('datacollector_id'):
            data_colletor_id = request.session['datacollector_id']
        else:
            return redirect('/')
        data_collect = user_registration.objects.filter(id=data_colletor_id)
        data_id = user_registration.objects.get(id=int(request.POST['dev_id']))
    
        if request.method == "POST":
            leaves = leave()
            leaves.from_date = request.POST['from']
            leaves.to_date = request.POST['to']
            leaves.leave_status = request.POST['haful']
            leaves.reason = request.POST['reason']
            leaves.leaveapprovedstatus=0
            leaves.user_id = request.POST['dev_id']
            leaves.designation_id = data_id.id
            
            start = datetime.strptime(leaves.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(leaves.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                leaves.days = 1
            else:
                leaves.days = diff - cnt
                
            leaves.save()
            return render(request, 'data_collection/data_leave.html', {'data_collect': data_collect})
        else:
            return render(request, 'data_collection/data_leave_form.html', {'data_collect': data_collect})
    else:
        return redirect('/')




def data_collectorleaverequiest(request):
    if 'datacollector_id' in request.session:
            if request.session.has_key('datacollector_id'):
                data_colletor_id = request.session['datacollector_id']
            else:
                return redirect('/')
            data_collect = user_registration.objects.filter(id=data_colletor_id)
            data_col = leave.objects.filter(user_id=data_colletor_id)
       
            return render(request, 'data_collection/data_leave_requests.html', {'data_collect': data_collect, 'data_col': data_col})
    else:
        return redirect('/')





