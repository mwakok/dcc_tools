import os
import argparse


def create_parser():
    """Create a CLI argument parser

    Returns
    -------
    args
        defined arguments for CLI
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.MetavarTypeHelpFormatter,
    )

    parser.add_argument(
        "--repo", type=str, required=True, help="name of the GitHub repository"
    )
    parser.add_argument(
        "--path", type=str, help="path to the folder with markdown files"
    )
    parser.add_argument(
        "--project", default="DCC Support", type=str, help="name of the project board"
    )
    parser.add_argument(
        "--owner",
        default=os.environ["GITHUB_USER"],
        type=str,
        help="GitHub username or organization name",
    )
    parser.add_argument(
        "--token",
        default=os.environ["GITHUB_TOKEN"],
        type=str,
        help="GitHub Personal Access Token",
    )
    parser.add_argument(
        "--columns",
        default=["To do", "In progress", "Done"],
        type=list,
        help="list of column names in project board",
    )
    parser.add_argument(
        "--issue_column", type=str, help="project board column to add issues to"
    )
    parser.add_argument("--loglevel", default="WARNING", type=str, help="loglevels")
    args = parser.parse_args()

    return args
