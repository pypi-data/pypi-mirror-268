"""Handle /save."""
import prompt_toolkit as pt
from ..utils import clrtxt
from ..OwegaSession import OwegaSession as ps


# saves the messages and prompt to a json file
def handle_save(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /save."""
    given = given.strip()
    try:
        if given:
            file_path = given
        else:
            file_path = ps['save'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " file output ") + ': ')).strip()
        messages.save(file_path)
    except (Exception, KeyboardInterrupt, EOFError):
        if not silent:
            print(clrtxt("red", " ERROR ") + f": could not write to \"{file_path}\"")
    else:
        if not silent:
            print(clrtxt("green", " SUCCESS ") + ": conversation saved!")
    return messages


item_save = {
    "fun": handle_save,
    "help": "saves the conversation history to a file",
    "commands": ["save"],
}
