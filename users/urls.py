from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import (UserListApiView, UserDestroyApiView,
                         UserCreateApiView, UserRetrieveApiView,
                         UserUpdateApiView)
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path("", UserListApiView.as_view(), name="list"),
    path("<int:pk>/", UserRetrieveApiView.as_view(), name="read"),
    path("create/", UserCreateApiView.as_view(), name="create"),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDestroyApiView.as_view(), name="delete")
]
