from django.contrib import admin
from django.urls import path, include

from rest_framework  import routers

from . import views

router = routers.DefaultRouter()
router.register('posts', views.ExperienceViewSet)
# router.register('phototext', views.PhotoTextViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('phototexts/', views.PhotoTextView.as_view()),
]
