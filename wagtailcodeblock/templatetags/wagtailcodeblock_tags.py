from django.template import Library
from django.utils.safestring import mark_safe

from ..settings import get_theme, get_line_numbers, get_copy_to_clipboard, PRISM_VERSION, PRISM_PREFIX

register = Library()


@register.simple_tag
def prism_version():
    """Returns the version of PrismJS."""

    return PRISM_VERSION


@register.simple_tag
def load_prism_css():
    """Loads the PrismJS theme."""
    theme = get_theme()
    toolbar = True

    if theme:
        script = f"""<link href="{PRISM_PREFIX}{PRISM_VERSION}/themes/prism-{theme}""" """.min.css" rel="stylesheet">"""
    else:
        script = f"""<link href="{PRISM_PREFIX}{PRISM_VERSION}/themes/prism.min.css" """ """rel="stylesheet">"""

    if get_line_numbers():
        script += (
            f"""<link href="{PRISM_PREFIX}{PRISM_VERSION}/plugins/line-numbers/"""
            """prism-line-numbers.min.css" rel="stylesheet">"""
        )

    if toolbar is True:
        script += (
            f"""<link href="{PRISM_PREFIX}{PRISM_VERSION}/plugins/toolbar/"""
            """prism-toolbar.min.css" rel="stylesheet">"""
        )

    return mark_safe(script)


@register.simple_tag
def load_prism_js():
    prism_scripts_to_load = [
        f"{PRISM_PREFIX}{PRISM_VERSION}/components/prism-core.min.js",
        f"{PRISM_PREFIX}{PRISM_VERSION}/plugins/autoloader/prism-autoloader.min.js",
    ]

    if get_line_numbers():
        prism_scripts_to_load.append(f"{PRISM_PREFIX}{PRISM_VERSION}/plugins/line-numbers/prism-line-numbers.min.js")

    if get_copy_to_clipboard():
        prism_scripts_to_load.append(f"{PRISM_PREFIX}{PRISM_VERSION}/plugins/toolbar/prism-toolbar.min.js")
        prism_scripts_to_load.append(
            f"{PRISM_PREFIX}{PRISM_VERSION}/plugins/copy-to-clipboard/prism-copy-to-clipboard.min.js"
        )

    script = ""
    for src_url in prism_scripts_to_load:
        script += f'<script type="text/javascript" src={src_url}></script>'

    return mark_safe(script)
