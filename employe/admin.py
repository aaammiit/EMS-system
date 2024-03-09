from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Leave_user)
admin.site.register(Employe)
admin.site.register(Emp_Edu)
admin.site.register(Emp_Exp)
