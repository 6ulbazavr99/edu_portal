from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from account.models import Grade


User = get_user_model()


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=32,
                                     required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=8, max_length=32,
                                      required=True, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirmation', 'grade')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password_confirmation != password:
            raise serializers.ValidationError(_('Пароли не совпадают'))
        validate_password(password)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
