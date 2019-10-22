from django.urls import include, re_path

from wagtail.core import urls as wagtail_urls

urlpatterns = [
    re_path(r'', include(wagtail_urls)),
]
