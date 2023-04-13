#!/usr/bin/env python3
from subprocess import check_output, CalledProcessError
import os
from datetime import datetime


def root():
    """returns the absolute path of the repository root"""
    try:
        base = check_output(["git", "rev-parse", "--show-toplevel"])
    except CalledProcessError:
        raise OSError("Current working directory is not a git repository")
    return base.decode("utf-8").strip()


def abspath(relpath):
    """returns the absolute path for a path given relative to the root of
    the git repository
    """
    return os.path.join(root(), relpath)


def add_to_git(file_path):
    """adds a file to git"""
    try:
        base = check_output(["git", "add", file_path])
        base = check_output(["git", "update-index", "--add", file_path])
    except CalledProcessError:
        raise OSError("Current working directory is not a git repository")
    return base.decode("utf-8").strip()


# def update_index():
#     try:
#         base = check_output(["git", "update-index", "-z", "--index-info"])
#     except CalledProcessError:
#         raise OSError("Current working directory is not a git repository")
#     return base.decode("utf-8").strip()


def main():
    file_path = abspath("src/django_project/last-update.txt")
    with open(file_path, "w") as f:
        f.write(datetime.now().strftime("%Y%m%d%H%M%S"))
    add_to_git(file_path)


if __name__ == "__main__":
    main()
