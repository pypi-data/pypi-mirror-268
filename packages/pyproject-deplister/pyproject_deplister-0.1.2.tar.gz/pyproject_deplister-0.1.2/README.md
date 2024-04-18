
# pyproject-deplister

Python package for extracting dependencies from `pyproject.toml` files and converting them into the format of a `requirements.txt` file.

## Installation

You can install `pyproject-deplister` using pip:

```
pip install pyproject-deplister
```

## Usage

To use `pyproject-deplister`, simply provide the path to your `pyproject.toml` file as an argument:

```
pyproject-deplister -p path/to/pyproject.toml
```

The output will be a list of dependencies in the format of a `requirements.txt` file, which you can use with `pip` to install and manage your project's dependencies.

For example:

```
numpy==1.21.0
pandas==1.3.0
scikit-learn==0.24.2
```

There are also additional options available:
* `-p` or `--path`: Specify the path to the `pyproject.toml` file. By default, the current working directory will be used.
* `-o` or `--output`: Specify the output file for the `requirements.txt` file. By default, the output will be printed to the console.
* `-e` or `--extra`: Include dependencies from the specified extras in the output. For example, `-e dev` will include dependencies from the `dev` extras. You can specify multiple extras separated by space.

```
pyproject-deplister [-h] [--extra [EXTRA ...]] [--path [PATH]] [--output_file [OUTPUT_FILE]]
```

## Features

* Extract dependency information from `pyproject.toml` files
* Convert dependency information into the format of a `requirements.txt` file
* Simple and intuitive interface

## Disclaimer

Dependencies can only be extracted if they follow specifically the specification introduced in [PEP 631](https://peps.python.org/pep-0631/).

## Requirements

* Python 3.6 or higher

## License

`pyproject-deplister` is licensed under the [MIT License](LICENSE).