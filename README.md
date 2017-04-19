# wagtailcodeblock

A just started work-in-progress of a Streamfield block for source code with real-time syntax highlighting.

It uses the excellent [PrismJS](http://prismjs.com/) library both in the CMS and the website.

## Django Settings

You can customize the languages available by configuring `WAGTAIL_CODE_BLOCK_LANGUAGES` in your Django settings.
By default, it will be set with these languages:

    WAGTAIL_CODE_BLOCK_LANGUAGES = (
        ('python', 'Python'),
        ('javascript', 'Javascript'),
        ('json', 'JSON'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
        ('yaml', 'YAML'),
    )

The are set as a tuple of the PrismJS code and a descriptive label.

## Example Usage

    from wagtailcodeblock.blocks import CodeBlock

    class ContentStreamBlock(StreamBlock):
        paragraph = RichTextBlock()
        heading = TextBlock()
        code = CodeBlock(label='Code Snippet')
