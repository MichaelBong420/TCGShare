from Card import Card

from _helper_functions import *

class Face_melter(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card has things to do before being entered
        self.satisfied = 0

        #card is a spell
        self.spell = 1

    async def on_play_spell(self, app):

        self.satisfied = 1

        set_targets(app, (1, 1, 1))
        
        #return self to be set as app.limbo
        return self

    async def on_cast(self, app = None, card = None, player = None, choice = None):

        #deal 6 dmg to selected target

        dmg = -10
        if card:
            card.update_stats(HP, dmg, app.font)

        elif player:
            player.update_hp(dmg, app.font)

        return None