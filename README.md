# Collection of Digital Competence Center support tools

## Documentation for users

### Installation

I recommend installing the tool inside a conda environment:

```bash
git clone https://github.com/mwakok/dcc_tools.git
cd dcc_tools
conda env create -f environment.yml
conda activate dcc_tools
pip install -e .
```

### Usage

#### Create a GitHub project with issues

You can call the module to upload a new project to a GitHub reposotory from the terminal. To 

```bash
python -m  dcc_tools.github.upload_project -h
```

An example would be

```bash
python -m dcc_tools.github.upload_project --repo "my_repository" --loglevel "INFO" --columns ["Backlog", "To do", "In progress", "Done"]
```

Using the GitHub API requires a Personal Access Token, which can be created via your GitHub settings. 

Example usage in a 

```python
import os

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

Copyright (c) 2021, Maurits Kok

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.