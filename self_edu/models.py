from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from edu.models import Subject, Lesson, Test

User = get_user_model()


class UserSubject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        related_name="user_subjects",

        # blank=False, null=False, default=serializers.CurrentUserDefault()


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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        related_name="user_lessons"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Урок",
        related_name="user_lessons"
    )
    progress = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Прогресс (%)"
    )
    status = models.BooleanField(
        default=False,
        verbose_name="Статус завершенности урока"
    )

    def __str__(self):
        return f"{self.lesson} - Progress: {self.progress}%"


class UserTest(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        related_name="user_tests"
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name="Тест",
        related_name="user_tests"
    )
    user_answers = models.JSONField(verbose_name="Ответы пользователя", default=dict)
    status = models.BooleanField(
        default=False,
        verbose_name="Статус завершенности теста"
    )

    def __str__(self):
        return f"Test {self.test} - Completed: {'Yes' if self.status else 'No'}"
