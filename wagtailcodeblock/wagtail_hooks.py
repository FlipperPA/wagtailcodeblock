from django.templatetags.static import static
from django.utils.html import format_html_join

from wagtail import hooks

from .settings import get_theme, PRISM_VERSION, PRISM_PREFIX


@hooks.register("insert_global_admin_css")
def global_admin_css():
    THEME = get_theme()

    if THEME:
        prism_theme = f"-{THEME}"
    else:
        prism_theme = ""

    extra_css = [
        f"{PRISM_PREFIX}{PRISM_VERSION}/themes/prism{prism_theme}.min.css",
        static("wagtailcodeblock/css/wagtail-code-block.min.css"),
    ]

    return format_html_join(
        "\n",
        '<link rel="stylesheet" style="text/css" href="{}">',
        ((f,) for f in extra_css),
    )


@hooks.register("insert_global_admin_js")
def global_admin_js():
    """Add all prism languages"""

    js_files = [
        f"{PRISM_PREFIX}{PRISM_VERSION}/prism.min.js",
        f"{PRISM_PREFIX}{PRISM_VERSION}/plugins/autoloader/prism-autoloader.min.js",
    ]

    js_includes = format_html_join(
        "\n",
        """<script type="text/javascript" src="{}"></script>""",
        ((f,) for f in js_files),
    )

    return js_includes
