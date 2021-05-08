from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import RegistrationSerializer,StudentSerializer
from django.contrib.auth.models import User
from testapp.models import Student
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegistrationSerializer


    def post(self,request,*args,**kwargs):
        if request.method=='POST':
            serializer=RegistrationSerializer(data=request.data)
            data={}
        if serializer.is_valid():
            user=serializer.save()
            data['msg']="Successfully Registered"
            data['username']=user.username
            data['email']=user.email
        else:    
            data=serializer.errors

        return Response(data)

class StudentView(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
