"""
URL configuration for EMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.Home),
    path('employe_resister',v.Resister_emp),
    path('employe_list',v.Emp_list),
    path('employe_login',v.Emp_login),
    path('logout',v.Logout_view),
    path('emp_home',v.Emp_Home),
    path('emp_home_dashboard',v.dashboard),
    path('emp_profile',v.Emp_profile),
    path('emp_list',v.Emp_view),
    path('up/<int:pk>',v.Update_Emp.as_view()),
    path('emp_education',v.Emp_Education),
    path('emp_education_detail',v.Emp_Education_detail),
    path('emp_education_update/<int:pk>',v.Edu_Update_Emp.as_view()),
    path('emp_exp',v.Emp_exp),
    path('emp_exp_detail',v.Emp_Exp_detail),
    path('leave_r_form',v.Leave_request_form),
    path('leave_r_dt',v.Leave_detail),
]
