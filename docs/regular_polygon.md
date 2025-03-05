# Better Regular Polygon

The better regular polygon class is a subclass of the `BetterPolygon` class in manim-kodisc.

## Reference

```python
class BetterPolygon(Polygon):
    def __init__(self, n: int, **kwargs)
```

- `n` : The number of sides of the polygon.
- `kwargs` : Additional arguments to be passed to the `Polygon` class.

## Example

```python
from manim import *
from manim_kodisc import *

class RegularPolygonExample(Scene):
    def construct(self):
        polygon = BetterRegularPolygon(n=8)
        self.play(Create(polygon))
        self.wait(1)
        self.play(Create(polygon.get_angles(radius=0.3, label_as_angle=True)))
        self.wait(5)
```