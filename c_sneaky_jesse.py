from Card import Card
from _helper_functions import *

class Sneaky_jesse(Card):

    def on_death(self, app = None, index = None):

        #owner draws a card
        app.players[self.owner].draw_card()