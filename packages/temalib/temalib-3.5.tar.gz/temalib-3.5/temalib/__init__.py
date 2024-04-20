import codecs
import os
from typing import Any

"""
a library that was made for working with files
"""

__author__ = "tema5002 <tema5002@gmail.com>"
__version__ = "3.5"
__license__ = "MIT"
__copyright__ = "2024, tema5002"
__short_description__ = "a library that works with files i guess"


def smthfile(fp: str, mode: str) -> codecs.StreamReaderWriter:
    """
Opens a text file with UTF-8 encoding at the specified path (fp) with specified opening mode (mode)

Keyword arguments:
- fp (str): The filepath of the text file to open.
- mode (str): The opening mode for the file.
    (List of opening modes: https://docs.python.org/3/library/functions.html#open)

Returns:
- codecs.StreamReaderWriter: A file object opened with UTF-8 encoding.

Raises:
- OSError: If the file cannot be opened at the specified path.
    """
    return codecs.open(fp, mode, encoding="utf-8")


def openfile(fp: str) -> codecs.StreamReaderWriter:
    """
smthfile() but with "r" opening mode
    """
    return smthfile(fp, "r")


def editfile(fp: str) -> codecs.StreamReaderWriter:
    """
smthfile() but with "w" opening mode
    """
    return smthfile(fp, "w")


def get_folder_path(
        caller: str,
        *args: Any,
        # this is probably a bad idea to allow using anything but whatever
        create_folders: bool = True
) -> str:
    """
Construct a folder path relative to the caller's directory, optionally creating missing folders.

This function builds a filepath by combining:
- The directory of the caller file (caller)
- Additional subfolders specified as positional arguments (args)

Parameters:

- caller (str): The path of the caller file (usually __file__).
- *args (Any): One or more subfolder names to be added to the path.
  (args will be converted to str but i don't recommend putting anything except str and int)
- create_folders (bool, optional): Whether to create missing folders in the path. (True by default)

Returns:

- str: The constructed folder path.

Raises:

- OSError: If there are errors creating folders (e.g., permission issues).

Example Usage:

folder_path = get_folder_path(__file__, "data", "results")

print(folder_path)
# Output: C:\\path\\to\\__file__\\data\\results
    """
    args = list(map(str, args))

    folder_dir = os.path.dirname(caller)
    for f in args:
        folder_dir = os.path.join(folder_dir, f)
        if create_folders and not os.path.exists(folder_dir):
            try:
                os.makedirs(folder_dir)
            except OSError as err:
                raise OSError(f"Failed to create folders: {err}") from err

    return folder_dir


def get_file_path(caller: str, *args: str, create_folders: bool = True, create_file: str = "") -> str:
    """
Constructs a file path relative to the caller's directory, optionally creating missing folders and the file itself.

This function builds a file path by combining:

- The directory of the caller file (caller)
- Additional subfolders and a final file name specified as positional arguments (args)

It optionally creates any missing folders in the path and the file itself if it doesn't exist.

Parameters:

- caller (str): The path of the caller file (usually __file__).
- *args (str): One or more subfolder names and the final file name to be added to the path.
- create_folders (bool, optional): Whether to create missing folders in the path. Defaults to True.
- create_file (str, optional): The content to write to the file if it doesn't exist. Defaults to an empty string ("").
  Set to False if you don't want the file to be created automatically.

Returns:

- str: The constructed file path.

Raises:

- TypeError: If non-string values are passed as subfolder names or file name in `args`.
- OSError: If there are errors creating folders (e.g., permission issues).

Example Usage:

file_path = get_file_path(__file__, "results", "data.txt", create_file=":amigger: :and: :his: 👪")

with editfile(file_path) as f:
    content = f.read()
    print(content)  # output: ":amigger: :and: :his: 👪"
    """
    args = list(map(str, args))

    folder_dir = get_folder_path(caller, *args[:-1], create_folders=create_folders)
    filepath = os.path.join(folder_dir, args[-1])

    if create_file is not False and not os.path.exists(filepath):
        editfile(filepath).write(create_file)

    return filepath


def add_line(fp: str, line: str) -> None:
    """
Appends a line of text to the end of a file.

This function opens the specified file (fp) in append mode (a+)
and performs the following actions:

1. Checks if the file is not empty (has existing content).
2. If the file is not empty, appends a newline character to ensure the new line is added on a separate line.
3. Writes the provided line to the end of the file.

Parameters:

- fp (str): The filepath of the text file to modify.
- line (str): The line of text to append to the file.

Raises:

- OSError: If there are issues opening or writing to the file (e.g., permission issues).

Example Usage:

editfile("my_file.txt").write("This is the first line.")
add_line("my_file.txt", "This is the second line.")

print(("my_file.txt").read())
# Output: This is the first line.\nThis is the second line.
    """
    with smthfile(fp, "a+") as f:
        f.seek(0)
        if f.read():
            line = "\n" + line
        f.write(line)


def remove_line(fp: str, line: str) -> None:
    """
Removes a specific line of text from a file, if it exists.

This function opens the specified file (fp) and attempts to remove the provided
line if it's found within the file content. (won't remove duplicates)

How it Works:

1. Splits the file content into a list of lines.
2. Filters out the line that matches the provided line argument.
3. Joins the filtered lines back into a string with newline characters.
4. Writes the modified content (without the removed line) back to the file.

Parameters:

- fp (str): The filepath of the text file to modify.
- line (str): The exact line of text to remove from the file.

Raises:

- OSError: If there are issues opening or writing to the file (e.g., permission issues).

Example Usage:

remove_line("my_file.txt", "This is the first line")
print(openfile("my_file.txt").read())
# Output: This is the second line.
    """
    file = openfile(fp).read().split("\n")
    file.remove(line)
    editfile(fp).write("\n".join(file))


def listpaths(fp: str) -> list[str]:
    """
Retrieves a list of file paths within a specified directory.

This function takes a directory path (fp) as input and returns a list of
complete file paths (including the directory) for all files found within that directory.

Parameters:

- fp (str): The path to the directory for which you want to list file paths.

Returns:

- list[str]: A list containing the complete file paths for all files within the directory.

Raises:

- OSError: If there's an issue accessing the directory (e.g., permission issues, path not found).
    """
    return [os.path.join(fp, i) for i in os.listdir(fp)]


def generate_ip(name: str) -> str:
    """
generates random ip
    """
    import random
    random.seed(name)
    return ".".join([str(random.randint(0, 255)) for _ in range(4)])
