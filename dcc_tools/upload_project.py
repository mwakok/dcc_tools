from arg_parser import create_parser

from .logging_functions import _init_logger, set_logger_level
from .GithubAPI import GitHubAPI

# _init_logger()


def main(
    repo_name,
    path_issues,
    project_name,
    repo_owner,
    token,
    columns,
    issue_column,
    loglevel,
):

    set_logger_level(loglevel)

    repo = GitHubAPI(repo_name, repo_owner, token)
    repo.load_markdown_files(path_issues)
    repo.push_project(project_name, columns)
    repo.push_issues()
    repo.add_issues_to_project(project_name, issue_column)


if __name__ == "__main__":

    args = create_parser()

    main(
        repo_name=args.repo,
        path_issues=args.path,
        project_name=args.project,
        repo_owner=args.owner,
        token=args.token,
        columns=args.columns,
        issue_column=args.issue_column,
        loglevel=args.loglevel,
    )
