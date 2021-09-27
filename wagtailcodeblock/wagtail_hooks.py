from django.templatetags.static import static
from django.utils.html import format_html_join

from wagtail.core import hooks

from .settings import get_theme, get_prism_version

@hooks.register('insert_editor_css')
def editor_css():
    THEME = get_theme()
    PRISM_VERSION = get_prism_version()
    if THEME:
        prism_theme = "-{theme}".format(theme=THEME)
    else:
        prism_theme = ""
    
    extra_css = [
        "//cdnjs.cloudflare.com/ajax/libs/prism/{prism_version}/themes/prism{prism_theme}.min.css".format(
            prism_version=PRISM_VERSION, prism_theme=prism_theme,
        ),
        static("wagtailcodeblock/css/wagtail-code-block.min.css"),
    ]

    return format_html_join(
        '\n', '<link rel="stylesheet" type="text/css" href="{}">',
        extra_css
    )
