from rest_framework import serializers

from . import models

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['pk', 'writer', 'title', 'content', 'answered', 'create_at']