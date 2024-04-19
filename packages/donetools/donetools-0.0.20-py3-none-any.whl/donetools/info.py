import os
import sys

def warn(string: str) -> str:
    """Display messages in red bold format."""
    return f"\x1b[1;31m{string}\x1b[0m" if sys.stdout.isatty() else string

def info(string: str) -> str:
    """Display messages in green bold format."""
    return f"\x1b[1;32m{string}\x1b[0m" if sys.stdout.isatty() else string

def indent(lines: str) -> str:
    """Indent each lines in a paragraph."""
    return os.linesep.join(map(lambda line: f"\t{line}", lines.splitlines()))

def dilemma(words: str, positive: str = "yes", negative: str = "no") -> bool:
    """Prompt the user with a binary question and wait for a choice."""
    command, words = None, words
    print(words, end=os.linesep if words.endswith(os.linesep) else os.linesep*2)
    while command not in (positive, negative):
        command = input(warn(f"[{positive}/{negative}]: "))
    return command == positive
