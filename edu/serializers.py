from rest_framework import serializers

from account.serializers import CustomUserSerializer
from edu.models import Subject, Lesson, Test


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class AvailableSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'