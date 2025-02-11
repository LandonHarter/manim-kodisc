from manim import *


class SlopeField(VGroup):
    def __init__(self, func, x_range=(-10, 10), y_range=(-10, 10), step_size=1, **kwargs):
        self.func = func
        self.x_range = x_range
        self.y_range = y_range
        self.step_size = step_size
        self.axes = self.get_axes()
        self.field = self.get_field()
        super().__init__(self.axes, self.field, **kwargs)

    def get_axes(self):
        axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            axis_config={"include_tip": False},
        )
        axes.center()
        return axes

    def get_field(self):
        f = lambda p: np.array([1, self.get_slope(p[0], 0.000001), 0])
        field = ArrowVectorField(f)
        
        field.set_opacity(0.5)
        field.set_color(WHITE)
        field.length_func = lambda norm: 0.1

        field.move_to(self.axes)
        field.fit_to_coordinate_system(self.axes)
        return field
    
    def get_slope(self, x, dx):
        return (self.func(x + dx) - self.func(x)) / dx