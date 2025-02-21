from manim import *

from manim_kodisc import *


class WebImageExample(Scene):
    def construct(self):
        # any image url
        url = "https://picsum.photos/1024"
        web_image = WebImage(url)
        self.add(web_image)
        self.wait(2)