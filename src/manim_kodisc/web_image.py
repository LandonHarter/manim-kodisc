from io import BytesIO

import numpy as np
import requests
from manim import ImageMobject
from PIL import Image


class WebImage(ImageMobject):
    def __init__(self, url, **kwargs):
        self.url = url
        arr = self.load_image()
        super().__init__(arr, **kwargs)

    def load_image(self):
        response = requests.get(self.url)
        image = Image.open(BytesIO(response.content))
        np_array = np.array(image)
        return np_array