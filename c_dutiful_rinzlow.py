from Card import Card

from _helper_functions import *

class Dutiful_rinzlow(Card):

    def on_play(self, app, index):
        #if there's still room
        if len(app.field.fields[self.owner]) < MAX_FIELD_SIZE:
            #summon an extra unit
            unit = Card(2,2,2, "dutiful michael 2.2.2", app.font)
            #start unit with -1 energy so that it can't immediately attack
            unit.energy = 0

            unit.owner = self.owner

            unit.chat_owner = self.chat_owner

            async def on_damage_deal(self, app = None, card=None):
                #award points to viewer who owns card
                await add_points(app, self.chat_owner, POINTS_PER_ATK)

            unit.on_damage_deal = types.MethodType(on_damage_deal, unit )

            unit.played = True

            unit.played = True

            app.field.fields[self.owner].insert(index + 1, unit)

            unit.entry_animation(app)
           
        return 1

    
    async def on_damage_deal(self, app = None, card=None):
        #award points to viewer who owns card
        await add_points(app, self.chat_owner, POINTS_PER_ATK)