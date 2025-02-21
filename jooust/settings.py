import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MIDDLEWARE = [
    # ...existing code...
    'django.middleware.csrf.CsrfViewMiddleware',
    # ...existing code...
]

TEMPLATES = [
    {
        # ...existing code...
        'DIRS': [os.path.join(BASE_DIR, 'jooust/templates')],
        # ...existing code...
    },
]
