from django.urls import path
from subscription.apps import SubscriptionConfig
from subscription.views import (SubscriptionCreateApiView, SubscriptionListApiView)


app_name = SubscriptionConfig.name

urlpatterns = [
    path("", SubscriptionListApiView.as_view(), name="list"),
    path("create/", SubscriptionCreateApiView.as_view(), name="create")
]
