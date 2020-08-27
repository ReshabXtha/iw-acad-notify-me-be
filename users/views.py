from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, LoginSerializer, UserSerializer
from .utils import Util
import jwt
from django.conf import settings

USER = get_user_model()


class UserRegisterView(generics.GenericAPIView):

    serializer_class = UserRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = USER.objects.get(email=user_data['email'])
        Util.send_verification_email(request, user)
        message = {
            'message': 'Use link in your email to verify your account.',
            'data': user_data
        }
        return Response(message, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = USER.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'message': 'Your email is successfully verified.'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifiers:
            return Response({'error': 'Verification link expired.'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifiers:
            return Response({'error': 'Invalid Token.'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = USER.objects.all()

class UserDestroyView(generics.DestroyAPIView):
    # serializer_class = UserSerializer
    queryset = USER.objects.all()