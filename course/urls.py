from rest_framework.routers import SimpleRouter
from course.apps import CourseConfig
from course.views import CourseViewSet


app_name = CourseConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = []
urlpatterns += router.urls
