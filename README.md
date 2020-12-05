# Wagtail Code Block

Wagtail Code Block is a syntax highlighter block for source code for the Wagtail CMS. It features real-time highlighting in the Wagtail editor, the front end, line numbering, and support for PrismJS themes.

It uses the [PrismJS](http://prismjs.com/) library both in Wagtail Admin and the website and requires jQuery.

## Example Usage

```python
from wagtailcodeblock.blocks import CodeBlock

class ContentStreamBlock(StreamBlock):
    heading = TextBlock()
    paragraph = TextBlock()
    code = CodeBlock(label='Code')
```

You can also force it to use a single language or set a default language by providing a language code which must be included in your `WAGTAIL_CODE_BLOCK_LANGUAGES` setting:

```python
bash_code = CodeBlock(label='Bash Code', language='bash')
any_code = CodeBlock(label='Any code', default_language='python')
```

## Screenshot of the CMS Editor Interface

![Admin in Action](img/screenshot-editor.png)

## Installation & Setup

To install Wagtail Code Block simply run:

`pip install wagtailcodeblock`

And add `wagtailcodeblock` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'wagtailcodeblock',
    ...
]
``` 

## Django Settings

### Themes

Wagtail Code Block defaults to the PrismJS "Coy" theme, which looks good with Wagtail's CMS editor design. You can choose a different theme by configuring `WAGTAIL_CODE_BLOCK_THEME` in your Django settings. PrismJS provides several themes:

* **None**: <a href="http://prismjs.com/index.html?theme=prism" target="_blank">Default</a>
* **'coy'**: <a href="http://prismjs.com/index.html?theme=prism-coy" target="_blank">Coy</a>
* **'dark'**: <a href="http://prismjs.com/index.html?theme=prism-dark" target="_blank">Dark</a>
* **'funky'**: <a href="http://prismjs.com/index.html?theme=prism-funky" target="_blank">Funky</a>
* **'okaidia'**: <a href="http://prismjs.com/index.html?theme=prism-okaidia" target="_blank">Okaidia</a>
* **'solarizedlight'**: <a href="http://prismjs.com/index.html?theme=prism-solarizedlight" target="_blank">Solarized Light</a>
* **'tomorrow'**: <a href="http://prismjs.com/index.html?theme=prism-tomorrow" target="_blank">Tomorrow Night</a>
* **'twilight'**: <a href="http://prismjs.com/index.html?theme=prism-twilight" target="_blank">Twilight</a>

For example, in you want to use the Solarized Light theme: `WAGTAIL_CODE_BLOCK_THEME = 'solarizedlight'`
If you want to use the Default theme: `WAGTAIL_CODE_BLOCK_THEME = None`

### Languages Available

You can customize the languages available by configuring `WAGTAIL_CODE_BLOCK_LANGUAGES` in your Django settings.
By default, it will be set with these languages, since most users are in the Python web development community:

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

# Change Log

## 1.17.1.0

* Ensure compatibility with new ReactJS StreamFields with Wagtail 2.7.
* Update to PrismJS 1.17.1
* Add pytest-django for a basic test suite.
* Switch to using `setuptools_scm` instead of a `MANIFEST.in` file. Use tagging for PyPI version. 

## 1.15.0.0

* Update to PrismJS 1.15.0
* Bug fix: do not key off of `Language` label, as it is translatable.

## 1.14.0.0

* Upgrade to PrismJS 1.14.0
* Allow passing a language code as an attribute, only allowing the single language to be used.
* Fix conflict in CSS between `tag` class for Wagtail and markup syntax types.

## 1.11.0.0

* Upgrade to PrismJS 1.11.0
    * Changed version numbers to match the included PrismJS release
* Patch to add support for natively included PrismJS languages ['html', 'mathml', 'svg', 'xml']

## 0.4

* Support for Wagtail 2.0

### 0.4.1

* Upgrade to PrismJS 1.9.0, which includes a patch we made to the 'coy' theme we use as a default.

## 0.3

* Support for PrismJS themes

### 0.3.1

* Bug fixes for some front-end issues. Update documentation.

# Project Maintainers

* Timothy Allen (https://github.com/FlipperPA)
* Milton Lenis (https://github.com/MiltonLn)

# Contributors

* Andy Woods (https://github.com/andytwoods)
* Brandon Lafving (https://github.com/blafving)
* José Luis (https://github.com/SalahAdDin)
* Lucas Moeskops (https://github.com/lucasmoeskops)
* Michel Wortmann (https://github.com/mwort)
* Nick Sarbicki (https://github.com/NDevox)
