from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from .serializers import UserProfileSerializer
from .models import UserProfile

class ProfileRetrieveView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    # authentication_classes = [TokenAuthentication]

class ProfileModelListAPIView(ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class ProfileModelUpdateAPIView(UpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    parser_classes = (JSONParser, FormParser, MultiPartParser)