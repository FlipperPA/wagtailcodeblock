from json import dumps

import pytest

from tests.models import CodeBlockPage


@pytest.mark.django_db
def test_create_page(test_page):
    """
    Tests creating a page with a Code Block.
    """
    assert (
        '<code id="target-element-current">print([x for x in range(1, 5)])</code>'
        in test_page.body.render_as_block()
    )
