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

@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def WriteContact(request):
    """
    data = {
        writer: string,
        title: stirng,
        content: string
    }
    response = {
        success: boolean,
        msg: string
    }
    """
    writer = request.data['writer']
    title = request.data['title']
    content = request.data['content']
    contact = models.Contact.objects.create(writer=writer, title=title, content=content)
    return Response({
        'success': True,
        'msg': '연락주셔서 감사합니다. 곧 답변 드리겠습니다.'
    },status=status.HTTP_200_OK)


# class ContactViewSet(viewsets.ModelViewSet):
#     authentication_classes = []
#     permission_classes = [AllowAny]

#     queryset = models.Comment.objects.order_by('-created_at')
#     serializer_class = serializers.CommentSerializer
