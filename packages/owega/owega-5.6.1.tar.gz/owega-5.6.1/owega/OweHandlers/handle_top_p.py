"""Handle /top_p."""
import prompt_toolkit as pt
from ..config import baseConf
from ..utils import (
    info_print,
    clrtxt,
)
from ..OwegaSession import OwegaSession as ps


# change top_p value
def handle_top_p(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /top_p."""
    given = given.strip()
    try:
        new_top_p = float(given)
    except ValueError:
        if not silent:
            info_print(f'Current top_p: {baseConf.get("top_p", 1.0)}')
            info_print('New top_p value (0.0 - 1.0, defaults 1.0)')
        try:
            new_top_p = ps['float'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " top_p ") + ': ')).strip()
        except (ValueError, KeyboardInterrupt, EOFError):
            if not silent:
                info_print("Invalid top_p.")
            return messages
    baseConf["top_p"] = float(new_top_p)
    nv = baseConf.get('top_p', 1.0)
    if nv > 1.0:
        if not silent:
            info_print('top_p too high, capping to 1.0')
        baseConf["top_p"] = 1.0
    if nv < 0.0:
        if not silent:
            info_print('top_p too low, capping to 0.0')
        baseConf["top_p"] = 0.0
    if not silent:
        info_print(f'Set top_p to {baseConf.get("top_p", 1.0)}')
    return messages


item_top_p = {
    "fun": handle_top_p,
    "help": "sets the top_p value (0.0 - 1.0, defaults 1.0)",
    "commands": ["top_p"],
}
