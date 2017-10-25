# Wagtail Code Block

Wagtail Code Block is a syntax highlighted block for source code for the Wagtail CMS. It features real-time highlighting in the Wagtail editor, the front end, line numbering, and support for PrismJS themes.

It uses the [PrismJS](http://prismjs.com/) library both in Wagtail Admin and the website and requires jQuery.

## Example Usage

```python
from wagtailcodeblock.blocks import CodeBlock

class ContentStreamBlock(StreamBlock):
    heading = TextBlock()
    paragraph = TextBlock()
    code = CodeBlock(label='Code')
```

## Screenshot

![Admin in Action](https://cloud.githubusercontent.com/assets/68164/25201886/600c5366-2521-11e7-8aba-3e1cf5955c34.png)

## Django Settings

You can customize the languages available by configuring `WAGTAIL_CODE_BLOCK_LANGUAGES` in your Django settings.
By default, it will be set with these languages:

```python
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
```

Each language in this setting is a tuple of the PrismJS code and a descriptive label. If you want use all available languages, here is a list:

```python
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('abap', 'ABAP'),
    ('actionscript', 'ActionScript'),
    ('ada', 'Ada'),
    ('apacheconf', 'Apache Configuration'),
    ('apl', 'APL'),
    ('applescript', 'AppleScript'),
    ('arduino', 'Arduino'),
    ('asciidoc', 'AsciiDoc'),
    ('aspnet', 'ASP.NET (C#)'),
    ('autoit', 'AutoIt'),
    ('autohotkey', 'AutoHotkey'),
    ('bash', 'Bash'),
    ('basic', 'BASIC'),
    ('batch', 'Batch'),
    ('bison', 'Bison'),
    ('brainfuck', 'Brainfuck'),
    ('bro', 'Bro'),
    ('c', 'C'),
    ('clike', 'C-like'),
    ('csharp', 'C#'),
    ('cpp', 'C++'),
    ('coffeescript', 'CoffeeScript'),
    ('crystal', 'Crystal'),
    ('css', 'CSS'),
    ('css-extras', 'CSS Extras'),
    ('d', 'D'),
    ('dart', 'Dart'),
    ('django', 'Django/Jinja2'),
    ('diff', 'Diff'),
    ('docker', 'Docker'),
    ('eiffel', 'Eiffel'),
    ('elixir', 'Elixir'),
    ('erlang', 'Erlang'),
    ('fsharp', 'F#'),
    ('fortran', 'Fortran'),
    ('gherkin', 'Gherkin'),
    ('git', 'Git'),
    ('glsl', 'GLSL'),
    ('go', 'Go'),
    ('graphql', 'GraphQL'),
    ('groovy', 'Groovy'),
    ('haml', 'Haml'),
    ('handlebars', 'Handlebars'),
    ('haskell', 'Haskell'),
    ('haxe', 'Haxe'),
    ('http', 'HTTP'),
    ('icon', 'Icon'),
    ('inform7', 'Inform 7'),
    ('ini', 'Ini'),
    ('j', 'J'),
    ('java', 'Java'),
    ('javascript', 'JavaScript'),
    ('jolie', 'Jolie'),
    ('json', 'JSON'),
    ('julia', 'Julia'),
    ('keyman', 'Keyman'),
    ('kotlin', 'Kotlin'),
    ('latex', 'LaTeX'),
    ('less', 'Less'),
    ('livescript', 'LiveScript'),
    ('lolcode', 'LOLCODE'),
    ('lua', 'Lua'),
    ('makefile', 'Makefile'),
    ('markdown', 'Markdown'),
    ('markup', 'Markup'),
    ('matlab', 'MATLAB'),
    ('mel', 'MEL'),
    ('mizar', 'Mizar'),
    ('monkey', 'Monkey'),
    ('n4js', 'N4JS'),
    ('nasm', 'NASM'),
    ('nginx', 'nginx'),
    ('nim', 'Nim'),
    ('nix', 'Nix'),
    ('nsis', 'NSIS'),
    ('objectivec', 'Objective-C'),
    ('ocaml', 'OCaml'),
    ('opencl', 'OpenCL'),
    ('oz', 'Oz'),
    ('parigp', 'PARI/GP'),
    ('parser', 'Parser'),
    ('pascal', 'Pascal'),
    ('perl', 'Perl'),
    ('php', 'PHP'),
    ('php-extras', 'PHP Extras'),
    ('powershell', 'PowerShell'),
    ('processing', 'Processing'),
    ('prolog', 'Prolog'),
    ('properties', '.properties'),
    ('protobuf', 'Protocol Buffers'),
    ('pug', 'Pug'),
    ('puppet', 'Puppet'),
    ('pure', 'Pure'),
    ('python', 'Python'),
    ('q', 'Q'),
    ('qore', 'Qore'),
    ('r', 'R'),
    ('jsx', 'React JSX'),
    ('renpy', 'Ren'py'),
    ('reason', 'Reason'),
    ('rest', 'reST (reStructuredText)'),
    ('rip', 'Rip'),
    ('roboconf', 'Roboconf'),
    ('ruby', 'Ruby'),
    ('rust', 'Rust'),
    ('sas', 'SAS'),
    ('sass', 'Sass (Sass)'),
    ('scss', 'Sass (Scss)'),
    ('scala', 'Scala'),
    ('scheme', 'Scheme'),
    ('smalltalk', 'Smalltalk'),
    ('smarty', 'Smarty'),
    ('sql', 'SQL'),
    ('stylus', 'Stylus'),
    ('swift', 'Swift'),
    ('tcl', 'Tcl'),
    ('textile', 'Textile'),
    ('twig', 'Twig'),
    ('typescript', 'TypeScript'),
    ('vbnet', 'VB.Net'),
    ('verilog', 'Verilog'),
    ('vhdl', 'VHDL'),
    ('vim', 'vim'),
    ('wiki', 'Wiki markup'),
    ('xojo', 'Xojo (REALbasic)'),
    ('yaml', 'YAML'),
)
```

# Contributors

* Timothy Allen (https://github.com/FlipperPA)
* José Luis (https://github.com/SalahAdDin)
