from Card import Card

from _helper_functions import *

class Test(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card is a spell
        self.spell = 1


    async def on_play_spell(self, app):
        #return none so that app knows we're done
        return await app.cast_spell(card = self)


    async def on_cast(self, app = None, card = None, player = None, choice = None):
        #give owner +1 drinks this turn only
        app.players[self.owner].update_drinks(1, app.font)

        return None

# from Card import Card

# from _helper_functions import *

# class Test(Card):
#     def __init__(self, cost, card_string, font):
        
#         #spells have no atk or hp
#         atk, hp = "", ""
#         super().__init__(cost, atk, hp, card_string, font)

#         #card has things to do before being entered
#         self.satisfied = 0

#         #card is a spell
#         self.spell = 1

#     def on_play(self, app):
#         #if satisfied, we already did on_play
#         if self.satisfied:
#             return None

#         else:
#             self.satisfied = 1

#             set_targets(app, (1, 1, 1))
            
#             #return self to be set as app.limbo
#             return self

#     async def on_cast(self, app = None, card = None, player = None, choice = None):
#         #reset app.limbo
#         app.limbo = None

#         #deal 6 dmg to selected target
#         if card:
#             card.update_stats(HP, -6, app.font)

#         elif player:
#             player.update_hp(-6, app.font)

#         set_targets(app)

#         #remove card from hand
#         app.drop()
#         app.players[self.owner].hand.remove(self)

# class Test(Card):
#     def __init__(self, card_string, font, cost, atk, hp):
#         super().__init__(card_string, font, cost, atk, hp)

#     def on_death(self, app = None, index = None):
#         #summon 2 extra units if room on the board
#         card_strings = ["Milked Joey 2.2.2", "Milked Levi 2.2.2"]

#         for i in range(2):
#             #if there's room on the field. <= used so that both units can spawn if there's 7 spots
#                 #before death, as card is removed the instant after these spawns
#             if len(app.field.fields[self.owner]) <= MAX_FIELD_SIZE:
#                 #summon an extra unit
#                 unit = Card(1, 2, 2, card_strings[i], app.font)
#                 #start unit with -1 energy so that it can't immediately attack
#                 unit.energy = 0
#                 app.field.fields[self.owner].insert(index, unit)

        #card has things to do before being entered
        # self.satisfied = 0

    # def on_damage_deal(self, card = None):
    #     card.energy = 0
    #     card.stuck = 1

    # def on_play(self, app, index):

    #     #if satisfied, we already did on_play
    #     if self.satisfied:
    #         return self.satisfied
    #     else:
    #         #if field is empty, just play card without entry
    #         if not len(app.field.fields[self.owner]) and not len(app.field.fields[not(self.owner)]):
    #             self.satisfied = 1
    #             return self.satisfied

    #         #otherwise tell main that we have something to do before being played

    #         #save playpos for later, namely on_entry
    #         self.playpos = index

    #         #set targetables
    #         set_targets(app, 1, 1, 0)

    #         #next time on_play is called we want to say we're all good
    #         self.satisfied = 1

    #         #but for now we still need to select a card for on_entry from main
    #         #so return 0            
    #         return 0

    # def on_entry(self, app = None, card = None, index = None, choice = None, player = None):

    #     #give selected unit +2 atk for this turn only
    #     if card:
    #         if card.shield:
    #             card.shield = 0
    #         else:
    #             #+2 atk
    #             card.update_stats(ATK, 2, app.font)
    #             #-1 hp
    #             card.update_stats(HP, -1, app.font)
            

    #     #try to play card again
    #     app.limbo = app.play_card(self, self.playpos)


    #     #set targetables
        # set_targets(app)