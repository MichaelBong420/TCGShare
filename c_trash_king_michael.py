from Card import Card

from _helper_functions import *

class Trash_king_michael(Card):

    def on_play(self, app, index):
        #how many OTHER (-1) units on owners field
        num = len(app.field.fields[self.owner]) - 1

        self.update_stats(ATK, num, app.font)
        self.set_statsbase()
        self.update_stats(HP, num, app.font)
        self.set_statsbase()
           
        return 1