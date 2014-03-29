import os

BASE_DIR = "/home/user/projects/box/"


DEBUG=True
ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'box',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STRIPE_SECRET_KEY = 'sk_test_',
STRIPE_PUBLIC_KEY = 'pk_test_',

PAYMENTS_PLANS = {
    "monthly": {
        "stripe_plan_id": "college-men",
        "name": "Personalized Care Package",
        "description": "A monthly care package by college guys for college guys",
        "price": 20,
        "currency": "usd",
        "interval": "month"
    },
    "monthly-discount": {
        "stripe_plan_id": "college-men-discount",
        "name": "Personalized Care Package (Discount)",
        "description": "A monthly care package by college guys for college guys",
        "price": 10,
        "currency": "usd",
        "interval": "month",
    },
    },

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'aq3lpz23_vqy@02(+3^8k8_+7w%chstavs(1ymt+gc$)$kyjr*'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'no-reply@thenicepackage.com' #bulk sender
EMAIL_HOST_PASSWORD = 'N!cepackage!'
