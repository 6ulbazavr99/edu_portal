from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import UserSubject, UserLesson, UserTest
from .permissions import IsOwner
from .serializers import UserSubjectSerializer, UserLessonSerializer, UserTestSerializer


class UserSubjectViewSet(viewsets.ModelViewSet):
    queryset = UserSubject.objects.all()
    serializer_class = UserSubjectSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return UserSubject.objects.filter(user=user)


class UserLessonViewSet(viewsets.ModelViewSet):
    queryset = UserLesson.objects.all()
    serializer_class = UserLessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return UserLesson.objects.filter(user=user)


class UserTestViewSet(viewsets.ModelViewSet):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return UserTest.objects.filter(user=user)
