"""Utilities that don't fit anywhere else."""
import os
import tempfile
import sys
import json5 as json
import tiktoken
import openai
import warnings
from .conversation import Conversation
from .config import baseConf
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*pygame.*")
import pygame  # noqa


def genconfig(conf_path=""):
    """Generate the config file if it doesn't exist already."""
    if not conf_path:
        conf_path = get_home_dir() + "/.owega.json"
    is_blank = True
    if (os.path.exists(conf_path)):
        is_blank = False
        with open(conf_path, "r") as f:
            if len(f.read()) < 2:
                is_blank = True
    if is_blank:
        with open(conf_path, "w") as f:
            f.write('// vim: set ft=json5:\n')
            f.write(json.dumps(baseConf.baseConf, indent=4))
        info_print(f"generated config file at {conf_path}!")
        return
    print(clrtxt('red', ' WARNING ')
        + f": YOU ALREADY HAVE A CONFIG FILE AT {conf_path}")
    print(clrtxt('red', ' WARNING ')
        + ": DO YOU REALLY WANT TO OVERWRITE IT???")
    inps = clrtxt("red", "   y/N   ") + ': '
    inp = input(inps).lower().strip()
    if inp:
        if inp[0] == 'y':
            with open(conf_path, "w") as f:
                f.write('// vim: set ft=json5:\n')
                f.write(json.dumps(baseConf.baseConf, indent=4))
            info_print(f"generated config file at {conf_path}!")
            return
    info_print("Sorry, not sorry OwO I won't let you nuke your config file!!!")


def play_opus(location: str) -> None:
    """Play an OPUS audio file."""
    pygame.mixer.init()
    sound = pygame.mixer.Sound(location)
    sound.play()
    try:
        while pygame.mixer.get_busy():
            pygame.time.delay(100)
    except KeyboardInterrupt:
        pass
    pygame.mixer.quit()


def play_tts(text: str, voice: str = 'nova') -> None:
    """Generate TTS audio from given text and play it."""
    tmpfile = tempfile.NamedTemporaryFile(
        prefix="owegatts.",
        suffix=".opus",
        delete=False
    )
    tmpfile.close()
    tts_answer = openai.audio.speech.create(
        model='tts-1',
        voice=voice,
        input=text
    )
    tts_answer.stream_to_file(tmpfile.name)
    play_opus(tmpfile.name)
    os.remove(tmpfile.name)


def estimated_tokens(ppt: str, messages: Conversation, functions):
    """Estimate the history tokens."""
    try:
        encoder = tiktoken.encoding_for_model("gpt-4")
        req = ""
        req += ppt
        req += json.dumps(messages.get_messages())
        req += json.dumps(functions)
        tokens = encoder.encode(req)
        return len(tokens)
    except Exception as e:
        if baseConf.baseConf.get("debug"):
            print(
                "An error has occured while estimating tokens:",
                file=sys.stderr
            )
            print(e, file=sys.stderr)
        return 0


def get_temp_file() -> str:
    """Get a temp file location."""
    tmp = tempfile.NamedTemporaryFile(
        prefix="owega_temp.",
        suffix=".json",
        delete=False
    )
    filename = tmp.name
    tmp.close()
    return filename


def get_home_dir() -> str:
    """Get the user home directory, cross platform."""
    return os.path.expanduser('~')


def clr(color: str) -> str:
    """Return the ANSI escape sequence for the given color."""
    esc = '\033['
    colors = {
        "red": f"{esc}91m",
        "green": f"{esc}92m",
        "yellow": f"{esc}93m",
        "blue": f"{esc}94m",
        "magenta": f"{esc}95m",
        "cyan": f"{esc}96m",
        "white": f"{esc}97m",
        "reset": f"{esc}0m",
    }
    return colors[color]


def clrtxt(color: str, text: str) -> str:
    """Print text in color between square brackets."""
    return "[" + clr(color) + text + clr("reset") + "]"


def debug_print(text: str, debug: bool = False) -> None:
    """Print text if debug is enabled."""
    if debug:
        print(' ' + clrtxt("magenta", " DEBUG ") + ": " + text)


def success_msg():
    """Return the standard success message."""
    return '  ' + clrtxt("cyan", " INFO ") + ": Owega exited successfully!"


def clearScreen():
    """Clear the terminal screen, depends on system (unix or windows-based)."""
    if os.name == 'nt':
        os.system('cls')
    else:
        print("\033[2J\033[0;0f", end="")


def do_quit(msg="", value=0, temp_file="", is_temp=False, should_del=False):
    """Quit and delete the given file if exists."""
    if (temp_file):
        if should_del:
            try:
                os.remove(temp_file)
            except Exception:
                pass
        else:
            if is_temp:
                try:
                    with open(temp_file, 'r') as f:
                        contents = json.loads(f.read())
                        if not (
                            (len(contents.get("messages", [])) > 0)
                            or (len(contents.get("souvenirs", [])) > 0)
                        ):
                            os.remove(temp_file)
                except Exception:
                    pass
    if (msg):
        print()
        print(msg)
    sys.exit(value)


def info_print(msg):
    """Print an info message."""
    print('  ' + clrtxt("cyan", " INFO ") + ": ", end='')
    print(msg)


def command_text(msg):
    """Print an command message."""
    return ' ' + clrtxt("red", "COMMAND") + ": " + msg


def print_help(commands_help={}):
    """Print the command help."""
    commands = list(commands_help.keys())
    longest = 0
    for command in commands:
        if len(command) > longest:
            longest = len(command)
    longest += 1
    print()
    info_print("Enter your question after the user prompt, "
        + "and it will be answered by OpenAI")
    info_print("other commands are:")
    for cmd, hstr in commands_help.items():
        command = '/' + cmd
        info_print(f"   {command:>{longest}}  - {hstr}")
    print()
