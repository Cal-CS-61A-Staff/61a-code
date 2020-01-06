
from .canvas import Canvas

def _forward(method):
    def func(self, *args, **kwargs):
        # pylint: disable=W0212
        return getattr(self._canvas, method)(*args, **kwargs)
    func.name = method
    return func

class ForwardingCanvas(Canvas):
    """
    Canvas that dispatches all calls to a contained canvas
    """
    def __init__(self, canvas):
        super().__init__(-1, -1)
        self._canvas = canvas

    def set_canvas(self, canvas):
        canvas.turtle = self._canvas.turtle
        self._canvas = canvas

    draw_rectangular_line = _forward("draw_rectangular_line")
    draw_circle = _forward("draw_circle")
    fill_polygon = _forward("fill_polygon")
    set_bgcolor = _forward("set_bgcolor")
    clear = _forward("clear")
    refreshed_turtle = _forward("refreshed_turtle")
