from Card import Card

from _helper_functions import *

class Centaurguy(Card):

    def on_play(self, app, index):

        #give all friendly units +2/+2

        buff = 2

        owner_field = app.field.fields[self.owner]

        for card in owner_field:
            if card != self:

                card.update_stats(ATK, buff, app.font)
                card.update_stats(HP, buff, app.font)
        
        
        #card doesn't need to do anything else so just return 1
        return 1