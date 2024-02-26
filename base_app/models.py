from email.policy import default
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models
# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
# Create your models here.


class branch_registration(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    branch_admin = models.CharField(max_length=100)
    branch_type = models.CharField(max_length=100)
    mobile  = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="")
    logo = models.FileField(upload_to='images/', null=True, blank=True,default="")
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.branch_name





class department(models.Model):
    branch = models.ForeignKey(branch_registration, on_delete=models.SET_NULL,
                               related_name='departmentbranch', null=True, blank=True)
    department = models.CharField(max_length=100)
   
    files=models.FileField(upload_to = 'images/', null=True, blank=True)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.department

class designation(models.Model):
    department = models.ForeignKey(department, on_delete=models.SET_NULL , related_name='departmentbranch',null=True,blank=True)
    branch = models.ForeignKey(branch_registration, on_delete=models.SET_NULL,
                               related_name='designationbranch', null=True, blank=True)
    designation = models.CharField(max_length=100)
   
    files=models.FileField(upload_to = 'images/', null=True, blank=True)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.designation

class Batch(models.Model):
    batch_name=models.CharField(max_length=200,default='Batch')
    bt_start_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    bt_end_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    bt_status=models.CharField(max_length=20,default='0')

class create_team(models.Model):
    bt_name=models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200)
    trainer = models.CharField(max_length=200, default='')
    progress = models.IntegerField()
    status = models.CharField(max_length=200)
    team_count = models.IntegerField(default=0)
    team_status = models.CharField(max_length=200, default='0')
    trainer_id = models.CharField(max_length=200,null=True, blank=True, default='')
    startdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)


    def __str__(self):
        return self.name

class course(models.Model):
    name=models.CharField(max_length=200)
    total_fee=models.IntegerField()

    def _str_(self):
        return self.name

class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.SET_NULL,
                                    related_name='userregistrationdesignation', null=True, blank=True)
    department = models.ForeignKey(department, on_delete=models.SET_NULL,
                                   related_name='userregistrationdepartment', null=True, blank=True)
    branch = models.ForeignKey(branch_registration, on_delete=models.SET_NULL,
                               related_name='userregistrationbranch', null=True, blank=True,default=1)
    team = models.ForeignKey(create_team, on_delete=models.SET_NULL,
                             related_name='userregistrationteam', null=True, blank=True)
    course = models.ForeignKey(course, on_delete=models.SET_NULL, related_name='course_name',null=True,blank=True)
    fullname = models.CharField(max_length=240, null=True)
    employee_type = models.CharField(max_length=15, null=True, default='0')
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=50, null=True)
    employee_id = models.CharField(max_length=240,null=True,default='')
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default="active")
    tl_id = models.IntegerField(default='0',null=True, blank=True)
    projectmanager_id = models.IntegerField(default='0',null=True, blank=True)
    total_pay=models.IntegerField(default='0')
    payment_balance = models.IntegerField( default='0')
    account_no = models.CharField(max_length=200, null=True,blank=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True,blank=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='')
    payment_status = models.CharField(max_length=200, null=True, default='')
    offerqr = models.CharField(max_length=500, default='',null=True,blank=True)
    relieveqr = models.CharField(max_length=500, default='',null=True,blank=True)
    expqr = models.CharField(max_length=500, default='',null=True,blank=True)
    hrmanager = models.CharField(max_length=500, default='',null=True,blank=True)
    confirm_salary = models.CharField(max_length=10, default='')
    confirm_salary_status = models.CharField(max_length=255, default='0')
    payment_file_downlod = models.FileField(upload_to = 'images/', null=True, blank=True)
    total_amount=models.IntegerField(default='0')
    payment_amount_date =models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    salary_pending = models.CharField(max_length=100, default='')
    salary_status =  models.CharField(max_length=10, default='')
    trainer_level = models.CharField(max_length=20, default='',null=True, blank=True)
    hr_designation = models.CharField(max_length=120, default='',null=True, blank=True)
    reg_status =  models.CharField(max_length=10, default='0')
    trainee_delay=models.IntegerField(default=0)
    work_status =  models.CharField(max_length=10, default='')
    desig_input = models.CharField(max_length=30, default='')
    department_input=models.CharField(max_length=30, default='')
    trainee_status = models.IntegerField(default='0')
  
   
 
    def __str__(self):
        return self.fullname

    @property
    def avg(self):
        return (self.attitude+self.creativity+self.workperformance)/3
    

class extracurricular(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='extracurricularuser', null=True, blank=True)
    internshipdetails = models.CharField(max_length=240, null=True)
    internshipduration = models.CharField(max_length=240, null=True)
    internshipcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    onlinetrainingdetails = models.CharField(max_length=240, null=True)
    onlinetrainingduration = models.CharField(max_length=240, null=True)
    onlinetrainingcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    projecttitle = models.CharField(max_length=240, null=True)
    projectduration = models.CharField(max_length=240, null=True)
    projectdescription = models.TextField(null=True)
    projecturl = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill1 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill2 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill3 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    status = models.CharField(max_length=240, default='')


    def __str__(self):
        return self.projecttitle


