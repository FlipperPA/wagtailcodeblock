from wagtail.admin.panels import StreamFieldPanel
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
    body = StreamField(CodeStreamBlock(), blank=True,)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
