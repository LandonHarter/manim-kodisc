# Force Diagram

The force diagram is great for modeling the forces acting on an object. It uses arrows to represent the forces and can be used to visualize the net force acting on an object. The length and direction of the arrows represent the magnitude and direction of the forces, respectively.

## Reference

```python
class ForceDiagram(VGroup):
    def __init__(self, object, **kwargs)
    def add_force(self, magnitude, angle, text = "", text_side = RIGHT, equal_length = False)
```

### Constructor
- `object`: The object that the forces are acting on. This can be a `Circle`, `Square`, or any other `Mobject`.

### add_force
- `magnitude`: The magnitude of the force.
- `angle`: The angle of the force in radians. Based on the unit circle, where 0 is to the right and π/2 is up.
- `text`: The text to display next to the force arrow.
- `text_side`: The side of the arrow to place the text.
- `equal_length`: This will add a marking on the arrow to indicate equal magnitude.
Returns a VGroup containing the force arrow, text, and any other markings.

## Example

```python
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
        self.play(Uncreate(gravity))
        self.wait(1)
        self.play(Uncreate(normal))
        self.wait(1)
```