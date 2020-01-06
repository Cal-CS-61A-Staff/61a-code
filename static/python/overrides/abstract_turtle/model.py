
from collections import namedtuple

from math import sin, cos

class Color(namedtuple('Color', ['red', 'green', 'blue'])):
    @staticmethod
    def of(*color):
        if len(color) == 3:
            if any(not isinstance(c, int) for c in color):
                raise RuntimeError("Not a valid color: %s" % color)
            return Color(*color)
        raise RuntimeError("String colors not supported")

Position = namedtuple('Position', ['x', 'y'])

class DrawnTurtle(namedtuple('DrawnTurtle', ['pos', 'heading', 'stretch_wid', 'stretch_len'])):
    @property
    def points(self):
        unadjusted_points = [
            (-3, 8),
            (0, 0),
            (-3, -8),
            (8, 0),
        ]
        stretched_points = [
            (dx * self.stretch_len, dy * self.stretch_wid) for dx, dy in unadjusted_points
        ]
        rotated_points = [
            rotate(*dxy, self.heading) for dxy in stretched_points
        ]
        moved_points = [
            Position(self.pos.x + dx, self.pos.y + dy) for dx, dy in rotated_points
        ]
        return moved_points

    @property
    def json_friendly(self):
        return [
            [self.pos.x, self.pos.y],
            self.heading,
            self.stretch_wid,
            self.stretch_len
        ]

def rotate(x, y, theta):
    return x * cos(theta) - y * sin(theta), x * sin(theta) + y * cos(theta)
