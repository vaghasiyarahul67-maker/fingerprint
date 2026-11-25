#!/usr/bin/env bash
# Quick Launcher for Phone Fingerprint Engine
cd "$(dirname "$0")"

export DISPLAY="${DISPLAY:-:0}"
python3 main.py "$@"
