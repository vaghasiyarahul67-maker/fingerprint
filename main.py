#!/usr/bin/env python3
"""
Main Entrypoint for Phone Fingerprint Engine
Usage:
  python3 main.py           # Launches sleek Cyber-Dark PyQt6 GUI (if DISPLAY exists)
  python3 main.py --cli     # Launches CLI mode
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    has_display = bool(os.environ.get("DISPLAY"))
    force_cli = "--cli" in sys.argv or "-c" in sys.argv or not has_display

    if force_cli:
        from cli import main as cli_main
        # Strip --cli before passing to argparse
        if "--cli" in sys.argv:
            sys.argv.remove("--cli")
        if "-c" in sys.argv:
            sys.argv.remove("-c")
        cli_main()
    else:
        try:
            from gui import main as gui_main
            gui_main()
        except Exception as e:
            print(f"[!] Warning: Failed to launch GUI ({e}). Falling back to CLI mode...")
            from cli import main as cli_main
            cli_main()


if __name__ == "__main__":
    main()
