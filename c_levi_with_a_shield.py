from Card import Card

from _helper_functions import *

class Levi_with_a_shield(Card):
    def __init__(self, card_string, font, cost, atk, hp):
        super().__init__(card_string, font, cost, atk, hp)

        #card has things to do before being entered
        self.satisfied = 0

    def on_play(self, app, index):
        
        #if enemy field is empty (-1 because not including self), just play card without entry
        if not len(app.field.fields[1-self.owner]):
            self.satisfied = 1
            return self.satisfied

        #otherwise tell main that we have something to do before being played

        #save playpos for later, namely on_entry
        self.playpos = index

        #set targetables
        set_targets(app, (0, 1, 0))

        #next time on_play is called we want to say we're all good
        self.satisfied = 1

        #but for now we still need to select a card for on_entry from main
        #so return 0            
        return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #set selected unit to 1 atk
        if card and card != self:
            #set atk to 1
            card.statsbase[ATK] = 1
            card.update_stats(ATK, - card.stats[ATK] + 1, app.font)
            

        #reset app.limbo
        app.limbo = None

        set_targets(app)