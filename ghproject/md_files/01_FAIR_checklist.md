---
title: Create FAIR software checklist
labels: ["documentation"]
---

# Checklist for FAIR research software

#### Version control with GitHub 
_Essential_  
- [x] Use [git](https://www.atlassian.com/git) as a version control system 
- [x] Upload your project on [GitHub](https://github.com/) or [TU Delft GitLab](https://gitlab.tudelft.nl/)

_Recommended_  
- [ ] Make your repository [public](https://coderefinery.github.io/social-coding/social_coding/)
- [ ] [Branch hygiene](https://coderefinery.github.io/git-branch-design/)
- [ ] Use a branching model ([GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow))
- [ ] [Meaningful commit messages](https://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines)


#### Documentation - Repository
_Essential_  
- [ ] Add [README](https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md)
- [ ] Add [LICENSE](https://doi.org/10.5281/zenodo.4629662)
- [ ] Add [CITATION](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

_Recommended_
- [ ] Read the [Divio documentation system](https://documentation.divio.com/)
- [ ] Make use of [Github issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [ ] Add [Contribution guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [ ] Add [Code of conduct](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)

#### Documentation - Software
_Essential_  
- [ ] Source code documentation ([docstrings](https://numpydoc.readthedocs.io/en/latest/format.html))
- [ ] Installation instructions
- [ ] Usage documentation
- [ ] Developer setup

_Recommended_  
- [ ] Examples and tutorials (Jupyter notebooks, videos, screencasts)
- [ ] Website ([github.io pages](https://pages.github.com/), [Readthedocs](https://readthedocs.org/), [JupyterBook](https://jupyterbook.org/intro.html)
- [ ] Build [API reference](https://developer.lsst.io/python/numpydoc.html) from docstrings


#### Testing
_Recommended_  
- [ ] [Defensive programming](https://swcarpentry.github.io/python-novice-inflammation/10-defensive/index.html)
- [ ] Integration or build test
- [ ] User installation test
- [ ] Unit tests (coverage >70%)
- [ ] Continuous integration (GitHub Actions)
- [ ] Code coverage check ([Codecov](https://about.codecov.io/), [Sonarcloud](https://sonarcloud.io/), [Travis](https://www.travis-ci.com/))


#### Releases
_Essential_  
- [ ] Obtain a DOI from ([Zenodo](https://zenodo.org/) or [4TU.ResearchData](https://data.4tu.nl/info/en/))

_Recommended_  
- [ ] [Semantic versioning](https://semver.org/)
- [ ] Tagged releases ([GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github))
- [ ] [CHANGELOG](https://keepachangelog.com/en/1.0.0/)
- [ ] Upload to registry ([PyPI](https://realpython.com/pypi-publish-python-package/), [conda](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html), [DockerHub](https://docs.docker.com/docker-hub/repos/#:~:text=To%20push%20an%20image%20to,docs%2Fbase%3Atesting%20))
- [ ] [Release guide](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [ ] Continuous Integration for build and release

#### Code quality
_Essential_
- [ ] Project [organisation](https://coderefinery.github.io/reproducible-research/02-organizing-projects/)
- [ ] Record [software dependencies](https://coderefinery.github.io/reproducible-research/03-dependencies/)

_Recommended_
- [ ] Follow [PEP8 guidelines](https://realpython.com/python-pep8/)
- [ ] Use linter (e.g. [pylint](https://pypi.org/project/pylint/), [flake8](https://pypi.org/project/flake8/))
- [ ] Use a formatter (e.g. [black](https://github.com/psf/black), [yapf](https://github.com/google/yapf))
- [ ] Follow [best coding practices](https://alan-turing-institute.github.io/rse-course/html/index.html)