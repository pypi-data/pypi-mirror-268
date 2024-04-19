"""Handle /commands."""
from ..OwegaFun import existingFunctions
from ..config import baseConf
from ..utils import info_print
from ..OwegaSession import OwegaSession as ps


# enables/disables command execution
def handle_commands(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /add_commands."""
    given = given.strip()
    if given.lower() in ["on", "true", "enable", "enabled"]:
        baseConf["commands"] = True
        existingFunctions.enableGroup("utility.system")
        if not silent:
            info_print("Command execution enabled.")
        return messages

    if given.lower() in ["off", "false", "disable", "disabled"]:
        baseConf["commands"] = False
        existingFunctions.disableGroup("utility.system")
        if not silent:
            info_print("Command execution disabled.")
        return messages

    baseConf["commands"] = (not baseConf.get("commands", False))
    if baseConf.get("commands", False):
        existingFunctions.enableGroup("utility.system")
        if not silent:
            info_print("Command execution enabled.")
    else:
        existingFunctions.disableGroup("utility.system")
        if not silent:
            info_print("Command execution disabled.")
    return messages


item_commands = {
    "fun": handle_commands,
    "help": "toggles command execution / file creation",
    "commands": ["commands"],
}
