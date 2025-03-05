from manim import *

from manim_kodisc import *


class PolygonExample(Scene):
    def construct(self):
        position_list = [
            [-2.5, -2.5, 0],
            [2.5, -2.5, 0],
            [2.5, 2.5, 0],
        ]
        polygon = BetterPolygon(
            *position_list
        )
        self.play(Create(polygon))   
        self.wait(1)
        self.play(Create(polygon.get_angles(angle_labels=["a", "b", "c", "d"], radius=0.6, label_size=30)))
        self.wait(5)

class RegularPolygonExample(Scene):
    def construct(self):
        polygon = BetterRegularPolygon(n=8)
        self.play(Create(polygon))
        self.wait(1)
        self.play(Create(polygon.get_angles(radius=0.3, label_as_angle=True)))
        self.wait(5)