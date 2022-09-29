from Card import Card

from _helper_functions import *

class Iberique_first_sub(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card is a spell
        self.spell = 1

        self.chat_owner = "Megsyy"

    async def on_play_spell(self, app):

        #award points to viewer who owns card
        await add_points(app, self.chat_owner, POINTS_PER_DRAW*2)

        #return none so that app knows we're done
        return await app.cast_spell(self)


    async def on_cast(self, app = None, card = None, player = None, choice = None):
        #draw two cards
        for i in range(2):
            app.players[self.owner].draw_card()

        return None