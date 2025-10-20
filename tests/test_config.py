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

import unittest


class TestConfig(unittest.TestCase):

    def test_bpy(self):
        """Test if bpy module was installed correctly."""

        try:
            import bpy
        except ImportError as e:
            self.fail(f"Could not import bpy: {e}")

    def test_version(self):
        """Test if bl_info and manifest versions match."""

        from .utils import get_bl_info, get_manifest_info

        bl_info: dict = get_bl_info()
        bl_info_version: tuple = bl_info.get("version")
        manifest: dict = get_manifest_info()

        bl_info_str: str = (
            f"{bl_info_version[0]}.{bl_info_version[1]}.{bl_info_version[2]}"
        )
        self.assertEqual(bl_info_str, manifest.get("version"))

    def test_import_from_addon(self):
        """Test if we can import from the parent folder relativly."""

        try:
            from ..operators.operator_website import BLENDER_ADDON_TESTING_OT_website
        except ImportError as e:
            self.fail(f"Relative import error: {e}")
