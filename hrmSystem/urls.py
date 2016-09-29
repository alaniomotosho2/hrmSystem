"""hrmSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from hr import views as hrViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #all my url configs
    url(r'^$',hrViews.home_animate,name='home_animate'),
    url(r'^addNewAdmin_login/$',hrViews.addNewAdmin_login,name='addNewAdmin_login'),
    url(r'^updateAdmin_login/$',hrViews.updateAdmin_login,name='updateAdmin_login'),
    url(r'^newEmployee_reg/$',hrViews.newEmployee_reg,name='newEmployee_reg'),
    url(r'^updateEmployee_reg/$',hrViews.updateEmployee_reg,name='updateEmployee_reg'),
    url(r'^updateSearch_employee/$',hrViews.updateSearch_employee,name='updateSearch_employee'),
    url(r'^logout_admin/$',hrViews.logout_admin,name='logout_admin'),
    url(r'^delete_employee/$',hrViews.delete_employee,name='delete_employee'),
    url(r'^deleteEmployee_login/$',hrViews.deleteEmployee_login,name='deleteEmployee_login'),
    url(r'^employeeSearch_login/$',hrViews.employeeSearch_login,name='employeeSearch_login'),
    url(r'^employee_search/$',hrViews.employee_search,name='employee_search'),
    url(r'^payrollEmployee_login/$',hrViews.payrollEmployee_login,name='payrollEmployee_login'),
    url(r'^payroll_employee$',hrViews.payroll_employee,name='payroll_employee'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
