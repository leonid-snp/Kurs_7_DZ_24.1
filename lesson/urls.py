from django.urls import path
from lesson.apps import LessonConfig
from lesson.views import (LessonCreateApiView, LessonDestroyApiView,
                          LessonListApiView, LessonRetrieveApiView,
                          LessonUpdateApiView)


app_name = LessonConfig.name

urlpatterns = [
    path("", LessonListApiView.as_view(), name="list"),
    path("<int:pk>/", LessonRetrieveApiView.as_view(), name="read"),
    path("create/", LessonCreateApiView.as_view(), name="create"),
    path("<int:pk>/update/", LessonUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete/", LessonDestroyApiView.as_view(), name="delete")

]
