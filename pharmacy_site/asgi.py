"""
ASGI config for pharmacy_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from pharmacy_site.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pharmacy_site.settings')

application = get_asgi_application()
STATIC_URL = '/static/'

# Ensure that Django can find your static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'store/static'),
]
