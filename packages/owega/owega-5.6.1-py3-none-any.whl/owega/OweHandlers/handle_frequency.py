"""Handle /frequency."""
import prompt_toolkit as pt
from ..config import baseConf
from ..utils import (
    info_print,
    clrtxt,
)
from ..OwegaSession import OwegaSession as ps


# change frequency penalty
def handle_frequency(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /frequency."""
    given = given.strip()
    try:
        new_frequency_penalty = float(given)
    except ValueError:
        if not silent:
            info_print('Current frequency penalty: '
                + f'{baseConf.get("frequency_penalty", 1.0)}')
            info_print('New frequency penalty value (0.0 - 2.0, defaults 0.0)')
        try:
            new_frequency_penalty = ps['float'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " frequency penalty ") + ': ')).strip()
        except (ValueError, KeyboardInterrupt, EOFError):
            if not silent:
                info_print("Invalid frequency penalty.")
            return messages
    baseConf["frequency_penalty"] = float(new_frequency_penalty)
    nv = baseConf.get('frequency_penalty', 0.0)
    if nv > 2.0:
        if not silent:
            info_print('Penalty too high, capping to 2.0')
        baseConf["frequency_penalty"] = 2.0
    if nv < 0.0:
        if not silent:
            info_print('Penalty too low, capping to 0.0')
        baseConf["frequency_penalty"] = 0.0
    if not silent:
        info_print('Set frequency penalty to '
            + f'{baseConf.get("frequency_penalty", 0.0)}')
    return messages


item_frequency = {
    "fun": handle_frequency,
    "help": "sets the frequency penalty (0.0 - 2.0, defaults 0.0)",
    "commands": ["frequency"],
}
