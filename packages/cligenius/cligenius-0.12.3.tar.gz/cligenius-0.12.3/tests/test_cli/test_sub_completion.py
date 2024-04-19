import os
import subprocess
import sys


def test_script_completion_run():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", "-m", "cligenius"],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "___MAIN__.PY_COMPLETE": "complete_bash",
            "_PYTHON _M CLIGENIUS_COMPLETE": "complete_bash",
            "COMP_WORDS": "cligenius tests/assets/cli/sample.py run hello --",
            "COMP_CWORD": "4",
        },
    )
    assert "--name" in result.stdout
