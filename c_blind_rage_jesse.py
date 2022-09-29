from _helper_functions import *

from Card import Card

class Blind_rage_jesse(Card):
    def __init__(self, cost, atk, hp, card_string, font):
        super().__init__(cost, atk, hp, card_string, font)
        self.shield = 1
    
    def on_play(self, app, index):
        self.energy = 1

        return 1