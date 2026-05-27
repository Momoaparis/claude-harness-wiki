#!/usr/bin/env python3
"""
Convert Obsidian [[wiki-links]] to standard Markdown [text](file.md) in wiki/ directory.
Idempotent — safe to run multiple times.
Skips wiki/templates/ subdirectory.
Respects fenced code blocks and inline backtick spans.
"""

import re
import sys
import os
from pathlib import Path

WIKI_DIR = Path(__file__).parent / "wiki"
SKIP_DIRS = {"templates"}

WIKI_LINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]')


def relative_path(from_file: Path, target_name: str) -> str:
    target_filename = target_name.strip() + ".md"
    from_dir = from_file.parent
    try:
        rel = os.path.relpath(WIKI_DIR / target_filename, from_dir)
    except ValueError:
        rel = target_filename
    return rel.replace("\\", "/")


def convert_line_safe(line: str, file_path: Path) -> str:
    """Convert [[wiki-links]] in a line, skipping inline `backtick code` spans."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            j = line.find('`', i + 1)
            if j == -1:
                result.append(line[i:])
                break
            result.append(line[i:j + 1])
            i = j + 1
            continue
        if line[i:i + 2] == '[[':
            m = WIKI_LINK_RE.match(line, i)
            if m:
                page = m.group(1).strip()
                alias = m.group(2).strip() if m.group(2) else page
                rel = relative_path(file_path, page)
                result.append(f"[{alias}]({rel})")
                i = m.end()
                continue
        result.append(line[i])
        i += 1
    return "".join(result)


def is_fence_marker(line: str) -> bool:
    """True if the line is a standard fenced code block marker (``` or ~~~ at line start)."""
    stripped = line.strip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def process_file(file_path: Path, dry_run: bool = True) -> int:
    """Process a single file. Returns number of links converted."""
    original = file_path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    new_lines = []
    in_code_block = False

    for line in lines:
        if is_fence_marker(line):
            in_code_block = not in_code_block
            new_lines.append(line)
        elif in_code_block:
            new_lines.append(line)
        else:
            new_lines.append(convert_line_safe(line, file_path))

    new_content = "".join(new_lines)
    if new_content != original:
        if not dry_run:
            file_path.write_text(new_content, encoding="utf-8")
        return original.count("[[")
    return 0


def collect_files() -> list[Path]:
    files = []
    for f in sorted(WIKI_DIR.rglob("*.md")):
        parts = f.relative_to(WIKI_DIR).parts
        if any(p in SKIP_DIRS for p in parts[:-1]):
            continue
        files.append(f)
    return files


def main():
    dry_run = "--apply" not in sys.argv
    files = collect_files()
    total_links = 0
    total_files = 0

    for f in files:
        n = process_file(f, dry_run=dry_run)
        if n > 0:
            total_links += n
            total_files += 1
            rel = f.relative_to(WIKI_DIR)
            print(f"  {'[DRY]' if dry_run else '[OK] '} {rel}  ({n} link(s))")

    mode = "DRY RUN — nothing written" if dry_run else "APPLIED"
    print(f"\n{mode}: {total_links} links across {total_files} files")
    if dry_run:
        print("Run with --apply to execute.")


if __name__ == "__main__":
    main()
