django-dinero-auth/README.rst
=============================
DINERO_AUTH
===========

dinero_auth is a token authentication system with 
ip validation and browser validation.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "dinero_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'dinero_auth',
    )

2. Run `python manage.py migrate` to create the dinero_auth models.
