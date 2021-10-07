function CodeBlockDefinition() {
    window.wagtailStreamField.blocks.StructBlockDefinition.apply(this, arguments);
}

CodeBlockDefinition.prototype.render = function(placeholder, prefix, initialState, initialError) {
    var block = window.wagtailStreamField.blocks.StructBlockDefinition.prototype.render.apply(
        this, arguments
    );

    var languageField = $(document).find('#' + prefix + '-language');
    var codeField = $(document).find('#' + prefix + '-code');
    var targetField = $(document).find('#' + prefix + '-target');

    function updateLanguage() {
        var languageCode = languageField.val();
        targetField.removeClass().addClass('language-' + languageCode);
        prismRepaint();
    }

    function prismRepaint() {
        Prism.highlightElement(targetField[0]);
    }

    function populateTargetCode() {
        var codeText = codeField.val();
        targetField.text(codeText);
        prismRepaint(targetField);
    }

    updateLanguage();
    populateTargetCode();
    languageField.on('change', updateLanguage);
    codeField.on('keyup', populateTargetCode);

    return block;
}

window.telepath.register('wagtailcodeblock.blocks.CodeBlock', CodeBlockDefinition);
