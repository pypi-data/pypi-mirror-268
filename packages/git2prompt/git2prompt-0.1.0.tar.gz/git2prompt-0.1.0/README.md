# git2prompt

git2prompt is a command-line utility that converts a local Git repository into a formatted text representation.
This can be useful for sharing code snippets, project structures, or entire repositories in a plain text format,
without needing to archive or transmit the actual files.

## Installation
```shell
pip install git2prompt --user
```
## Usage

To use git2prompt, simply run the `git2prompt` script and provide the path to the Git repository you want to convert:

```shell
git2prompt /path/to/your/repo
```

This will output the formatted text representation of the repository to the console.

## Output Format

The output follows this structure:
The text represents a Git repository with the following format:

filename: The name of the file, within a repository format: The format of the file contents <multiple lines of content for the file>
The repository ends with --END--

Any text after --END-- are instructions related to the repository.


Copy code

Each file in the repository is represented as a block, with the filename, file format, and contents included. The supported file formats are:

- Text files (`.txt`)
- Markdown files (`.md`)
- HTML files (`.html`)
- Python scripts (`.py`)

After all file blocks, the output ends with `--END--`. Any text after this line is considered instructions related to the repository.

## Ignored Files

git2prompt respects `.gitignore` files in the repository. Any files or directories listed in these ignore files will be excluded from the output.

## Example

Running `python -m git2prompt /path/to/your/repo` with the provided example repository will output:
<contents of the example output> ```
# License
This project is licensed under the MIT License.

