import subprocess
import sys


def test_script_help():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", "-m", "cligenius", "--version"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Cligenius version:" in result.stdout
