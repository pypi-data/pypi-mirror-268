"""Handle /context."""
import prompt_toolkit as pt
from ..utils import (info_print, clrtxt)
from ..OwegaSession import OwegaSession as ps


# change owega's system prompt
def handle_context(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /context."""
    given = given.strip()
    if given:
        messages.set_context(given)
        if not silent:
            info_print(f"New context: {messages.get_context()}")
        return messages
    if not silent:
        info_print("Old context: " + messages.get_context())
    new_context = ps['context'].prompt(pt.ANSI(
        '\n' + clrtxt("magenta", " new context ") + ': ')).strip()
    if new_context:
        messages.set_context(new_context)
        if not silent:
            info_print(f"New context: {messages.get_context()}")
    else:
        if not silent:
            info_print("New context empty, keeping old context!")
    return messages


item_context = {
    "fun": handle_context,
    "help": "changes the AI's behaviour",
    "commands": ["context"],
}
