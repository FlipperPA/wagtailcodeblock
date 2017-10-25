from django.template import Library
from django.utils.safestring import mark_safe

from ..settings import (
    get_prism_version,
    get_theme
)

register = Library()


@register.simple_tag
def load_prism_theme():
    prism_version = get_prism_version()
    theme = get_theme()

    if theme:
        script = "<link href='https://cdnjs.cloudflare.com/ajax/libs/prism/{0}/themes/prism-{1}.min.css' rel='stylesheet'/>".format(
            prism_version,
            theme,
        )
        return mark_safe(script)
    return ''


@register.simple_tag
def load_prism_js():
    prism_version = get_prism_version()
    script = "<script defer src='https://cdnjs.cloudflare.com/ajax/libs/prism/{0}/prism.min.js'></script>".format(
        prism_version,
    )
    return mark_safe(script)


@register.simple_tag
def load_prism_laguanges(field):
    prism_version = get_prism_version()
    scripts = "<script defer src='https://cdnjs.cloudflare.com/ajax/libs/prism/{0}/prism.min.js'></script>".format(
        prism_version
    )
    values = []
    for block in field:
        if block.block_type == 'code_quote':
            values.append(block.value['code']['language'])

    for value in values:
        scripts += "" \
                   "<script defer src='https://cdnjs.cloudflare.com/ajax/libs/prism/{0}/components/prism-{1}.min.js'></script>".format(
            prism_version,
            value
        )

    return mark_safe(scripts)
