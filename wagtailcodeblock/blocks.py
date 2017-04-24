from django.forms import Media
from wagtail.wagtailcore.blocks import StructBlock, TextBlock, ChoiceBlock

from .settings import get_language_choices


class CodeBlock(StructBlock):
    """
    Code Highlighting Block
    """

    WCB_LANGUAGES = get_language_choices()

    language = ChoiceBlock(choices=WCB_LANGUAGES)
    code = TextBlock()

    @property
    def media(self):
        prism_version = "1.6.0"
        js_list = [
            "https://cdnjs.cloudflare.com/ajax/libs/prism/{}/prism.min.js".format(
                prism_version,
            ),
        ]

        for lang_code, lang_name in self.WCB_LANGUAGES:
            js_list.append(
                "https://cdnjs.cloudflare.com/ajax/libs/prism/{}/components/prism-{}.min.js".format(
                    prism_version,
                    lang_code,
                )
            )
        print(js_list)
        return Media(
            js=js_list,
            css={
                'all': [
                    "https://cdnjs.cloudflare.com/ajax/libs/prism/{}/themes/prism.min.css".format(
                        prism_version,
                    ),
                ]
            }
        )

    class Meta:
        icon = 'code'
        template = 'wagtailcodeblock/code_block.html'
        form_classname = 'code-block struct-block'
        form_template = 'wagtailcodeblock/code_block_form.html'
