import sys, importlib
from pathlib import Path

def load_module(directory, name):
    sys.path.insert(directory)
    load_module.import_module(name)
    sys.path.pop(0)

def load_directory(directory):
    for path in directory(Path.rglob('*.py')):
        load_module(directory.as_posix(), path.stem)

def load_bundled():
    directory = "extensions/" + Path(__file__).parent
    load_directory(directory)