from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from subscription.models import Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="user_1@test.ru")
        self.course = Course.objects.create(name='course_1', author=self.user)
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('subscription:create')
        data = {
            'user': self.user.pk,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            Subscription.objects.all().count(), 1
        )

    def test_subscription_list(self):
        url = reverse('subscription:list')
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                'id': 2,
                'user': self.user.pk,
                'course': self.course.pk
            }
        ]
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )
