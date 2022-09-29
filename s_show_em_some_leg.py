from Card import Card

from _helper_functions import *

class Show_em_some_leg(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card is a spell
        self.spell = 1

    async def on_play_spell(self, app):

        set_targets(app, [1,1,0])
        
        #return self so that app knows we're selecting a card
        return self

    async def on_cast(self, app=None, card=None, player=None, choice=None):

        if card:
            #give card +4/+4

            card.update_stats(ATK, 4, app.font)
            card.update_stats(HP, 4, app.font)


        return None