class qualification(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='qualificationuser', null=True, blank=True)
    plustwo = models.CharField(max_length=240, null=True)
    schoolaggregate = models.CharField(max_length=240, null=True)
    schoolcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    ugdegree = models.CharField(max_length=240, null=True)
    ugstream = models.CharField(max_length=240, null=True)
    ugpassoutyr = models.CharField(max_length=240, null=True)
    ugaggregrate = models.CharField(max_length=240, null=True)
    backlogs = models.CharField(max_length=240, null=True)
    ugcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    pg = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.user


class project(models.Model):
    
    projectmanager = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='projectuser', null=True, blank=True)
    designation = models.ForeignKey(
        designation, on_delete=models.SET_NULL, related_name='projectdesignation', null=True, blank=True)
    department = models.ForeignKey(
        department, on_delete=models.SET_NULL, related_name='projectdepartment', null=True, blank=True)
    tester = models.ForeignKey(user_registration, on_delete=models.SET_NULL, 
                               related_name='projecttester',null=True,blank=True,default='')
    branch = models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING,
                               related_name='branch', null=True, blank=True, default='')
    project = models.CharField(max_length=100,  null=True, blank=True)
    rejectdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    files = models.FileField(upload_to='images/', null=True, blank=True)
    uifile = models.FileField(upload_to='images/', null=True, blank=True)
    progress = models.CharField(max_length=100)
    user_reason = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.project


class project_taskassign(models.Model):
    project = models.ForeignKey(project, on_delete=models.SET_NULL,
                                related_name='project_taskassignproject', null=True, blank=True)
    developer = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='project_taskassignuser', null=True, blank=True)
    tl = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                           related_name='project_taskassigntl', null=True, blank=True)
    teamleader = models.CharField(max_length=200, null=True, blank=True),                    
    tester = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                               related_name='project_taskassign_tester', null=True, blank=True)
    description = models.TextField()
    projmodule=models.CharField(max_length=150, null=True, blank=True)
    task = models.CharField(max_length=200, null=True, blank=True)
    subtask = models.CharField(max_length=200, null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    files = models.FileField(upload_to='images/', null=True, blank=True)
    extension = models.IntegerField(null=True, blank=True,default='0')
    reason = models.TextField(null=True, blank=True)
    extension_status = models.CharField(max_length=200, null=True, blank=True)
    extension_date= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    tl_description = models.CharField(max_length=200, null=True, blank=True)
    submitted_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    employee_files = models.FileField(
        upload_to='images/', null=True, blank=True)
    employee_description = models.TextField(null=True, blank=True)
    designation=models.CharField(max_length=200,null=True,blank=True)
    department=models.CharField(max_length=200,null=True,blank=True)
    progress = models.IntegerField(default='0', null=True) 
    projectstatus = models.CharField(max_length=200, null=True, blank=True,default="In progress")
    status = models.CharField(max_length=200, null=True, blank=True)
    delay = models.CharField(max_length=200, null=True,default="")
    git_link = models.TextField(null=True,default='')
    workaccept = models.FileField(upload_to='images/', null=True, blank=True,default="0")
    worktype = models.CharField(max_length=15, null=True,default="0")
    tsakworkdays= models.IntegerField(default='0', null=True) 
    tsakdelaydays= models.IntegerField(default='0', null=True) 
    tester_delay = models.IntegerField(default='0', null=True) 
    

    def __str__(self):
        return self.project.project

class test_status(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='test_statususer', null=True, blank=True)
    project = models.ForeignKey(project, on_delete=models.SET_NULL,
                                related_name='test_statusproject', null=True, blank=True)
    subtask = models.ForeignKey(project_taskassign, on_delete=models.SET_NULL,
                                 related_name='test_statustaskname', null=True, blank=True)
    taskname = models.ForeignKey(user_registration, on_delete=models.SET_NULL, 
                                 related_name='test_statustaskname',null=True,blank=True)
    date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    workdone = models.TextField(null=True)
    json=models.FileField(upload_to = 'images/', null=True, blank=True)
    json_testerscreenshot = JSONField(blank=True, null=True)
    git_commit = models.TextField(null=True, blank=True, default='')
    git_link= models.TextField(null=True, blank=True, default='')


    def __str__(self):
        return self.project.project
    
class tester_status(models.Model):
    tester = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                               related_name='tester_statustester', null=True, blank=True)
    project = models.ForeignKey(project, on_delete=models.SET_NULL,
                                related_name='tester_statusproject', null=True, blank=True)
    task = models.ForeignKey(project_taskassign, on_delete=models.SET_NULL,
                             related_name='tester_statustask', null=True, blank=True)
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='tester_statususer', null=True, blank=True)
    subtask = models.ForeignKey(project_taskassign, on_delete=models.SET_NULL, 
                                related_name='tester_statussubtask',null=True,blank=True)
    date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    workdone = models.TextField(max_length=200, null=True, blank=True)
    files = models.FileField(upload_to='images/', null=True, blank=True)
    progress = models.IntegerField()
    status = models.CharField(max_length=200, null=True, blank=True)

   
    def __str__(self):
        return self.project.project


