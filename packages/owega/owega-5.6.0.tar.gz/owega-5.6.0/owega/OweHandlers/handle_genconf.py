"""Handle /genconf."""
from ..utils import genconfig
from ..OwegaSession import OwegaSession as ps


# generates config file
def handle_genconf(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /genconf."""
    genconfig()
    return messages


item_genconf = {
    "fun": handle_genconf,
    "help": "generates a sample config file",
    "commands": ["genconf"],
}
