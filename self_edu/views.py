from rest_framework import viewsets

from .models import UserSubject, UserLesson, UserTest
from .serializers import UserSubjectSerializer, UserLessonSerializer, UserTestSerializer


class UserSubjectViewSet(viewsets.ModelViewSet):
    queryset = UserSubject.objects.all()
    serializer_class = UserSubjectSerializer


class UserLessonViewSet(viewsets.ModelViewSet):
    queryset = UserLesson.objects.all()
    serializer_class = UserLessonSerializer


class UserTestViewSet(viewsets.ModelViewSet):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