class reported_issue(models.Model):
    reporter = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                                 related_name='reported_issuereporter', null=True, blank=True)
    reported_to = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                                    related_name='reported_issuereported_to', null=True, blank=True)
    issue = models.TextField()
    reported_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    reply = models.TextField()
    status = models.CharField(max_length=200)
    issuestatus = models.CharField(max_length=200)
    designation_id = models.CharField(max_length=200)


    def __str__(self):
        return self.reporter


class attendance(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='attendanceuser', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
    status = models.CharField(max_length=200)
    attendance_status = models.CharField(max_length=200)




class leave(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='leaveuser', null=True, blank=True)
    from_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    to_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    reason = models.TextField()
    leave_status = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    designation_id = models.CharField(max_length=200)
    leaveapprovedstatus = models.CharField(max_length=200, default="0")
    leave_rejected_reason = models.CharField(max_length=300)
    days = models.IntegerField(default=0)

    
    def __str__(self):
        return self.user

class internship_type(models.Model):
    type = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)    


class internship(models.Model):
    branch = models.ForeignKey(branch_registration, on_delete=models.SET_NULL,
                               related_name='internshipbranch', null=True, blank=True)
    reg_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    fullname = models.CharField(max_length=200)
    collegename = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    stream = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    alternative_no = models.CharField(max_length=200)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    attach_file = models.FileField(upload_to='images/', null=True, blank=True)
    rating = models.CharField(max_length=200)
    hrmanager = models.CharField(max_length=200)
    guide = models.CharField(max_length=200)
    qr = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=200)
    complete_status =models.CharField(max_length=10,default='0')
    verify_status =models.CharField(max_length=10,default='0')
    total_fee = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    pay_date = models.DateField(null=True, blank=True)
    balance = models.IntegerField(default=0)
    total_pay =models.IntegerField(default=0)
    internshiptype = models.ForeignKey(internship_type,on_delete=models.SET_NULL,related_name='internship_type', null=True, blank=True)    

    
    def __str__(self):
        return self.fullname

class internship_paydata(models.Model):
    date = models.DateField()
    internship_user = models.ForeignKey(internship,on_delete=models.SET_NULL,
                             related_name='internship_user', null=True, blank=True)
    amount = models.IntegerField()  


class trainer_task(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='trainer_task_trainee', null=True, blank=True)
    team_name = models.ForeignKey(
        create_team, on_delete=models.SET_NULL, related_name='team_name', null=True, blank=True)
    taskname = models.CharField(max_length=240)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    submitteddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    files = models.FileField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=240)
    user_description = models.TextField(max_length=240)
    user_files = models.FileField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=200)
    task_status = models.CharField(max_length=200)
    task_progress = models.IntegerField(default=0)
    delay = models.IntegerField(default=0)
    task_type = models.CharField(max_length=10,default='0')
    
    

    def __str__(self):
        return self.trainee
    
class Trainer_Task_Correction(models.Model):
    task_id = models.ForeignKey(trainer_task, on_delete=models.SET_NULL,
                             related_name='trainer_task', null=True, blank=True)
    correctiondate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    correction_description = models.TextField(max_length=240)
    correctionfiles = models.FileField(upload_to='images/', null=True, blank=True)


    

# Trainee Task test by Trainer
class trainer_task_test(models.Model):

    team_name = models.ForeignKey(
        create_team, on_delete=models.SET_NULL, related_name='team_name_trainer', null=True, blank=True)
    trainer = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='trainer_task', null=True, blank=True)
    trainee = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='trainee_task', null=True, blank=True)
    traine_task = models.ForeignKey (trainer_task, on_delete=models.SET_NULL, related_name='ttname', null=True, blank=True)
    test_task_type=models.CharField(max_length=25,default='0')
    trainer_correction = models.TextField()
    trainer_files = models.FileField(upload_to='images/', null=True, blank=True)
    t_status =models.CharField(max_length=50,default='')
    sub_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    test_date = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)


