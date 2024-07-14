from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.serializer import CourseSerializer, CourseDetailSerializer
from users.permissions import IsModer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
