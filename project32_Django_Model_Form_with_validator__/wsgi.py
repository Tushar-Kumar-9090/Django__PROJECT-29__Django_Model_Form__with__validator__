"""
WSGI config for project32_Django_Model_Form_with_validator__ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project32_Django_Model_Form_with_validator__.settings')

application = get_wsgi_application()
