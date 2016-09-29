from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Employee, Attendance, Payroll,Department,Project
from .forms import Employee_form,AdminForm,Attendance_form,Department_form,Project_form,Payroll_form,updateEmployee_form,Payroll_form

#from django.core.urlresolvers import reverse

#Home Page
def home_animate(request):
	return render(request,'hr/home_animate.html')




#adming login before adding new employee
def addNewAdmin_login(request):
	form = AdminForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		pwd = form.cleaned_data['password']
		user = authenticate(username=username,password=pwd)
		storage = messages.get_messages(request)
		for _ in storage:
			pass
		if user is None:
			messages.add_message(request, messages.ERROR, 'We Could Not Find You in Our System!')
		if user is not None:
			request.session['username'] = username
			return redirect('newEmployee_reg')
	return render(request,'hr/addNewAdmin_login.html',{'form':form})

#clear message before adding another this is a generic clear message handler
def clear_msg(request):
	storage = messages.get_messages(request)
	for _ in storage:
		pass

#admin login and out
def logout_admin(request):
	request.session.flush()
	return render(request,'hr/home_animate.html')
#updateEmploye_login
def updateAdmin_login(request):
	form = AdminForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		pwd = form.cleaned_data['password']
		user = authenticate(username=username,password=pwd)
		storage = messages.get_messages(request)
		for _ in storage:
			pass
		if user is None:
			messages.add_message(request, messages.ERROR, 'We Could Not Find You in Our System!')
		if user is not None:
			#will code here later maybe i have to change design a little bit
			request.session['username'] = username
			return redirect('updateSearch_employee')
	return render(request,'hr/updateEmployee_login.html',{'form':form})
#search for update Page
def updateSearch_employee(request):
	form = updateEmployee_form(request.POST or None)
	if request.method == 'POST':
		form = updateEmployee_form(request.POST)
		if form.is_valid():
			#form = Employee_form(request.POST,request.FILES)
			#form = updateEmployee_form(request.POST)
			pk = form.cleaned_data['employee_id']
			employee_details = get_object_or_404(Employee,employee_id = pk)
			request.session['employee_id'] = pk
			#session wont throw eror by using this
			if 'delete' in request.session:
				del request.session['delete']
				request.session.modified = True
				return redirect('delete_employee')
			if 'search' in request.session:
				del request.session['search']
				request.session.modified = True
				return redirect('employee_search')
			return redirect('updateEmployee_reg')
			#return redirect('updateEmployee_reg',args=(backend,))
			#return redirect(reverse('updateEmployee_reg',args=(backend,)))
	return render(request,'hr/updateSearch_employee.html',{'form':form})


#admin add new Employee
def newEmployee_reg(request):
	context = dict({})
	#we like to give user feedback so i will do that late
	form = Employee_form(request.POST or None)
	if request.method == 'POST':
		form = Employee_form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			#clear the message
			messages.add_message(request, messages.SUCCESS, 'Form Succesfully Submitted!')
			form = Employee_form()
	context['form'] = form
	#context['form'] = form
	#context['message'] = message
	return render(request,'hr/newEmployee_reg.html',context)

#update Employee Details
def updateEmployee_reg(request):
	id = request.session['employee_id']
	employee = Employee.objects.get(employee_id=id)
	form = Employee_form(instance=employee)
	image = employee.employee_image.path.split('media/')[-1]
	#image = employee.employee_image.name.split('/')[-1]
	print(image)
	if request.FILES is None:
		print("Outer File Request")
	if request.method == 'POST':
		#i should test form validity but am not doing it
		clear_msg(request)
		for key, value in request.POST.dict().items():
			if key != 'project' and key != 'department':
				setattr(employee,key,value)
			if key == 'project':
				project = Project.objects.get(project_id=int(value))
				employee.project = project
			if key == 'department':
				department = Department.objects.get(department_id=int(value))
				employee.department = department
		try:
			if request.FILES is None:
				employee.employee_image = image
			else:
				employee.employee_image = request.FILES['employee_image']
		except MultiValueDictKeyError:
			employee.employee_image = image

		employee.save(force_update=True)
		#we are covered if user change primary key too
		id = employee.employee_id
		messages.add_message(request, messages.SUCCESS, 'Form Succesfully Updated!')
		employee = Employee.objects.get(employee_id=id)
		form = Employee_form(instance=employee)
	return render(request,'hr/temp.html',{'form':form})


#deleteEmployeee Login
def deleteEmployee_login(request):
	form = AdminForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		pwd = form.cleaned_data['password']
		user = authenticate(username=username,password=pwd)
		storage = messages.get_messages(request)
		for _ in storage:
			pass
		if user is None:
			messages.add_message(request, messages.ERROR, 'We Could Not Find You in Our System!')
		if user is not None:
			#will code here later maybe i have to change design a little bit
			request.session['username'] = username
			request.session['delete'] = True
			return redirect('updateSearch_employee')
	#i use update employee login for delete too
	return render(request,'hr/updateEmployee_login.html',{'form':form})

#payroll loin
def payrollEmployee_login(request):
	form = AdminForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		pwd = form.cleaned_data['password']
		user = authenticate(username=username,password=pwd)
		storage = messages.get_messages(request)
		for _ in storage:
			pass
		if user is None:
			messages.add_message(request, messages.ERROR, 'We Could Not Find You in Our System!')
		if user is not None:
			#will code here later maybe i have to change design a little bit
			request.session['username'] = username
			request.session['payroll'] = True
			return redirect('payroll_employee')
	#i use update employee login for delete too
	return render(request,'hr/updateEmployee_login.html',{'form':form})

def payroll_employee(request):
	form = Payroll_form(request.POST or None)
	if request.method == 'POST':
		form = Employee_form(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Form Succesfully Submitted!')
			form = Employee_form()
	return render(request,'hr/payroll_employee.html',{'form':form})

#deleteEmployeee Login
def employeeSearch_login(request):
	form = AdminForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		pwd = form.cleaned_data['password']
		user = authenticate(username=username,password=pwd)
		storage = messages.get_messages(request)
		for _ in storage:
			pass
		if user is None:
			messages.add_message(request, messages.ERROR, 'We Could Not Find You in Our System!')
		if user is not None:
			#will code here later maybe i have to change design a little bit
			request.session['username'] = username
			request.session['search'] = True
			return redirect('updateSearch_employee')
	#i use update employee login for search too
	return render(request,'hr/updateEmployee_login.html',{'form':form})

#delete Employee
def delete_employee(request):
	id = request.session['employee_id']
	employee = Employee.objects.get(employee_id=id)
	form = Employee_form(instance=employee)
	if request.method == 'POST':
		employee.delete()
		clear_msg(request)
		#delete employee id from session
		del request.session['employee_id']
		request.session.modified = True
		messages.add_message(request, messages.ERROR, 'Record Succsfully Deleted!')
		#prblem is here
		#form = Employee_form()
	return render(request,'hr/delete_employee.html',{'form':form})
def employee_search(request):
	id = request.session['employee_id']
	employee = Employee.objects.get(employee_id=id)
	#form = Employee_form(instance=employee)
	return render(request,'hr/employee_search.html',{'employee':employee})
