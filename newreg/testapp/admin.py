from django.contrib import admin
from testapp import models
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(models.Student,StudentAdmin)    