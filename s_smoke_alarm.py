from Card import Card

from _helper_functions import *

class Smoke_alarm(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card is a spell
        self.spell = 1

    async def on_play_spell(self, app):
        #return none so that app knows we're done
        return await app.cast_spell(self)


    async def on_cast(self, app = None, card = None, player = None, choice = None):
        #draw two cards
        num = 4
        for i in range(num):
            app.players[self.owner].draw_card()

        return None