"""Handle /history."""
from ..OwegaSession import OwegaSession as ps


# shows chat history
def handle_history(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /history."""
    if not silent:
        messages.print_history()
    return messages


item_history = {
    "fun": handle_history,
    "help": "prints the conversation history",
    "commands": ["history"],
}
