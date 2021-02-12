from django.contrib import admin
from myApp.models import employee
# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    L = ['eid','ename','edesig','edob','exp','esal']

admin.site.register(employee,employeeAdmin)