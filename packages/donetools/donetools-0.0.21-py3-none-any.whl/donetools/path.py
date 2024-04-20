import os
import os.path as op
import shutil

from donetools import info

def join(*paths: str) -> str:
    """Concatenate path components."""
    return op.join(*paths)

def is_dir(path: str) -> bool:
    """Test whether a path is intended to represent a directory."""
    return path.endswith(os.sep)

def is_file(path: str) -> bool:
    """Test whether a path is intended to represent a file."""
    return not path.endswith(os.sep)

def is_abs(path: str) -> bool:
    """Test whether path is an absolute pathname."""
    return op.isabs(path)

def to_dir(path: str) -> str:
    """Ensure the tail separator exists in a directory path."""
    return path if is_dir(path) else path + os.sep

def to_file(path: str) -> str:
    """Ensure there exists no tail separator exists in a file path."""
    return path.rstrip(os.sep)

def to_abs(path: str) -> str:
    """Absolutize path without normalizing it."""
    return join(os.getcwd(), path)

def to_rel(path: str, start=os.curdir) -> str:
    """Return a relative path from a `start` directory without normalizing the output."""
    return to_dir(op.relpath(path, start)) if is_dir(path) else op.relpath(path, start)

def holds_dir(path: str) -> bool:
    """Test whether a path points to an existing directory."""
    return op.isdir(op.normpath(path))

def holds_file(path: str) -> bool:
    """Test whether a path points to an existing file."""
    return op.isfile(op.normpath(path))

def has_child(path: str) -> bool:
    """Test whether a path has child nodes in the file system."""
    return holds_dir(path) and len(os.listdir(path)) > 0

def exists(path: str) -> bool:
    """Test whether a path points to an existing system object."""
    return op.exists(op.normpath(path))

def dirname(path: str) -> str:
    """Return the directory name of a path."""
    return to_dir(op.dirname(to_abs(path)) if is_abs(path) else to_rel(op.dirname(to_abs(path))))

def collide(path: str) -> bool:
    """Test whether a path collides with an non-empty system object."""
    return (holds_file(path) or has_child(path)) if is_dir(path) else exists(path)

def listdir(path: str) -> list[str]:
    """List all files and sub-directories in a specified folder."""
    return [to_dir(child) if holds_dir(join(path, child)) else child for child in os.listdir(path)]

def move_children(source: str, target: str) -> None:
    """Move all files and sub-directories in the source folder to the target."""
    children = listdir(source)
    mapping = [(op.join(source, child), op.join(target, child)) for child in children]
    for source, target in mapping: shutil.move(source, target)

def remove(*paths: str) -> None:
    """Remove existing objects on specified paths."""
    for path in paths: shutil.rmtree(path) if holds_dir(path) else os.unlink(path)

def reconcile(*paths: str, overwrite: bool = False) -> None:
    """Reconcile the potential conflicts between specified paths and existing objects."""
    paths = [to_dir(path) if holds_dir(path) else to_file(path) for path in filter(collide, paths)]
    if len(paths) > 0:
        prompt = f"Agree to {info.warn('remove')} conflicts?" + 2 * os.linesep
        if overwrite or info.dilemma(prompt + info.indent(os.linesep.join(paths))):
            remove(*paths)
        else: exit()

def secure(*paths: str, overwrite: bool = False) -> None:
    """Secure the specified paths."""
    reconcile(*paths, overwrite=overwrite)
    for dir in map(dirname, paths): os.makedirs(dir, exist_ok=True)
