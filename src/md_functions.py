import os
import glob
import logging
import frontmatter

logger = logging.getLogger("gh_project")


def load_markdown_files(path: str):
    """Load markdown files for uploading as issues

    Parameters
    ----------
    path : str
        Path to markdown files
    """

    files = glob.glob(f"{path}/*.md")
    issues = []

    if not files:
        logger.warning(f"No markdown files found in {path}")
    else:

        for file in files:
            with open(file, "r") as f:
                issues.append(frontmatter.load(f))
                logger.info(
                    f"Issue '{issues[-1]['title']}' imported from file '{os.path.basename(file)}'"
                )

    return issues


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
