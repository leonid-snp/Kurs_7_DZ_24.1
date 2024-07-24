from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.paginations import CustomPagination
from course.serializer import CourseSerializer, CourseDetailSerializer
from users.models import User
from users.permissions import IsModer, IsOwner
from course.tasks import send_information_about_course


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        course = serializer.save()
        send_information_about_course(course)
        course.save()

