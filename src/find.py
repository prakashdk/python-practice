import sys
from typing import DefaultDict
import click
import os
from option import Option

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


def is_match_file(file, options):
    opt = Option(file)
    option_lookup = {
        "type": opt.match_by_type,
        "name": opt.match_by_name,
        "size": opt.match_by_size,
        "user": opt.match_by_user,
        "uid": opt.match_by_uid,
        "mtime": opt.match_by_mtime,
        "ctime": opt.match_by_ctime
    }
    for k, v in options.items():
        if v:
            option_lookup[k](v)
    return opt.is_match()


def find_files(files, options):
    """To find matching files using options"""
    return [file for file in files if is_match_file(file, options)]


def print_files(files):
    for file in files:
        print(file, os.stat(file).st_mtime)


def find(path, **options):
    files = get_files(path)
    match_files = find_files(files, options)
    print_files(match_files)


@click.command()
@click.argument("path", nargs=-1)
@click.option("-type", default="", help="determines the type of a file [f d l]")
@click.option("-name", default="", help="pattern for matching files or dirs")
@click.option("-size", default="", help="match the files with size")
@click.option("-user", default="", help="match the files with user")
@click.option("-uid", default="", help="match the files with user id", type=int)
@click.option("-mtime", default="", help="match the files with modification time")
@click.option("-ctime", default="", help="match the files with creation time")
def main(type, name, path, size, uid, user, mtime):
    for dir in path:
        find(dir, type=type, name=name, size=size.upper(),
             user=user, uid=uid, mtime=mtime)


if __name__ == "__main__":
    # try:
    main()
    # except Exception as e:
    # print(e)
