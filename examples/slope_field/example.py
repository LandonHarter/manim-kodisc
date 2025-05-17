from manim import *

from manim_kodisc import *


class SlopeFieldExample(Scene):
    def construct(self):
        slope_field = SlopeField(
            lambda x: np.cos(x),
            x_range=(-5, 5),
            y_range=(-5, 5),
            step_size=0.5,
        )
        self.play(Write(slope_field))

        self.wait(0.5)
        self.play(Write(slope_field.axes.plot(lambda x: np.sin(x), color=BLUE)))

        self.wait(5)