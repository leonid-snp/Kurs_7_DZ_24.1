from rest_framework.serializers import ValidationError


url = 'youtube.com'


def validates_url(value):
    if not value.endswith(url):
        raise ValidationError('URL - не соответствует правилами сайта')
