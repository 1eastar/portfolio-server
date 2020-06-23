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
from rest_framework.filters import SearchFilter

from . import models, serializers

# Create your views here.

class StudyViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = models.Study.objects.order_by('-create_at')
    serializer_class = serializers.StudySerializer

    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        # domain = self.request.META.get('HTTP_DOMAIN', None)
        # if domain is None:
        #     raise Exception("Domain is missing in request header")
        category = int(self.request.GET.get('category'))
        order = int(self.request.GET.get('order'))
        pagination = int(self.request.GET.get('pagiantenum'))
        qs = models.Study.objects.all()
        if category == 0:
            if order == 0:
                qs = models.Study.objects.order_by('-create_at')
            elif order == 1:
                qs = models.Study.objects.order_by('create_at')
            elif order == 2:
                qs = models.Study.objects.order_by('-update_at')
        else:
            if order == 0:
                qs = models.Study.objects.filter(category=category).order_by('-create_at')
            elif order == 1:
                qs = models.Study.objects.filter(category=category).order_by('create_at')
            elif order == 2:
                qs = models.Study.objects.filter(category=category).order_by('-update_at')
        return qs

    # def perform_create(self, serializer):
    #     study = self.get_object()
    #     paragraphs = self.request.data['paragraphs']
    #     for paragraph in paragraphs:
    #         p = models.Paragraph.objects.create(number=paragraph.number, title=paragraph.title, content=paragraph.content, study=study)
    #     serializer.save()


class ParagraphViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = models.Paragraph.objects.order_by('-create_at')
    serializer_class = serializers.ParagraphSerializer

