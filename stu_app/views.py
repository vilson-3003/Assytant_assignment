from django.db.models import query
from django.db.models.base import Model
from django.shortcuts import render
from django.http import response
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import Student, Department
from rest_framework.response import Response
from .serializers import Stu_deptSerializer, Studentserializer
from .serializers import Departmentserializer
from rest_framework import status 
from .models import *
# Create your views here.



# def index(request):
#     if request.method=="POST":
#         dept_id=request.POST.getlist('dept_id')
#         dept_name=request.POST.getlist('dept_name')
#         dept_head=request.POST.getlist('dept_head')
#         data = []
#         for i in range(len(dept_id)):
#             data.append(Department(dept_id=dept_id, dept_name=dept_name, dept_head=dept_head, stu_dept=request.user))
#         Department.objects.bulk_create(data)
#     return render(request, 'stu_app/index.html')

class StudentdetailView(APIView):
    def get(self, request):
        query=Student.objects.get(stu_id=request.data['stu_id'])
        serializers = Studentserializer(query)
        query2 = Department.objects.filter(stu_dept=query)
        dept = []
        for i in query2:
            dept.append({"dept_id" : i.dept_id,"dept_name" :i.dept_name,"dept_head":i.dept_head})
        return Response({"id":serializers.data['id'], "stu_id":serializers.data['stu_id'],"first_name":serializers.data['first_name'],"last_name":serializers.data['last_name'], "departments":dept})

    def post(self,request):
        serializers = Stu_deptSerializer(data={"student":Student.objects.get(stu_id=request.data['student']),"department":Department.objects.get(dept_id=request.data['department'])})
        if not serializers.is_valid():
            return Response(serializers.errors)
        serializers.save()
        print(serializers.data)
        
        return Response(serializers.data)

    def put(self, request):
        query = Department.objects.get(dept_id=request.data['dept_id'])
        serializers = Departmentserializer(query, data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors)
        serializers.save()
        return Response(serializers.data)

    def delete(self, request):
        query =  Department.objects.get(dept_id=request.data['dept_id'])
        query.delete()
        return Response({"status":"data deleted successfully"})

class StudentView(APIView):
    def get(self,request):
        query=Student.objects.all()
        serializer=Studentserializer(query, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Studentserializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)    
        serializer.save()
        return Response(serializer.data)

    def put(self,request):
        query=Student.objects.get(id=request.data['id'])
        serializer=Studentserializer(query,data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data) 

    def delete(self,request):
        query=Student.objects.get(id=request.data['id'])
        query.delete()
        return Response({"message":"Deleted sucessfully!"})


class StudentName(APIView):
    def get(self,request):
        query = Student.objects.get(stu_id=request.data['stu_id'])
        return Response({"Fullname":query.first_name+" "+query.last_name})

class DepartmentName(APIView):
    def get(self,request,*args,**kwargs):
        try:
            query=Department.objects.filter(dept_id=self.kwargs.get('id'))
        except:
            query=Department.objects.all()
        serializer=Departmentserializer(query, many=True)
        return Response(serializer.data)

class Alldepartment(APIView):
    def get(self,request):
        query=Department.objects.all()
        serializer=Departmentserializer(query, many=True)
        return Response(serializer.data)      

class Alldetails(APIView):
    def get(self,request):
        query=Student.objects.all()
        serializer=Studentserializer(query, many=True)
        return Response(serializer.data)  

#Answer no. 4 on(index.html)
def dep(request):
    data = {}
    query = Department.objects.all().order_by('dept_name')
    for i in query:
        if i.dept_name in data:
            data[i.dept_name]+=1
        else:
            data[i.dept_name]=1
    print(data)
    return render(request, 'stu_app/index.html',{"data":zip(data.keys(),data.values())})