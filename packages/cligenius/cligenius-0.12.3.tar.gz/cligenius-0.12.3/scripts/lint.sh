#!/usr/bin/env bash

set -e
set -x

mypy cligenius
ruff check cligenius tests docs_src
ruff format cligenius tests docs_src --check
