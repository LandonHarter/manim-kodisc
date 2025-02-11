# Slope Field

The slope field is a graphical representation of the solutions to a first-order differential equation. It is a grid of short line segments, each of which represents the slope of the solution at a particular point. The slope field can be used to visualize the behavior of the solutions and to estimate the shape of the solution curves.

## Reference

```python
class SlopeField(VGroup):
    def __init__(self, func, x_range=(-10, 10), y_range=(-10, 10), step_size=1, **kwargs)
```

- `func`: The function that defines the slope field.
- `x_range`: The range of x-values over which to draw the slope field.
- `y_range`: The range of y-values over which to draw the slope field.
- `step_size`: How dense the grid of line segments should be.

## Example

```python
from manim import *
from manim_kodisc import *

class SlopeFieldExample(Scene):
    def construct(self):
        slope_field = SlopeField(
            lambda x: np.sin(x),
            x_range=(-5, 5),
            y_range=(-5, 5),
            step_size=0.5,
        )
        self.play(Write(slope_field))

        self.wait(0.5)
        self.play(Write(slope_field.axes.plot(slope_field.func, color=BLUE)))

        self.wait(5)
```