class topic(models.Model):
    trainee = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                                related_name='topictrainee', null=True, blank=True, default='')
    trainer = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                                related_name='topictrainer', null=True, blank=True)
    team = models.ForeignKey(create_team, on_delete=models.SET_NULL,
                             related_name='topicteam', null=True, blank=True)
    topic = models.CharField(max_length=240)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    files = models.FileField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    review = models.TextField()
    status = models.CharField(max_length=200)
    topic_status = models.CharField(max_length=200)

    
    def __str__(self):
        return self.topic

class tasks(models.Model):
    department = models.ForeignKey(department, on_delete=models.SET_NULL, related_name='taskdepartment',null=True,blank=True)
    designation = models.ForeignKey(designation, on_delete=models.SET_NULL, related_name='taskdesignation',null=True,blank=True)
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='taskuser',null=True,blank=True)
    tasks = models.CharField(max_length=240)
    startdate= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    files=models.FileField(upload_to = 'images/', null=True, blank=True)
    description = models.TextField()
    status =  models.CharField(max_length=200)
    
    


class paymentlist(models.Model):
    user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='userpay',null=True,blank=True)
    amount_pay = models.IntegerField(default='0')
    amount_date =models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    current_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    amount_status = models.CharField(max_length=200, null=True)
    amount_downlod = models.FileField(upload_to = 'images/', null=True, blank=True)
    balance_amt = models.IntegerField(default='0')
    course = models.ForeignKey(course, on_delete=models.SET_NULL, related_name='total',null=True,blank=True, default='')

    @property
    def balance(self):
        return (self.course.total_fee-self.amount_pay)
    

# class acntspayslip(models.Model):

#     basic_salary = models.IntegerField()
#     eno = models.CharField(max_length=100) 
#     user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='user',null=True,blank=True)
#     designation = models.ForeignKey(designation, on_delete=models.SET_NULL, related_name='desic',null=True,blank=True)
#     department =models.ForeignKey(department, on_delete=models.SET_NULL, related_name='dept',null=True,blank=True)
#     hra = models.IntegerField()
#     conveyns = models.CharField(max_length=100)
#     tax = models.IntegerField()
#     incentives = models.IntegerField()
#     fromdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
#     todate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
#     taxengine = models.CharField(max_length=100) 
#     incometax = models.IntegerField() 
#     uan = models.CharField(max_length=100) 
#     pf = models.IntegerField() 
#     esi = models.CharField(max_length=100)  
#     pro = models.CharField(max_length=100) 
#     leavesno = models.IntegerField() 
#     pf_tax = models.IntegerField()
#     delay = models.IntegerField()
#     basictype =  models.CharField(max_length=255,default='')
#     hratype = models.CharField(max_length=255,default='')
#     contype = models.CharField(max_length=255,default='')
#     protype = models.CharField(max_length=255,default='')
#     instype = models.CharField(max_length=255,default='')
#     deltype = models.CharField(max_length=255,default='')
#     leatype = models.CharField(max_length=255,default='')
#     pftype =  models.CharField(max_length=255,default='')
#     esitype =  models.CharField(max_length=255,default='')

class acntspayslip(models.Model):

    basic_salary = models.IntegerField(default='0')
    eno = models.CharField(max_length=100) 
    user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='user',null=True,blank=True)
    designation = models.ForeignKey(designation, on_delete=models.SET_NULL, related_name='desic',null=True,blank=True)
    department =models.ForeignKey(department, on_delete=models.SET_NULL, related_name='dept',null=True,blank=True)
    hra = models.IntegerField(default='0')
    conveyns = models.CharField(max_length=100)
    tax = models.IntegerField(default='0')
    incentives = models.IntegerField(default='0')
    fromdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    todate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    taxengine = models.CharField(max_length=100) 
    incometax = models.IntegerField(default='0') 
    uan = models.CharField(max_length=100) 
    pf = models.IntegerField(default='0') 
    esi = models.CharField(max_length=100)  
    pro = models.CharField(max_length=100) 
    leavesno = models.IntegerField(default='0') 
    pf_tax = models.IntegerField(default='0')
    delay = models.IntegerField(default='0')
    other_allovance = models.IntegerField(default='0')
    basictype =  models.CharField(max_length=255,default='')
    hratype = models.CharField(max_length=255,default='')
    other_allovancetype = models.CharField(max_length=255,default='')
    contype = models.CharField(max_length=255,default='')
    protype = models.CharField(max_length=255,default='')
    instype = models.CharField(max_length=255,default='')
    deltype = models.CharField(max_length=255,default='')
    leatype = models.CharField(max_length=255,default='')
    pftype =  models.CharField(max_length=255,default='')
    esitype =  models.CharField(max_length=255,default='')
    # duedate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    pending_status = models.CharField(max_length=25, default='0')
    net_salary = models.IntegerField(null=True, default=0)
    da = models.IntegerField(null=True, default=0)
    account_no = models.CharField(max_length=200, null=True,blank=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True,blank=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='')


