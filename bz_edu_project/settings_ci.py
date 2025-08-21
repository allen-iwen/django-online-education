from .settings import *

# Override database settings for CI to use SQLite (no external services required)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Ensure DEBUG doesn't affect checks in CI
DEBUG = False

# Keep a permissive ALLOWED_HOSTS for CI environment
ALLOWED_HOSTS = ["*"]