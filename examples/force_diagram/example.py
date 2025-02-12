from manim import *

from manim_kodisc import *


class ForceDiagramExample(Scene):
    def construct(self):
        ball = Circle(radius=0.5, color=BLUE)
        ball.move_to(ORIGIN)

        force_diagram = ForceDiagram(ball)
        gravity = force_diagram.add_force(3, -PI/2, "F_{g}", equal_length=True)
        normal = force_diagram.add_force(3, PI / 2, "F_{n}", equal_length=True)

        self.add(ball)
        self.play(Create(force_diagram))
        self.wait(2)