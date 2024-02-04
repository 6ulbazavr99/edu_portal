from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from account.models import Grade
from edu.models import Lesson, Test
from self_edu.models import UserSubject, UserLesson, UserTest

User = get_user_model()


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomUserListSerializer(CustomUserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'grade', 'subjects',)


class CustomUserRetrieveSerializer(CustomUserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'grade', 'subjects', 'first_name', 'last_name',
                  'email', 'last_login', 'date_joined', 'is_superuser', )


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=32,
                                     required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=8, max_length=32,
                                      required=True, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirmation', 'grade', 'subjects')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password_confirmation != password:
            raise serializers.ValidationError(_('Пароли не совпадают'))
        validate_password(password)
        user_grade = attrs['grade']
        for subject in attrs['subjects']:
            if user_grade not in subject.grades.all():
                raise ValidationError("The user's grade does not correspond to the subject.")
        return attrs

    def create(self, validated_data):
        subjects = validated_data['subjects']
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        validated_data['subjects'] = subjects
        self.after_create(instance, validated_data)
        return instance

    def after_create(self, instance, validated_data):
        subjects = validated_data['subjects']
        for subject in subjects:
            UserSubject.objects.create(user=instance, subject=subject)
            lessons = Lesson.objects.filter(subject=subject)
            for lesson in lessons:
                UserLesson.objects.create(user=instance, lesson=lesson)
                tests = Test.objects.filter(lesson=lesson)
                for test in tests:
                    UserTest.objects.create(user=instance, test=test)
        return instance
