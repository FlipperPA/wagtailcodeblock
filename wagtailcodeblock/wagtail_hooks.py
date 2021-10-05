from django.templatetags.static import static
from django.utils.html import format_html_join

from wagtail.core import hooks

from .settings import get_theme, get_prism_version


@hooks.register("insert_editor_css")
def editor_css():
    THEME = get_theme()
    PRISM_VERSION = get_prism_version()
    if THEME:
        prism_theme = f"-{THEME}"
    else:
        prism_theme = ""

    extra_css = [
        f"//cdnjs.cloudflare.com/ajax/libs/prism/{PRISM_VERSION}/themes/prism"
        f"{prism_theme}.min.css",
        static("wagtailcodeblock/css/wagtail-code-block.min.css"),
    ]

    return format_html_join(
        "\n",
        '<link rel="stylesheet" style="text/css" href="{}">',
        ((f,) for f in extra_css),
    )


@hooks.register("insert_editor_js")
def editor_js():
    """Add all prism languages"""
    PRISM_VERSION = get_prism_version()

    js_files = [
        f"//cdnjs.cloudflare.com/ajax/libs/prism/{PRISM_VERSION}/prism.min.js",
        f"//cdnjs.cloudflare.com/ajax/libs/prism/{PRISM_VERSION}/plugins/autoloader/"
        "prism-autoloader.min.js",
    ]

    js_includes = format_html_join(
        "\n",
        '<script type="text/javascript" src="{}"></script>',
        ((f,) for f in js_files),
    )
    return js_includes
