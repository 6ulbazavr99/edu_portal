from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from edu.models import Subject


class Grade(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название класса/уровня обучения"))
    maturity = models.BooleanField(default=False, verbose_name=_("Статус зрелости"))

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        verbose_name=_("Класс/уровень обучения"),
        related_name="users",
        blank=True,
        null=True
    )
    subjects = models.ManyToManyField(Subject, blank=True, related_name='users')

    def __str__(self):
        return self.username
