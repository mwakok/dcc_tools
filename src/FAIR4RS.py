import sys
import os
from requests import request
import json
import glob
import time

from .utils import convert_md


def main(
    repository,
    repo_owner=None,
    path_issues="../issues/*.md",
    project_name="FAIR Software",
    columns=["To do", "In progress", "Done"],
):
    """Create a project board with issues in a GitHub repository

    Function requires the presence of local environement variables:
    "GITHUB_USER" - GitHub username
    "GITHUB_TOKEN" - Check Personal Access Token in the Settings/Developer Settings within your GitHub profile

    Parameters
    ----------
    repository : str
        Name of the repository in which to create a project board with issues
    repo_owner : str
        Name of the repository owner. Value will default to GITHUB_USER.
    path_issues : str
        Path to directory containing markdown files that will be converted into issues.
        The first line of the markdown file will become the issue title (can be preceeded by a #).
        This remainder of the markdown file will be converted into the issue body.
    project_name : str
        Name of the project board to be created. Default is "FAIR Software".
    columns : list
        Sorted list of columns to be created in the project board. 
        Issues will automatically be moved to the first column.
        Default is ["To do", "In progress", "Done"]
    """

    # GitHub authentication
    username = os.environ["GITHUB_USER"]
    token = os.environ["GITHUB_TOKEN"]

    # The repository to add a project and issues to
    if not repo_owner:
        repo_owner = username
    repo_name = repository

    # Authentication settings
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    id_column = create_project(repo_owner, repo_name, headers, project_name, columns)

    # Get paths to local markdown files
    files = glob.glob(path_issues)

    titles = create_issues(repo_owner, repo_name, headers, files)

    # Get issue id's from Github repository.
    # While loop requried to deal with delay in posting issues
    id_issues = []
    while len(id_issues) != len(titles):
        time.sleep(1)
        id_issues = get_issues(
            repo_owner=repo_owner,
            repo_name=repo_name,
            issue_titles=titles,
            headers=headers,
        )

    move_issues_to_project(headers, id_column, id_issues)


def create_project(
    repo_owner,
    repo_name,
    headers,
    project_name,
    columns=["To do", "In progress", "Done"],
):
    """Create a project board in a GitHub repository

    Parameters
    ----------
    repo_owner : str
        Name of the repository owner
    repo_name : str
        Name of te repository
    headers : dict
        Dictionary of authentication details
    project_name : str
        Name of the project board
    columns : list
        Sorted list of columns to be created in the project board. 
        Issues will automatically be moved to the first column.
        Default is ["To do", "In progress", "Done"]

    Returns
    -------
    list
        List of column id's
    """

    url_project = f"https://api.github.com/repos/{repo_owner}/{repo_name}/projects"

    data = {"name": project_name}
    payload = json.dumps(data)
    r = request("POST", url=url_project, data=payload, headers=headers)
    id_project = json.loads(r.content)["id"]

    # Create columns
    url_columns = f"https://api.github.com/projects/{id_project}/columns"
    columns = ["To do", "In progress", "Done"]

    for column in columns:
        data = {"name": column}
        payload = json.dumps(data)
        r = request("POST", url=url_columns, data=payload, headers=headers)
        if column == "To do":
            id_column = json.loads(r.content)["id"]

    return id_column


def create_issues(repo_owner, repo_name, headers, files):
    """Post issues on GitHub repository from local markdown files

    Parameters
    ----------
    repo_owner : str
        Name of the repository owner
    repo_name : str
        Name of te repository
    headers : dict
        Dictionary of authentication details
    files : list
        List of local markdown file that will be converted into issues

    Returns
    -------
    list
        List of issue titles created in the GitHub repository
    """

    url_post_issues = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/import/issues"
    )
    titles = []
    labels = ["documentation", "DCC Support"]

    for file in files:
        [title, contents] = convert_md(file)
        titles.append(title)
        data = {
            "issue": {
                "title": title,
                "body": contents,
                "closed": False,
                "labels": labels,
            }
        }
        payload = json.dumps(data)
        r = request("POST", url=url_post_issues, data=payload, headers=headers)
        assert r.status_code == 202, f"Could not upload issue '{title}'"

    return titles


def get_issues(repo_owner, repo_name, headers, issue_titles):
    """Get issue id from GitHub repository from issue titles

    Parameters
    ----------
    repo_owner : str
        Name of the repository owner
    repo_name : str
        Name of te repository
    headers : dict
        Dictionary of authentication details
    titles : list
        List of issue titles to retrieve from Github repository
    

    Returns
    -------
    list
        List of issue id numbers
    """

    id_issues = []
    url_get_issues = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    r = request("GET", url_get_issues, headers=headers)
    issues = json.loads(r.content)

    for issue in issues:
        if issue["title"] in issue_titles:
            id_issues.append(issue["id"])

    return id_issues


def move_issues_to_project(headers, id_column, id_issues):
    """Move specific issues to a specific column in a project board

    Parameters
    ----------
    headers : dict
        Dictionary of authentication details
    id_column : [type]
        [description]
    id_issues : [type]
        [description]
    """

    url_cards = f"https://api.github.com/projects/columns/{id_column}/cards"
    for id in id_issues:
        data = {"content_type": "Issue", "content_id": id}
        payload = json.dumps(data)
        r = request("POST", url=url_cards, data=payload, headers=headers)


if __name__ == "__main__":
    assert len(sys.argv) >= 2, "Please provide a repository name"
    main(repository=sys.argv[1])

