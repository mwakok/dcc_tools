import os
import glob
import logging

logger = logging.getLogger("gh_project")


def load_markdown_files(path: str):
    """Load markdown files for uploading as issues

    Parameters
    ----------
    path : str
        Path to markdown files
    """

    files = glob.glob(f"{path}/*.md")
    markdown = {}

    if not files:
        logger.warning(f"No markdown files found in {path}")
    else:

        for file in files:
            [title, contents] = convert_md(file)
            markdown[title] = contents
            logger.info(
                f"Issue '{title}' imported from file '{os.path.basename(file)}'"
            )

    return markdown


def convert_md(file):
    """Convert markdown file for issue creation on GitHub.
    The first line of the markdown file will become the issue title (can be preceeded by a #), while
    the remainder of the markdown file will be converted into the issue body.

    Parameters
    ----------
    file : str
        Path to markdown file

    Returns
    -------
    [type]
        [description]
    """

    with open(file, "r") as f:
        text = f.read()

        # Get title
        title = text.split("\n", 2)[:1]
        title = title[0].replace("# ", "")

        # Remove title from content and store
        contents = text.split("\n", 2)[2]

    return title, contents

