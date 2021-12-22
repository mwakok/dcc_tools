import os
from setuptools import setup

here = os.path.abspath(os.path.dirname("__file__"))

version = {}
with open(os.path.join(here, "src", "__version__.py")) as f:
    exec(f.read(), version)

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="GitHub_API",
    version=version["__version__"],
    description="",
    long_description=readme,
    long_description_content_type="text/md",
    url="https://github.com/mwakok/github_api",
    author="Maurits Kok",
    author_email="mwakok@gmail.com",
    license="Apache Software License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    test_suite="tests",
    install_requires=["requests>=2.24.0"],
)
