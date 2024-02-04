# from rest_framework import routers
# from .views import SubjectViewSet, LessonViewSet, TestViewSet
#
# router = routers.DefaultRouter()
# router.register(r'subject', SubjectViewSet, basename='subject')
# router.register(r'lesson', LessonViewSet, basename='lesson')
# router.register(r'test', TestViewSet, basename='test')
#
from django.urls import path

from edu.views import AvailableSubjects

# urlpatterns = [
    # path('available-subjects/', AvailableSubjects.as_view(), name='available_subjects_by_grade'),

# ]

# urlpatterns += router.urls
