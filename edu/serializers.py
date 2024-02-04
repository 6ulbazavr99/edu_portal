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


# class SubjectListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         representation = super(SubjectListSerializer, self).to_representation(instance)
#         user = super(CustomUserSerializer, self).to_representation(instance)
#         representation['test_questions'] = instance.grade.subjects.all()
#         # representation['correct_answers'] = instance.test.correct_answers
#         return representation

class AvailableSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'