from rest_framework import serializers
from edu.models import Test
from .models import UserSubject, UserLesson, UserTest


class UserSubjectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserSubject
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class UserLessonSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserLesson
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class UserTestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserTest
        fields = '__all__'
        read_only_fields = ('status', 'test')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return self.check_answers(validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr != 'status':
                setattr(instance, attr, value)
        instance = self.check_answers(validated_data, instance)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super(UserTestSerializer, self).to_representation(instance)
        representation['test_questions'] = instance.test.questions
        representation['correct_answers'] = instance.test.correct_answers
        return representation

    def check_answers(self, validated_data, instance=None):
        user_answers = validated_data.get('user_answers')
        test = validated_data.get('test', instance.test if instance else None)
        correct_answers = test.correct_answers

        user_answers_sorted = sorted(user_answers.items())
        correct_answers_sorted = sorted(correct_answers.items())

        status = user_answers_sorted == correct_answers_sorted
        validated_data['status'] = status

        if instance:
            instance.status = status
        else:
            instance = UserTest.objects.create(**validated_data)

        self.update_lesson_and_subject_progress(instance, status)
        return instance

    def update_lesson_and_subject_progress(self, user_test_instance, status):
        user_lesson, created = UserLesson.objects.get_or_create(
            user=user_test_instance.user,
            lesson=user_test_instance.test.lesson,
            defaults={'progress': 0}
        )

        if status:
            total_tests = user_lesson.lesson.tests.count()
            progress_increment = 100 / total_tests if total_tests > 0 else 0
            user_lesson.progress = min(user_lesson.progress + progress_increment, 100)

            if self.all_lessons_tests_passed(user_lesson):
                user_lesson.status = True

        user_lesson.save()
        self.update_subject_progress(user_lesson)

    def all_lessons_tests_passed(self, user_lesson):
        lesson_tests = Test.objects.filter(lesson=user_lesson.lesson)
        return all(
            UserTest.objects.filter(user=user_lesson.user, test=test, status=True).exists() for test in lesson_tests
        )

    def all_subject_lessons_completed(self, user, subject):
        user_lessons = UserLesson.objects.filter(user=user, lesson__subject=subject)
        return all(ul.status for ul in user_lessons)

    def update_subject_progress(self, user_lesson):
        user_subject, created = UserSubject.objects.get_or_create(
            user=user_lesson.user,
            subject=user_lesson.lesson.subject,
            defaults={'progress': 0}
        )

        total_lessons = user_lesson.lesson.subject.lessons.count()
        total_progress = sum(
            ul.progress for ul in UserLesson.objects.filter(
                user=user_lesson.user,
                lesson__subject=user_lesson.lesson.subject
            )
        )
        user_subject.progress = total_progress / total_lessons if total_lessons > 0 else 0

        if self.all_subject_lessons_completed(user_lesson.user, user_lesson.lesson.subject):
            user_subject.status = True

        user_subject.save()




