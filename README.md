# python-boilerplate #

Python Poetry Boilerplate Project Structure

## Folder Structure ##

```sh
python-poetry-boilerplate
├── .github
│   └── workflows                 # Workflows
│       ├── development.yaml      # Production workflow
│       └── production.yaml       # Development workflow
├── conftest.py                   # pytest configuration file
├── notebooks
│   └── test.ipynb                # Test Jupyter notebook (for development)
├── src
│   └── python_poetry_boilerplate
│       ├── config
│       │   ├── __init__.py 
│       │   └── env.py            # Environment variables module
│       ├── libs
│       │   ├── __init__.py 
│       │   └── my_libs.py        # Utility libraries
│       ├── main.job.py           # Main job script
│       └── main.service.py       # Main service script
├── tests
│   ├── __init__.py
│   ├── test_job.py               # Test job script
│   └── test_my_libs.py           # Test libraries
├── .dockerignore                 # Docker ignore file
├── .env.example                  # Environment variables example
├── .gitignore                    # Git ignore file
├── conftest.py                   # Test configuration file
├── Dockerfile.kubernetes         # Dockerfile for kubernetes
├── Dockerfile.lambda             # Dockerfile for lambda
├── Makefile                      # Makefile
├── poetry.lock                   # Poetry lock file
├── pyproject.toml                # Pyproject.toml
└── README.md                     # Readme
```

## How to Create a new Project ##

There are two ways to create a new Project.

### 1. Create a new Project from the repo as a template ### 

Pretty straightforward. Go to the [repository](https://github.com/face0b1101/python-poetry-boilerplate) and click the green `Use this template` button.

See [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) for more details.

### 2. Create a Fork ###

Alternatively, create a fork the _old-fashioned_ way:

- Create new repository on GitHub (`new-repository-name`)
- Create another folder on local machine
- Bare clone this repository

    ```bash
    git clone --bare https://github.com/face0b1101/python-poetry-boilerplate
    ```

- CD to this folder (with .git suffix) and push mirror to GitHub

    ```bash
    cd python-boilerplate.git
    git push --mirror https://github.com/face0b1101/new-repository-name.git
    ```

- Remove `python-poetry-boilerplate.git` folder from local folder
- Clone `new-repository-name` to local folder

### Housekeeping ###

When you have your new project set up, a bit of housekeeping is required:

1. Rename `src/python_poetry_boilerplate` to `src/new_repository_name`
2. Update `pyproject.toml`
    - replace `python-poetry-boilerplate` with `new-repository-name`
    - replace `python_poetry_boilerplate` with `new_repository_name`
    - update other items in `[tool.poetry]` as appropriate
3. Update pytest scripts
    - update imports in `tests/test_my_app.py`
4. Install Poetry

    ```bash
    poetry install
    ```

5. Run pytest

    ```bash
    poetry run pytest
    ```

    If the tests run without error then you have configured your project and you're ready to get coding.

## How to Code ##

1. Create a new branch

   ```bash
   git branch <new-branch>
   ```
  
2. Install Poetry

   ```bash
   # probably not necessary, but it does no harm
   poetry install
   poetry shell
   ```

3. Do some coding and stuff...

4. Push the new branch and changes
  
   ```bash
   git push -u origin <new-branch>
   ```

## How to Commit ##

- Commit on the branch
- PR if it should be merged
- Specify the type of commit:
  - feat: The new feature you're adding to a particular application
  - fix: A bug fix
  - style: Feature and updates related to styling
  - refactor: Refactoring a specific section of the codebase
  - test: Everything related to testing
  - docs: Everything related to documentation
  - chore: Regular code maintenance.[ You can also use emojis to represent commit types]
