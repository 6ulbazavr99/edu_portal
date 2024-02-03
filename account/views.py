from django.contrib.auth import get_user_model
from rest_framework import viewsets

from account.models import Grade
from account.serializers import CustomUserSerializer, GradeSerializer, CustomUserRegisterSerializer

User = get_user_model()


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserRegisterSerializer
        return CustomUserSerializer
