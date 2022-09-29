from _helper_functions import *

class Atk():
    async def atk(self, card0, card1):

        #check atking card has >0 atk
        if card0.stats[ATK] <= 0:
            return 0


        #check if enemy has a steadfast card
        has_steadfast = False
        enemy_field = self.field.fields[card1.owner]
        for card in enemy_field:
            if card.steadfast:
                has_steadfast = True
        
        if has_steadfast and not card1.steadfast:
            return 0



        #minus energy from card0
        card0.energy -= 1

        #card0 deals, card1 takes
        if card1.shield:
            card1.shield = 0

        else:
            #subtract card0 atk from card1
            card1.update_stats(HP, - card0.stats[ATK], self.font)

            #onhit
            await card0.on_damage_deal(self, card1)
            await card1.on_damage_take(self, card0)
            

        #card1 deals, card0 takes
        if card0.shield:
            card0.shield = 0
        else:
            #subtract card1 atk from card0
            card0.update_stats(HP, - card1.stats[ATK], self.font)

            #onhit
            await card1.on_damage_deal(self, card0)

            print(self)
            await card0.on_damage_take(self, card1)

        self.drop()