# onepredict python project template

## prerequisite

- python ^3.10
- poetry

## how to use

- `make setup`
  - set git commit message
  - make virtualenv via python venv module
  - install dev library via poetry
- write your code
  - if you need, use  `make format`, `make lint`, `make typecheck` and `make test`
- commit your changes
  - add your changes to git staging area
  - `git commit`
    - ***DO NOT USE*** `git commit -n` or `git commit -m`, they avoid some procedures.

## Tools in template

- Formatter `make format`
  - black
  - isort
- Linter `make lint`
  - refurb
  - flakeheaven (wrapping flake8)
- Typecheck `make typecheck`
  - mypy
- Test `make test`
  - pytest
- CI/CD `pre-commit` or `git commit` + `git push`
  - pre-commit
  - github action
