from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.serializer import CourseSerializer, CourseDetailSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer
