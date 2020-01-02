class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return "[{}, {}, {}]".format(self.red, self.green, self.blue)

    __json_repr__ = __repr__

    @staticmethod
    def of(*color):
        if len(color) == 3:
            if any(not isinstance(c, int) for c in color):
                raise RuntimeError("Not a valid color: %s" % color)
            return Color(*color)
        raise RuntimeError("String colors not supported")


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)

    __json_repr__ = __repr__
