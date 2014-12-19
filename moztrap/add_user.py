#!/usr/bin/env python

import os
import sys
import argparse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moztrap.settings.default")

from django.contrib.auth.models import User


def add_user(username, email, password, is_admin=False):

    default_user, created = User.objects.get_or_create(
        username=username, email=email,
        is_active=True, is_staff=is_admin, is_superuser=is_admin
    )
    default_user.set_password(password)
    default_user.save()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('username')
    parser.add_argument('email')
    parser.add_argument('password')
    parser.add_argument('--is_admin', action='store_true')
    args = parser.parse_args()

    add_user(args.username, args.email, args.password, args.is_admin)
    print "User: %s added." % args.username
