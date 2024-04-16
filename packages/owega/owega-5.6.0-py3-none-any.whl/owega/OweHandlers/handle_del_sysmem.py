"""Handle /del_sysmem."""
import prompt_toolkit as pt
from ..utils import (
    info_print,
    clrtxt,
)
from ..OwegaSession import OwegaSession as ps


# adds a system message
def handle_del_sysmem(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /del_sysmem."""
    given = given.strip()
    for index, sysmem in enumerate(messages.systemsouv):
        if not silent:
            print(f"[\033[0;95mSystem souvenir\033[0m] [\033[0;92m{index}\033[0m]:")
            print('\033[0;37m', end='')
            print(sysmem)
            print('\033[0m', end='')
            print()
    try:
        if not given:
            msg_id = ps['integer'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " message ID ") + ': ')).strip()
        else:
            msg_id = given
    except (ValueError, KeyboardInterrupt, EOFError):
        if not silent:
            info_print("Invalid message ID, cancelling edit")
        return messages

    try:
        msg_id = int(msg_id)
    except ValueError:
        info_print("Invalid message ID, cancelling edit")
        return messages

    if (msg_id < 0) or (msg_id >= len(messages.systemsouv)):
        if not silent:
            info_print("Invalid message ID, cancelling edit")
        return messages

    messages.systemsouv.pop(msg_id)

    return messages


item_del_sysmem = {
    "fun": handle_del_sysmem,
    "help": "deletes a system souvenir",
    "commands": ["del_sysmem"],
}
