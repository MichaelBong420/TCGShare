from Card import Card
from _helper_functions import *

class Prestream_jesse(Card):

    def on_death(self, app = None, index = None):
        #summon an extra unit
        unit = Card(6, 4, 5, "poststream jesse 6.4.5", app.font)
        #start unit with -1 energy so that it can't immediately attack
        unit.energy = 0

        unit.owner = self.owner

        unit.played = True
        
        app.field.fields[self.owner].insert(index, unit)

        unit.entry_animation(app)