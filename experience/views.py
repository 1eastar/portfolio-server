from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.conf import settings

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from . import models, serializers

# Create your views here.

# class ExperienceListView(APIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]

#     def get(self, request, format=None):
#         experiences = models.Experience.objects.all()
#         serializer = serializers.ExperienceSerializer(experiences)
#         return

#     def post(self, request, format=None):
#         return

# class ExperienceDetailView(APIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]

#     def get(self, request, pk, format=None):
#         return

#     def put(self, request, pk, format=None):
#         return

#     def delete(self, request, pk, format=None):
#         return


class ExperienceViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = models.Experience.objects.order_by('-update_at')
    serializer_class = serializers.ExperienceSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    

class PhotoTextViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = models.PhotoText.objects.order_by('-update_at')
    serializer_class = serializers.PhotoTextSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
