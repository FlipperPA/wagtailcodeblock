from wagtail.wagtailcore.blocks import StructBlock, TextBlock, ChoiceBlock

from .settings import get_language_choices


class CodeBlock(StructBlock):
    """
    Code Highlighting Block
    """

    WCB_LANGUAGES = get_language_choices()

    language = ChoiceBlock(choices=WCB_LANGUAGES)
    code = TextBlock()

    class Meta:
        icon = 'code'
        template = 'wagtailcodeblock/code_block.html'
        form_template = 'wagtailcodeblock/code_block_form.html'
