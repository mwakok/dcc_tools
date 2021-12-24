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
        "--repo",
        type=str,
        required=True,
    )
    parser.add_argument("--path", type=str, required=True)
    parser.add_argument("--project", default="DCC Support", type=str)
    parser.add_argument("--owner", default=os.environ["GITHUB_USER"], type=str)
    parser.add_argument("--token", default=os.environ["GITHUB_TOKEN"], type=str)
    parser.add_argument(
        "--columns", default=["To do", "In progress", "Done"], type=list
    )
    parser.add_argument("--issue_column", default="To do", type=str)
    parser.add_argument("--loglevel", default="WARNING", type=str)
    args = parser.parse_args()

    return args
