# Web Image
Load an image from a URL. The WebImage class is a subclass of ImageMobject, so it can be used in the same way as ImageMobject.

## Reference

```python
class WebImage(ImageMobject):
    def __init__(self, url, **kwargs)
```

- `url`: The URL of the image to load.

## Example

```python
from manim import *

from manim_kodisc import *


class WebImageExample(Scene):
    def construct(self):
        # any image url
        url = "https://picsum.photos/1024"
        web_image = WebImage(url)
        self.add(web_image)
        self.wait(2)
```