from .base import Command


def python_pip(name, op="install", upgrade=False, venv=None, version=3, **kwargs):
    """Use pip to install or uninstall a Python package.

    :param name: The name of the package.
    :type name: str

    :param op: The operation to perform; ``install``, ``remove``
    :type op: str

    :param upgrade: Upgrade an installed package.
    :type upgrade: bool

    :param venv: The name of the virtual environment to load.
    :type venv: str

    :param version: The Python version to use, e.g. ``2`` or ``3``.
    :type version: int

    """
    manager = "pip"
    if version == 3:
        manager = "pip3"

    if upgrade:
        statement = "%s install --upgrade %s" % (manager, name)
    else:
        statement = "%s %s %s" % (manager, op, name)

    if venv is not None:
        kwargs['prefix'] = "source %s/bin/activate" % venv

    kwargs.setdefault("comment", "%s %s" % (op, name))

    return Command(statement, **kwargs)


def python_pip_file(path, venv=None, version=3, **kwargs):
    """Install Python packages from a pip file.

    :param path: The path to the file.
    :type path: str

    :param venv: The name (and/or path) of the virtual environment.
    :type venv: str

    :param version: The pip version to use.

    """
    manager = "pip"
    if version == 3:
        manager = "pip3"

    if venv is not None:
        kwargs['prefix'] = "source %s/bin/activate" % venv

    kwargs.setdefault("comment", "install packages from pip file %s" % path)

    statement = "%s install -r %s" % (manager, path)

    return Command(statement, **kwargs)


def python_virtualenv(name, **kwargs):
    """Create a Python virtual environment.

    :param name: The name of the environment to create.
    :type name: str

    """
    kwargs.setdefault("comment", "create %s virtual environment" % name)

    return Command("virtualenv %s" % name, **kwargs)


PYTHON_MAPPINGS = {
    'pip': python_pip,
    'pipf': python_pip_file,
    'pip_file': python_pip_file,
    'virtualenv': python_virtualenv,
}
