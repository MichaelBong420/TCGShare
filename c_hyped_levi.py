from Card import Card

from _helper_functions import *

class Hyped_levi(Card):

    def on_play(self, app, index):

        #save playpos for later, namely on_entry
        self.playpos = index

        #set targetables
        set_targets(app, (1, 1, 1))
        
        return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #heal 3 hp to target
        dmg = 3


        heal_target(app, dmg, card, player)


        #reset app.limbo
        app.limbo = None


        set_targets(app)