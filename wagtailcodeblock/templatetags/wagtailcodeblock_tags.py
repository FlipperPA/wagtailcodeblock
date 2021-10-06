from django.template import Library
from django.utils.safestring import mark_safe

from ..settings import get_theme, PRISM_VERSION, PRISM_PREFIX

register = Library()


@register.simple_tag
def prism_version():
    """Returns the version of PrismJS."""

    return PRISM_VERSION


@register.simple_tag
def load_prism_theme():
    """Loads a PrismJS theme from settings."""
    theme = get_theme()

    if theme:
        script = (
            f"""<link href="{PRISM_PREFIX}{PRISM_VERSION}/themes/prism-{theme}"""
            """.min.css" rel="stylesheet">"""
        )

        return mark_safe(script)
    return ""


@register.simple_tag
def load_prism_css():
    """Loads the PrismJS theme."""
    theme = get_theme()

    if theme:
        script = (
            f"""<link href="{PRISM_PREFIX}{PRISM_VERSION}/themes/prism-{theme}"""
            """.min.css" rel="stylesheet">"""
        )
    else:
        script = (
            f"""<link href="{PRISM_PREFIX}{PRISM_VERSION}/prism.min.css" """
            """rel="stylesheet">"""
        )

    return mark_safe(script)
