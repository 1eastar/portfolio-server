from django.contrib import admin
from django.urls import path, include

from rest_framework  import routers

from . import views

router = routers.DefaultRouter()
router.register('post', views.StudyViewSet)
router.register('paragraph', views.ParagraphViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
