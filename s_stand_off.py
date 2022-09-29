from Card import Card

from _helper_functions import *

class Stand_off(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card is a spell
        self.spell = 1

    async def on_play_spell(self, app):
        
        #call cast_spell and return none so that app knows we're done
        return await app.cast_spell(self)

    async def on_cast(self, app = None, card = None, player = None, choice = None):
        #deal two damage to all enemies
        dmg = -3

        for field in app.field.fields:

            for card in field:

                if card.shield:

                    card.shield = 0

                else:

                    card.update_stats(HP, dmg, app.font)

        #and players
        for player in app.players:
           player.update_hp(dmg, app.font)

        return None