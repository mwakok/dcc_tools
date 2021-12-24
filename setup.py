import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname("__file__"))

version = {}
with open(os.path.join(here, "dcc_tools", "__version__.py")) as f:
    exec(f.read(), version)

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="dcc_tools",
    version=version["__version__"],
    description="Tool to create GitHub project boards with issues",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mwakok/dcc_tools",
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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    test_suite="tests",
    packages=find_packages(exclude=["*tests*"]),
    python_requires=">=3.7,<3.9",
    install_requires=["python-frontmatter", "requests>=2.24.0"],
)
