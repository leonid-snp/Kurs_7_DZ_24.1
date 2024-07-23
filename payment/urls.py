from django.urls import path
from payment.apps import PaymentConfig
from payment.views import (PaymentListApiView, PaymentDestroyApiView,
                           PaymentCreateApiView, PaymentRetrieveApiView,
                           PaymentUpdateApiView)

app_name = PaymentConfig.name

urlpatterns = [
    path("", PaymentListApiView.as_view(), name="list"),
    path("<int:pk>/", PaymentRetrieveApiView.as_view(), name="read"),
    path("create/", PaymentCreateApiView.as_view(), name="create"),
    path("<int:pk>/update/", PaymentUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete/", PaymentDestroyApiView.as_view(), name="delete")
]
