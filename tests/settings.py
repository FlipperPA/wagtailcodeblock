from django.conf import settings

SECRET_KEY = "tests"

TEMPLATES = [
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True}
]

INSTALLED_APPS = settings.INSTALLED_APPS + [
    "wagtail.core",
    "wagtail.admin",
    "wagtailcodeblock",
]

MIDDLEWARE = settings.MIDDLEWARE + ["wagtail.core.middleware.SiteMiddleware"]
