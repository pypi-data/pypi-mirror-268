import mimetypes
import os
from typing import Union

HEADER = """
The text represents a Git repository with the following format:

--- 
filename: The name of the file, within a repository
format: The format of the file contents 

<multiple lines of content for the file>
---

The repository ends with --END--
Any text after --END-- are instructions related to the repository.
"""

BLOCK = """
---
filename: {filename}
format: {format}

{content}
---
"""

FOOTER = """
--END--
"""
EXTENDED_MIMETYPE_SUFFIXES = {
    '.md': 'text/markdown',
}


ALLOWED_MIMETYPES = [
    'text/markdown',
    'text/plain',
    'text/html'
    'text/x-script.python',
    'text/x-python',
]


def allowed_mimetype(mimetype):
    return mimetype in ALLOWED_MIMETYPES or mimetype.startswith('text/')


def guess_mimetype(filename: str) -> str:
    fmt = mimetypes.guess_type(filename)
    if fmt is None or fmt[0] is None:
        _, ext = os.path.splitext(filename)
        return EXTENDED_MIMETYPE_SUFFIXES.get(ext)
    else:
        return fmt[0] if fmt else fmt


def create_block(filename, tree_root) -> Union[str, None]:
    fmt = guess_mimetype(filename)
    if fmt not in ALLOWED_MIMETYPES:
        return None
    with open(filename, 'r') as f:
        content = f.read()
    relpath = os.path.join(os.path.basename(tree_root), os.path.relpath(filename, tree_root))
    return BLOCK.format(filename=relpath, format=fmt, content=content)


def traverse_tree(root='.', ignore=lambda x: False):
    yield HEADER
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for file in files:
            abspath = os.path.join(path, file)
            if ignore(abspath):
                continue
            block = create_block(abspath, tree_root=root)
            if block:
                yield block
    yield FOOTER
