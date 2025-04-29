# Pi Chart

Construct a pie chart using the `PiChart` class. This class is a subclass of `VGroup` and is used to create pie charts in Manim.

## Reference

```python
class PiChart(VGroup):
    def __init__(self, data: dict[str, int], colors: list, show_labels=True, **kwargs)
```

- `data`: A dictionary with the data to be represented. The keys are the labels and the values are the sizes.
- `colors`: A list of colors to be used in the chart. Must be the same length as the number of data entries.
- `show_labels`: Whether to show the labels or not.

## Example

```python
from manim import *
from manim_kodisc import *

class PiChartExample(Scene):
    def construct(self):
        chart = PiChart(
            data={"A": 1, "B": 2, "C": 3},
            colors=[BLUE, GREEN, RED]
        )

        self.play(Write(chart))

        self.wait(2)
```