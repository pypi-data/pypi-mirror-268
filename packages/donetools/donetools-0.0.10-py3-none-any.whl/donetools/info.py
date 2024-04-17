import os
import sys

def warn(string: str) -> str:
    return f"\033[1m\033[31m{string}\033[0m" if sys.stdout.isatty() else string

def info(string: str) -> str:
    return f"\033[1m\033[32m{string}\033[0m" if sys.stdout.isatty() else string

def indent(lines: str) -> str:
    return os.linesep.join(map(lambda line: f"\t{line}", lines.splitlines()))

def dilemma(words: str, positive: str = "yes", negative: str = "no") -> bool:
    command, words = None, words
    print(words, end=os.linesep if words.endswith(os.linesep) else os.linesep*2)
    while command not in (positive, negative):
        command = input(warn(f"[{positive}/{negative}]: "))
    return command == positive
