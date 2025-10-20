# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import ast
import logging
import tomllib
from pathlib import Path


def get_bl_info() -> dict:
    """Get the bl_info dict from the init file."""

    with open(Path(Path(__file__).parent.parent / "__init__.py"), "r") as f:
        node = ast.parse(f.read())

    n: ast.Module
    for n in ast.walk(node):
        for b in n.body:
            if (
                isinstance(b, ast.Assign)
                and isinstance(b.value, ast.Dict)
                and (any(t.id == "bl_info" for t in b.targets))
            ):
                return ast.literal_eval(b.value)

    raise ValueError("Cannot find bl_info")


def get_manifest_info() -> dict:
    """Get the Blender manifest file."""

    toml_file = Path(__file__).parent.parent / "blender_manifest.toml"
    with open(toml_file, "rb") as f:
        config = tomllib.load(f)

    logging.debug(config)

    return config


def get_wheels() -> list[str]:
    """Get the wheels from the manifest file."""

    manifest: dict = get_manifest_info()
    manifest_wheels: list[str] = manifest.get("wheels", {}) or {}
    manifest_wheels = [w.removeprefix("./wheels/") for w in manifest_wheels]

    return manifest_wheels
