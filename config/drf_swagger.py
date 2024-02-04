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
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMjM5OTk5LCJpYXQiOjE3MDcwNDQ3OTksImp0aSI6ImU2ZTFmNGY1NzZlNTQxZmNiZTMxNWRlN2ZjYzc0Y2JkIiwidXNlcl9pZCI6MX0.RBD887Sr3AuSYaYFWCv2BlnPZsmWHqb831hfevGc8j0

2. andrey[bastard123] +
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMjI4Mjk2LCJpYXQiOjE3MDcwMzMwOTYsImp0aSI6IjQ5NWUwNGU3NzE3YTRlZGViODY2YWQ5ZjBmNjlmMmUyIiwidXNlcl9pZCI6Mn0.S31Glog8UXIWa50jRTkOy9IjsPZaB01jwNO7j5zewsw

3. oleg[bastard123] +
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMjMwNTEzLCJpYXQiOjE3MDcwMzUzMTMsImp0aSI6IjUzNzRhY2Y2NDQyMDRjOWI4MzYxMzg2NjU0MTQ4OTZiIiwidXNlcl9pZCI6M30.T2LKW3YRd5A539WuhTawoXj3HOGY_eCpRkzkhTIEy3I

4. sanya2[bastard123] +
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzExMjMwODkzLCJpYXQiOjE3MDcwMzU2OTMsImp0aSI6IjRmYTA1NTM4MmFlNzQ5MmU4OWY0MTdjYjliN2IxYTcwIiwidXNlcl9pZCI6NH0.WiUaIGASD2CkW5Ls5QnBGFSHmjXtTdX9EL2pPyOpKDw          

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
