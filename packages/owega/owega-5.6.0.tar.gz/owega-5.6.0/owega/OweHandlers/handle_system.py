"""Handle /system."""
import prompt_toolkit as pt
from ..utils import (
    info_print,
    clrtxt,
)
from ..OwegaSession import OwegaSession as ps


# adds a system message
def handle_system(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /system."""
    given = given.strip()
    if not given:
        try:
            given = ps['main'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " System message ") + ": ")).strip()
        except (KeyboardInterrupt, EOFError):
            return messages
    if given:
        messages.add_system(given)
    else:
        if not silent:
            info_print("System message empty, not adding.")
    return messages


item_system = {
    "fun": handle_system,
    "help": "adds a system prompt in the chat",
    "commands": ["system"],
}
