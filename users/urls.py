from django.urls import path
from users.apps import UsersConfig
from users.views import (UserListApiView, UserDestroyApiView,
                          UserCreateApiView, UserRetrieveApiView,
                          UserUpdateApiView)


app_name = UsersConfig.name

urlpatterns = [
    path("", UserListApiView.as_view(), name="list"),
    path("<int:pk>/", UserRetrieveApiView.as_view(), name="read"),
    path("create/", UserCreateApiView.as_view(), name="create"),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDestroyApiView.as_view(), name="delete")
]
