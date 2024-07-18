from rest_framework.serializers import ValidationError


url = 'youtube.com'


def validates_url(value):
    if value.split('@')[1] != url:
        raise ValidationError('URL - не соответствует правилами сайта')
