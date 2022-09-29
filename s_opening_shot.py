from Card import Card

from _helper_functions import *

class Opening_shot(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card is a spell
        self.spell = 1


    async def on_play_spell(self, app):
        #return none so that app knows we're done
        return await app.cast_spell(card = self)


    async def on_cast(self, app = None, card = None, player = None, choice = None):
        #give owner +1 drinks this turn only
        app.players[self.owner].update_drinks(1, app.font)

        return None