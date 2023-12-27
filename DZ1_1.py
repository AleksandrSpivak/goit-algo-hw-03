import os
import shutil
from pathlib import Path


class WrongInputDirectoryError(Exception):
    pass


def copy_dir(path_input, path_output="dist"):
    if not Path(path_input).is_dir():
        raise WrongInputDirectoryError

    if not Path(path_output).is_dir():
        os.mkdir(path_output)

    children = Path(path_input).iterdir()

    for child in children:
        if child.is_dir():
            new_dir = os.path.join(Path(path_input), Path(child.name))
            copy_dir(new_dir, path_output)
        else:
            copy_file(child, path_output)


def copy_file(file_name, to_directory):
    ext_dir = Path(file_name).suffix.replace(".", "")
    path_output = os.path.join(Path(to_directory), Path(ext_dir))
    if not os.path.exists(path_output):
        os.mkdir(path_output)
    try:
        shutil.copy(file_name, path_output)
    except PermissionError:
        print(f"File {file_name} permission denied")


def parse_input(user_input):
    args = user_input.split()
    if args[0] == "":
        raise WrongInputDirectoryError
    else:
        input = args[0]
    if len(args) == 1:
        output = None
    else:
        output = args[1]
    return input, output, *args


if __name__ == "__main__":
    user_input = input("Enter input durectory [and output directory]\n")
    try:
        root_input, root_output, *args = parse_input(user_input)
        if root_output == None:
            copy_dir(root_input)
            print(
                f"Files were copied from '{root_input}' directory to 'dist' directory"
            )
        else:
            copy_dir(root_input, root_output)
            print(
                f"Files were copied from '{root_input}' directory to '{root_output}' directory"
            )
    except (ValueError, IndexError, FileNotFoundError, WrongInputDirectoryError):
        print("Wrong input")
