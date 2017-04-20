from django.conf import settings


def get_language_choices():
    """
    Default list of language choices, if not overridden by Django.
    """
    DEFAULT_LANGUAGES = (
        ('bash', 'Bash/Shell'),
        ('css', 'CSS'),
        ('diff', 'diff'),
        ('django', 'Django/Jinja Templates'),
        ('http', 'HTML'),
        ('javascript', 'Javascript'),
        ('json', 'JSON'),
        ('python', 'Python'),
        ('scss', 'SCSS'),
        ('yaml', 'YAML'),
    )

    return getattr(settings, "WAGTAIL_CODE_BLOCK_LANGUAGES", DEFAULT_LANGUAGES)
