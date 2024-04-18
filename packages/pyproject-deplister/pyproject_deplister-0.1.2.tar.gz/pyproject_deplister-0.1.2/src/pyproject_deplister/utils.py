"""Code logic for the pyproject_deplister module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

import tomli


@dataclass
class Args:
    """Input arguments for the program."""

    extra: List[str]
    path: str
    output_file: Optional[str]


@dataclass
class Output:
    """Output of the extraction function."""

    dependencies: List[str]
    extra_dependencies: Dict[str, List[str]]

    def __str__(self: Output) -> str:
        """Follows the format of requirements.txt."""
        output = "\n".join(self.dependencies)
        for dependencies in self.extra_dependencies.values():
            output += "\n" + "\n".join(dependencies)
        return output


def read_pyproject_dependencies(args: Args) -> Output:
    """Reads the pyproject.toml file and returns it as a dictionary.

    Args:
        args (Args): The input arguments.

    Returns:
        Output: The output of the function.
    """
    with open(args.path, "rb") as f:
        toml_dict = tomli.load(f)

    return Output(
        dependencies=toml_dict["project"].get("dependencies", []),
        extra_dependencies={
            k: v
            for k, v in toml_dict["project"].get("optional-dependencies", {}).items()
            if k in args.extra
        },
    )


def save_output(output: Output, path: str) -> None:
    """Saves the output of the program to a file.

    Follows the format of requirements.txt.

    Args:
        output (Dict[str, List[str]]): The output of the program.
        path (str): The path to the file.
    """
    with open(path, "w") as f:
        f.write(str(output))


def print_output(output: Output) -> None:
    """Prints the output of the program.

    Follows the format of requirements.txt.

    Args:
        output (Dict[str, List[str]]): The output of the program.
    """
    print(output)  # noqa: T201
