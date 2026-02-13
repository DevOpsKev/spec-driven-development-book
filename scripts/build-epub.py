#!/usr/bin/env python3
"""
SDD Book EPUB Build Script

Usage: python scripts/build-epub.py

Assembles front matter, parts, chapters, and back matter into EPUB using pandoc.
Scans content/ directory structure and includes files in order.
Missing content is skipped gracefully.

Dependencies:
  - pandoc
  - Run scripts/build-cover.py first to generate cover image
"""

import re
import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===

REPO_ROOT = Path(__file__).resolve().parent.parent
BOOK_TITLE = "spec-driven-development"
CONTENT_DIR = REPO_ROOT / "content"
COVER_IMAGE = REPO_ROOT / "output" / "front-cover.png"
METADATA_FILE = REPO_ROOT / "build" / "epub" / "metadata.yaml"
CSS_FILE = REPO_ROOT / "build" / "epub" / "styles.css"
OUTPUT_DIR = REPO_ROOT / "output"
OUTPUT_EPUB = OUTPUT_DIR / f"{BOOK_TITLE}.epub"

# Directory order (matches book structure)
SECTION_ORDER = [
    "00-front-matter",
    "01-part-1-foundation",
    "02-part-2-writing-specifications",
    "03-part-3-the-workflow",
    "04-part-4-practice",
    "05-part-5-governance-and-evolution",
    "06-closing",
    "07-back-matter",
]


# === BUILD LOGIC ===


def get_file_order(path: Path) -> tuple[int, str]:
    """Extract numeric prefix for sorting, then alpha."""
    match = re.match(r"^(\d+)", path.stem)
    num = int(match.group(1)) if match else 999
    return (num, path.stem)


def get_section_files(section_dir: Path) -> list[Path]:
    """Get markdown files from a section directory, sorted by prefix."""
    if not section_dir.exists():
        return []

    files = sorted(section_dir.glob("*.md"), key=get_file_order)
    return files


def scan_content() -> list[Path]:
    """Scan content directory and return all files in book order."""
    all_files = []

    for section in SECTION_ORDER:
        section_dir = CONTENT_DIR / section
        files = get_section_files(section_dir)

        if files:
            print(f"\n{section}/")
            for f in files:
                print(f"  [ok] {f.name}")
                all_files.append(f)
        else:
            print(f"\n{section}/ (empty or missing)")

    return all_files


def check_deps():
    """Verify pandoc is available."""
    try:
        subprocess.run(
            ["pandoc", "--version"],
            capture_output=True,
            check=True,
        )
    except FileNotFoundError:
        print("Error: pandoc not found. Install with: sudo apt-get install pandoc")
        sys.exit(1)


def build_epub():
    """Assemble and build the EPUB."""
    print(f"Building {OUTPUT_EPUB}...\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Check for cover image
    cover_flag = []
    if COVER_IMAGE.exists():
        cover_flag = [f"--epub-cover-image={COVER_IMAGE}"]
        print(f"Cover: {COVER_IMAGE}")
    else:
        print("Cover: (none found, run scripts/build-cover.py first)")

    # Check for metadata
    metadata_flag = []
    if METADATA_FILE.exists():
        metadata_flag = [f"--metadata-file={METADATA_FILE}"]
        print(f"Metadata: {METADATA_FILE}")
    else:
        print("Metadata: (none found, using defaults)")

    # Check for CSS
    css_flag = []
    if CSS_FILE.exists():
        css_flag = [f"--css={CSS_FILE}"]
        print(f"CSS: {CSS_FILE}")
    else:
        print("CSS: (none found, using defaults)")

    # Scan content
    print("\nScanning content...")
    all_files = scan_content()

    if not all_files:
        print("\nERROR: No content files found.")
        sys.exit(1)

    print(f"\nTotal files: {len(all_files)}")

    # Build pandoc command
    cmd = (
        [
            "pandoc",
            "--toc",
            "--toc-depth=2",
            "--epub-chapter-level=1",
            "--epub-title-page=false",
            "-o",
            str(OUTPUT_EPUB),
        ]
        + metadata_flag
        + cover_flag
        + css_flag
        + [str(f) for f in all_files]
    )

    print("\nRunning pandoc...")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"ERROR: pandoc failed:\n{result.stderr}")
        sys.exit(1)

    size_kb = OUTPUT_EPUB.stat().st_size / 1024
    print(f"\nDone: {OUTPUT_EPUB}")
    print(f"Size: {size_kb:.1f} KB")


if __name__ == "__main__":
    check_deps()
    build_epub()