class Salary_hold(models.Model):
    sal_id = models.ForeignKey(acntspayslip, on_delete=models.SET_NULL, related_name='salarys',null=True,blank=True)
    hddate = models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    sal_reason= models.TextField()
    sal_amount = models.IntegerField(null=True, default=0)
    sal_status = models.CharField(max_length=50,default='')

class acntexpensest (models.Model):
    payee =models.CharField(max_length=100)
    payacnt=models.CharField(max_length=200)
    paymethod =models.CharField(max_length=100)
    paydate=models.CharField(max_length=100)
    refno=models.CharField(max_length=100)
    amount =models.IntegerField()
    tax=models.IntegerField()
    total=models.IntegerField()
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=100)

class acnt_monthdays(models.Model): 
    month_fromdate = models.DateField(null=True, blank=True)
    month_todate = models.DateField(null=True, blank=True) 
    month_workingdays = models.IntegerField()
    month_holidays = models.IntegerField()    


class conditions(models.Model):
    condition1=models.CharField(max_length=1000)
    condition2=models.CharField(max_length=1000)
    condition3=models.CharField(max_length=1000)
    condition4=models.CharField(max_length=1000)
    condition5=models.CharField(max_length=1000)
    condition6=models.CharField(max_length=1000)
    
    
class previousTeam(models.Model):
    teamname = models.ForeignKey(create_team, on_delete=models.SET_NULL, related_name='teamname', null=True, blank=True)
    user =  models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='user1',null=True,blank=True)
    tr_start_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    tr_end_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    pstatus = models.CharField(max_length=200)
    progress = models.IntegerField(default='0')
    


class Promissory(models.Model):
    user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='promissory_user',null=True,blank=True)
    inital_amount=models.CharField(max_length=100,null=True, blank=True ,default='')
    inital_paid_on=models.CharField(max_length=100,null=True, blank=True ,default='')
    inital_paid_amount=models.CharField( max_length=100,null=True, blank=True,default='')
    inital_paid_date=models.CharField(max_length=100,null=True, blank=True ,default='')
    inital_balance_amount=models.CharField(max_length=100,null=True, blank=True,default='')
    inital_due_date=models.CharField(max_length=100,null=True, blank=True ,default='')
    inital_total_payment=models.IntegerField(default='0')
    
    second_amount=models.CharField(max_length=100,null=True, blank=True,default='')
    second_due_date_on=models.CharField(max_length=100,null=True, blank=True ,default='')
    second_due_on=models.CharField(max_length=100,null=True, blank=True ,default='')
    second_paid_amount=models.CharField(max_length=100,null=True, blank=True,default='')
    second_paid_date=models.CharField(max_length=100,null=True, blank=True ,default='')
    second_balance_amount=models.CharField(max_length=100,null=True, blank=True,default='')
    second_due_date=models.CharField(max_length=100,null=True, blank=True ,default='')
    second_total_payment=models.IntegerField(default='0')
    
    final_amount=models.CharField(max_length=100,null=True, blank=True,default='')
    final_due_date_on=models.CharField(max_length=100,null=True, blank=True ,default='')
    final_due_on=models.CharField(max_length=100,null=True, blank=True ,default='')
    final_paid_amount=models.CharField(max_length=100,null=True, blank=True,default='')
    final_paid_date=models.CharField(max_length=100,null=True, blank=True ,default='')
    final_balance_amount=models.CharField(max_length=100,null=True, blank=True,default='')
    final_due_date=models.CharField(max_length=100,null=True, blank=True ,default='')
    final_total_payment=models.IntegerField(default='0')

    complete_status=models.CharField(max_length=100,null=True, blank=True,default='0')     
    
    
class probation(models.Model):
    team=models.ForeignKey(create_team, on_delete=models.SET_NULL,related_name='p_team', null=True, blank=True)
    user=models.ForeignKey(user_registration, on_delete=models.SET_NULL,related_name='p_user', null=True, blank=True)
    trainer=models.ForeignKey(user_registration, on_delete=models.SET_NULL,related_name="p_trainer", null=True, blank=True)
    startdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    reason = models.TextField()
    stop_reason = models.TextField(default='')
    extension = models.IntegerField(default=0)
    stopdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    renewdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.IntegerField(default=0)
    
    class Meta:
        get_latest_by = ['status']
        
class project_module_assign(models.Model):
    project_name = models.ForeignKey(project, on_delete=models.SET_NULL,related_name='project_name', null=True, blank=True)
    module =models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField()
        
class project_other_assign(models.Model):
    othproject_name = models.ForeignKey(project, on_delete=models.SET_NULL,related_name='project_other_name', null=True, blank=True)
    other_name =models.CharField(max_length=255,null=True, blank=True)
    other_description = models.TextField()

