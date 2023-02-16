class CodeBlockDefinition extends window.wagtailStreamField.blocks
    .StructBlockDefinition {
    render(placeholder, prefix, initialState, initialError) {
        const block = super.render(
            placeholder,
            prefix,
            initialState,
            initialError,
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
}

window.telepath.register('wagtailcodeblock.blocks.CodeBlock', CodeBlockDefinition);
