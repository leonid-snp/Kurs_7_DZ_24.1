from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="su@test.ru")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("12345")
        user.save()
