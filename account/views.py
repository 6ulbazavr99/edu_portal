from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Grade
from account.permissions import IsAccountOwnerOrAdmin
from account.serializers import CustomUserSerializer, GradeSerializer, CustomUserRegisterSerializer, \
    CustomUserRetrieveSerializer, CustomUserListSerializer, ProfileSerializer  # , ProfileSerializer

User = get_user_model()


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [IsAuthenticated()]
        return [IsAdminUser()]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserRegisterSerializer
        if self.action == 'retrieve':
            return CustomUserRetrieveSerializer
        if self.action == 'list':
            return CustomUserListSerializer
        return CustomUserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update'):
            return [IsAccountOwnerOrAdmin()]
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
