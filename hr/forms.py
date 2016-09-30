from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText,PrependedText
from .models import Employee,Payroll,Project,Department,Attendance,Account,Salary,Perfomance,Training,Leave

class AdminForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class Employee_form(forms.ModelForm):
    class Meta:
        #i remove department_id
        model = Employee
        fields = ['employee_id','first_name','last_name','mobile','department','project','account_number','salary',
            'dob','year_experience','date_hired','gender','city','country','employee_image','qualification',
            'email','address','employement_status','skill_summary'
        ]
        widgets = {'dob': forms.DateInput(attrs={'class':'datetimepicker1'}),
                   'date_hired':forms.DateInput(attrs={'class':'datetimepicker1'})
        }



    def clean_email(self):
        #we can use this method to clean any fields
        email = self.cleaned_data.get('email')
        if not email.endswith('.com'):
            raise forms.ValidationError('Invalid Email')
        return email

class Payroll_form(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee','account_number','salary','allowances','others','loan','tax']

class Department_form(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_id','dept_name']


class Project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_id','project_name','department']

class Attendance_form(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['attendance_id','date','day','attendance_status']

class Account_form(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_id','account_number','account_name']
class Salary_form(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['salary_id','salary']


class Training_form(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['training_id','employee','project_name','department','skill_report','start_date','end_date','remarks']


class Perfomance_form(forms.ModelForm):
    class Meta:
        models = Perfomance
        fields = ['perfomance_id','date_recorded','employee','perfomance_rating','remarks']

#Update serach Form
class updateEmployee_form(forms.Form):
    employee_id = forms.IntegerField(label='Enter Employee Id',required=True)


class Leave_form(forms.ModelForm):
    class Meta:
        models = Leave
        fields = ['leave_id','employee','start_date','end_date','reason']
