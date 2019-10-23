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
        body=dumps([{
            "type": "code",
            "value": {
                "language": "python",
                "code": "print([x for x in range(1, 5)])",
            }
        }])
    )
    t.save()

    assert t.body == """<div class="block-code">
<script src="/static/wagtailcodeblock/js/prism.min.js" type='text/javascript'></script><link href="/static/wagtailcodeblock/css/prism.min.css" rel="stylesheet"><link href='https://cdnjs.cloudflare.com/ajax/libs/prism/1.17.1/themes/prism-coy.min.css' rel='stylesheet'/><script>
                language_class_name = 'language-python';
            </script><pre class="line-numbers"><code id="target-element-current">print([x for x in range(1, 5)])</code></pre><script>
                var block_num = (typeof block_num === 'undefined') ? 0 : block_num;
                block_num++;
                document.getElementById('target-element-current').className = language_class_name;
                document.getElementById('target-element-current').id = 'target-element-' + block_num;
            </script>
</div>"""
