from Card import Card

from _helper_functions import *

class Rinzlows_tts(Card):
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

        #deal 3 dmg and stuck to selected target
        dmg = -3
        if card:
            if card.shield:
                card.shield = 0

            else:
                card.update_stats(HP, dmg, app.font)
                card.stuck = 1
                card.energy = -1

        elif player:
            player.update_hp(dmg, app.font)

        return None