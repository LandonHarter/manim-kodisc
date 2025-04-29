# Rotating Function

Allows for a 2D function to be rotated around a 3D graph, forming a 3D shape.

## Reference

```python
class RotatingFunction(VMobject):
    def __init__(self, func, axis=[1, 0], color=BLUE, opacity=0.5, x_range=[-1, 1], **kwargs)
    def rotate(self, angle=2*PI)
```

## Example

```python
from manim import *
from manim_kodisc import *

class RotatingFunctionExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.rotating_function = RotatingFunction(lambda x: x**3, axis=[0, 1], color=RED, opacity=0.5, x_range=[-2, 2])
        self.add(self.rotating_function)

        self.play(self.rotating_function.rotate(2 * PI), run_time=5)
        self.wait(2)
```