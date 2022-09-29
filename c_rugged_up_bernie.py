from _helper_functions import *

from Card import Card

class Rugged_up_bernie(Card):
    def __init__(self, cost, atk, hp, card_string, font):
        super().__init__(cost, atk, hp, card_string, font)
        self.shield = 1