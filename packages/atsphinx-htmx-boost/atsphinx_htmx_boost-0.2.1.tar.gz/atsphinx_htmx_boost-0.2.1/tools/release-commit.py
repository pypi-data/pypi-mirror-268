#!/usr/bin/env python
"""Batch script to generate 'release' commit."""

import argparse
import shutil
import subprocess
from datetime import date
from pathlib import Path
from textwrap import dedent

import tomllib
from jinja2 import Template

root = Path(__file__).parent.parent
parser = argparse.ArgumentParser()
parser.add_argument("level", type=str, choices=["major", "minor", "patch"])


def get_version() -> str:  # noqa: D103
    cmd = ["rye", "version"]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE)
    return proc.stdout.decode("utf-8").strip()


def bump_version(level: str) -> str:  # noqa: D103
    """Bump version for sources."""
    cmd = ["age", level]
    subprocess.run(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def replace_version(target, current_version: str, new_version: str):
    """Change old/new version text from source."""
    src = root / target["filename"]
    lines = []
    from_ = target["search"].format(current_version=current_version)
    to_ = target["replace"].format(new_version=new_version)
    for line in src.read_text().split("\n"):
        if line == from_:
            lines.append(to_)
        else:
            lines.append(line)
    src.write_text("\n".join(lines))


def update_changes(current_version: str, new_version: str):
    """Generate changelog for new version.

    Currently, this works only generate template.
    """
    CHANGELOG_TEMPLATE = Template(
        dedent(
            """
        v{{version}}
        ={{'=' * version|length}}

        :date: {{now.strftime('%Y-%m-%d')}} (JST)

        Features
        --------

        Bug fixes
        ---------

        Miscellaneous
        -------------

        """
        ).strip()
    )
    now = date.today()
    target = root / "CHANGES.rst"
    move_to = root / "doc" / "changelogs" / f"v{current_version}.rst"
    move_to.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(target, move_to)
    target.write_text(CHANGELOG_TEMPLATE.render(version=new_version, now=now))


def main(args: argparse.Namespace):
    """Handle multi functions."""
    pyproject_toml = root / "pyproject.toml"
    current_version = tomllib.loads(pyproject_toml.read_text())["project"]["version"]
    print(f"Current version: v{current_version}")
    bump_version(args.level)
    new_version = tomllib.loads(pyproject_toml.read_text())["project"]["version"]
    print(f"Next version:    v{new_version}")
    update_changes(current_version, new_version)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
