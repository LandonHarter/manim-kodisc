# Better Polygon

The better polygon class is a subclass of the `Polygon` class in Manim. It adds a few extra features that make it easier to work with polygons.

## Reference

```python
class BetterPolygon(Polygon):
    def __init__(self, *vertices, **kwargs)
    def get_angles(self, angle_labels: list[str] = None, radius: float = 0.5, label_size: int = 24, label_as_angle=False) -> VGroup
    def get_angle(self, index: int, label: str = None, radius: float = 0.5, label_size: int = 24, label_as_angle=False) -> VGroup
```

### get_angles
Returns a `VGroup` of angle labels for each angle in the polygon.
- `angle_labels`: A list of labels for each angle in the polygon. If `None`, no labels will be added.
- `radius`: The radius (size) of the angle arc.
- `label_size`: The font size of the angle labels.
- `label_as_angle`: If `True`, the angle labels will be displayed as the angle measure. If `False`, the angle labels will be displayed as the given label.

### get_angle
`get_angle`: Returns a `VGroup` of a single angle label for the angle at the given index.
- `index`: The index of the angle in the polygon.
- `label`: The label for the angle. If `None`, no label will be added.
- `radius`: The radius (size) of the angle arc.
- `label_size`: The font size of the angle label.
- `label_as_angle`: If `True`, the angle label will be displayed as the angle measure. If `False`, the angle label will be displayed as the given label.

## Example

```python
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
        self.play(Create(polygon.get_angles(angle_labels=["a", "b", "c"], radius=0.6, label_size=30)))
        self.wait(5)
```