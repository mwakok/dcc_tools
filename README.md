# Tool for uploading creating project boards on GitHub

`ghproject` is a tool for uploading project boards to GitHub filled with labelled issues. This has been created to aid project management for consulting in research software projects on GitHub. The package comes with default values and default issues that upload a projecy board containing issues to implement FAIR for research software.

## Documentation for users

### Installation

I recommend installing the tool inside a conda environment:

```bash
git clone https://github.com/mwakok/ghprojects.git
cd ghproject
conda env create -f environment.yml
conda activate ghproject
pip install .
```

### Usage

The tool can be used both from the command line and from a Python interpretor, e.g. a Jupyter notebook. We take as an example the following use case in which we want to upload a project board with accompanying issues. Issues are generated from markdown files that need to contain a header with the issue title and associated labels (as a list of strings). 

```yml
---
title: Create FAIR software checklist
labels: ["documentation", "feature"]
---
```

The issue body is then created from the following markdown text. Examples of issues can be found in the folder `/md_files` in the repository.

You can call the module to upload a new project to a GitHub reposotory from the command line. Use to following command to view the help file:

```bash
python -m  ghproject.upload_project -h
```

To upload a project board to an existing repository from the command line, use:

```bash
python -m ghproject.upload_project --repo "my_repository" --owner "username" --path "./md_files" --project "My project" --columns ["Backlog", "To do", "In progress", "Done"]
```

Using the GitHub API requires a Personal Access Token (PAT), which can be created via your [GitHub settings](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). To prevent hardcoding of any access tokens, it's a best practice to keep your GitHub PAT as a local environment variable. By default, the package will inspect the environment variable `GITHUB_TOKEN` for the argument `--token`.

The various functions can also be accessed directly from the GitHubAPI class. Example usage would be:

```python
import os
from ghproject import GitHubAPI, init_logger

# Initialize logger
init_logger()

# Setup arguments
repo_name = "my_repository"
repo_owner = "username" # Github user name or organization name
token = os.environ["GITHUB_TOKEN"]
path_issues = "./md_files"
project_name = "My project"

repo = GitHubAPI(repo_name, repo_owner, token)
repo.load_markdown_files(path_issues)
repo.push_project(project_name)
repo.push_issues()
repo.add_issues_to_project(project_name)
```


## License

Copyright (c) 2022, Maurits Kok

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.