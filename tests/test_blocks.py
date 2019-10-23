from json import dumps

from tests.models import CodeBlockPage


def test_create_page():
    """
    Tests creating a page with a Code Block.
    """
    t = CodeBlockPage(
        title='Test Page',
        slug='test-page',
        body=dumps([{
            "type": "code",
            "value": {
                "language": "python",
                "code": "print([x for x in range(1, 5)])",
            }
        }])
    )
    # t.save()
    print(t)

    assert True


"""
def test_render_moment_unlocalized():
    form = forms.DateTimeFieldForm()
    widget = form.fields["datetime_field"].widget
    assert isinstance(widget, widgets.DateTimePicker)
    assert "YYYY-MM-DD HH:mm:ss" in widget.js_options["format"]
"""
