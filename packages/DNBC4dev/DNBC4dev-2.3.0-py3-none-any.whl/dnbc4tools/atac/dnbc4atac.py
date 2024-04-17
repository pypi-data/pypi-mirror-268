import sys
import argparse
import textwrap
import importlib
from typing import Any

from dnbc4tools.__init__ import __version__
from dnbc4tools.atac.__init__ import _pipe
from dnbc4tools.tools.text import help_text, help_sub_text

def safe_import_module(package_name: str) -> Any:
    """
    Safely import a module, handling any potential `ImportError`s.
    
    If an error occurs, prints an error message to standard error and exits the program.
    """
    try:
        return importlib.import_module(package_name)
    except ImportError as e:
        print(f"Failed to import module: {package_name}. Error: {e}", file=sys.stderr)
        sys.exit(1)
def get_steps_help(package: Any, pipe: str) -> Any:
    """
    Safely retrieve step help information, handling any potential `AttributeError`s.

    If an error occurs, prints an error message to standard error and exits the program.
    """
    try:
        steps_help = getattr(package, f"helpInfo_{pipe}")
        return steps_help
    except AttributeError as e:
        print(f"Failed to retrieve help information: {e}", file=sys.stderr)
        sys.exit(1)


def validate_pipe_name(pipe: str) -> bool:
    """
    Validate the safety and validity of a pipe name.

    For demonstration purposes, assume valid pipe names contain only letters and numbers.
    Returns True if the pipe name is valid, False otherwise.
    """
    if not pipe.isalnum():
        print(f"Invalid pipe name: {pipe}", file=sys.stderr)
        return False
    return True

def pipeline_package(pipe: str) -> Any:
    package_name = f"dnbc4tools.atac.{pipe}"
    if not validate_pipe_name(pipe):
        return None
    return safe_import_module(package_name)

def main() -> None:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(help_text('atac', 'dnbc4atac'))
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=__version__
    )
    subparsers = parser.add_subparsers(dest='parser_step')

    for pipe in _pipe:
        package = pipeline_package(pipe)
        if package is None:  # If pipe validation fails, move on to the next one
            continue

        steps = getattr(package, pipe)
        steps_help = get_steps_help(package, pipe)

        parser_step = subparsers.add_parser(
            pipe,
            description=textwrap.dedent(help_sub_text('atac', pipe)),
            formatter_class=argparse.RawDescriptionHelpFormatter
        )
        steps_help(parser_step)
        parser_step.set_defaults(func=steps)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    # Add simple validation before calling the command line step function, which can be expanded based on actual requirements
    if not hasattr(args.func, '__call__'):
        print("Unable to execute the specified step function", file=sys.stderr)
        sys.exit(1)

    args.func(args)


if __name__ == '__main__':
    main()