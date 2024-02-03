from django.contrib import admin

from .models import UserSubject, UserLesson, UserTest

admin.site.register(UserSubject)
admin.site.register(UserLesson)
admin.site.register(UserTest)
