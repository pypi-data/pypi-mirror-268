"""Handle /tts."""
from ..config import baseConf
from ..utils import info_print
from ..OwegaSession import OwegaSession as ps


# enables/disables the TTS
def handle_tts(
    temp_file,
    messages,
    given="",
    temp_is_temp=False,
    silent=False
):
    """Handle /tts."""
    given = given.strip()
    if given.lower() in ["on", "true", "enable", "enabled"]:
        baseConf["tts_enabled"] = True
        if not silent:
            info_print("Text-to-speech enabled.")
        return messages

    if given.lower() in ["off", "false", "disable", "disabled"]:
        baseConf["tts_enabled"] = False
        if not silent:
            info_print("Text-to-speech disabled.")
        return messages

    baseConf["tts_enabled"] = (not baseConf.get("tts_enabled", False))
    if baseConf.get("tts_enabled", False):
        if not silent:
            info_print("Text-to-speech enabled.")
    else:
        if not silent:
            info_print("Text-to-speech disabled.")
    return messages


item_tts = {
    "fun": handle_tts,
    "help": "enables/disables the TTS",
    "commands": ["tts"],
}
