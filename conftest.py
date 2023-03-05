from json import dumps

from django.contrib.contenttypes.models import ContentType

import pytest
from wagtail.models import Page, Locale, Site

from tests.models import CodeBlockPage


@pytest.fixture
def test_page(db):
    """
    Create a root page in the same way Wagtail does in migrations. See:
    https://github.com/wagtail/wagtail/blob/main/wagtail/core/migrations/0002_initial_data.py#L12  # noqa
    """
    """
    We should created the home and vendor pages at the same time so they can be done in
    any order, since both require a Site.
    """
    page_content_type, created = ContentType.objects.get_or_create(
        model="page", app_label="wagtailcore"
    )
    # Locale.objects.create(language_code="en")
    root_page, created = Page.objects.get_or_create(
        title="Root",
        slug="root",
        content_type=page_content_type,
        path="0001",
        depth=1,
        numchild=1,
        url_path="/",
    )
    # Create homepage
    test_page, created = CodeBlockPage.objects.get_or_create(
        # Required Wagtail Page fields
        title="TEST Wagtail Code Block Page",
        slug="wagtail-code-block",
        content_type=page_content_type,
        path="00010002",
        depth=2,
        numchild=0,
        url_path="/wagtail-code-block/",
        # Wagtail Code Block test fields
        body=dumps([{
            "type": "code",
            "value": {
                "language": "python",
                "code": "print([x for x in range(1, 5)])",
            },
        }]),
    )

    return test_page
