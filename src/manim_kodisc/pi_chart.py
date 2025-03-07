from manim import *


class PiChart(VGroup):
    def __init__(self, data: dict[
        str, int
    ], colors: list, show_labels=True, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.colors = colors
        self.show_labels = show_labels
        self.create_pi_chart()
    
    def create_pi_chart(self):
        total = sum([value for key, value in self.data.items()])
        angle = 0
        index = 0
        for key, value in self.data.items():
            color = self.colors[index] if self.colors else BLUE
            sector = Sector(
                arc_center=ORIGIN,
                start_angle=angle,
                angle=value/total*TAU,
                fill_color=color,
                fill_opacity=1,
                stroke_width=0
            )

            if self.show_labels:
                outward_direction = rotate_vector(RIGHT, angle + value/total*TAU/2)
                label = MathTex(f"{key} ({value})", color=color).scale(0.5)
                label.next_to(sector.get_center() + outward_direction*0.5, outward_direction)
                self.add(label)

            self.add(sector)
            angle += value/total*TAU
            index += 1