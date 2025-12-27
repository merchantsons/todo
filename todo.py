#!/usr/bin/env python3
"""Interactive CLI wrapper for Todo app."""

import sys
from src.cli.main import main

if __name__ == "__main__":
    # Run in interactive mode (no args = interactive, with args = CLI mode)
    sys.exit(main())

