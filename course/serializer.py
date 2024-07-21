from rest_framework.serializers import ModelSerializer, SerializerMethodField
from course.models import Course
from lesson.models import Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lesson = SerializerMethodField()
    subscription = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lesson(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_subscription(self, course):
        user = self.context['request'].user
        subscription = Subscription.objects.all().filter(course=course.id)
        if subscription:
            return True
        return False

    class Meta:
        model = Course
        fields = ('name', 'description', 'number_of_lessons', 'lesson', 'subscription')
