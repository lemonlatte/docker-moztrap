import os

# DOMAIN_NAME = "moztrap.example.com"
ADMIN_USERNANE = "moztrap"
ADMIN_PASSWORD = "000000"
ADMIN_EMAIL = "admin@localhost"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moztrap.settings.default")

from django.contrib.auth.models import User

default_user, created = User.objects.get_or_create(
    username=ADMIN_USERNANE, email=ADMIN_EMAIL,
    is_active=True, is_staff=True, is_superuser=True
)
default_user.set_password(ADMIN_PASSWORD)
default_user.save()
