from django.contrib import admin
from django.urls import path, include

from rest_framework  import routers

from . import views

# router = routers.DefaultRouter()
# router.register('post', views.StudyViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('contact/', views.WriteContact),
]
