from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from edu.models import Subject, Lesson, Test
from edu.serializers import SubjectSerializer, LessonSerializer, TestSerializer, \
    AvailableSubjectsSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [IsAuthenticated()]
        return [IsAdminUser()]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [IsAuthenticated()]
        return [IsAdminUser()]


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [IsAuthenticated()]
        return [IsAdminUser()]

class AvailableSubjects(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_grade = request.user.grade
        subjects = Subject.objects.filter(grades__in=[user_grade])
        serializer = AvailableSubjectsSerializer(subjects, many=True)
        return Response(serializer.data)
