#!/bin/sh -e
set -x
set -e

ruff check cligenius tests docs_src scripts --fix
ruff format cligenius tests docs_src scripts
