from _helper_functions import *

from Card import Card

class Sunwalker(Card):
    def __init__(self, cost, atk, hp, card_string, font):
        super().__init__(cost, atk, hp, card_string, font)
        self.shield = 1
        self.steadfast = 1