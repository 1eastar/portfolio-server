from rest_framework import serializers

from . import models

class PhotoTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoText
        fields = ['pk', 'image', 'content', 'create_at', 'update_at', 'experience']


class ExperienceSerializer(serializers.ModelSerializer):
    phototexts = PhotoTextSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = models.Experience
        fields = ['pk', 'main_title', 'main_image', 'title', 'phototexts', 'temporary', 'create_at', 'update_at']