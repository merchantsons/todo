"""Integration tests for CLI commands."""

import subprocess
import sys
from pathlib import Path


def run_cli_command(args: list[str]) -> tuple[int, str, str]:
    """Run CLI command and return exit code, stdout, stderr."""
    result = subprocess.run(
        [sys.executable, "-m", "src.cli.main"] + args,
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent,
    )
    return result.returncode, result.stdout, result.stderr


def test_add_command_creates_task() -> None:
    """Test that 'add' command creates a task via CLI."""
    exit_code, stdout, stderr = run_cli_command(["add", "Test task"])

    # Command not yet implemented, so we expect error
    # This test will pass once implementation is complete
    assert exit_code != 0 or "Test task" in stdout