class project_table(models.Model):
    project = models.ForeignKey(project, on_delete=models.SET_NULL,related_name='project_table_name', null=True, blank=True)
    module_name_id = models.IntegerField(default='0')
    description = models.TextField()        
    
    
    

    
    
class payment_head(models.Model):
    payment_head = models.CharField(max_length=255,null=True, blank=True, default='')
    description_paymenthead = models.TextField()


class income(models.Model):
     
    pay_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    party_name = models.CharField(max_length=255,null=True, blank=True)
    amount = models.IntegerField(default=0)
    pay_method = models.CharField(max_length=255,null=True, blank=True)
    pay_description = models.TextField(null=True, blank=True, default='')
    department = models.ForeignKey(department, on_delete=models.SET_NULL,related_name='accounts_department_name', null=True, blank=True)
    payment_head = models.ForeignKey(payment_head, on_delete=models.SET_NULL,related_name='accounts_payment_head', null=True, blank=True)
    pay_status = models.IntegerField(default=0)


############################## Digital Marketing (15-10-22 Shebin Shaji) ###################################################



class DM_projects(models.Model):
    dm_date = models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    dm_project_name=models.CharField(max_length=255,null=True, blank=True)
    dm_project_categ=models.CharField(max_length=150,null=True, blank=True)
    dm_project_start=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    dm_project_status=models.CharField(max_length=50,null=True, blank=True, default="Not Started")


class DM_project_dese(models.Model):
    dm_task_project_id=models.ForeignKey(DM_projects,on_delete=models.CASCADE,null=True,blank=True)
    dm_task_date = models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    dm_task_dese = models.TextField()


class Dm_project_Task(models.Model):
    dm_project_id=models.ForeignKey(DM_projects,on_delete=models.CASCADE,null=True,blank=True)
    dm_user_name=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    dm_task_name=models.CharField(max_length=255,null=True, blank=True)
    dm_task_assigndate= models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    dm_task_status=models.CharField(max_length=100,null=True, blank=True)

#*************************************** Tasks *****************************************************

class DataCollect(models.Model):
      Project_name=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
      Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
      dc_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
      dc_name=models.CharField(max_length=100,null=True, blank=True)
      dc_email=models.CharField(max_length=100,null=True, blank=True)
      dc_phone=models.CharField(max_length=50,null=True, blank=True)
      dc_loc=models.CharField(max_length=110,null=True, blank=True)
      dc_internship=models.CharField(max_length=100,null=True, blank=True)
      dc_Fr_Ex=models.CharField(max_length=50,null=True, blank=True)
      dc_status=models.CharField(max_length=50,null=True, blank=True)
      dc_reason=models.CharField(max_length=50,null=True, blank=True)

class Backlinks(models.Model):
    bd_taskid=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
    bd_Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    bd_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    bd_url=models.URLField()
    bd_type=models.CharField(max_length=150,null=True, blank=True)
    bd_status=models.CharField(max_length=50,null=True, blank=True)

class WebpageContent(models.Model):
    web_taskid=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
    web_Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    web_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    web_url=models.URLField()
    web_dese=models.TextField()
    web_key=models.TextField()

class CompanyAnalysis(models.Model):
    analysis_taskid=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
    analysis_Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    analysis_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    analysis_compname=models.CharField(max_length=150,null=True, blank=True)

class ClientData(models.Model):
    cd_taskid=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
    cd_Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    cd_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    cd_name=models.CharField(max_length=150,null=True, blank=True)
    cd_email=models.EmailField()
    cd_phno=models.CharField(max_length=50,null=True, blank=True)
    cd_bussines=models.TextField()

class OnPage(models.Model):
    op_taskid=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
    op_Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    op_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    op_url=models.URLField()
    op_work=models.TextField()
    op_status=models.CharField(max_length=50,null=True, blank=True)

class BlogCalander(models.Model):
    blog_taskid=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
    blog_Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    blog_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    blog_title=models.CharField(max_length=50,null=True, blank=True)
    blog_key=models.TextField()
    blog_status=models.CharField(max_length=50,null=True, blank=True)
    
class SmmPoster(models.Model):
    smm_taskid=models.ForeignKey(Dm_project_Task,on_delete=models.CASCADE,null=True,blank=True)
    smm_Employeeid=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    smm_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    smm_sub=models.CharField(max_length=100,null=True, blank=True)
    smm_type=models.CharField(max_length=50,null=True, blank=True)
    smm_content=models.TextField()
    smm_dese=models.TextField()
    smm_satus=models.CharField(max_length=50,null=True, blank=True)
    smm_file=models.ImageField(upload_to="poster", null=True)


