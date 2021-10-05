from django.conf import settings

PRISM_PREFIX = "//cdnjs.cloudflare.com/ajax/libs/prism/"
PRISM_VERSION = "1.25.0"


def get_language_choices():
    """
    Default list of language choices, if not overridden by Django.
    """
    DEFAULT_LANGUAGES = (
        ("bash", "Bash/Shell"),
        ("css", "CSS"),
        ("diff", "diff"),
        ("html", "HTML"),
        ("javascript", "Javascript"),
        ("json", "JSON"),
        ("python", "Python"),
        ("scss", "SCSS"),
        ("yaml", "YAML"),
    )

    return getattr(settings, "WAGTAIL_CODE_BLOCK_LANGUAGES", DEFAULT_LANGUAGES)


def get_theme():
    """
    Returns a default theme, if not in the proejct's settings. Default theme is 'coy'.
    """

    return getattr(settings, "WAGTAIL_CODE_BLOCK_THEME", "coy")
