from rest_framework.generics import (CreateAPIView, ListAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.models import Course
from subscription.models import Subscription
from subscription.serializer import SubscriptionSerializer
from users.permissions import IsModer


class SubscriptionCreateApiView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (~IsModer, IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        if Subscription.objects.filter(user=user, course=course_item).exists():
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'

        return Response({'message': message})


class SubscriptionListApiView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
