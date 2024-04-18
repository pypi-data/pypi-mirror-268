# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

CLASSIFIERS = ['Environment :: Web Environment', 'Framework :: Django', 'Programming Language :: Python', ]

setup(
  name = "django-unique-session",
  description = "Unique session handler for Django",
  long_description = open('README.rst').read(),
  author = "Gaël Le Mignot",
  author_email = "gael@pilotsystems.net",
  version = '1.0',
  platforms=['OS Independent'],
  license='GPL v3',
  classifiers = CLASSIFIERS,
  packages = find_packages(),
  zip_safe = True,
)
