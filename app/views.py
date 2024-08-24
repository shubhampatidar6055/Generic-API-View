from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import StudentSerializer
from rest_framework.views import APIView
# Create your views here.

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer