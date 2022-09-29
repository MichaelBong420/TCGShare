from Card import Card

from _helper_functions import *

class Two_pistol_levi(Card):
    def __init__(self, card_string, font, cost, atk, hp):
        super().__init__(card_string, font, cost, atk, hp)

        #card has things to do before being entered
        self.satisfied = 0

    def on_play(self, app, index):

        #save playpos for later, namely on_entry
        self.playpos = index

        #set targetables
        set_targets(app, (1, 1, 1))
         
        return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #deal two damage to target
        dmg = -2

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