"""
name: DAS Readability Checker
license: Copyright (C) 2024 Novo Nordisk A/S
author: LZVB <lzvb@novonordisk.com>
file: readability.py

Checks the readability of markdown files in a directory and its subdirectories.
It uses the textstat library to calculate the SMOG Index and Flesch Reading Ease score.
The SMOG Index is chosen due to its general application in the healthcare industry.
The Flesch Reading Ease score is chosen due to its wide and storied use.
The script outputs a table of the results, including the file name, SMOG Index, and
Flesch Reading Ease score.

CLI Arguments:

--directory (required) argument is required and specifies the directory to search for .md files.
--show-all argument can be used to show scores for all files, even if they meet the
desired readability levels.
--ignore argument can be used to specify directories to ignore.
--verbose argument can be used to print the content that is being evaluated.
--smog argument can be used to specify the SMOG Index threshold.
--flesch argument can be used to specify the Flesch Reading Ease threshold.

The reasoning for creating this script is to ensure that the documentation and
communication materials are easily understood by the intended audience.
Intended audience for most of DAS documentation is IT Professionals, so the readability
should be at the level of an undergraduate student or higher.

Unfortunately, the textstat library does not report on the words or structures that are
causing the readability issues. This would be a useful feature to add in the future.
"""

from argparse import ArgumentParser
from fnmatch import fnmatch
from os import path, sep, walk
from re import DOTALL, sub

from bs4 import BeautifulSoup
from prettytable import PrettyTable
from textstat import textstat

from markdown import markdown

def _find_md_files(directory: str, ignore: list[str]) -> list[str]:
    """
    Finds all .md files in the directory and its subdirectories.
    """
    md_files = []
    for root, dirs, files in walk(directory):
        dirs[:] = [dir for dir in dirs if dir not in ignore]
        for basename in files:
            if fnmatch(basename, "*.md"):
                filename = path.join(root, basename)
                md_files.append(filename)
    return md_files


"""
The following regular expressions are used to remove markdown elements from the content.
We define them here close to their usage but not in the function as to not spend
time compiling them on every function call.
"""
_links = r"\[.*?\]\(.*?\)"
_linked_images = r"\!\[.*?\]\(.*?\)"
_linked_images_with_hyperlinks = r"\[!\[.*?\]\(.*?\)\]\(.*?\)"
_code_blocks = r"```.*?```"
_inline_code = r"`.*?`"


def _raw_text_extract(content: str) -> str:
    """
    Extracts the raw text from a markdown file.
    This is done by removing all links, images, code blocks, and inline code then
    transforming the markdown to HTML and extracting the text from the HTML.
    We need to remove the links, images, and code blocks because they are not to be
    included in the textstat calculation and would skew the results.
    There might be more markdown elements that need to be removed, but this is a start.
    """
    content = sub(_linked_images, "", content)
    content = sub(_linked_images_with_hyperlinks, "", content)
    content = sub(_links, "", content)
    content = sub(_code_blocks, "", content, flags=DOTALL)
    content = sub(_inline_code, "", content, flags=DOTALL)

    html = markdown(content)

    soup = BeautifulSoup(html, features="html.parser")
    text = soup.get_text()
    return text


def _evaluate_files(
    md_files: list[str],
    directory: str,
    verbose: bool,
    smog: int,
    flesch: int,
    show_all: bool,
) -> PrettyTable:
    """
    Evaluates the readability of the markdown files and returns a table of the results.
    The table includes the file name, SMOG Index, and Flesch Reading Ease score.
    """
    print(f"SMOG Index: Below {smog}")
    print(f"Flesch Reading Ease: Above {flesch}\n")

    table = PrettyTable()
    table.align = "l"
    table.field_names = ["File", "SMOG", "Flesch"]

    for file in md_files:
        relative_file = file.replace(directory + sep, "")
        with open(file, "r") as file_handle:
            content = file_handle.read()
            text = _raw_text_extract(content)
            flesch_score = textstat.flesch_reading_ease(text)
            smog_score = textstat.smog_index(text)
            if show_all or smog_score > smog or flesch_score < flesch:
                table.add_row([relative_file, smog_score, flesch_score])
                if verbose:
                    print(f"Content of {relative_file}:\n{text}\n")

    return table


parser = ArgumentParser()
parser.add_argument(
    "--directory", "-d", required=True, help="The directory to search for .md files"
)
parser.add_argument(
    "--show-all",
    "-a",
    action="store_true",
    default=False,
    help="Show scores for all files, even if they meet the desired readability levels",
)
parser.add_argument(
    "--ignore",
    "-i",
    action="append",
    default=["node_modules", ".venv", "cdk.out", ".pytest_cache", ".git"],
    help="Directories to ignore",
)
parser.add_argument(
    "--verbose",
    "-v",
    action="store_true",
    help="Print the content that is being evaluated",
)

_smog_undergraduate = 13
_flesch_college = 30

parser.add_argument(
    "--smog", "-s", type=int, default=_smog_undergraduate, help="SMOG Index threshold"
)
parser.add_argument(
    "--flesch",
    "-f",
    type=int,
    default=_flesch_college,
    help="Flesch Reading Ease threshold",
)


def main():
    """
    Main entry point for the script.
    Parses the command line arguments and evaluates the files.
    """
    try:
        args = parser.parse_args()

        if not path.isdir(args.directory):
            print(f"Error: The directory {args.directory} does not exist.")
            exit(1)

        absolute_directory = path.abspath(args.directory)
        md_files = _find_md_files(absolute_directory, ignore=args.ignore)

        if not md_files:
            print(f"Warning: No .md files found in the directory {args.directory}.")
            exit(0)

        evaluation = _evaluate_files(
            md_files,
            directory=absolute_directory,
            verbose=args.verbose,
            smog=args.smog,
            flesch=args.flesch,
            show_all=args.show_all,
        )

        readability_levels_are_good = len(evaluation._rows) == 0

        if readability_levels_are_good:
            print("SUCCESS: All files meet the desired readability levels.")
        else:
            print(evaluation)

        if not args.show_all:
            exit_code = 1 if len(evaluation._rows) > 0 else 0
            exit(exit_code)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit(1)
