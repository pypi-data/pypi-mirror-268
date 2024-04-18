# Recursive Output Utility

## Overview

This Python script recursively searches for files based on their extensions starting from a specified directory. It can print the directory structure, include or exclude specific files, use syntax highlighting for output, and anonymize file paths for privacy.

## Requirements

* Python 3.10 or higher,
* `bat` (optional, for syntax highlighting),

## Installation

### Using pip

```bash
python -m pip install routput
```

On some systems, you may need to put the version number of python:

```bash
python3.12 -m pip install routput
```

> For the sake of simplicity, whenever I mention `python` in the following sections, you can replace it with `python3.x` version if necessary.

### From source

Clone this repository.

```bash
git clone https://github.com/nacioboi/routput.git
```

Navigate to the repository directory.

```bash
cd routput
```

And install the package.

```bash
python -m pip install .
```

## Usage

```bash
python -m routput [options]
```

Options

* -d, --starting-directory: Directory to start the search from (default: current directory).
* -s, --do-print-structure: Print the directory structure.
* -e, --extensions: List of file extensions to search for, format [ext1,ext2,...] (default: [c,h]).
* -p, --do-protect-privacy: Anonymize file paths.
* -a, --also-include: List of additional filenames to include, format [file1,file2,...].
* -i, --ignore: List of filenames to ignore, format [file1,file2,dir1,dir2...].
* -n, --no-print: Don't print the files, just return them.
* -b, --do-use-bat: Use bat for syntax highlighting.
* -c, --do-colors: Use different colors for each file type.
* -h, --help: Show help message and exit.

## Examples

To print the structure of a directory:

```bash
python -m routput.py -d /path/to/directory -s
```

To find and print .py files in the current directory, using bat for highlighting:

```bash
python routput.py -e [py] -b
```

## License

Open-source software licensed under GPL-2 license.
