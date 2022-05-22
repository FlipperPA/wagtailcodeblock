import wagtail

from django.forms import Media
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock,
    TextBlock,
    ChoiceBlock,
)
from wagtail.blocks.struct_block import StructBlockAdapter
from wagtail.telepath import register

from .settings import get_language_choices


class CodeBlock(StructBlock):
    """
    A Wagtail StreamField block for code syntax highlighting using PrismJS.
    """

    def __init__(self, local_blocks=None, **kwargs):
        # Languages included in PrismJS core
        # Review: https://github.com/PrismJS/prism/blob/gh-pages/prism.js#L602
        self.INCLUDED_LANGUAGES = (
            ("html", "HTML"),
            ("mathml", "MathML"),
            ("svg", "SVG"),
            ("xml", "XML"),
        )

        if local_blocks is None:
            local_blocks = []
        else:
            local_blocks = local_blocks.copy()

        language_choices, language_default = self.get_language_choice_list(**kwargs)

        local_blocks.extend(
            [
                (
                    "language",
                    ChoiceBlock(
                        choices=language_choices,
                        help_text=_("Coding language"),
                        label=_("Language"),
                        default=language_default,
                        identifier="language",
                    ),
                ),
                ("code", TextBlock(label=_("Code"), identifier="code")),
            ]
        )

        super().__init__(local_blocks, **kwargs)

    def get_language_choice_list(self, **kwargs):
        # Get default languages
        WCB_LANGUAGES = get_language_choices()
        # If a language is passed in as part of a code block, use it.
        language = kwargs.get("language", False)

        total_language_choices = WCB_LANGUAGES + self.INCLUDED_LANGUAGES

        if language in [lang[0] for lang in total_language_choices]:
            for language_choice in total_language_choices:
                if language_choice[0] == language:
                    language_choices = (language_choice,)
                    language_default = language_choice[0]
        else:
            language_choices = WCB_LANGUAGES
            language_default = kwargs.get("default_language")

        return language_choices, language_default

    class Meta:
        icon = "code"
        template = "wagtailcodeblock/code_block.html"
        form_classname = "code-block struct-block"
        form_template = "wagtailcodeblock/code_block_form.html"


class CodeBlockAdapter(StructBlockAdapter):
    js_constructor = "wagtailcodeblock.blocks.CodeBlock"

    @cached_property
    def media(self):
        structblock_media = super().media
        return Media(
            js=structblock_media._js + ["wagtailcodeblock/js/wagtailcodeblock.js"],
            css=structblock_media._css,
        )


register(CodeBlockAdapter(), CodeBlock)
