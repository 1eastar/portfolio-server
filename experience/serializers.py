from rest_framework import serializers

from . import models

class PhotoTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoText
        fields = ['id', 'number', 'image', 'content', 'create_at', 'update_at', 'experience']


class ExperienceSerializer(serializers.ModelSerializer):
    # phototexts = PhotoTextSerializer(many=True, read_only=True, required=False)
    phototexts = serializers.SerializerMethodField()
    class Meta:
        model = models.Experience
        fields = ('id', 'main_title', 'main_image', 'title', 'content', 'phototexts', 'temporary', 'create_at', 'update_at')

    def get_phototexts(self, obj):
        phototexts = models.PhotoText.objects.filter(experience=obj)
        return PhotoTextSerializer(phototexts, many=True).data