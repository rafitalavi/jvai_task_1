from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets , generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer , UserRegistrationSerializer , UserLoginSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationViewset(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
class LoginViewset(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)