from _helper_functions import *

from Card import Card

class Frantic_chef_jesse(Card):
    def on_play(self, app = None, index = None):
        self.energy = 1

        return 1