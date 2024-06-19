#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup

setup(
    name="django_remote_jsonschema_forms",
    version="1.0.0",
    description="A platform independent form serializer for Django.",
    author="Gorka Garcia",
    author_email="ggarcia@codesyntax.com",
    url="http://github.com/codesyntax/django_remote_jsonschema_forms/",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=[
        "django_remote_jsonschema_forms",
    ],
    package_data={},
    zip_safe=False,
    requires=[],
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
)
