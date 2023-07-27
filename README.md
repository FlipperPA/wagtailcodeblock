# Wagtail Code Block

Wagtail Code Block is a syntax highlighter block for source code for the Wagtail CMS. It features real-time highlighting in the Wagtail editor, the front end, line numbering, and support for PrismJS themes.

It uses the [PrismJS](http://prismjs.com/) library both in Wagtail Admin and the website.

## Example Usage

First, add `wagtailcodeblock` to your `INSTALLED_APPS` in Django's settings. Here's a bare bones example:

```python
from wagtail.blocks import TextBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from wagtailcodeblock.blocks import CodeBlock


class HomePage(Page):
    body = StreamField([
        ("heading", TextBlock()),
        ("code", CodeBlock(label='Code')),
    ])

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
```

You can also force it to use a single language or set a default language by providing a language code which must be included in your `WAGTAIL_CODE_BLOCK_LANGUAGES` setting:

```python
bash_code = CodeBlock(label='Bash Code', language='bash')
any_code = CodeBlock(label='Any code', default_language='python')
```

## Screenshot of the CMS Editor Interface

![Admin in Action](https://raw.githubusercontent.com/FlipperPA/wagtailcodeblock/main/docs/img/screenshot-editor.png)

## Installation & Setup

To install Wagtail Code Block run:

```bash
# Wagtail 4.0 and greater
pip install wagtailcodeblock

# Wagtail 3.x
pip install wagtailcodeblock==1.28.0.0

# Wagtail 2.x
pip install wagtailcodeblock==1.25.0.2
```

And add `wagtailcodeblock` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'wagtailcodeblock',
    ...
]
```

## Django Settings

### Line Numbers

Line numbers are enabled by default, but can be disabled in Django's settings:

```python
WAGTAIL_CODE_BLOCK_LINE_NUMBERS = False
```

### Copy to clipboard

Copy to clipboard is enabled by default, but can be disabled in Django's settings:

```python
WAGTAIL_CODE_BLOCK_COPY_TO_CLIPBOARD = False
```

### Themes

Wagtail Code Block defaults to the PrismJS "Coy" theme, which looks good with Wagtail's CMS editor design. You can choose a different theme by configuring `WAGTAIL_CODE_BLOCK_THEME` in your Django settings. PrismJS provides several themes:

* **None**: <a href="http://prismjs.com/index.html?theme=prism" target="_blank">Default</a>
* **'coy'**: <a href="http://prismjs.com/index.html?theme=prism-coy" target="_blank">Coy</a>
* **'dark'**: <a href="http://prismjs.com/index.html?theme=prism-dark" target="_blank">Dark</a>
* **'funky'**: <a href="http://prismjs.com/index.html?theme=prism-funky" target="_blank">Funky</a>
* **'okaidia'**: <a href="http://prismjs.com/index.html?theme=prism-okaidia" target="_blank">Okaidia</a>
* **'solarizedlight'**: <a href="http://prismjs.com/index.html?theme=prism-solarizedlight" target="_blank">Solarized Light</a>
* **'twilight'**: <a href="http://prismjs.com/index.html?theme=prism-twilight" target="_blank">Twilight</a>

For example, in you want to use the Solarized Light theme: `WAGTAIL_CODE_BLOCK_THEME = 'solarizedlight'`
If you want to use the Default theme: `WAGTAIL_CODE_BLOCK_THEME = None`

### Languages Available

You can customize the languages available by configuring `WAGTAIL_CODE_BLOCK_LANGUAGES` in your Django settings. By default, it will be set with these languages, since most users are in the Python web development community:

```python
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('bash', 'Bash/Shell'),
    ('css', 'CSS'),
    ('diff', 'diff'),
    ('html', 'HTML'),
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
    ('abnf', 'Augmented Backus–Naur form'),
    ('actionscript', 'ActionScript'),
    ('ada', 'Ada'),
    ('antlr4', 'ANTLR4'),
    ('apacheconf', 'Apache Configuration'),
    ('apl', 'APL'),
    ('applescript', 'AppleScript'),
    ('aql', 'AQL'),
    ('arduino', 'Arduino'),
    ('arff', 'ARFF'),
    ('asciidoc', 'AsciiDoc'),
    ('asm6502', '6502 Assembly'),
    ('aspnet', 'ASP.NET (C#)'),
    ('autohotkey', 'AutoHotkey'),
    ('autoit', 'AutoIt'),
    ('bash', 'Bash + Shell'),
    ('basic', 'BASIC'),
    ('batch', 'Batch'),
    ('bison', 'Bison'),
    ('bnf', 'Backus–Naur form + Routing Backus–Naur form'),
    ('brainfuck', 'Brainfuck'),
    ('bro', 'Bro'),
    ('c', 'C'),
    ('clike', 'C-like'),
    ('cmake', 'CMake'),
    ('csharp', 'C#'),
    ('cpp', 'C++'),
    ('cil', 'CIL'),
    ('coffeescript', 'CoffeeScript'),
    ('clojure', 'Clojure'),
    ('crystal', 'Crystal'),
    ('csp', 'Content-Security-Policy'),
    ('css', 'CSS'),
    ('css-extras', 'CSS Extras'),
    ('d', 'D'),
    ('dart', 'Dart'),
    ('diff', 'Diff'),
    ('django', 'Django/Jinja2'),
    ('dns-zone-file', 'DNS Zone File'),
    ('docker', 'Docker'),
    ('ebnf', 'Extended Backus–Naur form'),
    ('eiffel', 'Eiffel'),
    ('ejs', 'EJS'),
    ('elixir', 'Elixir'),
    ('elm', 'Elm'),
    ('erb', 'ERB'),
    ('erlang', 'Erlang'),
    ('etlua', 'Embedded LUA Templating'),
    ('fsharp', 'F#'),
    ('flow', 'Flow'),
    ('fortran', 'Fortran'),
    ('ftl', 'Freemarker Template Language'),
    ('gcode', 'G-code'),
    ('gdscript', 'GDScript'),
    ('gedcom', 'GEDCOM'),
    ('gherkin', 'Gherkin'),
    ('git', 'Git'),
    ('glsl', 'GLSL'),
    ('gml', 'GameMaker Language'),
    ('go', 'Go'),
    ('graphql', 'GraphQL'),
    ('groovy', 'Groovy'),
    ('haml', 'Haml'),
    ('handlebars', 'Handlebars'),
    ('haskell', 'Haskell'),
    ('haxe', 'Haxe'),
    ('hcl', 'HCL'),
    ('http', 'HTTP'),
    ('hpkp', 'HTTP Public-Key-Pins'),
    ('hsts', 'HTTP Strict-Transport-Security'),
    ('ichigojam', 'IchigoJam'),
    ('icon', 'Icon'),
    ('inform7', 'Inform 7'),
    ('ini', 'Ini'),
    ('io', 'Io'),
    ('j', 'J'),
    ('java', 'Java'),
    ('javadoc', 'JavaDoc'),
    ('javadoclike', 'JavaDoc-like'),
    ('javascript', 'JavaScript'),
    ('javastacktrace', 'Java stack trace'),
    ('jolie', 'Jolie'),
    ('jq', 'JQ'),
    ('jsdoc', 'JSDoc'),
    ('js-extras', 'JS Extras'),
    ('js-templates', 'JS Templates'),
    ('json', 'JSON'),
    ('jsonp', 'JSONP'),
    ('json5', 'JSON5'),
    ('julia', 'Julia'),
    ('keyman', 'Keyman'),
    ('kotlin', 'Kotlin'),
    ('latex', 'LaTeX'),
    ('less', 'Less'),
    ('lilypond', 'Lilypond'),
    ('liquid', 'Liquid'),
    ('lisp', 'Lisp'),
    ('livescript', 'LiveScript'),
    ('lolcode', 'LOLCODE'),
    ('lua', 'Lua'),
    ('makefile', 'Makefile'),
    ('markdown', 'Markdown'),
    ('markup', 'Markup + HTML + XML + SVG + MathML'),
    ('markup-templating', 'Markup templating'),
    ('matlab', 'MATLAB'),
    ('mel', 'MEL'),
    ('mizar', 'Mizar'),
    ('monkey', 'Monkey'),
    ('n1ql', 'N1QL'),
    ('n4js', 'N4JS'),
    ('nand2tetris-hdl', 'Nand To Tetris HDL'),
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
    ('pascal', 'Pascal + Object Pascal'),
    ('pascaligo', 'Pascaligo'),
    ('pcaxis', 'PC Axis'),
    ('perl', 'Perl'),
    ('php', 'PHP'),
    ('phpdoc', 'PHPDoc'),
    ('php-extras', 'PHP Extras'),
    ('plsql', 'PL/SQL'),
    ('powershell', 'PowerShell'),
    ('processing', 'Processing'),
    ('prolog', 'Prolog'),
    ('properties', '.properties'),
    ('protobuf', 'Protocol Buffers'),
    ('pug', 'Pug'),
    ('puppet', 'Puppet'),
    ('pure', 'Pure'),
    ('python', 'Python'),
    ('q', 'Q (kdb+ database)'),
    ('qore', 'Qore'),
    ('r', 'R'),
    ('jsx', 'React JSX'),
    ('tsx', 'React TSX'),
    ('renpy', 'Ren\'py'),
    ('reason', 'Reason'),
    ('regex', 'Regex'),
    ('rest', 'reST (reStructuredText)'),
    ('rip', 'Rip'),
    ('roboconf', 'Roboconf'),
    ('robot-framework', 'Robot Framework'),
    ('ruby', 'Ruby'),
    ('rust', 'Rust'),
    ('sas', 'SAS'),
    ('sass', 'Sass (Sass)'),
    ('scss', 'Sass (Scss)'),
    ('scala', 'Scala'),
    ('scheme', 'Scheme'),
    ('shell-session', 'Shell Session'),
    ('smalltalk', 'Smalltalk'),
    ('smarty', 'Smarty'),
    ('solidity', 'Solidity (Ethereum)'),
    ('sparql', 'SPARQL'),
    ('splunk-spl', 'Splunk SPL'),
    ('sqf', 'SQF: Status Quo Function (Arma 3)'),
    ('sql', 'SQL'),
    ('soy', 'Soy (Closure Template)'),
    ('stylus', 'Stylus'),
    ('swift', 'Swift'),
    ('tap', 'TAP'),
    ('tcl', 'Tcl'),
    ('textile', 'Textile'),
    ('toml', 'TOML'),
    ('tt2', 'Template Toolkit 2'),
    ('twig', 'Twig'),
    ('typescript', 'TypeScript'),
    ('t4-cs', 'T4 Text Templates (C#)'),
    ('t4-vb', 'T4 Text Templates (VB)'),
    ('t4-templating', 'T4 templating'),
    ('vala', 'Vala'),
    ('vbnet', 'VB.Net'),
    ('velocity', 'Velocity'),
    ('verilog', 'Verilog'),
    ('vhdl', 'VHDL'),
    ('vim', 'vim'),
    ('visual-basic', 'Visual Basic'),
    ('wasm', 'WebAssembly'),
    ('wiki', 'Wiki markup'),
    ('xeora', 'Xeora + XeoraCube'),
    ('xojo', 'Xojo (REALbasic)'),
    ('xquery', 'XQuery'),
    ('yaml', 'YAML'),
    ('zig', 'Zig'),
)
```

# What's With the Versioning?

Our version numbers are based on the underlying version of PrismJS we use. For example, if we are using PrismJS `1.28.0`, our versions will be named `1.28.0.X`.

# Release Notes & Contributors

* Thank you to our [wonderful contributors](https://github.com/FlipperPA/wagtailcodeblock/graphs/contributors)!
* Release notes are [available on GitHub](https://github.com/FlipperPA/wagtailcodeblock/releases).

# Project Maintainers

* Timothy Allen (https://github.com/FlipperPA)
* Milton Lenis (https://github.com/MiltonLn)

This package was created by the staff of [Wharton Research Data Services](https://wrds.wharton.upenn.edu/). We are thrilled that [The Wharton School](https://www.wharton.upenn.edu/) allows us a certain amount of time to contribute to open-source projects. We add features as they are necessary for our projects, and try to keep up with Issues and Pull Requests as best we can. Due to constraints of time (our full time jobs!), Feature Requests without a Pull Request may not be implemented, but we are always open to new ideas and grateful for contributions and our users.
