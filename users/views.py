from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserSerilizers, CustomeUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from core.models import Author


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomeUserSerializer
    permission_classes = [permissions.AllowAny]


    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user.refresh_token = str(refresh)
        user.save()

        author = Author.objects.create(user=user)
        

        serializer.instance.refresh_token = str(refresh)
        serializer.validated_data['tokens'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return super().perform_create(serializer)

        



class SignInView(generics.CreateAPIView):
    
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password.'}, status=400)

        user = authenticate(username=username, password=password)
        author = Author.objects.get(user=user)

        if not user:
            return Response({'error': 'Invalid credentials.'}, status=401)
        
    
        refresh = RefreshToken.for_user(user)
        return Response({
            'author_id': author.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username,
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,

        })

