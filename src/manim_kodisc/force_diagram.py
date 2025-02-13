from manim import *


class ForceDiagram(VGroup):
    def __init__(self, object, **kwargs):
        self.forces = []
        self.object = object
        self.force_arrows = VGroup()
        super().__init__(self.force_arrows, **kwargs)

    def add_force(self, magnitude, angle, text = "", text_side = RIGHT, equal_length = False):
        group = VGroup()
        force = magnitude * np.array([np.cos(angle), np.sin(angle), 0])
        arrow = Arrow(
            start=self.object.get_center(),
            end=self.object.get_center() + force,
            buff=0,
        )

        if equal_length:
            midpoint = (arrow.get_start() + arrow.get_end()) / 2
            line = Line(
                start=midpoint + 0.1 * np.array([np.sin(angle), -np.cos(angle), 0]),
                end=midpoint - 0.1 * np.array([np.sin(angle), -np.cos(angle), 0]),
                color=WHITE
            )
            group.add(line)

        label = MathTex(text).next_to(arrow, text_side)
        self.forces.append({
            "vector": force,
            "label": label
        })
        self.force_arrows.add(arrow)

        group.add(arrow, label)
        self.add(group)
        return group

    def remove_force(self, index):
        self.forces.pop(index)
        self.force_arrows.remove(self.force_arrows[index])