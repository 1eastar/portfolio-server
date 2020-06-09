from rest_framework import serializers

from . import models

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paragraph
        fields = ['pk', 'number', 'title', 'content', 'create_at', 'study']

class StudySerializer(serializers.ModelSerializer):
    paragraphs = serializers.SerializerMethodField()
    class Meta:
        model = models.Study
        fields = ['pk', 'title', 'category', 'paragraphs', 'content', 'create_at', 'update_at']

    def get_paragraphs(self, obj):
        paragraphs = models.Paragraph.objects.filter(study=obj)
        return ParagraphSerializer(paragraphs, many=True).data
