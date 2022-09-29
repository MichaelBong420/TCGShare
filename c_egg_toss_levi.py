from Card import Card

from _helper_functions import *

class Egg_toss_levi(Card):
    def __init__(self, card_string, font, cost, atk, hp):
        super().__init__(card_string, font, cost, atk, hp)

    def on_play(self, app, index):
        #discard a random card
        app.players[self.owner].discard_card(app, self)

        return self.satisfied