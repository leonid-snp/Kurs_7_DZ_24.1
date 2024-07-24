import datetime

import pytz
from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from subscription.models import Subscription
from users.models import User


@shared_task()
def send_information_about_course(course):
    course_subscriptions = Subscription.objects.filter(course=course.pk)
    for subscription in course_subscriptions:
        send_mail(
            subject='Обновление курса!',
            message=f'Ваш курс {subscription.course.name} был успешно обновлен!',
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email]
        )


@shared_task()
def check_user_is_active():
    users = User.objects.filter(is_active=True, is_superuser=False, last_login__isnull=False)
    if users.exists():
        for user in users:
            print("start!")
            if datetime.datetime.now(pytz.timezone("Europe/Moscow")) - user.last_login > datetime.timedelta(weeks=4):
                user.is_active = False
                user.save()
