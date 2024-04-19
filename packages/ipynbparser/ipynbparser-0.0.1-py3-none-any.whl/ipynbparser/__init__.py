from importlib.metadata import version
from pathlib import Path

import nbformat as nbf
from IPython import get_ipython  # type: ignore

__version__ = version('ipynbparser')


def parseipynb(as_version: int = 4, **kwargs) -> nbf.NotebookNode:
    """
    Parse the current notebook file and return the notebook object.

    :param as_version: the version of the notebook to parse, default is 4
    :param kwargs: additional keyword arguments to pass to `nbformat.read`
    :return: the parsed notebook object
    """
    shell = get_ipython()
    nbfile = shell.user_ns.get(
        '__vsc_ipynb_file__', shell.user_ns.get('__session__', None)
    )
    if not nbfile:
        raise ValueError('No notebook file found in the current session.')
    session_dir: Path = shell.user_ns['_dh'][-1]
    nbfile = Path(nbfile).resolve()

    # Check if the nbfile path starts with the session_dir path
    if not nbfile.exists() and nbfile.is_relative_to(session_dir):
        nbfile = session_dir / nbfile.relative_to(session_dir).parts[1]

    if not nbfile.exists():
        raise FileNotFoundError(f'Notebook file {nbfile} not found.')
    return nbf.read(nbfile, as_version, **kwargs)
