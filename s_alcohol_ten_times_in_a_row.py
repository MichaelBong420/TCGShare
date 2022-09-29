from Card import Card

from _helper_functions import *

class Alcohol_ten_times_in_a_row(Card):
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
            #turn target card into 1/1

            card.__class__ = Card

            card.__init__(1, 1, 1, "broken levi 1.1.1", app.font)

            card.owner = self.owner
            card.played = 1

            #make sure card can't attack with haste
            card.energy = 0

        return None