"""Handle /presence."""
import prompt_toolkit as pt
from ..config import baseConf
from ..utils import (
    info_print,
    clrtxt,
)
from ..OwegaSession import OwegaSession as ps


# change presence penalty
def handle_presence(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /presence."""
    given = given.strip()
    try:
        new_presence_penalty = float(given)
    except ValueError:
        if not silent:
            info_print('Current presence penalty: '
                + f'{baseConf.get("presence_penalty", 1.0)}')
            info_print('New presence penalty value (0.0 - 2.0, defaults 0.0)')
        try:
            new_presence_penalty = ps['float'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " presence penalty ") + ': ')).strip()
        except (ValueError, KeyboardInterrupt, EOFError):
            if not silent:
                info_print("Invalid presence penalty.")
            return messages
    baseConf["presence_penalty"] = float(new_presence_penalty)
    nv = baseConf.get('presence_penalty', 0.0)
    if nv > 2.0:
        if not silent:
            info_print('Penalty too high, capping to 2.0')
        baseConf["presence_penalty"] = 2.0
    if nv < 0.0:
        if not silent:
            info_print('Penalty too low, capping to 0.0')
        baseConf["presence_penalty"] = 0.0
    if not silent:
        info_print('Set presence penalty to '
            + f'{baseConf.get("presence_penalty", 0.0)}')
    return messages


item_presence = {
    "fun": handle_presence,
    "help": "sets the presence penalty (0.0 - 2.0, defaults 0.0)",
    "commands": ["presence"],
}
