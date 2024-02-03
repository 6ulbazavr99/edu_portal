"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from account.views import GradeViewSet
from edu.views import SubjectViewSet, LessonViewSet, TestViewSet
from self_edu.views import UserSubjectViewSet, UserLessonViewSet, UserTestViewSet
from .drf_swagger import urlpatterns as doc_urls


# router = routers.DefaultRouter()
# router.register(r'api/v1/grade', GradeViewSet, basename='grade')
#
# router.register(r'api/v1/subject', SubjectViewSet, basename='subject')
# router.register(r'api/v1/lesson', LessonViewSet, basename='lesson')
# router.register(r'api/v1/test', TestViewSet, basename='test')
#
# router.register(r'api/v1/usersubject', UserSubjectViewSet, basename='usersubject')
# router.register(r'api/v1/userlesson', UserLessonViewSet, basename='userlesson')
# router.register(r'api/v1/usertest', UserTestViewSet, basename='usertest')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/edu/', include('edu.urls')),
    path('api/v1/self-edu/', include('self_edu.urls')),
]

# urlpatterns += router.urls

urlpatterns += doc_urls  # swagger docs urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
