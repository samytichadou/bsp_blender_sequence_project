'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou (tonton)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


# register
##################################

from . import (
    properties,
    addon_preferences,
    gui,
    op_open_scene,
)

def register():
    properties.register()
    addon_preferences.register()
    gui.register()
    op_open_scene.register()

def unregister():
    properties.unregister()
    addon_preferences.unregister()
    gui.unregister()
    op_open_scene.unregister()
