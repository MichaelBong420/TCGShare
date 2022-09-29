from Card import Card

from _helper_functions import *

class Mayo_andy(Card):

    async def on_damage_deal(self, app = None, card = None):
        if card:
            if not card.shield:

                card.energy = -1
                card.stuck = 1