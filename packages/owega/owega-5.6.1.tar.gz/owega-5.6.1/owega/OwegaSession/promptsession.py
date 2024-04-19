"""Prompt sessions."""
import re
import os
import prompt_toolkit as pt
from ..config import baseConf
from ..utils import get_home_dir
from .main_bottom_toolbar import main_bottom_toolbar
from ..handlerBase import handlers


def set_ps(ps):
    """Set the prompt sessions."""
    # generate completion from command list (handlers)
    command_list = ['/' + command for command in handlers.keys()]

    # CTRL+N makes a new line
    main_kb = pt.key_binding.KeyBindings()

    @main_kb.add('c-n')
    def _(event):
        event.current_buffer.insert_text('\n')

    # this defines how newlines are shown
    def main_prompt_continuation(width, line_number, is_soft_wrap):
        cont = '   ' if is_soft_wrap else '...'
        if (width >= 4):
            return (' ' * (width - 4)) + cont + ' '
        else:
            return ' ' * width

    # get main style
    main_style = main_bottom_toolbar("style")

    class SlashCommandCompleter(pt.completion.WordCompleter):
        def __init__(self, words, ignore_case=False):
            super().__init__(words, ignore_case=ignore_case)
            # Define a regex pattern that includes the slash as a word character
            self.pattern = re.compile(r'[^ \t\n\r\f\v]+')

        def get_completions(self, document, complete_event):
            # Use the custom pattern to find the word before the cursor
            word_before_cursor = document.get_word_before_cursor(
                pattern=self.pattern)
            for word in self.words:
                if word.startswith(word_before_cursor):
                    yield pt.completion.Completion(
                        word, -len(word_before_cursor))

    # keyword autocompletion
    main_completer = SlashCommandCompleter(
        words=command_list,
        ignore_case=True
    )

    # main session, for general context
    ps['main'] = pt.PromptSession(
        history=pt.history.FileHistory(
            '' + get_home_dir() + '/.owega.history'
        ),
        completer=main_completer,
        complete_while_typing=True,
        complete_in_thread=True,
        auto_suggest=pt.auto_suggest.AutoSuggestFromHistory(),
        bottom_toolbar=main_bottom_toolbar,
        style=main_style,
        key_bindings=main_kb,
        prompt_continuation=main_prompt_continuation,
    )

    # context session, when editing owega's system prompt
    ps['context'] = pt.PromptSession()

    class SaveValidator(pt.validation.Validator):
        def validate(self, document):
            text = document.text

            if os.path.isdir(text):
                raise pt.validation.ValidationError(
                    message='you specified a directory, not a file',
                    cursor_position=len(text)
                )
            elif not os.path.isdir(os.path.dirname(text)):
                raise pt.validation.ValidationError(
                    message='parent dir does not exist, cannot create file',
                    cursor_position=len(text)
                )

    ps['save'] = pt.PromptSession(
        completer=pt.completion.PathCompleter(),
        validator=SaveValidator()
    )

    class LoadValidator(pt.validation.Validator):
        def validate(self, document):
            text = document.text

            if os.path.isdir(text):
                raise pt.validation.ValidationError(
                    message='this is a directory, not a file',
                    cursor_position=len(text)
                )

            if not os.path.isfile(text):
                raise pt.validation.ValidationError(
                    message='file does not exist',
                    cursor_position=len(text)
                )

    class DirValidator(pt.validation.Validator):
        def validate(self, document):
            text = document.text

            if not os.path.isdir(text):
                raise pt.validation.ValidationError(
                    message='this is not a directory',
                    cursor_position=len(text)
                )

    ps['load'] = pt.PromptSession(
        completer=pt.completion.PathCompleter(),
        validator=LoadValidator()
    )

    ps['dirload'] = pt.PromptSession(
        completer=pt.completion.PathCompleter(),
        validator=DirValidator()
    )

    # file session, with file completion
    ps['file'] = pt.PromptSession(
        completer=pt.completion.PathCompleter()
    )

    # file session with file completion for file_input directive
    ps['file_input'] = pt.PromptSession(
        completer=pt.completion.PathCompleter()
    )

    # model session, for model selection
    # TODO: add model completion
    ps['model'] = pt.PromptSession()

    class IntegerValidator(pt.validation.Validator):
        def validate(self, document):
            text = document.text

            try:
                int(text)
            except ValueError:
                raise pt.validation.ValidationError(
                    message='This input contains non-numeric characters',
                    cursor_position=len(text)
                )

    class FloatValidator(pt.validation.Validator):
        def validate(self, document):
            text = document.text

            try:
                float(text)
            except ValueError:
                raise pt.validation.ValidationError(
                    message='This input is not a valid floating-point number',
                    cursor_position=len(text)
                )

    ps['integer'] = pt.PromptSession(validator=IntegerValidator())
    ps['float'] = pt.PromptSession(validator=FloatValidator())


ps = {}
