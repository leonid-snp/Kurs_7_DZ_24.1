from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="user_1@test.ru")
        self.course = Course.objects.create(name='course_1', author=self.user)
        self.lesson = Lesson.objects.create(name='lesson_1', course=self.course, author=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('lesson:read', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse('lesson:create')
        data = {
            'name': 'lesson_2',
            'url': 'lesson_2@youtube.com',
            'course': 1,
            'author': self.user.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('lesson:update', args=(self.lesson.pk,))
        data = {
            'name': 'lesson_2.1',
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'lesson_2.1'
        )

    def test_lesson_delete(self):
        url = reverse('lesson:delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('lesson:list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.lesson.pk,
                    'url': self.lesson.url,
                    'name': self.lesson.name,
                    'description': self.lesson.description,
                    'photo': self.lesson.photo,
                    'course': self.course.pk,
                    'author': self.user.pk
                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )
