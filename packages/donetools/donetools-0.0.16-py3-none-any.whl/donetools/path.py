import os
import shutil

from donetools import info

def isDir(path: str) -> bool:
    """Test whether a path is intended to represent a directory."""
    return path.endswith(os.sep)

def isFile(path: str) -> bool:
    """Test whether a path is intended to represent a file."""
    return not path.endswith(os.sep)

def isAbs(path: str) -> bool:
    """Test whether path is an absolute pathname."""
    return os.path.isabs(path)

def toDir(path: str) -> str:
    """Ensure the tail separator exists in a directory path."""
    return path if isDir(path) else path + os.sep

def toAbs(path: str) -> str:
    """Absolutize path without normalizing it."""
    return os.path.join(os.getcwd(), path)

def toRel(path: str, start=os.curdir) -> str:
    """Return a relative path from a `start` directory without normalizing the output."""
    return toDir(os.path.relpath(path, start)) if isDir(path) else os.path.relpath(path, start)

def dirname(path: str) -> str:
    """Return the directory name of a path."""
    dirname = toDir(os.path.dirname(toAbs(path)))
    return dirname if isAbs(path) else toRel(dirname)

def holdsDir(path: str) -> bool:
    """Test whether a path points to an existing directory."""
    return os.path.isdir(path)

def holdsFile(path: str) -> bool:
    """Test whether a path points to an existing file."""
    return os.path.isfile(path)

def hasChild(path: str) -> bool:
    """Test whether a path has child nodes in the file system."""
    return os.path.isdir(path) and len(os.listdir(path)) > 0

def exists(path: str) -> bool:
    """Test whether a path points to an existing system object."""
    return os.path.exists(path)

def collide(path: str) -> bool:
    """Test whether a path collides with an existing system object."""
    return (holdsFile(path) or hasChild(path)) if isDir(path) else exists(path)

def listDir(path: str) -> list[str]:
    """List all files and sub-directories in a specified folder."""
    children = os.listdir(path)
    return [toDir(child) if holdsDir(os.path.join(path, child)) else child for child in children]

def moveChildren(source: str, target: str) -> None:
    """Move all files and sub-directories in the source folder to the target."""
    children = listDir(source)
    sources = [os.path.join(source, child) for child in children]
    targets = [os.path.join(target, child) for child in children]
    for source, target in zip(sources, targets): shutil.move(source, target)

def remove(*paths: str) -> None:
    """Remove existing objects on specified paths."""
    for path in paths: shutil.rmtree(path) if holdsDir(path) else os.unlink(path)

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
    for dir in map(dirname, paths): os.makedirs(dir, exist_ok=True)
