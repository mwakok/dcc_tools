import os
import glob
from requests import request
import json

from utils import convert_md


class GitHubAPI:
    """Create a project board with issues in a GitHub repository
    """

    def __init__(
        self, repo_name: str, repo_owner: str, github_token: str,
    ):
        """[summary]

        Parameters
        ----------
        repo_name : str
            Name of the repository
        repo_owner : str
            Name of the organization or GitHub user that owns the repository
        github_token : str
            GitHub Personal Access Token
        """
        self.repo_name = repo_name
        self.repo_owner = repo_owner
        self.headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.base_url = (
            f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        )
        self.verify_authentication(self.base_url, self.headers)

    def get_issues(self):
        url = f"{self.base_url}/issues"
        r = self.get_request(url, self.headers)
        self.issues = {issue["title"]: issue["id"] for issue in r}

    def get_projects(self):
        url = f"{self.base_url}/projects"
        r = self.get_request(url, self.headers)
        self.projects = {project["name"]: project["id"] for project in r}

    def import_markdown(self, path):
        """Path to directory containing markdown files that will be converted into issues.
        The first line of the markdown file will become the issue title (can be preceeded by a #), while
        the remainder of the markdown file will be converted into the issue body.

        Parameters
        ----------
        path : str
            Path to local directory with markdown files
        """
        self.markdown = {}
        files = glob.glob(f"{path}/*.md")
        for file in files:
            [title, contents] = convert_md(file)
            self.markdown[title] = contents
            print(f"Issue '{title}' imported from file '{os.path.basename(file)}'")

    def push_project(self, project_name, columns=["To do", "In progress", "Done"]):
        """Push project to GitHub repository

        Parameters
        ----------
        project_name : str
            Name of the project
        columns : list, optional
            List of column names to be created in the project board, defaults to ["To do", "In progress", "Done"]

        """
        url = f"{self.base_url}/projects"

        # Check if project exists on GitHub
        self.get_projects()
        if bool(self.projects):
            if project_name in self.projects.keys():
                print(f"Project '{project_name}' already exists")
                return
        else:
            data = {"name": project_name}
            r = self.post_request(url, data, self.headers)
            id_project = r["id"]

            # Add columns
            url = f"https://api.github.com/projects/{id_project}/columns"
            for column in columns:
                data = {"name": column}
                r = self.post_request(url, data, self.headers)
                if column == columns[0]:
                    self.id_column = r["id"]

    def push_issues(self, labels=["documentation"]):
        """Upload issues to GitHub repository

        Parameters
        ----------
        labels : list, optional
            List of issue labels, by default ["documentation"]
        """
        url = f"{self.base_url}/import/issues"

        self.get_issues()

        for title, body in self.markdown.items():
            data = {
                "issue": {
                    "title": title,
                    "body": body,
                    "closed": False,
                    "labels": labels,
                }
            }
            # Check if issue exists
            if title not in self.issues.keys():
                self.post_request(url, data, self.headers)
                print(f"Issue '{title}' uploaded")
            else:
                print(f"Issue '{title}' already exists")

    def move_issues_to_project(self, project_name, column_name="To do"):

        # Get column ids
        columns = self.get_columns(project_name)
        assert (
            column_name in columns.keys()
        ), "Cannot find column_name in the columns of the project board"
        id_column = columns[column_name]
        url = f"https://api.github.com/projects/columns/{id_column}/cards"

        # Only move issues if all uploaded issues are present on GitHub
        self.get_issues()
        if set(self.markdown.keys()).issubset(self.issues.keys()):
            issue_ids = [self.issues[name] for name in self.markdown.keys()]
            for id in issue_ids:
                data = {"content_type": "Issue", "content_id": id}
                self.post_request(url, data, self.headers)
        else:
            print(
                "Cannot find all issues on GitHub, process could be delayed. Please try again."
            )

    def get_columns(self, project_name):
        """Get column names and id's from a project

        Parameters
        ----------
        project_name : str
            Name of the project board

        Returns
        -------
        dict
            Dictionary with [column_name:column_id] as [key:value]
        """
        self.get_projects()
        assert bool(self.projects), f"Cannot find project {project_name}"

        if project_name in self.projects.keys():
            project_id = self.projects[project_name]
            url = f"https://api.github.com/projects/{project_id}/columns"
            r = self.get_request(url, self.headers)
            columns = {column["name"]: column["id"] for column in r}
            return columns
        else:
            print(f"Cannot find project {project_name}")
            return None

    @staticmethod
    def post_request(url, data, headers):
        payload = json.dumps(data)
        r = request("POST", url=url, data=payload, headers=headers)
        if r.status_code in [201, 202]:
            print("Successfully posted the request")
            return json.loads(r.content)
        else:
            print("Could not post the request:", r.status_code)
            print("Response:", json.loads(r.content))

    @staticmethod
    def get_request(url, headers):
        r = request("GET", url=url, headers=headers)
        if r.status_code == 200:
            return json.loads(r.content)
        else:
            print("Could not get content", r.status_code)
            print("Response:", json.loads(r.content))
            return None

    @staticmethod
    def get_base_url(repo_owner, org_name, repo_name):
        if repo_owner is None and org_name is not None:
            return f"https://api.github.com/orgs/{org_name}/repos/{repo_name}"
        elif org_name is None and repo_owner is not None:
            return f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        else:
            print("Cannot determine repo_owner or org_name")
            return None

    @staticmethod
    def verify_authentication(url, headers):
        r = request("GET", url=url, headers=headers)
        if r.status_code == 200:
            print(f"Authentication successful to {url}")
        else:
            print(f"Could not connect to {url}: {r.status_code}")
            print("Response", json.loads(r.content))

