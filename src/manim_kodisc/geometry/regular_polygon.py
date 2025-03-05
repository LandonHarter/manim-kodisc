from manim import *

from .polygon import BetterPolygon


class BetterRegularPolygon(BetterPolygon):
    def __init__(self, n: int, **kwargs):
        self.n = n
        regular_polygon = RegularPolygon(n=n, **kwargs).scale(2)
        super().__init__(*regular_polygon.get_vertices(), **kwargs)