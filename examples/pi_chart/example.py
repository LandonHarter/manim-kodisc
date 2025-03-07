from manim import *

from manim_kodisc import *


class PiChartExample(Scene):
    def construct(self):
        chart = PiChart(
            data={"A": 1, "B": 2, "C": 3},
            colors=[BLUE, GREEN, RED]
        )

        self.play(Write(chart))

        self.wait(2)