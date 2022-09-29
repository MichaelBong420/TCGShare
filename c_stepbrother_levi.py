from Card import Card

from _helper_functions import *

class Stepbrother_levi(Card):

    def on_play(self, app, index):

        #save playpos for later, namely on_entry
        self.playpos = index

        #set targetables
        set_targets(app, (1, 0, 0))
        
        return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #give +1/+1 to target
        buff = 1


        card.update_stats(ATK, buff, app.font)
        card.update_stats(HP, buff, app.font)


        #reset app.limbo
        app.limbo = None


        set_targets(app)