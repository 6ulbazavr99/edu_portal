from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from edu.models import Lesson, Test
from .models import UserSubject, UserLesson, UserTest


class UserSubjectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserSubject
        fields = '__all__'

    def validate(self, attrs):
        user_grade = self.context['request'].user.grade
        if user_grade not in attrs['subject'].grades.all():
            raise ValidationError("The user's grade does not correspond to the subject.")
        return attrs

    def after_create(self, instance, validated_data):
        lessons = Lesson.objects.filter(subject=validated_data['subject'])
        for lesson in lessons:
            UserLesson.objects.create(user=instance.user, lesson=lesson)
            tests = Test.objects.filter(lesson=lesson)
            for test in tests:
                UserTest.objects.create(user=instance.user, test=test)
        return instance

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        instance = super().create(validated_data)
        self.after_create(instance, validated_data)
        return instance


class UserLessonSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserLesson
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        instance = super().create(validated_data)
        return instance


class UserTestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserTest
        fields = '__all__'
        read_only_fields = ('status',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return self.check_answers(validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr != 'status':
                setattr(instance, attr, value)
        instance = self.check_answers(validated_data, instance)
        instance.save()
        return instance

    def check_answers(self, validated_data, instance=None):
        user_answers = validated_data.get('user_answers')
        test = validated_data.get('test', instance.test if instance else None)
        correct_answers = test.correct_answers

        user_answers_sorted = sorted(user_answers.items())
        correct_answers_sorted = sorted(correct_answers.items())

        status = user_answers_sorted == correct_answers_sorted

        if instance:
            instance.status = status
            return instance
        else:
            validated_data['status'] = status
            return UserTest.objects.create(**validated_data)
