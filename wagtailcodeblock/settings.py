from django.conf import settings


def get_language_choices():
    """
    Default list of language choices, if not overridden by Django.
    """
    DEFAULT_LANGUAGES = (
        ('bash', 'Bash/Shell'),
        ('css', 'CSS'),
        ('diff', 'diff'),
        ('http', 'HTML'),
        ('javascript', 'Javascript'),
        ('json', 'JSON'),
        ('python', 'Python'),
        ('scss', 'SCSS'),
        ('yaml', 'YAML'),
    )

    return getattr(settings, "WAGTAIL_CODE_BLOCK_LANGUAGES", DEFAULT_LANGUAGES)


def get_theme():
    """
    Default theme is none, if not overridden by Django.
    """

    return getattr(settings, "WAGTAIL_CODE_BLOCK_THEME", None)


def get_prism_version():
    prism_version = "1.8.3"

    return prism_version
