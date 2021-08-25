from django.shortcuts import render
import jwt
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import authenticate
# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    def post(self, request):
        data = request.data
        username = data.get('username', ' ')
        password = data.get('password', ' ')
        user = authenticate(username=username, password=password)
        
        print(user)
        # print(auth.authenticate(username=username,password=password))
        if user:
            auth_token = jwt.encode({'username':user.username},settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {
                'user': serializer.data,'token':auth_token
            }

            return Response(data, status=status.HTTP_200_OK)
        print(username)
        return Response({'details': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)