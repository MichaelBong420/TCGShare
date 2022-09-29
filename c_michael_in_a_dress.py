from _helper_functions import *

from Card import Card

class Michael_in_a_dress(Card):
    def __init__(self, cost, atk, hp, card_string, font):
        super().__init__(cost, atk, hp, card_string, font)
        self.shield = 1