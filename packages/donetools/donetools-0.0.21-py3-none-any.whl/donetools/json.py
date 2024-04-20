import json

def dump(obj: dict | list | tuple, path: str, indent: int = 4) -> None:
    """Dump a JSON file."""
    with open(path, mode='w') as file:
        json.dump(obj, file, indent=indent)

def load(path: str) -> dict | list:
    """Load a JSON file."""
    with open(path, mode='r') as file:
        return json.load(file)
