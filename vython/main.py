from platform import python_version
import click
import json
import os
import subprocess
import sys

from datetime import datetime
from pathlib import Path

VYTHON_SAVE_DIR = (
    os.getenv("VYTHON_SAVE_DIR")
    if os.getenv("VYTHON_SAVE_DIR")
    else os.path.join(Path.home(), ".vython")
)


@click.command()
@click.argument("args", nargs=-1)
def cli(args):
    filename = os.path.join(os.getcwd(), args[0])
    contents = open(filename, "r").read()
    command = " ".join([sys.executable] + sys.argv[1:])
    timestamp = str(datetime.now())

    # Execute file
    args_copy = sys.argv[1:]
    args_copy[0] = filename
    result = subprocess.run([sys.executable] + args_copy)

    # Log timestamp, command, contents
    res = {
        "timestamp": timestamp,
        "filename": filename,
        "command": command,
        "contents": contents,
    }

    dirname = VYTHON_SAVE_DIR + "/" + filename.replace("/", "_")
    os.makedirs(dirname, exist_ok=True)
    with open(os.path.join(dirname, timestamp) + ".json", "w") as f:
        f.write(json.dumps(res))
