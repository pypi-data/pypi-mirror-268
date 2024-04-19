"""Handle /quit."""
from ..utils import (
    do_quit,
    success_msg,
)
from ..OwegaSession import OwegaSession as ps


# quits the program, deleting temp_file
def handle_quit(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /quit."""
    do_quit(
        success_msg(),
        temp_file=temp_file,
        is_temp=temp_is_temp,
        should_del=temp_is_temp
    )
    return messages


item_quit = {
    "fun": handle_quit,
    "help": "exits the program",
    "commands": ["quit", "exit"],
}
