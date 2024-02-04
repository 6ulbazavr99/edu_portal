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

1. admin[1] +
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMjIyMTUwLCJpYXQiOjE3MDcwMjY5NTAsImp0aSI6Ijc0MzU2OGNkZWZhMzQ4ZDNiOTM1YWIyZmQwNDM2NWMyIiwidXNlcl9pZCI6MX0.HebPuxXOlB1LtA5YoV4q9mhx5i0eAffKhGQn-cGYZ5o

6. andrey[bastard123] +
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMTU4OTMxLCJpYXQiOjE3MDY5NjM3MzEsImp0aSI6ImM0ZTU2OTAzOGMyNjRjYzdiZWU2Zjg0NTE2MmMyMDZlIiwidXNlcl9pZCI6Mn0.KXAXDQhRU-0nvS8I8NdXNMnCiKrVzKLNEfej0apThnA

7. oleg[bastard123] +
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMTQ4ODYxLCJpYXQiOjE3MDY5NTM2NjEsImp0aSI6IjRkZDAzMzg3NzYwMDQ3MzVhODNhZDQxY2NjMWNmNTA1IiwidXNlcl9pZCI6M30.Hu78ge0vmTRfcg-HU0IPeszrOWaHgRHHJDZ7PF2C3N4

4. sanya[bastard123] -
Bearer             

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
############### <account:
customuser: starter model, view, ser, urls, admin +
grade: starter model, view, ser, urls, admin +
user: auth +
user: sers, perms
grade: sers, perms
user: auto self_edu +
############### :account>
#
#
#
############### <edu:
subject: starter model, view, ser, urls, admin +
lesson: starter model, view, ser, urls, admin +
test: starter model, view, ser, urls, admin +
subject: sers, perms
lesson: sers, perms
test: sers, perms
subject: perm +
############### :edu>
#
#
#
############### <self_edu:
usersubject: starter model, view, ser, urls, admin +
userlesson: starter model, view, ser, urls, admin +
usertest: starter model, view, ser, urls, admin +
userlesson: new model +
usertest: new model +
usersubject: sers, perms
userlesson: sers, perms
usertest: sers, perms
usertest: check_answers +
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
