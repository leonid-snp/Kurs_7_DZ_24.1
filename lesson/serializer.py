from rest_framework import serializers
from lesson.models import Lesson
from lesson.validators import validates_url


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.CharField(validators=[validates_url])

    class Meta:
        model = Lesson
        fields = '__all__'
