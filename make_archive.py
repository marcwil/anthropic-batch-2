#!/usr/bin/env python3
"""Pack your problem folder(s) into a zip file to send to the batch coordinator.

Usage (from the repository root, or anywhere inside it):

    python3 make_archive.py                 # problems you added or changed
    python3 make_archive.py relu-max-units  # only the named folder(s) in problems/
    python3 make_archive.py --all           # every folder in problems/

Works without git (then it packs every folder in problems/ unless you name some).
Writes batch2-<folders>-<date>.zip next to this script and prints what it contains.
"""

import argparse
import datetime
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS = ROOT / "problems"

# LaTeX build artefacts and editor files; the coordinator rebuilds the PDFs.
SKIP_SUFFIXES = {
    ".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".toc",
    ".synctex", ".gz", ".pdf", ".el",
}
SKIP_DIRS = {".auctex-auto", "_minted", "__pycache__"}
SKIP_NAMES = {".DS_Store", "Thumbs.db"}


def changed_folders():
    """Problem folders with uncommitted or unpushed changes, or None without git."""
    try:
        status = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all", "--", "problems"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        paths = [line[3:].split(" -> ")[-1].strip('"') for line in status]
        upstream = subprocess.run(
            ["git", "diff", "--name-only", "@{upstream}", "HEAD", "--", "problems"],
            cwd=ROOT, capture_output=True, text=True,
        )
        if upstream.returncode == 0:
            paths += upstream.stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        return None
    folders = set()
    for p in paths:
        parts = Path(p).parts
        if len(parts) >= 3 and parts[0] == "problems":
            folders.add(parts[1])
    return sorted(f for f in folders if (PROBLEMS / f).is_dir())


def wanted(path):
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.name in SKIP_NAMES or path.name.startswith("."):
        return False
    return path.suffix.lower() not in SKIP_SUFFIXES


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("folders", nargs="*", help="folder names inside problems/")
    parser.add_argument("--all", action="store_true", help="pack every folder in problems/")
    args = parser.parse_args()

    every = sorted(p.name for p in PROBLEMS.iterdir() if p.is_dir()) if PROBLEMS.is_dir() else []
    if args.folders:
        folders = [Path(f).name for f in args.folders]
        missing = [f for f in folders if f not in every]
        if missing:
            sys.exit(f"Not found in problems/: {', '.join(missing)}")
    elif args.all:
        folders = every
    else:
        folders = changed_folders()
        if folders is None:
            print("git not available; packing every folder in problems/.")
            folders = every
    if not folders:
        sys.exit("Nothing to pack. Put your problem in problems/<topic>-<short-name>/, "
                 "or name the folder: python3 make_archive.py <folder>")

    for f in folders:
        if not any((PROBLEMS / f).glob("*.tex")):
            print(f"Warning: problems/{f}/ has no .tex file.")

    label = folders[0] if len(folders) == 1 else f"{len(folders)}-problems"
    out = ROOT / f"batch2-{label}-{datetime.date.today().isoformat()}.zip"
    files = [
        p for f in folders for p in sorted((PROBLEMS / f).rglob("*"))
        if p.is_file() and wanted(p.relative_to(PROBLEMS))
    ]
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in files:
            zf.write(p, p.relative_to(ROOT).as_posix())

    print(f"Wrote {out.name} with {len(files)} file(s):")
    for p in files:
        print(f"  {p.relative_to(ROOT).as_posix()}")
    print("Send it to Marcus Wilhelm (Zulip DM or the batch-2 topic in #AskAnthropic).")


if __name__ == "__main__":
    main()
