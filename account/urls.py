from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import CustomUserViewSet, GradeViewSet, ProfileView  # , #ProfileView
from edu.views import AvailableSubjects

router = routers.DefaultRouter()
router.register(r'user', CustomUserViewSet, basename='user')
# router.register(r'grade', GradeViewSet, basename='grade')


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('user/authorization/login/', TokenObtainPairView.as_view()),
    path('user/authorization/refresh/', TokenRefreshView.as_view()),
    path('available-subjects/', AvailableSubjects.as_view(), name='available_subjects_by_grade'),

]


urlpatterns += router.urls
