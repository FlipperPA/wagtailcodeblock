# Wagtail Code Block

A just started work-in-progress of a Streamfield block for source code with real-time syntax highlighting.

It uses the excellent [PrismJS](http://prismjs.com/) library both in Wagtail Admin and the website and requires jQuery.

## Django Settings

You can customize the languages available by configuring `WAGTAIL_CODE_BLOCK_LANGUAGES` in your Django settings.
By default, it will be set with these languages:

    WAGTAIL_CODE_BLOCK_LANGUAGES = (
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

This setting is comprised of the PrismJS code and a descriptive label. [Here is a list of available language highlighters
on the PrismJS CDN we use](https://cdnjs.com/libraries/prism).

## Example Usage

    from wagtailcodeblock.blocks import CodeBlock

    class ContentStreamBlock(StreamBlock):
        paragraph = RichTextBlock()
        heading = TextBlock()
        code = CodeBlock(label='Code Snippet')

## Screenshot

![Admin in Action](https://cloud.githubusercontent.com/assets/68164/25201886/600c5366-2521-11e7-8aba-3e1cf5955c34.png)
