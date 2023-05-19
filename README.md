# BatCave Python Module

A useful collection of tools for writing Python programs.

## Developing

Development is best accomplished using virtualenv or virtualenv-wrapper where a virtual environment can be generated:

    mkvirtualenv batcave
    python -m pip install -U pip
    pip install -U setuptools wheel

## Testing

### Static Analysis

The static analysis tools can be installed with

    pip install -U -e .[stest]

The static analysis test can be run with

    pylint batcave
    flake8 batcave
    mypy batcave

### Unit Tests

The unit testing tools can be installed with

    pip install -U -e .[utest]

The unit tests can be run with

    python -m xmlrunner discover -o unit_test_results

## Building

Building is performed by changing to the Build directory and running the build.py script which will perform two actions

1. run the unit tests and place the results in Build/unit_test_results/junit.xml
1. run the setup.py to create a PyPi distribution in Build/artifacts

## Publishing a Release

This is the procedure for releasing BatCave

1. Validate all issues are "Ready for Release"
1. Update CHANGELOG.rst
1. Run publish job
1. Validate GitHub release
1. Validate PyPi
1. Move issues to "Closed"
1. Close Milestone

<!--- cSpell:ignore virtualenv mkvirtualenv batcave stest mypy xmlrunner -->
