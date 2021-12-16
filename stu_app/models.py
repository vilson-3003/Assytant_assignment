from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id=models.IntegerField(unique=True)
   # stu_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name

class Department(models.Model):
    dept_id=models.IntegerField(unique=True)
    dept_name=models.CharField(max_length=100)
    dept_head=models.CharField(max_length=100)
    stu_dept=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.dept_name


class Stu_dep(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)