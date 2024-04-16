"""Handle /temperature."""
import prompt_toolkit as pt
from ..config import baseConf
from ..utils import (
    info_print,
    clrtxt,
)
from ..OwegaSession import OwegaSession as ps


# change temperature
def handle_temperature(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /temperature."""
    given = given.strip()
    try:
        new_temperature = float(given)
    except ValueError:
        if not silent:
            info_print('Current temperature: '
                + f'{baseConf.get("temperature", 1.0)}')
            info_print('New temperature value (0.0 - 2.0, defaults 0.8)')
        try:
            new_temperature = ps['float'].prompt(pt.ANSI(
                '\n' + clrtxt("magenta", " temperature ") + ': ')).strip()
        except (ValueError, KeyboardInterrupt, EOFError):
            if not silent:
                info_print("Invalid temperature.")
            return messages
    baseConf["temperature"] = float(new_temperature)
    nv = baseConf.get('temperature', 0.0)
    if nv > 2.0:
        if not silent:
            info_print('Temperature too high, capping to 2.0')
        baseConf["temperature"] = 2.0
    if nv < 0.0:
        if not silent:
            info_print('Temperature negative, capping to 0.0')
        baseConf["temperature"] = 0.0
    if not silent:
        info_print('Set temperature to '
            + f'{baseConf.get("temperature", 0.0)}')
    return messages


item_temperature = {
    "fun": handle_temperature,
    "help": "sets the temperature (0.0 - 1.0, defaults 0.8)",
    "commands": ["temperature"],
}
