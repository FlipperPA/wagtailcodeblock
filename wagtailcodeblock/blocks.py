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

    def __init__(self, **kwargs):
        self.language = ChoiceBlock(
            choices=self.get_language_choice_list(**kwargs),
            help_text=_('Coding language'),
            label=_('Language'),
        )
        self.code = TextBlock(label=_('Code'))

        super().__init__(**kwargs)

    def get_language_choice_list(self, **kwargs):
        print('Here')
        # If a language is passed in as part of a code block, use it.
        language = kwargs.get('language', False)

        if language in self.WCB_LANGUAGES + self.included_languages:
            language_choices = (('html', 'HTML',),)
        else:
            language_choices = self.WCB_LANGUAGES

        return language_choices

    @property
    def media(self):
        # Languages included in PrismJS core
        # Review: https://github.com/PrismJS/prism/blob/gh-pages/prism.js#L602
        INCLUDED_LANGUAGES = (
            ('html', 'HTML'),
            ('mathml', 'MathML'),
            ('svg', 'SVG'),
            ('xml', 'XML'),
        )

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
            if lang_code not in [included_language[0] for included_language in INCLUDED_LANGUAGES]:
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
                ]
            }
        )

    class Meta:
        icon = 'code'
        template = 'wagtailcodeblock/code_block.html'
        form_classname = 'code-block struct-block'
        form_template = 'wagtailcodeblock/code_block_form.html'
