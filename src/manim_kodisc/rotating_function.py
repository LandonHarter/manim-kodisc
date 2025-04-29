from manim import *


class RotatingFunction(VMobject):
    def __init__(self, func, axis=[1, 0], color=BLUE, opacity=0.5, x_range=[-1, 1], **kwargs):
        super().__init__(**kwargs)
        self.func = func

        self.axes = ThreeDAxes()
        self.add(self.axes)

        axis = np.array(axis, dtype=float)
        if np.allclose(axis, [0, 1]):
            axis = -axis
        self.axis = axis / np.linalg.norm(axis)

        self.graph = self.axes.plot(func, x_range=x_range)
        self.add(self.graph)

        self.angle_tracker = ValueTracker(0)
        
        # based on the axis passed in
        if np.allclose(self.axis, [1, 0]) or np.allclose(self.axis, [-1, 0]):
            self.surface_function = lambda u, v: np.array([
                u,
                self.func(u) * np.cos(v),
                self.func(u) * np.sin(v),
            ])
        elif np.allclose(self.axis, [0, 1]) or np.allclose(self.axis, [0, -1]):
            self.surface_function = lambda u, v: np.array([
                u * np.cos(v),
                self.func(u),
                u * np.sin(v),
            ])
        else:
            raise ValueError("Axis must be one of [1, 0], [0, 1]")

        self.surface = always_redraw(lambda: Surface(
            self.surface_function,
            u_range=x_range,
            v_range=[0, self.angle_tracker.get_value()],
            resolution=(16, 32),
            fill_opacity=opacity,
            fill_color=color,
            stroke_width=0,
            checkerboard_colors=False
        ))
        self.add(self.surface)

    def rotate(self, angle=2*PI):
        return AnimationGroup(
            self.angle_tracker.animate.set_value(angle),
            Rotate(
                self.graph,
                angle=angle,
                axis=np.array([self.axis[0], self.axis[1], 0]),
                about_point=ORIGIN
            )
        )