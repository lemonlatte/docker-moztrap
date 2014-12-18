#!/usr/bin/env python

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moztrap.settings.default")

from django.contrib.auth.models import User


def add_user(username, email, password):

    default_user, created = User.objects.get_or_create(
        username=username, email=email,
        is_active=True, is_staff=True, is_superuser=True
    )
    default_user.set_password(password)
    default_user.save()


if __name__ == "__main__":

    add_user(*sys.argv[1:4])
    print "User added."
