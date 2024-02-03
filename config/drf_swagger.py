from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="edu_portal API",
      default_version='v1',   # TODO:
      description="""

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

1. admin[1]
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMTQzMjMxLCJpYXQiOjE3MDY5NDgwMzEsImp0aSI6ImY1MTg0NTI4NjdhYjQ1YzE4YzRkYmIwYzI5MWNiNWJmIiwidXNlcl9pZCI6MX0.RL9ZIPK4_EWdw_EF6d5ALqPflD7wkXCeyeEvPZrbRZs

2. andrey[bastard123]
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMTQzMjcxLCJpYXQiOjE3MDY5NDgwNzEsImp0aSI6IjczOWY1MDlkOWNjYTQ0MTk4MWUxZDBiZjM2OTAxNDRlIiwidXNlcl9pZCI6Mn0.xoK2wXrRpiretVJGMefrGJ0LWrgxtMRihE_WnmXBs3U

3. oleg[bastard123]
Bearer 

4. sanya[bastard123]
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMTQzNDk3LCJpYXQiOjE3MDY5NDgyOTcsImp0aSI6ImU3MGQxYWEwZWY2NTRmYjk5ZjJjNWE1MGM2ZTQ0YTQ5IiwidXNlcl9pZCI6NH0.R_DMCeBagwThnt_t4yoRW5HavGvUeQP0lE2PBRYZEdQ            

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
############### <account:
customuser: starter model, view, ser, urls, admin +
grade: starter model, view, ser, urls, admin +
user: auth +
user: sers, perms
############### :account>
#
#
#
############### <edu:
subject: starter model, view, ser, urls, admin
lesson: starter model, view, ser, urls, admin
test: starter model, view, ser, urls, admin
############### :edu>
#
#
#
############### <self_edu:
usersubject: starter model, view, ser, urls, admin
userlesson: starter model, view, ser, urls, admin
usertest: starter model, view, ser, urls, admin
############### :self_edu>
#
#
#
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
############### <user reg:
#
{
  "username": "andrey",
  "password": "bastard123",
  "password_confirmation": "bastard123"
}
#
############### :user reg>
#
#
#
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
      """,
      terms_of_service="https://github.com/6ulbazavr99/edu_portal",
      license=openapi.License(name="↑ GitHub ↑"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
