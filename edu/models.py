from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import Grade


class Subject(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название предмета"))
    grades = models.ManyToManyField(Grade, verbose_name=_("Классы/уровни обучения"))
    description = RichTextField(verbose_name=_("Описание предмета"), blank=True, null=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=_("Предмет"),
        related_name="lessons"
    )
    topic = models.CharField(max_length=255, verbose_name=_("Тема урока"))
    description = RichTextField(verbose_name=_("Описание урока"), blank=True, null=True)

    def __str__(self):
        return self.topic


class Test(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name=_("Урок"),
        related_name="tests"
    )
    questions = RichTextField(verbose_name=_("Текст вопросов"))
    correct_answers = models.JSONField(verbose_name=_("Правильные ответы"))  # предполагаем, что ответы хранятся в формате JSON

    def __str__(self):
        return f"Test for {self.lesson.topic}"
