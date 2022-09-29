from _helper_functions import *

from Card import Card

class Steadfast_jesse(Card):
    def on_play(self, app = None, index = None):
        self.steadfast = 1

        return 1

    async def on_damage_take(self, app = None, card=None):
        #award points to viewer who owns card
        # await asyncio.sleep(2)
        await add_points(app, self.chat_owner, POINTS_PER_HP)