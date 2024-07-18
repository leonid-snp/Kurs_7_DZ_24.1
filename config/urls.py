from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("course/", include("course.urls", namespace="course")),
    path("lesson/", include("lesson.urls", namespace="lesson")),
    path("payment/", include("payment.urls", namespace="payment")),
    path("users/", include("users.urls", namespace="users")),
    path("subscription/", include("subscription.urls", namespace="subscription")),
]
