from Card import Card

from _helper_functions import *

class Tuna_breath_levi(Card):

    async def on_damage_deal(self, card = None):
        if card:
            card.stats[HP] = 0