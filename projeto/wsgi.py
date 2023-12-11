"""
WSGI config for projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Meus imports
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

# Meus imports
load_dotenv()

application = get_wsgi_application()
