from rest_framework import serializers

from . import models

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['id', 'writer', 'title', 'content', 'answered', 'create_at']