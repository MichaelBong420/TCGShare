from _helper_functions import *

from Card import Card

class Some_random_crazy_bitch_with_a_knife(Card):
    def on_play(self, app = None, index = None):
        self.energy = 1

        return 1

    
    async def on_damage_deal(self, app = None, card=None):
        #award points to viewer who owns card
        await add_points(app, self.chat_owner, POINTS_PER_ATK)

    # async def on_damage_take(self, app = None, card=None):
    #     #award points to viewer who owns card
    #     await add_points(app, self.chat_owner, POINTS_PER_HP)