from .base import *  # noqa: F403

ALLOWED_HOSTS = [
    "habitstacker.coderustle.com",
    "habitstacker.azurewebsites.net",
    "coderustle.go.ro",
]

# SECURITY
# -----------------------------------------------------------------------------
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_TRUSTED_ORIGINS = [
    "https://habitstacker.coderustle.com",
    "https://coderustle.go.ro",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "database/prod.sqlite3",  # noqa: F405
    }
}
