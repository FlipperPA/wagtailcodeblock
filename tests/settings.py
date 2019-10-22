from django.conf import settings

SECRET_KEY = "tests"
DEBUG = True

TEMPLATES = [
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True}
]

INSTALLED_APPS = settings.INSTALLED_APPS + [
    "django.contrib.auth",
    "django.contrib.contenttypes",

    "wagtail.core",
    "wagtail.admin",
    "wagtailcodeblock",

    "tests",
]

MIDDLEWARE = settings.MIDDLEWARE + ["wagtail.core.middleware.SiteMiddleware"]

ROOT_URLCONF = "tests.urls"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db.sqlite3',
    }
}
