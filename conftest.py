from json import dumps

from django.contrib.contenttypes.models import ContentType

import pytest
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page, Locale, Site, StreamField
from wagtailcodeblock.blocks import CodeBlock


class TestPage(Page):
    body = StreamField([
        ("code", CodeBlock()),
    ])

    content_panels = [
        FieldPanel("body"),
    ]


@pytest.fixture
def test_page(db):
    # Create a root page in the same way Wagtail does in migrations. See:
    # https://github.com/wagtail/wagtail/blob/main/wagtail/core/migrations/0002_initial_data.py#L12  # noqa
    page_content_type, created = ContentType.objects.get_or_create(
        model="page", app_label="wagtail"
    )
    Locale.objects.create(language_code="en")
    root_page, created = Page.objects.get_or_create(
        title="Root",
        slug="root",
        content_type=page_content_type,
        path="0001",
        depth=1,
        numchild=1,
        url_path="/",
    )
    # Create testpage
    test_page, created = TestPage.objects.get_or_create(
        # Required Wagtail Page fields
        title="TEST Code Block Page",
        slug="test-code-block",
        content_type=page_content_type,
        path="00010001",
        depth=2,
        numchild=0,
        url_path="/test-code-block/",
        # Code Block Fields
        body=dumps([
            {
                "type": "code", 
                "value": """{
                    "language": "python",
                    "code": "import json\n\nfor x in range(1, 5):\n    print(x)",
                }"""
            }
        ])
    )
    # Create default site
    site, created = Site.objects.get_or_create(
        hostname="localhost", root_page_id=test_page.id, is_default_site=True
    )

    return test_page
