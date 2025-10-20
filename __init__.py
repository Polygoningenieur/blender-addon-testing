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


from bpy.utils import register_class, unregister_class

from .utils.utils import classes_to_register

# necessary to import modules so they can get registered
from . import utils, operators


bl_info = {
    "name": "Blender Addon Testing",
    "author": "Polygoningenieur Gustav Hahn",
    "description": "...",
    "blender": (4, 4, 0),
    "version": (0, 0, 2),
    "location": "View3D",
    "support": "COMMUNITY",
}


def register():
    """Register everything blender needs registering for."""

    for c in classes_to_register:
        register_class(c)

    print("Blender Addon Testing Registered.")


def unregister():
    """Unregister and delete everything that was registered and created."""

    for c in reversed(classes_to_register):
        if c.is_registered:
            unregister_class(c)

    print("Blender Addon Testing Unregistered.")
