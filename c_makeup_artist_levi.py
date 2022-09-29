from Card import Card

from _helper_functions import *

class Makeup_artist_levi(Card):
    def __init__(self, card_string, font, cost, atk, hp):
        super().__init__(card_string, font, cost, atk, hp)

        #card has things to do before being entered
        self.satisfied = 0

    def on_play(self, app, index):

        #save playpos for later, namely on_entry
        self.playpos = index

        #set targetables
        set_targets(app, (1, 1, 0))
         
        return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #stuck target
    
        if card and card != self:
            card.energy = -1
            card.stuck = 1
            

        #reset app.limbo
        app.limbo = None


        set_targets(app)