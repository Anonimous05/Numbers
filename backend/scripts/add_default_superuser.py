import os

from django.contrib.auth.models import User


def run():
    user = User.objects.create_superuser(
        username=os.environ.get('DEFAULT_SUPERUSER_NAME', 'admin'),
        password=os.environ.get('DEFAULT_SUPERUSER_PASSWORD', '123'),
        email=os.environ.get('DEFAULT_SUPERUSER_EMAIL', 'email@gmail.com')
    )
    user.save()
