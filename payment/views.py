from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from payment.models import Payment
from payment.serializer import PaymentSerializer
from payment.services import create_stripe_price, create_stripe_sessions


class PaymentCreateApiView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(users=self.request.user)
        price = create_stripe_price(payment.sum)
        session_id, payment_link = create_stripe_sessions(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class PaymentListApiView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date_payment',)
    filterset_fields = ('paid_course', 'paid_lesson', 'cash_payment', 'payment_to_account')


class PaymentRetrieveApiView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateApiView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDestroyApiView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