class DM_Project_Report(models.Model):
    report_project_id=models.ForeignKey(DM_projects,on_delete=models.CASCADE,null=True,blank=True)
    report_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    re_project_name=models.CharField(max_length=100,null=True, blank=True)
    re_project_task=models.CharField(max_length=150,null=True, blank=True)
    re_project_task_file=models.FileField(upload_to="report",null=True,default=None)
    re_project_fromdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    re_project_todate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    re_project_dese=models.TextField(default=" ")


class TSproject_Task_verify(models.Model):
    ts_project_task=models.ForeignKey(project_taskassign,on_delete=models.CASCADE,null=True,blank=True)
    ts_tester=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    ts_task_verify_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    ts_task_sub_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    ts_task_status=models.CharField(max_length=200, null=True,default="")
    ts_delay= models.IntegerField(default='0', null=True) 
    ts_reson_dely=models.TextField(default=" ")



#******************** Project Document - shebin shaji (25-10-22) *****************
    
class PM_ProjectDocument(models.Model):
    doc_project_id=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    doc_project_name=models.CharField(max_length=100,null=True, blank=True)
    doc_project_currentdate=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    doc_project_startdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    doc_project_enddate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    doc_project_frontend=models.CharField(max_length=100,null=True, blank=True)
    doc_project_backend=models.CharField(max_length=100,null=True, blank=True)
    doc_status=models.CharField(max_length=10,null=True, blank=True,default='0')
    doc_project_ui=models.FileField(upload_to="ProjectUI", null=True)
    

class ProjectDocDetails(models.Model):
    doc_project_d=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    doc_project_currentdate_d=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    doc_project_mdname=models.CharField(max_length=100,null=True, blank=True)
    doc_project_mddise_d=models.TextField()
    doc_duser=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)

class ProjectDocModels(models.Model):
    doc_project_md=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    doc_project_currentdate_md=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    doc_project_mdname=models.CharField(max_length=100,null=True, blank=True)
    doc_project_dise_md=models.TextField()
    doc_mduser=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)

class ProjectDocViews(models.Model):
    doc_project_v=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    doc_project_currentdate_v=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    doc_project_vname=models.CharField(max_length=100,null=True, blank=True)
    doc_project_vdise=models.TextField()
    doc_vuser=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)

class ProjectDochtmlpages(models.Model):
    doc_project_hp=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    doc_project_currentdate_hp=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    doc_project_hpmdname=models.CharField(max_length=100,null=True, blank=True)
    doc_project_hpname=models.CharField(max_length=100,null=True, blank=True)
    doc_project_hpdise=models.TextField()
    doc_project_html_page=models.FileField(upload_to="ProjectUI", null=True)
    doc_hpuser=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)

class ProjectDoclibraryies(models.Model):
    doc_project_lb=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    doc_project_currentdate_lb=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    doc_project_lbname=models.CharField(max_length=100,null=True, blank=True)
    doc_project_lbdise=models.TextField()
    doc_lbuser=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)

class ProjectDocother(models.Model):
    doc_project_oth=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    doc_project_currentdate_oth=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    doc_project_othname=models.CharField(max_length=100,null=True, blank=True)
    doc_project_othdise=models.TextField()
    doc_othuser=models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)




class ProjectCorrectionUpdation(models.Model):
    project_cu_id=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    project_tsak_id=models.ForeignKey(project_taskassign,on_delete=models.CASCADE,null=True,blank=True)
    ptl_name=models.CharField(max_length=50,null=True, blank=True,default='')
    pdev_name=models.CharField(max_length=50,null=True, blank=True,default='')
    project_cu_module=models.CharField(max_length=100,null=True, blank=True)
    project_cu_descrip=models.TextField()
    project_oldui=models.ImageField(upload_to="ProjectUI", null=True)
    project_cu_olddescrip=models.TextField()
    project_cu_newui=models.ImageField(upload_to="ProjectUI", null=True)
    project_cu_newdescrip=models.TextField()
    project_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    project_cu_start=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    project_cu_end=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    project_cu_wdays=models.IntegerField(null=True,blank=True,default=0)
    project_cu_status=models.CharField(max_length=50,null=True, blank=True)


class wrdata(models.Model):
    wrn_develp=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='wr_devp',null=True,blank=True)
    wrn_user_name=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='wr_user',null=True,blank=True)
    wrn_task=models.ForeignKey(project_taskassign,on_delete=models.CASCADE,related_name='wr_task',null=True,blank=True)
    wrn_reason=models.CharField(max_length=200,null=True, blank=True)
    wrn_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)

class WorkRequest(models.Model):
    wrk_develp=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='wrk_devp',null=True,blank=True)
    wrkreq_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    wrkreq_tl=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='wrk_tl',null=True,blank=True)
    wrk_status=models.CharField(max_length=200,null=True, blank=True,default='')


