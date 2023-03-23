from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()

    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
class LoginView(GenericAPIView):
    def post(self,request):
        data=request.data
        username=data.get('username','')
        password=data.get('password','') 
        pass


