from django.contrib import admin
from stu_app import models
from stu_app.models import Department, Student, Stu_dep
# Register your models here.

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Stu_dep)