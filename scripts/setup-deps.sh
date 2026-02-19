#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
FONT_DIR="$REPO_ROOT/assets/fonts"

# Short-circuit if dependencies are already installed (cache hit)
if command -v xelatex > /dev/null && command -v pandoc > /dev/null && command -v rsvg-convert > /dev/null && command -v pre-commit > /dev/null && fc-list | grep -qi "source serif"; then
  echo "==> Dependencies already installed (cache hit), skipping."
  exit 0
fi

echo "==> Installing system dependencies..."
sudo apt-get update -qq || echo "    Warning: apt-get update had errors, continuing..."
sudo apt-get install -y -qq \
  librsvg2-bin \
  pandoc \
  texlive-xetex \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-latex-recommended \
  lmodern \
  > /dev/null

echo "==> Installing Python tools..."
pip install --quiet --break-system-packages pre-commit

echo "==> Installing pre-commit hooks..."
cd "$REPO_ROOT"
pre-commit install

echo "==> Installing fonts from repo..."
sudo mkdir -p /usr/local/share/fonts/sdd-book
sudo cp "$FONT_DIR"/*.ttf /usr/local/share/fonts/sdd-book/
sudo fc-cache -f

echo "==> Verifying..."
command -v rsvg-convert > /dev/null && echo "    rsvg-convert: OK" || { echo "    rsvg-convert: MISSING"; exit 1; }
command -v pandoc > /dev/null && echo "    pandoc: OK" || { echo "    pandoc: MISSING"; exit 1; }
command -v xelatex > /dev/null && echo "    xelatex: OK" || { echo "    xelatex: MISSING"; exit 1; }
command -v pre-commit > /dev/null && echo "    pre-commit: OK" || { echo "    pre-commit: MISSING"; exit 1; }
fc-list | grep -qi "source serif" && echo "    Source Serif 4: OK" || { echo "    Source Serif 4: MISSING"; exit 1; }
fc-list | grep -qi "inter" && echo "    Inter: OK" || { echo "    Inter: MISSING"; exit 1; }
fc-list | grep -qi "jetbrains mono\|JetBrainsMono" && echo "    JetBrains Mono: OK" || echo "    JetBrains Mono: not found (non-fatal)"
fc-list | grep -qi "alfa slab" && echo "    Alfa Slab One: OK" || { echo "    Alfa Slab One: MISSING"; exit 1; }

echo "==> Done."
