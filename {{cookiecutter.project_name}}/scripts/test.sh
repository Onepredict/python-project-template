#!/usr/bin/env bash
poetry run pytest --junitxml=pytest.xml\
--cov-report=term-missing:skip-covered --cov=app tests/ \
| tee pytest-coverage.txt
