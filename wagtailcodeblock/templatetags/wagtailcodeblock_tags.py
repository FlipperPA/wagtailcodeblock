from django.template import Library
from django.utils.safestring import mark_safe

from ..settings import (
    get_prism_version,
    get_theme
)

register = Library()


@register.simple_tag
def get_script_version():
    prism_version = get_prism_version()
    return prism_version


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
