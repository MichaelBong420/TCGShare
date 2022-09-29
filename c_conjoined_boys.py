from Card import Card

from _helper_functions import *

class Conjoined_boys(Card):

    def on_play(self, app, index):

        buff = 1

        owner_field = app.field.fields[self.owner]

        index = min(index, len(owner_field) - 1)

        if index - 1 >= 0:
            #give card +1/+1
            card = owner_field[index - 1]
            card.update_stats(ATK, buff, app.font)
            card.update_stats(HP, buff, app.font)

            #and steadfast
            card.steadfast = 1

        if index + 1 <= len(owner_field) - 1:

            #give card +1/+1
            card = owner_field[index + 1]
            card.update_stats(ATK, buff, app.font)
            card.update_stats(HP, buff, app.font)

            #and steadfast
            card.steadfast = 1
        
        
        #card doesn't need to do anything else so just return 1
        return 1