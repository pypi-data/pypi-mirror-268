import json

from donetools import path as dypath

def dump(obj: dict | list | tuple, path: str, overwrite: bool = False) -> None:
    dypath.secure(path, overwrite=overwrite)
    with open(path, mode='w') as file:
        json.dump(obj, file)

def load(path: str) -> dict | list:
    with open(path, mode='r') as file:
        return json.load(file)
