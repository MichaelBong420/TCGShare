from Card import Card

from _helper_functions import *

class Mad_scientist_andy(Card):
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
            set_targets(app, (1, 1, 0))

            #next time on_play is called we want to say we're all good
            self.satisfied = 1

            #but for now we still need to select a card for on_entry from main
            #so return 0            
            return 0

    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

        #swap selected unit's atk and hp
        #temp for three handed swap
        if card and card != self:
            #update card's base stats to new base stats
            card.set_statsbase([card.stats[COST], card.stats[HP], card.stats[ATK]])

            #minus current stat and add new stat
            delta_atk =  - card.stats[ATK] + card.stats[HP]
            delta_newhp = - card.stats[HP] + card.stats[ATK]

            card.update_stats(ATK, delta_atk, app.font)
            card.update_stats(HP, delta_newhp, app.font)
            

        #reset app.limbo
        app.limbo = None


        set_targets(app)