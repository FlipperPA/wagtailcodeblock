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
    A Wagtail StreamField block for code syntax highlighting using PrismJS.
    """

    def __init__(self, local_blocks=None, **kwargs):
        # Languages included in PrismJS core
        # Review: https://github.com/PrismJS/prism/blob/gh-pages/prism.js#L602
        self.INCLUDED_LANGUAGES = (
            ('html', 'HTML'),
            ('mathml', 'MathML'),
            ('svg', 'SVG'),
            ('xml', 'XML'),
        )

        if local_blocks is None:
            local_blocks = []
        else:
            local_blocks = local_blocks.copy()

        language_choices, language_default = self.get_language_choice_list(**kwargs)

        local_blocks.extend([
            ('language', ChoiceBlock(
                choices=language_choices,
                help_text=_('Coding language'),
                label=_('Language'),
                default=language_default,
            )),
            ('code', TextBlock(label=_('Code'))),
        ])

        super().__init__(local_blocks, **kwargs)

    def get_language_choice_list(self, **kwargs):
        # Get default languages
        WCB_LANGUAGES = get_language_choices()
        # If a language is passed in as part of a code block, use it.
        language = kwargs.get('language', False)

        total_language_choices = WCB_LANGUAGES + self.INCLUDED_LANGUAGES

        if language in [lang[0] for lang in total_language_choices]:
            for language_choice in total_language_choices:
                if language_choice[0] == language:
                    language_choices = (language_choice,)
                    language_default = language_choice[0]
        else:
            language_choices = WCB_LANGUAGES
            language_default = None

        return language_choices, language_default

    @property
    def media(self):
        # Theme and version from Wagtail Code Block settings
        THEME = get_theme()
        PRISM_VERSION = get_prism_version()
        if THEME:
            prism_theme = '-{theme}'.format(theme=THEME)
        else:
            prism_theme = ""

        js_list = [
            "https://cdnjs.cloudflare.com/ajax/libs/prism/{prism_version}/prism.min.js".format(
                prism_version=PRISM_VERSION,
            ),
        ]

        # Get the languages for the site from Django's settings, or the default in get_language_choices()
        for lang_code, lang_name in get_language_choices():
            if lang_code not in [included_language[0] for included_language in self.INCLUDED_LANGUAGES]:
                js_list.append(
                    "https://cdnjs.cloudflare.com/ajax/libs/prism/{prism_version}/components/prism-{lang_code}.min.js".format(
                        prism_version=PRISM_VERSION,
                        lang_code=lang_code,
                    )
                )
        return Media(
            js=js_list,
            css={
                'all': [
                    "https://cdnjs.cloudflare.com/ajax/libs/prism/{prism_version}/themes/prism{prism_theme}.min.css".format(
                        prism_version=PRISM_VERSION,
                        prism_theme=prism_theme,
                    ),
                    "wagtailcodeblock/css/wagtail-code-block.min.css",
                ]
            }
        )

    class Meta:
        icon = 'code'
        template = 'wagtailcodeblock/code_block.html'
        form_classname = 'code-block struct-block'
        form_template = 'wagtailcodeblock/code_block_form.html'
