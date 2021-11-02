import sys
import click
import os
from fnmatch import fnmatch
from pathlib import Path

"""
UNIX `find` command using Python
Usage:
    The `find` command is used to find files matching given conditions at the specified path.
Synopsis
    find [-type] [-name] [-user] [expression]
"""


def get_arguments():
    """To check if the arguments provided or not and returns it"""
    if len(sys.argv) > 2:
        return sys.argv[1:]
    raise Exception("No arguments provided")


def tolist(dir):
    all_files = []
    for basedir, subdirs, files in dir:
        for subdir in subdirs:
            all_files.append(basedir+"\\"+subdir)
        for file in files:
            all_files.append(basedir+"\\"+file)
    return all_files


def get_files(dir):
    if os.path.isdir(dir):
        return tolist(os.walk(dir))
    elif os.path.isfile(dir):
        return [dir]
    else:
        print(f"No such file or directory '{dir}'")
        return []


def is_valid_type(file, type):
    if type == 'a':
        return True
    filetypes = {
        "d": os.path.isdir,
        "f": os.path.isfile,
        "l": os.path.islink,
    }
    return filetypes[type](file) if type in filetypes else False


def find_files(files, type, pattern):
    return [file for file in files if (fnmatch(file, pattern) or pattern in file) and is_valid_type(file, type)]


def print_files(files):
    for file in files:
        print(os.stat(file))
        print(Path(file).owner())

def find(type, name, path):
    files = get_files(path)
    match_files = find_files(files, type, name)
    print_files(match_files)


@click.command()
@click.argument("path", nargs=-1)
@click.option("-type", default="a", help="determines the type of a file")
@click.option("-name", default="", help="pattern for matching files or dirs")
def main(type, name, path):
    for dir in path:
        find(type, name, dir)

if __name__ == "__main__":
    # try:
    main()
    # except Exception as e:
    # print(e)
