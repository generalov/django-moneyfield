#!/usr/bin/env python
import sys
from os import path

import django
from django.conf import settings, global_settings
from django.core.management import execute_from_command_line


if not settings.configured:
    module_root = path.dirname(path.realpath(__file__))

    settings.configure(
        DEBUG = False,
        TEMPLATE_DEBUG = True,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        MIDDLEWARE_CLASSES = [],
        TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner' if django.VERSION < (1,6) else 'django.test.runner.DiscoverRunner',
        USE_L10N = True,
        SECRET_KEY = "justthetestapp",
        INSTALLED_APPS = (
            'testapp',
        ),

        MONEY_CURRENCY_CHOICES = (
            ('AAA', 'AAA'),
            ('BBB', 'BBB'),
            ('CCC', 'CCC'),
        )
    )

def runtests():
    argv = sys.argv[:1] + ['test', 'testapp'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
