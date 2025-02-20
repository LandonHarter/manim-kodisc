# Card

The card is a graphic of a playing card.

## Reference

```python
class CardSuit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3

def Flip(card: Card, **kwargs):
    card.face_up = not card.face_up
    def update(group, alpha):
        if (card.face_up):
            group.back.set_opacity(0)
        else:
            group.back.set_opacity(1)
    return AnimationGroup([Rotate(card, PI, axis=np.array([0, 1, 0]), **kwargs), UpdateFromAlphaFunc(card, update, **kwargs)], lag_ratio=0.5)

class Card(Group):
    def __init__(self, suit: CardSuit, number: int = 1, face_up: bool = True, card_radius=0.1, **kwargs)
```

### Constructor

- `suit`: The suit of the card. This is an instance of `CardSuit`.
- `number`: The number of the card. This is an integer from 1 to 13.
- `face_up`: Whether the card is face up or face down.
- `card_radius`: The border radius of the card.

### Flip

Flip is an animation that flips the card over.

- `card`: The card to flip.

## Example

```python
from manim import *
from manim_kodisc import *

class CardsExample(Scene):
    def construct(self):
        cards = Group()
        for i in range(10):
            card = Card(CardSuit.HEARTS, i + 1)
            row = i // 5
            col = i % 5
            card.move_to(LEFT * 4.5 + RIGHT * col * 2.25 + DOWN * row * 3.25 + UP * 1.5)
            cards.add(card)
            self.play(FadeIn(card, run_time=0.3))
            self.wait(0.25)
            self.play(Flip(card))
            self.wait(0.25)

        self.wait(2)

        self.play(card.animate.move_to(cards.get_center()) for card in cards)
        self.wait(2)
```