"""
WSGI config for restaurants project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
root_path = os.path.abspath(os.path.split(__file__)[0])
sys.path.insert(0, os.path.join(root_path, 'restaurants'))
sys.path.insert(0, root_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurants.settings')

application = get_wsgi_application()
