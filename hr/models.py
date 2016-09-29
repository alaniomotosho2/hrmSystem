from __future__ import unicode_literals

from django.contrib.admin import widgets
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from .forms import Employee_form

# Create your models here.

class Employee(models.Model):
    BANGALORE = 'BGR'
    MUMBAI = 'MBI'
    DELHI = 'DLI'
    LAGOS = 'LAG'

    city_town = (
        (BANGALORE, 'Bangalore'),
        (MUMBAI, 'Mumbai'),
        (DELHI,'Delhi'),
        (DELHI,'LAGOS')
    )

    INDIA = 'IND'
    NIGERIA = 'NGR'
    GAMBIA = 'GMB'

    country_list = (
        (INDIA,'India'),
        (NIGERIA,'Nigeria'),
        (GAMBIA, 'Gambia')
    )


    MALE = 'Male'
    FEMALE = "Female"
    gender = (
        (MALE,'Male'),
        (FEMALE,'Female')
    )

    DEGREE = 'Degree'
    MASTER = 'Master'
    PHD = 'Phd'
    OTHER = 'Other'

    qualification_list = (
        (DEGREE,'Degree'),
        (MASTER,'Master'),
        (PHD,'Phd'),
        (OTHER,'Other')
    )

    PERMANENT = 'Permanent'
    CONTRACT = 'Contract'
    INTERN = 'Intern'

    empl_status = (
        (PERMANENT,'Permanent'),
        (CONTRACT,'Contract'),
        (INTERN,'Intern')
    )

    employee_id = models.IntegerField('Employee Id',primary_key=True)
    first_name = models.CharField('First Name',max_length=50)
    last_name = models.CharField('Last Name',max_length=50)
    mobile = models.IntegerField('Mobile')
    department = models.OneToOneField('Department',on_delete=models.CASCADE,default=0)
    account_number = models.OneToOneField('Account',on_delete=models.CASCADE,default=0)
    salary = models.OneToOneField('Salary',on_delete=models.CASCADE)
    project = models.ForeignKey('Project')
    dob = models.DateField('Date of Birth',blank=False)
    date_hired = models.DateField('Date hired',blank=False)
    year_experience = models.IntegerField('Year of experience')
    gender = models.CharField('Gender',max_length=7,choices=gender,default=MALE)
    city = models.CharField('City',max_length=20,choices=city_town,default=BANGALORE)
    country = models.CharField('country',max_length=50,choices=country_list,default=INDIA)
    employee_image = models.ImageField('Employee Image',upload_to = 'users/%Y/%M/%D/')
    qualification = models.CharField('Qualification',max_length=50,choices=qualification_list,default=DEGREE)
    email = models.EmailField('Email')
    address = models.TextField('address')
    employement_status = models.CharField('Employement Status',max_length=20,choices=empl_status,default=PERMANENT)
    skill_summary = models.TextField('Skill Summary')


    #can put class meta later for ordering
    class Meta:
        db_table = 'Employee'

    def __str__(self):
        return str(self.employee_id) + " " +self.first_name + " "+self.last_name

    #form = Employee_form

class Perfomance(models.Model):
    perfomance_id = models.IntegerField('Perfomance id',primary_key=True)
    date_recorded = models.DateTimeField('Date',auto_now_add=True)
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    perfomance_rating = models.IntegerField('Rating /100')
    remarks = models.TextField('remarks')
    class Meta:
        db_table = 'Perfomance'
    def __str__(self):
        return str(self.perfomance_id) + " "+str(self.employee)

class Training(models.Model):
    training_id = models.IntegerField('Training Id',primary_key=True)
    employee = models.ForeignKey('Employee')
    project_name = models.ForeignKey('Project',on_delete=models.CASCADE)
    department = models.ForeignKey('Department',on_delete=models.CASCADE)
    skill_report = models.TextField('Skill Report')
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    remarks = models.TextField('Remarks')

    class Meta:
        db_table = 'Training'
    def __str__(self):
        return str(self.training_id)+ " "+ str(self.employee)


class Account(models.Model):
    account_id = models.IntegerField('Account id')
    account_number = models.IntegerField('Bank Acount',primary_key=True)
    account_name = models.CharField('Account Name',max_length=250)
    class Meta:
        db_table = 'Account'
    def __str__(self):
        return str(self.account_number)


class Payroll(models.Model):
    payroll_id = models.IntegerField(primary_key=True)
    account_number = models.OneToOneField('Account',on_delete=models.CASCADE,default=0);
    employee = models.OneToOneField('Employee',on_delete=models.CASCADE,default=0)
    department = models.ForeignKey('Department',on_delete=models.CASCADE,default=0)
    salary = models.OneToOneField('Salary',on_delete=models.CASCADE)
    allowances = models.FloatField('Allowances',null=True)
    others = models.FloatField('Others',null=True);
    loan = models.FloatField('Loan',null=True)
    tax = models.FloatField('Tax')

    class Meta:
        db_table = 'Payroll'

    def __str__(self):
        return "Account " +str(self.account_number)+" "+str(self.employee)


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=40)
    #designation

    class Meta:
        db_table = 'Department'
    def __str__(self):
        return self.dept_name


class Project(models.Model):
    project_id = models.IntegerField('Project Id',primary_key=True)
    project_name = models.CharField('Project Name',max_length=50)
    department = models.ForeignKey('Department',on_delete=models.CASCADE)

    class Meta:
        db_table = 'Project'
    def __str__(self):
        return self.project_name

class Attendance(models.Model):
    PRESENT = 'Present'
    ABSENT = 'Absent'
    status_attendance =(
    (PRESENT,'Pesent'),
    (ABSENT,'Absent')
    )

    employee = models.ForeignKey('Employee',on_delete=models.CASCADE,default=0)
    attendance_id = models.IntegerField('Attendance Id',primary_key = True)
    date = models.DateTimeField('Date',default=timezone.now)
    day = models.CharField('Day of the week',max_length=25)
    attendance_status = models.CharField("Attendance Status",choices = status_attendance,default=ABSENT,max_length=25)

    class Meta:
        db_table = 'Attendance'
    def __str__(self):
        return str(self.attendance_id) + self.attendance_status

class Salary(models.Model):
    salary_id = models.IntegerField('Salary Id',primary_key=True)
    salary = models.FloatField('Salary')
    #employee = models.OneToOneField('employee',on_delete=models.CASCADE)
    class Meta:
        db_table = 'Salary'
    def __str__(self):
        return str(self.salary_id)+" "+str(self.salary)
