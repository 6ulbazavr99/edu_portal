# Generated by Django 5.0.1 on 2024-02-04 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveSmallIntegerField(default=0, verbose_name='Прогресс (%)')),
                ('status', models.BooleanField(default=False, verbose_name='Статус завершенности урока')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lessons', to='edu.lesson', verbose_name='Урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lessons', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='UserSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveSmallIntegerField(default=0, verbose_name='Прогресс')),
                ('status', models.BooleanField(default=False, verbose_name='Статус завершения')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_users', to='edu.subject', verbose_name='Предмет')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subjects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answers', models.JSONField(default=dict, verbose_name='Ответы пользователя')),
                ('status', models.BooleanField(default=False, verbose_name='Статус завершенности теста')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tests', to='edu.test', verbose_name='Тест')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tests', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
