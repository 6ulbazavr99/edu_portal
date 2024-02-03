from rest_framework import routers
from .views import UserSubjectViewSet, UserLessonViewSet, UserTestViewSet

router = routers.DefaultRouter()
router.register(r'user-subject', UserSubjectViewSet, basename='user-subject')
router.register(r'user-lesson', UserLessonViewSet, basename='user-lesson')
router.register(r'user-test', UserTestViewSet, basename='user-test')

urlpatterns = [
]

urlpatterns += router.urls
