"""Tests for pyproject_deplister.py."""

from pathlib import Path

from pyproject_deplister.utils import Args, read_pyproject_dependencies

HERE = Path(__file__).parent


def test_read_pyproject_with_no_dependencies() -> None:
    """Test reading a pyproject.toml file with no dependencies."""
    input_file = HERE / "sample_pyproject_1.toml"
    args = Args(extra=[], path=str(input_file))

    output = read_pyproject_dependencies(args)

    # there should be no dependencies
    assert len(output.dependencies) == 0, "There should be no dependencies"

    # there should be no extra dependencies
    assert len(output.extra_dependencies) == 0, "There should be no extra dependencies"


def test_read_project_with_dependencies() -> None:
    """Test reading a pyproject.toml file with dependencies."""
    input_file = HERE / "sample_pyproject_2.toml"
    args = Args(extra=[], path=str(input_file))

    expected_dependencies = ["pandas", "numpy==1.21.0"]

    output = read_pyproject_dependencies(args)

    # there should be as many dependencies as expected
    assert len(output.dependencies) == len(
        expected_dependencies,
    ), "There should be 2 dependencies"

    # the dependencies should be as expected
    assert output.dependencies == expected_dependencies, "Dependencies should match"


def test_read_project_with_extra_dependencies() -> None:
    """Test reading a pyproject.toml file with extra dependencies."""
    input_file = HERE / "sample_pyproject_3.toml"

    expected_dependencies = ["pandas", "numpy==1.21.0"]
    expected_extra_dependencies = {"dev": ["jupyter"], "test": ["pytest==6.2.4"]}

    args_empty = Args(extra=[], path=str(input_file))
    args_dev = Args(extra=["dev"], path=str(input_file))
    args_test = Args(extra=["test"], path=str(input_file))
    args_all = Args(extra=["dev", "test"], path=str(input_file))

    output_empty = read_pyproject_dependencies(args_empty)

    # there should be as many dependencies as expected
    assert len(output_empty.dependencies) == len(
        expected_dependencies,
    ), "There should be 2 dependencies"

    # the dependencies should be as expected
    assert (
        output_empty.dependencies == expected_dependencies
    ), "Dependencies should match"

    # there should be no extra dependencies
    assert (
        len(output_empty.extra_dependencies) == 0
    ), "There should be no extra dependencies"

    output_dev = read_pyproject_dependencies(args_dev)

    # there should be as many dependencies as expected
    assert len(output_dev.dependencies) == len(
        expected_dependencies,
    ), "There should be 2 dependencies"

    # the dependencies should be as expected
    assert output_dev.dependencies == expected_dependencies, "Dependencies should match"

    # there should be as many extra dependencies as expected
    assert len(output_dev.extra_dependencies) == len(
        expected_extra_dependencies["dev"],
    ), "There should be 1 extra dependency"

    # the extra dependencies should be as expected
    assert (
        output_dev.extra_dependencies["dev"] == expected_extra_dependencies["dev"]
    ), "Extra dependencies should match"

    output_test = read_pyproject_dependencies(args_test)

    # there should be as many dependencies as expected
    assert len(output_test.dependencies) == len(
        expected_dependencies,
    ), "There should be 2 dependencies"

    # the dependencies should be as expected
    assert (
        output_test.dependencies == expected_dependencies
    ), "Dependencies should match"

    # there should be as many extra dependencies as expected
    assert len(output_test.extra_dependencies) == len(
        expected_extra_dependencies["test"],
    ), "There should be 1 extra dependency"

    # the extra dependencies should be as expected
    assert (
        output_test.extra_dependencies["test"] == expected_extra_dependencies["test"]
    ), "Extra dependencies should match"

    output_all = read_pyproject_dependencies(args_all)

    # there should be as many dependencies as expected
    assert len(output_all.dependencies) == len(
        expected_dependencies,
    ), "There should be 2 dependencies"

    # the dependencies should be as expected
    assert output_all.dependencies == expected_dependencies, "Dependencies should match"

    # there should be as many extra dependencies as expected
    assert len(output_all.extra_dependencies) == len(
        expected_extra_dependencies["dev"] + expected_extra_dependencies["test"],
    ), "There should be 2 extra dependencies"

    # the extra dependencies should be as expected
    assert (
        output_all.extra_dependencies["dev"] == expected_extra_dependencies["dev"]
    ), "Extra dependencies should match"

    assert (
        output_all.extra_dependencies["test"] == expected_extra_dependencies["test"]
    ), "Extra dependencies should match"
