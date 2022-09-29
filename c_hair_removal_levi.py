from Card import Card

from _helper_functions import *

class Hair_removal_levi(Card):

    def on_play(self, app, index):
        #if there's still room
        if len(app.field.fields[self.owner]) < MAX_FIELD_SIZE:
            #summon an extra unit
            unit = Card(1, 1, 1, "Levi's Hair 1.1.1", app.font)
            #start unit with -1 energy so that it can't immediately attack
            unit.energy = 0

            unit.owner = self.owner

            unit.played = True

            app.field.fields[self.owner].insert(index + 1, unit)

            unit.entry_animation(app)
           
        return 1