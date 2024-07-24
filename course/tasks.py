from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from subscription.models import Subscription


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
