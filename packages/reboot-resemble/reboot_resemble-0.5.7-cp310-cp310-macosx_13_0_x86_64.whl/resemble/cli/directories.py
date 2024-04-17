import argparse
import git
# mypy fails with 'error: Trying to read deleted variable "exc"' if we use
# 'git.exc'
import git.exc as gitexc
import os
from contextlib import contextmanager
from pathlib import Path
from resemble.cli.rc import ArgumentParser, SubcommandParser
from resemble.cli.terminal import fail, verbose


def add_working_directory_options(subcommand: SubcommandParser) -> None:
    subcommand.add_argument(
        '--working-directory',
        type=Path,
        help=(
            "directory in which to execute; defaults to the location of the "
            "`.rsmrc` file."
        ),
    )


def is_on_path(file):
    """Helper to check if a file is on the PATH."""
    for directory in os.environ['PATH'].split(os.pathsep):
        if os.path.exists(os.path.join(directory, file)):
            return True
    return False


def dot_rsm_directory() -> str:
    """Helper for determining the '.rsm' directory."""
    try:
        repo = git.Repo(search_parent_directories=True)
    except gitexc.InvalidGitRepositoryError:
        return os.path.join(os.getcwd(), '.rsm')
    else:
        return os.path.join(repo.working_dir, '.rsm')


def dot_rsm_dev_directory() -> str:
    """Helper for determining the '.rsm/dev' directory."""
    return os.path.join(dot_rsm_directory(), 'dev')


@contextmanager
def chdir(directory):
    """Context manager that changes into a directory and then changes back
    into the original directory before control is returned."""
    cwd = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)


@contextmanager
def use_working_directory(args: argparse.Namespace, parser: ArgumentParser):
    """Context manager that changes into an explicitly specified --working-directory, or
    else the location of the `.rsmrc` file.

    `add_working_directory_options` must have been called to register the option which is
    used here.
    """
    working_directory: str
    if args.working_directory is not None:
        working_directory = args.working_directory
    elif parser.dot_rc is not None:
        working_directory = str(Path(parser.dot_rc).parent)
    else:
        fail(
            "Either a `.rsmrc` file must be configured, or the "
            "`--working-directory` option must be specified."
        )

    working_directory = os.path.abspath(working_directory)
    verbose(f"Using working directory {working_directory}\n")
    with chdir(working_directory):
        yield
