from Card import Card

from _helper_functions import *

class Sculling_rinzlow(Card):
    
    def on_play(self, app, index):
        self.energy = 1
        #discard 2 random cards
        app.players[self.owner].discard_card(app, self)
        app.players[self.owner].discard_card(app, self)

        return 1