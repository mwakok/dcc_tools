def convert_md(file):
    """Prepare markdown file for issue creation on GitHub

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

