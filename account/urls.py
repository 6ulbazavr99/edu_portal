from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import CustomUserViewSet, GradeViewSet

router = routers.DefaultRouter()
router.register(r'user', CustomUserViewSet, basename='user')
# router.register(r'grade', GradeViewSet, basename='grade')


urlpatterns = [
    path('user/authorization/login/', TokenObtainPairView.as_view()),
    path('user/authorization/refresh/', TokenRefreshView.as_view()),

]


urlpatterns += router.urls
