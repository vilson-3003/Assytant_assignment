from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

    def create(self,data):
        return Student.objects.create(**data)

class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"

class Stu_deptSerializer(serializers.Serializer):
    class Meta:
        models = Stu_dep
        fields="__all__"

    def create(self, data):
        return Stu_dep.objects.create(**data)
    
    def put(self, instance, data):
        return self.instance.update(**data)