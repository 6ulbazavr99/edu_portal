from rest_framework import routers
from .views import SubjectViewSet, LessonViewSet, TestViewSet

router = routers.DefaultRouter()
router.register(r'subject', SubjectViewSet, basename='subject')
router.register(r'lesson', LessonViewSet, basename='lesson')
router.register(r'test', TestViewSet, basename='test')

urlpatterns = [
]

urlpatterns += router.urls
