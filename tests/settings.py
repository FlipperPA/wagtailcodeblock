from django.conf import settings

WAGTAILADMIN_BASE_URL = "https://example.com"
ALLOWED_HOSTS = ["*"]
SECRET_KEY = "tests"
DEBUG = True
USE_TZ = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": True,
        },
    }
]

INSTALLED_APPS = settings.INSTALLED_APPS + [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "wagtail",
    "wagtail.admin",
    "wagtail.documents",
    "tests",
    "wagtail.images",
    "wagtail.users",
    "wagtailcodeblock",
    "modelcluster",
    "taggit",
]

MIDDLEWARE = settings.MIDDLEWARE + [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tests.urls"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "test_db.sqlite3"}
}

STATIC_URL = "/static/"

WAGTAIL_SITE_NAME = "Test Site"
