# Contributing guidelines

## You want to make a new release of the code base

To create release you need write permission on the repository.

1. Check author list in `citation.cff` and `.zenodo.json` files
1. Bump the version using `bump2version <major|minor|patch>`. For example, `bump2version major` will increase major version numbers everywhere its needed (code, meta, etc.) in the repo.
1. Update the `CHANGELOG.md` to include changes made
1. Goto [GitHub release page](https://github.com/mwakok/ghproject/releases)
1. Press draft a new release button
1. Fill version, title and description field
1. Press the Publish Release button
1. Wait until [PyPi publish workflow](https://github.com/mwakok/ghproject/actions/workflows/publish_pypi.yml) has completed
1. Verify new release is on [PyPi](https://pypi.org/project/ghproject/#history)

Also a Zenodo entry will be made for the release with its own DOI.