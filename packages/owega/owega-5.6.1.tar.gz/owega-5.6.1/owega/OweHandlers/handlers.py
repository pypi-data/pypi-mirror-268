"""Gather all the handlers."""
from ..utils import print_help
from .handle_quit import item_quit
from .handle_genconf import item_genconf
from .handle_history import item_history
from .handle_commands import item_commands
from .handle_estimation import item_estimation
from .handle_tokens import item_tokens
from .handle_context import item_context
from .handle_save import item_save
from .handle_load import item_load
from .handle_model import item_model
from .handle_finput import item_finput
from .handle_dinput import item_dinput
from .handle_temperature import item_temperature
from .handle_top_p import item_top_p
from .handle_frequency import item_frequency
from .handle_presence import item_presence
from .handle_edit import item_edit
from .handle_system import item_system
from .handle_add_sysmem import item_add_sysmem
from .handle_del_sysmem import item_del_sysmem
from .handle_tts import item_tts
from .handle_image import item_image
from ..OwegaSession import OwegaSession as ps
from ..handlerBase import items, handlers, handler_helps


# prints help
def handle_help(temp_file, messages, given="", temp_is_temp=False):
    """Handle /help."""
    print_help(handler_helps)
    return messages


item_help = {
    "fun": handle_help,
    "help": "Shows this help",
    "commands": ["help"],
}


def void_func(temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Void function."""
    return messages


def populate():
    """Gather all the handlers."""
    items.append(item_help)
    items.append(item_quit)
    items.append(item_genconf)
    items.append(item_history)
    items.append(item_commands)
    items.append(item_estimation)
    items.append(item_tokens)
    items.append(item_context)
    items.append(item_save)
    items.append(item_load)
    items.append(item_model)
    items.append(item_finput)
    items.append(item_dinput)
    items.append(item_temperature)
    items.append(item_top_p)
    items.append(item_frequency)
    items.append(item_presence)
    items.append(item_edit)
    items.append(item_system)
    items.append(item_add_sysmem)
    items.append(item_del_sysmem)
    items.append(item_tts)
    items.append(item_image)

    for item in items:
        for command in item.get('commands', []):
            handler_helps[command] = item.get('help', '')
            handlers[command] = item.get('fun', void_func)


populate()
