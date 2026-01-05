import os
import inspect

def _get_path(filename):
    if os.path.isabs(filename):
        return filename
    frame = inspect.stack()[2]
    module_path = os.path.dirname(os.path.abspath(frame.filename))
    return os.path.join(module_path, filename)

def read_input(filename="input.txt"):
    path = _get_path(filename)
    with open(path, "r") as f:
        return f.read().strip()

def read_lines(filename="input.txt"):
    path = _get_path(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]