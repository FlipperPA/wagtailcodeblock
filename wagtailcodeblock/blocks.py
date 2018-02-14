from django.forms import Media
from django.utils.translation import ugettext_lazy as _

# Wagtail 2.0 compatibility - new package paths
try:
    from wagtail.core.blocks import (
        StructBlock,
        TextBlock,
        ChoiceBlock,
    )
except ImportError:
    from wagtail.wagtailcore.blocks import (
        StructBlock,
        TextBlock,
        ChoiceBlock,
    )

from .settings import (
    get_language_choices,
    get_theme,
    get_prism_version
)


class CodeBlock(StructBlock):
    """
    Code Highlighting Block
    """

    WCB_LANGUAGES = get_language_choices()
    off_languages = ['html', 'mathml', 'svg', 'xml']


    language = ChoiceBlock(choices=WCB_LANGUAGES, help_text=_('Coding language'), label=_('Language'))
    code = TextBlock(label=_('Code'))

    @property
    def media(self):

        theme = get_theme()

        prism_version = get_prism_version()
        if theme:
            prism_theme = '-{}'.format(theme)
        else:
            prism_theme = ""

        js_list = [
            "https://cdnjs.cloudflare.com/ajax/libs/prism/{}/prism.min.js".format(
                prism_version,
            ),
        ]

        for lang_code, lang_name in self.WCB_LANGUAGES:
            # Review: https://github.com/PrismJS/prism/blob/gh-pages/prism.js#L602
            if lang_code not in self.off_languages:
                js_list.append(
                    "https://cdnjs.cloudflare.com/ajax/libs/prism/{}/components/prism-{}.min.js".format(
                        prism_version,
                        lang_code,
                    )
                )
        return Media(
            js=js_list,
            css={
                'all': [
                    "https://cdnjs.cloudflare.com/ajax/libs/prism/{}/themes/prism{}.min.css".format(
                        prism_version, prism_theme
                    ),
                ]
            }
        )

    class Meta:
        icon = 'code'
        template = 'wagtailcodeblock/code_block.html'
        form_classname = 'code-block struct-block'
        form_template = 'wagtailcodeblock/code_block_form.html'
