"""Main bottom toolbar for TUI."""
import prompt_toolkit as pt
from ..config import baseConf
from ..changelog import OwegaChangelog


# bottom toolbar and style for prompt_toolkit
def main_bottom_toolbar(what: str = "toolbar"):
    """Return the bottom style or toolbar."""
    if what == "style":
        msd = {
            'red':     '#000000 bg:#FF0000',  # noqa: E241
            'green':   '#000000 bg:#00FF00',  # noqa: E241
            'blue':    '#000000 bg:#0000FF',  # noqa: E241
            'yellow':  '#000000 bg:#FFFF00',  # noqa: E241
            'magenta': '#000000 bg:#FF00FF',  # noqa: E241
            'cyan':    '#000000 bg:#00FFFF',  # noqa: E241
            'white':   '#000000 bg:#FFFFFF',  # noqa: E241
        }
        msd['bottom-toolbar'] = msd['white']
        msd['bottom-even'] = msd['magenta']
        msd['bottom-odd'] = msd['cyan']
        msd['bottom-on'] = msd['green']
        msd['bottom-off'] = msd['red']
        main_style = pt.styles.Style.from_dict(msd)
        return main_style

    class tr:
        def __init__(self):
            self.table = []
            self.count = 0

        def add(self, prefix="/", txt="", color="yellow"):
            new_class = "white"
            if not isinstance(txt, str):
                txt = str(txt)
            if self.count:
                self.table.append((
                    "class:blue",
                    " - "
                ))
            if prefix:
                if txt:
                    prefix = prefix + ": "
                self.table.append((
                    f"class:{new_class}",
                    prefix
                ))
            if txt:
                self.table.append((
                    f"class:{color}",
                    txt
                ))
            self.count += 1

    to_ret = tr()
    to_ret.add(f"v{OwegaChangelog.version}")
    to_ret.add("model", baseConf.get("model", "unknown"))
    to_ret.add(
        "cmds",
        "ON" if baseConf.get("commands") else "OFF",
        "bottom-on" if baseConf.get("commands") else "bottom-off"
    )
    to_ret.add("tokens", baseConf.get("max_tokens", "unknown"))
    to_ret.add(
        "estm",
        "ON" if baseConf.get("estimation") else "OFF",
        "bottom-on" if baseConf.get("estimation") else "bottom-off"
    )
    to_ret.add("temp", baseConf.get("temperature", "unknown"))
    to_ret.add("top_p", baseConf.get("top_p", "unknown"))
    to_ret.add("freq.plty", baseConf.get("frequency_penalty", "unknown"))
    to_ret.add("pr.plty", baseConf.get("presence_penalty", "unknown"))
    to_ret.add(
        "TTS",
        "ON" if baseConf.get("tts_enabled") else "OFF",
        "bottom-on" if baseConf.get("tts_enabled") else "bottom-off"
    )
    return to_ret.table
