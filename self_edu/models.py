from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from edu.models import Subject


User = get_user_model()


class UserSubject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        related_name="user_subjects"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=_("Предмет"),
        related_name="subject_users"
    )
    progress = models.PositiveSmallIntegerField(default=0, verbose_name=_("Прогресс"))
    status = models.BooleanField(default=False, verbose_name=_("Статус завершения"))

    def __str__(self):
        return f"{self.user.username} - {self.subject.title} Progress: {self.progress}%"


class UserLesson(models.Model):
    user_subject = models.ForeignKey(
        UserSubject,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь и предмет"),
        related_name="user_lessons"
    )
    progress = models.PositiveSmallIntegerField(default=0, verbose_name=_("Прогресс"))
    status = models.BooleanField(default=False, verbose_name=_("Статус завершения"))

    def __str__(self):
        return f"{self.user_subject.user.username} - Lesson Progress: {self.progress}%"


class UserTest(models.Model):
    user_lesson = models.ForeignKey(
        UserLesson,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь и урок"),
        related_name="user_tests"
    )
    user_answers = models.JSONField(verbose_name=_("Ответы пользователя"))
    status = models.BooleanField(default=False, verbose_name=_("Статус завершения"))

    def __str__(self):
        return f"{self.user_lesson.user_subject.user.username} - Test Status: {'Completed' if self.status else 'Incomplete'}"
