"""Handle /model."""
import prompt_toolkit as pt
from ..config import baseConf, list_models
from ..utils import (info_print, clrtxt)
from ..OwegaSession import OwegaSession as ps


# changes the selected model
def handle_model(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /model."""
    given = given.strip()
    if not silent:
        info_print(f"Current model: {baseConf.get('model', '')}")
        list_models()
        print()
    if given:
        new_model = given
    else:
        new_model = ps['model'].prompt(pt.ANSI(
            '\n' + clrtxt("magenta", " new model ") + ': ')).strip()
    if (new_model.isnumeric()):
        if (int(new_model) < len(baseConf.get("available_models", []))):
            mn = int(new_model)
            baseConf["model"] = baseConf.get("available_models", [])[mn]
            if not silent:
                info_print(f"Model changed to {baseConf.get('model', '')}")
        else:
            if not silent:
                info_print(f"Model not available, keeping {baseConf.get('model', '')}")
    elif new_model in list(baseConf.get("available_models", [])):
        baseConf["model"] = new_model
        if not silent:
            info_print(f"Model changed to {baseConf.get('model', '')}")
    else:
        if not silent:
            info_print(f"Model not available, keeping {baseConf.get('model', '')}")
    return messages


item_model = {
    "fun": handle_model,
    "help": "list the available models and prompt for change",
    "commands": ["model"],
}
