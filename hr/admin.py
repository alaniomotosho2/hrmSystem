from django.contrib import admin
from .models import Employee,Payroll,Department,Project,Attendance,Account,Salary,Perfomance,Training

# Register your models here.

class Training_admin(admin.ModelAdmin):
    list_filter = ('project_name','employee','department')
    search_fields = ('employee','project_name','department')

class Perfomance_admin(admin.ModelAdmin):
    list_filter = ('employee','perfomance_rating','date_recorded')
    search_fields = ('employee','perfomance_rating')

class Employee_admin(admin.ModelAdmin):
    #we show all the fields
    list_filter = ('gender','country','qualification','project','department','salary','date_hired','account_number','year_experience')
    search_fields = ('employee_id','email','city','department')

class Payroll_admin(admin.ModelAdmin):
    list_filter = ('employee','department','loan','account_number','salary')
    search_fields = ('employee','salary','bank_account','tax')

class Department_admin(admin.ModelAdmin):
    pass

class Project_admin(admin.ModelAdmin):
    list_filter = ('project_name','department')
    search_fields = ('project_name','department')

class Attendance_admin(admin.ModelAdmin):
    list_filter = ('employee','date','day','attendance_status')
    search_fields = ('employee','date','attendance_status')

class Account_admin(admin.ModelAdmin):
    list_filter = ('account_number','account_id','account_name')
    search_fields = ('account_number','account_id','account_name')
class Salary_admin(admin.ModelAdmin):
    list_filter = ('salary_id','salary')
    search_fields = ('salary_id','salary')

admin.site.register(Perfomance,Perfomance_admin)
admin.site.register(Training,Training_admin)
admin.site.register(Salary,Salary_admin)
admin.site.register(Account,Account_admin)
admin.site.register(Department,Department_admin)
admin.site.register(Attendance,Attendance_admin)
admin.site.register(Project,Project_admin)
admin.site.register(Employee,Employee_admin)
admin.site.register(Payroll,Payroll_admin)
