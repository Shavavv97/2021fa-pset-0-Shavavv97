# Pset 0

[![Build Status](https://app.travis-ci.com/Shavavv97/2021fa-pset-0-Shavavv97.svg?token=BpfqDuqzLeqjoC5Nr4Mq&branch=main)](https://app.travis-ci.com/Shavavv97/2021fa-pset-0-Shavavv97)

[![Maintainability](https://api.codeclimate.com/v1/badges/1e6b7da5329c891ef428/maintainability)](https://codeclimate.com/github/Shavavv97/2021fa-pset-0-Shavavv97/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/1e6b7da5329c891ef428/test_coverage)](https://codeclimate.com/github/Shavavv97/2021fa-pset-0-Shavavv97/test_coverage)

# Objectives
In this problem set you will:

* Use conda and Pipenv to build an deterministic environment
* Implement a basic CI/CD cycle using Travis and Code Climate
* Explore the use of badges in your repository
* Dip your toes in the most basic prediction method: linear regression

This problem set is designed to be solvable with minimal prep work.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Pset 0](#pset-0)
- [Objectives](#objectives)
- [Before you begin](#before-you-begin)
  - [Setup a Repeatable Environment](#setup-a-repeatable-environment)
  - [Installing miniconda (for macOS)](#installing-miniconda-for-macos)
  - [Installing pipenv](#installing-pipenv)
      - [Usage (not critical for this pset)](#usage-not-critical-for-this-pset)
  - [Problems](#problems)
    - [Build badges](#build-badges)
    - [Lineal Models](#lineal-models)
    - [Submit!](#submit)
    - [Testing Quality](#testing-quality)
    - [Test Coverage](#test-coverage)
    - [Git History](#git-history)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Before you begin
*Add your build and code climate badges* to the top of this README, using the markdown template for your master branch. 

## Setup a Repeatable Environment

Python is cool but could lead to dependency hell very quickly. 

As a Software Engineers, we want to avoid such kind of situations by setting up a deterministic environment that can be replicated every time. 

As a good practice, you WANT to have a virtual environment per project (e.g. per each problem set in this course), so this way would be easier to manage specific dependencies. 

For that, we're going to use the following trick:

1.- Create a Conda Virtual Enviroment
2.- Within the Conda Environment, use pipenv to manage dependencies 

Rather than using a requirements.txt, we will use [pipenv](https://pipenv.pypa.io/en/latest/) to give us a pure, repeatable, application environment.

## Installing miniconda (for macOS)

Download the installer [from this url](https://docs.conda.io/projects/conda/en/4.6.1/user-guide/install/macos.html). You need **Miniconda Installer**

Follow the instructions to install it from your Terminal:

```bash
$ bash Miniconda3-latest-MacOSX-x86_64.sh 
```

Once Miniconda is installed, you can create a virtual environment

```bash
conda create -n ps0 python=3.8 

# ps0 is the name of our virtual environment

#
# To activate this environment, use
#
#     $ conda activate rps1
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

then activate the virtual environment 

```bash
$ conda activate ps0
```

(notice that your environment in your Oh My Zhs prompt will change to your new environment name)

## Installing pipenv

we can install pipenv inside our conda environment with this command

```bash
$ conda install pipenv # don't forget to get into the right conda env first!
```

and test that it was installed by executing

```bash
$ pipenv 

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  scripts    Lists scripts in current environment config.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
```

Pipenv is a powefull tool that improves the lives of python developers by taking care of creating environments, installing packages and solvind dependencies. 

An important component of the pipenv workflow is the *Pipfile* and *Pipfile.lock*, as these files are needed to produce deterministic builds.

The use of pipenv for the purposes of this course would be limited, but you should learn about its capabilities. You can [read this](https://pipenv.pypa.io/en/latest/) or [the pipenv docs](https://pipenv.readthedocs.io/en/latest/)

> Note: *poetry* is another manager of packages and dependencies for python. It has been growing in popularity in the last couple of years, becoming the main competitor for *pipenv*. [You can find some poetry here](https://python-poetry.org/) 


#### Usage (not critical for this pset)

Rather than `python some_file.py`, you should run `pipenv run python
some_file.py` or `pipenv shell` etc

***Never*** pip install something!  Instead you should `pipenv install pandas`
*or `pipenv install --dev pytest`.  Use `--dev` if your app only needs the
*dependency for development, not to actually do it's job.

You should ***avoid*** installing "IDE apps" like ipython or black into your
Pipenv environment - if you don't need it during CI or for the code to work, it
should not be an application dependency.

Pycharm [works great with pipenv](https://www.jetbrains.com/help/pycharm/pipenv.html)

Be sure to commit any changes to your [Pipfile](./Pipfile) and [Pipfile.lock](./Pipfile.lock)!


## Problems 

### Build badges
Update the build badges at the top of this README, using markdown templates for your master branch.

See [Travis](https://docs.travis-ci.com/user/status-images) and [Code Climate](https://docs.codeclimate.com/docs/overview#badges) for instructions. You may add multiple if you like for various branches (e.g. 'develop' branch), but only one for master is required.

### Lineal Models

A linear model describes a quantitive response in terms of a linear combination of predictors. You can use a linear model to make predictions or explain the relationship between the response and the predictors. 

Linear models are very flexible and widely used in applications and are the base for more sofisticated Satistical and Machine Learning models.

In this problem set, you will be given a series of data as vectors and your will be asked to calculate the coefficients (slope and y-intercept) of the best fit for the given data. First, using the formulas, and then with the help of the SciPy library. 

Then, using the results you will be asked to make some predictions.

You can find more practical information about linear regressions in [this article from Real Python] (https://realpython.com/linear-regression-in-python/)

### Submit!

Note the `deploy` in your [.travis.yml](.travis.yml) file. After your tests successfully run in CI, this will run [submit.py](submit.py) to submit your assignment. For this problem set there is not a real deployment but rather a printout messages.

You need to run the submit script manually from your machine to test your code before running your CI/CD cycle.

### Testing Quality

Take a look at the file [test_pset.py](test_pset.py). It has unittests you can run with `pipenv run pytest`, they all shoud pass!. Do not remove the existing test methods, but your are expected to add new ones to ensure your code is working properly. Aim to get a test coverage higher than 80%.

Try to ensure the right tets pass before you commit and merge/push new code on your main branch, this will help minimize the number of builds on the CI server. That is, ***test locally*** first before committing, pushing or merging to main. This is good practice in general and will help with the shared resources.

### Test Coverage

Travis/Code Climate will report overall test coverage if setup correctly; try to cover every major function and clause you write. Travis will also display an output of coverage on the terminal.

### Git History

Git commits should be logically structured, follow a branching model, etc. Do not commit irrelevant files to the VCS (e.g., anything under `__pycache__` or your editor/IDE configurations). Try to avoid to `git add *` or `git commit -a`! They lump all your changes together; you want each commit to be a logical bit of history that captures what was done and why in a cohesive unit.
