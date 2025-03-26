# Tree CLI

A lightweight Python implementation of the Linux `tree` command.

## Installation

Install the package using pip:

```bash
pip install .
```

## Usage

To display the directory structure, run:

```bash
tree /path/to/directory
```

If no path is provided, the current directory (.) is used.

## Example

```bash
$ tree
.
├── file1.txt
├── dir1
│   ├── file2.txt
│   └── file3.txt
└── dir2
    └── file4.txt
```