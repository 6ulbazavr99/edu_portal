# Generated by Django 5.0.1 on 2024-02-03 08:43

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название предмета')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание предмета')),
                ('grades', models.ManyToManyField(to='account.grade', verbose_name='Классы/уровни обучения')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, verbose_name='Тема урока')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание урока')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='edu.subject', verbose_name='Предмет')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', ckeditor.fields.RichTextField(verbose_name='Текст вопросов')),
                ('correct_answers', models.JSONField(verbose_name='Правильные ответы')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='edu.lesson', verbose_name='Урок')),
            ],
        ),
    ]