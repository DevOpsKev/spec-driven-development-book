#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
FONT_DIR="$REPO_ROOT/assets/fonts"
FONT_INSTALL_DIR="/usr/local/share/fonts/sdd-book"

# Short-circuit if dependencies are already installed (cache hit)
if command -v xelatex > /dev/null && command -v pandoc > /dev/null && command -v rsvg-convert > /dev/null && command -v pre-commit > /dev/null && [ -f "$FONT_INSTALL_DIR/SourceSerif4-Regular.ttf" ]; then
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

echo "==> Installing Python dependencies..."
pip install --quiet --break-system-packages -r "$REPO_ROOT/requirements.txt"
for req in "$REPO_ROOT"/.*mcp/requirements.txt; do
  [ -f "$req" ] && echo "    Installing from $req" && pip install --quiet --break-system-packages -r "$req"
done

echo "==> Installing pre-commit hooks..."
cd "$REPO_ROOT"
pre-commit install

echo "==> Installing fonts from repo..."
sudo mkdir -p "$FONT_INSTALL_DIR"
sudo cp "$FONT_DIR"/*.ttf "$FONT_INSTALL_DIR/"
sudo fc-cache -f > /dev/null 2>&1

echo "==> Verifying..."
command -v rsvg-convert > /dev/null && echo "    rsvg-convert: OK" || { echo "    rsvg-convert: MISSING"; exit 1; }
command -v pandoc > /dev/null && echo "    pandoc: OK" || { echo "    pandoc: MISSING"; exit 1; }
command -v xelatex > /dev/null && echo "    xelatex: OK" || { echo "    xelatex: MISSING"; exit 1; }
command -v pre-commit > /dev/null && echo "    pre-commit: OK" || { echo "    pre-commit: MISSING"; exit 1; }
[ -f "$FONT_INSTALL_DIR/SourceSerif4-Regular.ttf" ] && echo "    Source Serif 4: OK" || { echo "    Source Serif 4: MISSING"; exit 1; }
[ -f "$FONT_INSTALL_DIR/inter-regular.ttf" ] && echo "    Inter: OK" || { echo "    Inter: MISSING"; exit 1; }
[ -f "$FONT_INSTALL_DIR/JetBrainsMono-Regular.ttf" ] && echo "    JetBrains Mono: OK" || echo "    JetBrains Mono: not found (non-fatal)"
[ -f "$FONT_INSTALL_DIR/alfa-slab-one.ttf" ] && echo "    Alfa Slab One: OK" || { echo "    Alfa Slab One: MISSING"; exit 1; }

echo "==> Done."
