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
        # self.play(Create(polygon.get_points(point_labels=["A", "B", "C"], label_size=30)))
        self.wait(1)
        self.play(Create(polygon.get_angles(angle_labels=["A", "B", "C"], radius=0.6, label_size=30, label_as_angle=False)))
        self.wait(1)
        self.play(Create(polygon.get_side_labels(labels=["AB", "BC", "AC"], label_size=30)))
        self.wait(5)

class RegularPolygonExample(Scene):
    def construct(self):
        polygon = BetterRegularPolygon(n=8)
        self.play(Create(polygon))
        self.wait(1)
        self.play(Create(polygon.get_angles(radius=0.3, label_as_angle=True)))
        self.wait(5)