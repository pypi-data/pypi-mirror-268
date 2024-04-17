import os
import shutil

from donetools import info

def dir(path: str) -> str:
    """Ensure the tail separator exists in a directory path."""
    return path if isDir(path) else path + os.sep

def isDir(path: str) -> bool:
    """Test whether a path is intended to represent a directory."""
    return path.endswith(os.sep)

def isFile(path: str) -> bool:
    """Test whether a path is intended to represent a file."""
    return not path.endswith(os.sep)

def abs(path: str) -> str:
    """Absolutize path without normalizing it."""
    return os.path.join(os.getcwd(), path)

def rel(path: str, start=os.curdir) -> str:
    """Return a relative path from a `start` directory without normalizing the output."""
    return dir(os.path.relpath(path, start)) if isDir(path) else os.path.relpath(path, start)

def existDir(path: str) -> bool:
    """Test whether a path points to an existing directory."""
    return os.path.isdir(path)

def existFile(path: str) -> bool:
    """Test whether a path points to an existing file."""
    return os.path.isfile(path)

def collideDir(path: str) -> bool:
    """Test whether a path collides with an existing directory."""
    return existDir(path) if isFile(path) else (existDir(path) and len(os.listdir(path)) > 0)

def collideFile(path: str) -> bool:
    """Test whether a path collides with an existing file."""
    return existFile(path)

def collide(path: str) -> bool:
    """Test whether a path collides with an existing system object."""
    return collideFile(path) or collideDir(path)

def remove(*paths: str) -> None:
    """Remove existing objects on specified paths."""
    for path in paths: shutil.rmtree(path) if existDir(path) else os.unlink(path)

def reconcile(*paths: str, overwrite: bool = False) -> None:
    """Reconcile the potential conflicts between specified paths and existing objects."""
    conflicts = list(filter(collide, paths))
    if len(conflicts) > 0:
        prompt = f"Agree to {info.warn('remove')} conflicts?" + 2 * os.linesep
        if overwrite or info.dilemma(prompt + info.indent(os.linesep.join(conflicts))):
            remove(*conflicts)
        else: exit()

def secure(*paths: str, overwrite: bool = False) -> None:
    """Secure the specified paths."""
    reconcile(*paths, overwrite=overwrite)
    for dir in map(os.path.dirname, paths):
        os.makedirs(dir, exist_ok=True)
