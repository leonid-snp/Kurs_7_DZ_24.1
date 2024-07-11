from rest_framework.serializers import ModelSerializer, SerializerMethodField
from course.models import Course
from lesson.models import Lesson
from lesson.serializer import LessonSerializer


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lesson = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lesson(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = ('name', 'description', 'number_of_lessons', 'lesson')
