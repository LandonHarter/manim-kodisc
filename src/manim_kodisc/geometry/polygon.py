from manim import *


class BetterPolygon(Polygon):
    def __init__(self, *vertices, **kwargs):
        self.angles = []
        super().__init__(*vertices, **kwargs)

    def get_angles(self, angle_labels: list[str] = None, radius: float = 0.5, label_size: int = 24, label_as_angle=False) -> VGroup:
        self.angles = []

        vertices = self.get_vertices()
        num_vertices = len(vertices)
        for i in range(num_vertices):
            label = angle_labels[i] if angle_labels and i < len(angle_labels) else None
            angle = self.draw_angle(i, label, radius, label_size, label_as_angle)
            self.angles.append(angle)
        
        return VGroup(*self.angles)
    
    def draw_angle(self, index: int, label: str = None, radius: float = 0.5, label_size: int = 24, label_as_angle=False) -> VGroup:
        vertices = self.get_vertices()
        num_vertices = len(vertices)
        
        p1 = vertices[(index - 1) % num_vertices]
        p2 = vertices[index]
        p3 = vertices[(index + 1) % num_vertices]

        v1 = p1 - p2
        v2 = p3 - p2
        v1_unit = v1 / np.linalg.norm(v1)
        v2_unit = v2 / np.linalg.norm(v2)

        angle1 = np.arctan2(v1[1], v1[0])
        angle2 = np.arctan2(v2[1], v2[0])
        
        interior_angle = (angle2 - angle1) % (2 * PI)
        
        if interior_angle > PI:
            interior_angle = 2 * PI - interior_angle
            angle1, angle2 = angle2, angle1

        is_right_angle = abs(interior_angle - PI/2) < 0.01
        
        angle_marker = VGroup()
        
        if is_right_angle:
            right_angle_size = radius * 0.7
            
            # Calculate points for the right angle marker
            point1 = p2 + right_angle_size * v1_unit
            point2 = p2 + right_angle_size * v2_unit
            corner = p2 + right_angle_size * (v1_unit + v2_unit)
            
            # Create the L-shaped marker
            line1 = Line(point1, corner, color=WHITE)
            line2 = Line(corner, point2, color=WHITE)
            
            angle_marker.add(line1, line2)
        else:
            arc = Arc(
                radius=radius,
                start_angle=angle1,
                angle=interior_angle,
                arc_center=p2,
                color=WHITE
            )
            angle_marker.add(arc)
        
        if label or label_as_angle:
            mid_angle = angle1 + interior_angle / 2
            label_pos = p2 + 1.75 * radius * np.array([
                np.cos(mid_angle),
                np.sin(mid_angle),
                0
            ])

            content = f"{round(interior_angle * DEGREES * 3600)}" if label_as_angle else label
            text = MathTex(content, color=self.get_color(), font_size=label_size)
            text.move_to(label_pos)
            angle_marker.add(text)
        
        return angle_marker
    
    def get_start_angle(self, p1: np.ndarray, p2: np.ndarray) -> tuple[int, int]:
        v1 = p1 - p2
        return np.arctan2(v1[1], v1[0])