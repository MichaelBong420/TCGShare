from _helper_functions import *

class Atk_player():
    async def atk_player(self, card, player):

        #check atking card has >0 atk
        if card.stats[ATK] <= 0:
            return 0


        #check if enemy has a steadfast card
        enemy_field = self.field.fields[player.num]
        for card_check in enemy_field:
            if card_check.steadfast:
                return 0

        await card.on_damage_deal(self)

        #minus energy from card
        card.energy -= 1

        #subtract card atk from player
        player.update_hp(- card.stats[ATK], self.font)

        #drop the card
        self.drop()