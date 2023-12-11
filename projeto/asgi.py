"""
ASGI config for projeto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Meus imports
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

# Meus imports
load_dotenv()

application = get_asgi_application()
