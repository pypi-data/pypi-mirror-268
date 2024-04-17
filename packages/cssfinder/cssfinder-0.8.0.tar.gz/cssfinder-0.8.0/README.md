<p align="center">
   <img width="400" src="https://github.com/Argmaster/CSSFinder/assets/56170852/e84ee4e7-711e-405e-ab41-49ca24c7a350" alt="" />
</p>

<h1 align="center"> CSSFinder </h1>

<p align="center">
  <a href="https://github.com/Argmaster/CSSFinder/releases/"><img src="https://img.shields.io/github/v/release/Argmaster/cssfinder?style=flat" alt="GitHub release"></a>
  <a href="https://github.com/Argmaster/CSSFinder/releases"><img src="https://img.shields.io/github/release-date/Argmaster/cssfinder" alt="GitHub Release Date - Published_At"></a>
  <a href="https://pypi.org/project/cssfinder"><img src="https://img.shields.io/pypi/v/cssfinder?style=flat" alt="PyPI release"></a>
  <a href="https://pypi.org/project/cssfinder/"><img src="https://img.shields.io/pypi/dm/cssfinder.svg?label=PyPI%20downloads" alt="PyPI Downloads"></a>
  <a href="https://pypi.org/project/cssfinder"><img src="https://img.shields.io/pypi/pyversions/cssfinder?style=flat" alt="Supported Python versions"></a>
  <a href="https://pypi.org/project/cssfinder"><img src="https://img.shields.io/pypi/implementation/cssfinder?style=flat" alt="Supported Python implementations"></a>
  <a href="https://github.com/argmaster/cssfinder/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Argmaster/cssfinder" alt="license_mit"></a>
  <a href="https://github.com/Argmaster/CSSFinder/pulls"><img src="https://img.shields.io/github/issues-pr/Argmaster/cssfinder?style=flat" alt="Pull requests"></a>
  <a href="https://github.com/Argmaster/CSSFinder/issues"><img src="https://img.shields.io/github/issues-raw/Argmaster/cssfinder?style=flat" alt="Open issues"></a>
  <a href="https://github.com/Argmaster/CSSFinder"><img src="https://img.shields.io/github/repo-size/Argmaster/cssfinder" alt="GitHub repo size"></a>
  <a href="https://github.com/Argmaster/CSSFinder"><img src="https://img.shields.io/github/languages/code-size/Argmaster/cssfinder" alt="GitHub code size in bytes"></a>
  <a href="https://github.com/Argmaster/CSSFinder"><img src="https://img.shields.io/github/stars/Argmaster/cssfinder" alt="GitHub Repo stars"></a>
  <a href="https://python-poetry.org/"><img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" alt="Poetry"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style"></a>
</p>

## CSSFinder - Closest Separable State Finder

CSSFinder is a software designed to find the closest separable state (CSS) for
a given quantum state. This helps in quantifying entanglement and classifying
quantum states as entangled or separable.

This software has been designed in a modular way. This is manifested by the
separation of the main part, which contains the user interface and modularity
support elements, from the algorithm implementation. The main part was written
in Python and uses the mechanisms of Python modules. Since it is possible to
craft shared libraries in such a way that Python imports them as native modules
any compiled language can be used to create highly optimized implementations of
desired algorithms. Such implementations are called backends and they use
minimalistic interface to interact with main part of the program.

In parallel with the development of this main part, two implementations of the
algorithm were created:

- `cssfinder_backend_numpy` - based on Python NumPy library implementing highly
  optimized multidimensional arrays and linear algebra.
- `cssfinder_backend_rust` - based on Rust ndarray crate which is an equivalent
  of NumPy from Rust language world.

Development of those two implementations allowed us to better understand limits
of what can and what can not become faster.

## Documentation

CSSFinder online documentation can be found
[here](https://argmaster.github.io/CSSFinder/latest/).

## Installation

To install CSSFinder from PyPI, use `pip` in terminal:

```
pip install cssfinder
```

You will have to also install a `backend` package, which contains concrete
implementation of algorithms. Simples way is to just install `numpy` or `rust`
extras set:

```
pip install cssfinder[numpy]
```

```
pip install cssfinder[rust]
```

For more detailed description of installation process visit CSSFinder
[online documentation](https://argmaster.github.io/CSSFinder/latest/usage/00_installation_guide.md).

## Quick start guide

For quick start guide please visit
[Quick Start Guide](https://argmaster.github.io/CSSFinder/latest/usage/01_quick_start.md)
in CSSFinder online documentation.

## Command line interface

To display command line interface map use following command:

```
cssfinder show-command-tree
```

Output should look similar to this:

```log
 ...cssfinder show-command-tree
main                           - CSSFinder is a script for finding closest separable states.
├── clone-example              - Clone one of examples to specific location.
├── create-new-json-project    - Create new JSON based project directory `<name>` in current working directory.
├── create-new-python-project  - Create new Python based project directory `<name>` in current working
├── list-backends              - List available backends.
├── list-examples              - Show list of all available example projects.
├── project                    - Group of commands for interaction with projects.
│   ├── add-gilbert-task       - Add new gilbert algorithm task.
│   ├── create-json-summary    - Load and display project.
│   ├── create-task-report     - Create short report for task.
│   ├── inspect                - Load project from PROJECT_PATH and display its contents.
│   ├── inspect-output         - Load project from PROJECT_PATH and display output of task specified by
│   ├── inspect-tasks          - Load project from PROJECT_PATH and inspect configuration of tasks specified by
│   ├── list-tasks             - Load project from PROJECT_PATH and list names of all tasks defined.
│   ├── run-tasks              - Run tasks from the project.
│   └── to-python              - Load project from JSON_PROJECT_PATH and convert it to Python based project.
└── show-command-tree          - Show the command tree of your CLI.
```

## Development

For development guidelines please visit
[Development](https://argmaster.github.io/CSSFinder/latest/development/00_setup.md)
in CSSFinder online documentation.
