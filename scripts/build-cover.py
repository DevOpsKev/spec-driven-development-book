#!/usr/bin/env python3
"""Build cover PNGs from SVG sources."""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COVER_DIR = REPO_ROOT / "assets" / "cover"
OUTPUT_DIR = REPO_ROOT / "output"

# Cover definitions: (svg_name, output_name, width, height)
COVERS = [
    ("front-cover.svg", "front-cover.png", 1600, 2286),
    ("spine.svg", "spine.png", 228, 2286),
    ("back-cover.svg", "back-cover.png", 1600, 2286),
]


def check_deps():
    """Verify rsvg-convert is available."""
    try:
        subprocess.run(
            ["rsvg-convert", "--version"],
            capture_output=True,
            check=True,
        )
    except FileNotFoundError:
        print("Error: rsvg-convert not found. Run scripts/setup-deps.sh first.")
        sys.exit(1)


def build_cover(svg_name: str, png_name: str, width: int, height: int):
    """Convert a single SVG to PNG."""
    svg_path = COVER_DIR / svg_name
    png_path = OUTPUT_DIR / png_name

    if not svg_path.exists():
        print(f"  Skipping {svg_name} (not found)")
        return

    subprocess.run(
        [
            "rsvg-convert",
            "-w",
            str(width),
            "-h",
            str(height),
            str(svg_path),
            "-o",
            str(png_path),
        ],
        check=True,
    )
    size_kb = png_path.stat().st_size / 1024
    print(f"  {svg_name} -> {png_name} ({size_kb:.0f} KB)")


def main():
    """Build all cover images."""
    print("Building cover images...\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for svg_name, png_name, width, height in COVERS:
        build_cover(svg_name, png_name, width, height)

    print("\nDone.")


if __name__ == "__main__":
    check_deps()
    main()