class Projectmanagerworkassign(models.Model):
    pm_project_task=models.ForeignKey(project_taskassign,on_delete=models.CASCADE,related_name='pm_prtask',null=True,blank=True)
    assing_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    pm_task_status=models.CharField(max_length=200,null=True, blank=True,default='')

class Feedbacks(models.Model):
    fb_from=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='fb_tri',null=True,blank=True)
    fb_to=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='fb_tra',null=True,blank=True)
    fb_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    fb=models.CharField(max_length=200,null=True, blank=True,default='')

class Action_Taken(models.Model):
    atdep=models.ForeignKey(department,on_delete=models.CASCADE,related_name='depat',null=True,blank=True)
    atdesig=models.ForeignKey(designation,on_delete=models.CASCADE,related_name='desigat',null=True,blank=True)
    atemp=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='empat',null=True,blank=True)
    atby=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='ationby',null=True,blank=True)
    at_remark=models.TextField()
    at_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    at_status=models.CharField(max_length=200,null=True, blank=True,default='')
    

class UserManuvel(models.Model):
    user_project=models.ForeignKey(project,on_delete=models.CASCADE,related_name='usermanuvel',null=True,blank=True)
    um_head=models.CharField(max_length=255,null=True, blank=True,default='')
    um_subhead=models.CharField(max_length=255,null=True, blank=True,default='')
    um_dese=models.TextField()
    um_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    um_files = models.FileField(upload_to='images/', null=True, blank=True)

class UserManuvelPoints(models.Model):
    userp_project=models.ForeignKey(project,on_delete=models.CASCADE,related_name='umproj',null=True,blank=True)
    user_manuvelid=models.ForeignKey(UserManuvel,on_delete=models.CASCADE,related_name='usermanuvelid',null=True,blank=True)
    um_pfiles = models.FileField(upload_to='images/', null=True, blank=True)
    um_points=models.TextField()

class ProjectBudgect(models.Model):
    pb=models.ForeignKey(project,on_delete=models.CASCADE,related_name='pbug',null=True,blank=True)
    pb_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    pb_compdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    pb_title=models.CharField(max_length=255,null=True, blank=True,default='')
    pb_status=models.CharField(max_length=200,null=True, blank=True,default='')
    pb_amount=models.IntegerField(null=True,blank=True,default=0)
    
#  New model fo leads registraion 24/02/23
class Leads_Register(models.Model):
    r_fullname=models.CharField(max_length=200,null=True, blank=True,default='')
    r_email=models.EmailField(default='')
    r_phno=models.CharField(max_length=200,null=True, blank=True,default='')
    r_place=models.CharField(max_length=200,null=True, blank=True,default='')
    r_qulific=models.CharField(max_length=200,null=True, blank=True,default='')
    r_refference=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='lead_regi',null=True,blank=True)
    r_assing_id=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='lead_assign',null=True,blank=True)
    r_assign_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    r_assign_status=models.IntegerField(null=True,blank=True,default=0)
    r_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    r_wating_date=models.DateField(null=True, blank=True)
    r_dese=models.TextField(default='')
    r_lead_source=models.CharField(max_length=200,null=True, blank=True,default='')
    r_pass_out_year=models.CharField(max_length=1000,null=True, blank=True,default='')
    r_status=models.IntegerField(null=True,blank=True,default=0)
    r_completed_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    r_type_status=models.CharField(max_length=200,null=True, blank=True,default='')
    r_type=models.CharField(max_length=200,null=True, blank=True,default='')
    r_fre_exp=models.CharField(max_length=200,null=True, blank=True,default='')

class LeadExtradata(models.Model):
    leadid=models.ForeignKey(Leads_Register,on_delete=models.CASCADE,related_name='lead_id',null=True,blank=True)
    lead_ex_head=models.CharField(max_length=200,null=True, blank=True,default='')
    lead_ex_data=models.TextField(default='')


# Certficate Approvel table , Use in -  Office Admin Module

class Certificate_approve(models.Model):
    cf_develp=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='Certificate_user',null=True,blank=True)
    cf_intern=models.ForeignKey(internship,on_delete=models.CASCADE,related_name='Intern_Certificate_user',null=True,blank=True)
    cf_category=models.IntegerField(null=True,blank=True,default=0)
    cf_certificate=models.CharField(max_length=200,null=True, blank=True,default='')
    cf_request_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    cf_approve_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    cf_status=models.IntegerField(null=True,blank=True,default=0)


# Confirmations 
    
class ConfirmationList(models.Model):
    confirm_Employee = models.ForeignKey(user_registration,on_delete=models.CASCADE,null=True,blank=True)
    confirm_date = models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    confirm_title = models.TextField()
    confirm_option = models.CharField(max_length=100,null=True, blank=True,default='')
    send_date = models.DateField(auto_now_add=False,auto_now=False,  null=True, blank=True)