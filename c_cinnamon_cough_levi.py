from Card import Card

from _helper_functions import *

class Cinnamon_cough_levi(Card):

    def on_play(self, app, index):

        #save playpos for later, namely on_entry
        self.playpos = index

        #set targetables
        set_targets(app, (1, 1, 1))
         
        return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #deal 1 damage to target
        dmg = -1

        if card and card != self:
            if card.shield:
                card.shield = 0
            else:
                card.update_stats(HP, dmg, app.font)

        elif player:
            player.update_hp(dmg, app.font)
            

        #reset app.limbo
        app.limbo = None


        set_targets(app)