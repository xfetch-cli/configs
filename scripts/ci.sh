#!/usr/bin/env bash
# Local CI: run before committing (Linux / macOS).
set -euo pipefail
cd "$(dirname "$0")"

echo "==> validate JSON/JSONC"
python3 validate.py ..

echo "==> CI OK"
