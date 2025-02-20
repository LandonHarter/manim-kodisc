from enum import Enum

import numpy as np
from manim import *


class CardSuit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3

class Card(Group):
    def __init__(self, suit: CardSuit, number: int = 1, face_up: bool = True, card_radius=0.1, **kwargs):
        super().__init__(**kwargs)
        self.suit = suit
        self.number = number
        self.face_up = face_up
        self.card_radius = card_radius
        
        card = RoundedRectangle(width=2, height=3, corner_radius=card_radius, color=WHITE, fill_opacity=1)
        
        suit_element1 = self.get_suit(30)
        suit_element1.move_to(LEFT * 0.7 + UP * 0.9 + card.get_center())

        number_element1 = self.get_number()
        number_element1.move_to(LEFT * 0.7 + UP * 1.25 + card.get_center())

        suit_element2 = self.get_suit(30)
        suit_element2.rotate(PI)
        suit_element2.move_to(RIGHT * 0.7 + DOWN * 0.9 + card.get_center())

        number_element2 = self.get_number()
        number_element2.rotate(PI)
        number_element2.move_to(RIGHT * 0.7 + DOWN * 1.25 + card.get_center())

        picture = self.get_picture()
        picture.move_to(card.get_center())

        self.back = self.get_back()
        self.back.set_opacity(0)

        self.add(card, suit_element1, number_element1, suit_element2, number_element2, picture, self.back)

    def get_suit(self, size=45):
        if self.suit == CardSuit.HEARTS:
            return Text("♥", font_size=size, color=RED)
        elif self.suit == CardSuit.DIAMONDS:
            return Text("♦", font_size=size, color=RED)
        elif self.suit == CardSuit.CLUBS:
            return Text("♣", font_size=size, color=BLACK)
        elif self.suit == CardSuit.SPADES:
            return Text("♠", font_size=size, color=BLACK)
    
    def get_number(self):
        return Text(str(self.format_number()), font_size=26, color=BLACK)
    
    def get_picture(self):
        group = Group()
        group.add(self.get_suit())

        return group
    
    def get_back(self):
        return RoundedRectangle(width=2, height=3, fill_color=BLUE, corner_radius=self.card_radius, fill_opacity=1)
    
    def format_number(self):
        if self.number == 1:
            return "A"
        elif self.number == 11:
            return "J"
        elif self.number == 12:
            return "Q"
        elif self.number == 13:
            return "K"
        else:
            return str(self.number)

def Flip(card: Card, **kwargs):
    card.face_up = not card.face_up
    def update(group, alpha):
        if (card.face_up):
            group.back.set_opacity(0)
        else:
            group.back.set_opacity(1)
    return AnimationGroup([Rotate(card, PI, axis=np.array([0, 1, 0]), **kwargs), UpdateFromAlphaFunc(card, update, **kwargs)], lag_ratio=0.5)
