from json import dumps

import pytest

from tests.models import CodeBlockPage


@pytest.mark.django_db
def test_create_page():
    """
    Tests creating a page with a Code Block.
    """
    t = CodeBlockPage(
        title="Test Page",
        slug="test-page",
        path="000100010001",
        depth=3,
        body=dumps(
            [
                {
                    "type": "code",
                    "value": {
                        "language": "python",
                        "code": "print([x for x in range(1, 5)])",
                    },
                }
            ]
        ),
    )
    t.save()

    assert (
        '<code id="target-element-current">print([x for x in range(1, 5)])</code>'
        in t.body.render_as_block()
    )
