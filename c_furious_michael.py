from Card import Card

from _helper_functions import *

class Furious_michael(Card):
    def __init__(self, card_string, font, cost, atk, hp):
        super().__init__(card_string, font, cost, atk, hp)

        #card has things to do before being entered
        self.satisfied = 0

    def on_play(self, app, index):
        #if satisfied, we already did on_play
        if self.satisfied:
            return self.satisfied
        else:
            #if field is empty, just play card without entry
            if not len(app.field.fields[self.owner]) - 1 and not len(app.field.fields[not(self.owner)]):
                self.satisfied = 1
                return self.satisfied

            #otherwise tell main that we have something to do before being played

            #save playpos for later, namely on_entry
            self.playpos = index

            #set targetables
            app.fcard = 1
            app.ecard = 1
            app.pcard = 0

            #next time on_play is called we want to say we're all good
            self.satisfied = 1

            #but for now we still need to select a card for on_entry from main
            #so return 0            
            return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #give selected unit +2 atk for this turn only
        if card and card != self:
            #+2 atk
            card.update_stats(ATK, 2, app.font)

            #for this turn only
            command = "?.update_stats(ATK, -2, self.font)"
            args = [card]
            app.add_end_command(command, args)
            

        #reset app.limbo
        app.limbo = None

        #set targetables
        app.fcard = 1
        app.ecard = 0
        app.pcard = 0