from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtailcodeblock.blocks import CodeBlock


class CodeStreamBlock(StreamBlock):
    """
    Test StreamBlock with a CodeBlock.
    """

    code = CodeBlock()


class CodeBlockPage(Page):
    """
    Test Page with a code block in body.
    """
    body = StreamField([
        ('code', CodeBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
