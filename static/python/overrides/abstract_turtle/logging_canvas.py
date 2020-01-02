from abstract_turtle.canvas import Canvas


class LoggingCanvas(Canvas):
    def __init__(self, width, height):
        super().__init__(width, height)

    @staticmethod
    def report(data):
        print("TURTLE:", data)

    def draw_rectangular_line(self, start, end, color, width):
        self.report(
            ["draw_rectangular_line", [start.x, start.y, end.x, end.y], color, width]
        )

    def draw_circle(self, center, radius, color, width, is_filled):
        self.report(
            ["draw_circle", [center.x, center.y, radius], color, width, is_filled]
        )

    def fill_polygon(self, points, color):
        self.report(["fill_polygon", [[point.x, point.y] for point in points], color])

    def set_bgcolor(self, color):
        self.report(["set_bgcolor", color])

    def clear(self):
        self.report(["clear"])
