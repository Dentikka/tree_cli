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

Ignoring Hidden Files and Directories
To ignore hidden files and directories (those starting with .), use the --ignore-hidden option:

```bash
tree /path/to/directory --ignore-hidden
```

## Examples

Display Current Directory Structure
```bash
tree
```

Example output:
```bash
├── file1.txt
└── dir1
    ├── file2.txt
    └── file3.txt
```

Display Directory Structure, Ignoring Hidden Files

```bash
tree --ignore-hidden
```

Example output (assuming .hidden_dir and .hidden_file exist):

```bash
.
├── file1.txt
└── dir1
    ├── file2.txt
    └── file3.txt
```