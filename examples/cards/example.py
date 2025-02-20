from manim import *

from manim_kodisc import *


class CardsExample(Scene):
    def construct(self):
        cards = Group()
        for i in range(10):
            card = Card(CardSuit.HEARTS, i + 1, face_up=True)
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