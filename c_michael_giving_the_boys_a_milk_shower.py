from Card import Card
from _helper_functions import *

class Michael_giving_the_boys_a_milk_shower(Card):

    def on_death(self, app = None, index = None):
        #summon an extra unit
        unit = Card(1, 2, 2, "Milked Joey 2.2.2", app.font)
        #start unit with -1 energy so that it can't immediately attack
        unit.energy = 0

        unit.owner = self.owner

        unit.played = True

        field = app.field.fields[self.owner]

        field.insert(index, unit)

        unit.entry_animation(app)

        #if there's still room, + 1 as self hasn;t left field yet
        if len(field) < MAX_FIELD_SIZE + 1:
            #summon an extra unit
            unit = Card(1, 2, 2, "Milked Levi 2.2.2", app.font)
            #start unit with -1 energy so that it can't immediately attack
            unit.energy = 0

            unit.owner = self.owner

            unit.played = True

            field.insert(index, unit)

            unit.entry_animation(app)