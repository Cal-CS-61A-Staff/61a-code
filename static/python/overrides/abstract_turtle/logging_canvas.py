
from abc import abstractmethod

from .canvas import Canvas

class AbstractLoggingCanvas(Canvas):
    @abstractmethod
    def on_action(self, log_line):
        pass

    def draw_rectangular_line(self, start, end, color, width):
        self.on_action(['draw_rectangular_line', [start.x, start.y, end.x, end.y], color, width])

    def draw_circle(self, center, radius, color, width, is_filled):
        self.on_action(['draw_circle', [center.x, center.y, radius], color, width, is_filled])

    def fill_polygon(self, points, color):
        self.on_action(['fill_polygon', [[point.x, point.y] for point in points], color])

    def set_bgcolor(self, color):
        self.on_action(['set_bgcolor', color])

    def clear(self):
        self.on_action(['clear'])

    def update_turtle(self, drawn_turtle):
        self.on_action([
            'update_turtle',
            [drawn_turtle.pos.x, drawn_turtle.pos.y],
            drawn_turtle.heading,
            drawn_turtle.stretch_wid,
            drawn_turtle.stretch_len
        ])

class LoggingCanvas(AbstractLoggingCanvas):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.log = []
    def on_action(self, log_line):
        self.log.append(log_line)
