"""This module is the entry point for the package. It is executed when the package is run as a script."""  # noqa: E501

import argparse

from pyproject_deplister.utils import (
    Args,
    print_output,
    read_pyproject_dependencies,
    save_output,
)

parser = argparse.ArgumentParser(
    description="A package to list the dependencies from a pyproject.toml file.",
)
parser.add_argument(
    "--extra",
    "-e",
    type=str,
    help="The list of extra dependencies.",
    default="",
    nargs="*",
)
parser.add_argument(
    "--path",
    "-p",
    type=str,
    help="The path to the pyproject.toml file.",
    default="pyproject.toml",
    nargs="?",
)
parser.add_argument(
    "--output_file",
    "-o",
    type=str,
    help="The path to the output file, if not provided, the output will be printed to the console.",  # noqa: E501
    nargs="?",
)


def main() -> None:
    """The main function that executes the package."""
    args: Args = parser.parse_args()
    pyproject_content = read_pyproject_dependencies(args)
    if args.output_file and len(args.output_file) > 0:
        save_output(pyproject_content, args.output_file)
    else:
        print_output(pyproject_content)


if __name__ == "__main__":
    main()
