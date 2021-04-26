#
#  Video Editor
#  Video editor with a Python API.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


class Scene:
    is_saved: bool
    is_dirty: bool
    file_path: str
    meta: bytes

    frame_start: int
    frame_end: int
    frame_step: int
    fps: int

    def __init__(self, **kwargs) -> None:
        self.is_saved = False
        self.is_dirty = False
        self.file_path = ""
        self.meta = b""

        self.frame_start = 0
        self.frame_end = 600
        self.frame_step = 1
        self.fps = 30

        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])