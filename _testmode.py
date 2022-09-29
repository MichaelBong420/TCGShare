from _helper_functions import *

from cards import *


# from _main import *

class Test_mode():
    def test_mode(self):
        for player in self.players:
            #give a deck
            player.deck = all_cards(self.font)

            #give 6 mana
            player.update_drinks_total(8, self.font)
            player.update_drinks(font = self.font, reset = True)


            #add 2 test cards to hand
            for i in range(2):
                # unit = Test(0, "testcard", self.font)
                unit = Butthurt_chat(5, "butthurt chat 5", self.font)
                unit.owner = player.num
                player.hand.append(unit)

            #add 2 test cards to hand
            for i in range(2):
                # unit = Test(0, "testcard", self.font)
                unit = Steadfast_jesse(8,8,8, "steadfast jesse 8.8.8", self.font)
                unit.owner = player.num
                player.hand.append(unit)


            #give 5 cards
            # for i in range(5):
            #     player.draw_card()


            # #add 2 test cards to hand
            # for i in range(2):
            #     # unit = Test(0, "testcard", self.font)
            #     unit = Dutiful_rinzlow(5,4,4, "dutiful rinzlow 5.4.4", self.font)
            #     unit.owner = player.num
            #     player.hand.append(unit)

            # #add 2 test cards to hand
            # for i in range(2):
            #     # unit = Test(0, "testcard", self.font)
            #     unit = Some_random_crazy_bitch_with_a_knife(9,8,8, "some random crazy bitch with a knife 9.8.8", self.font)
            #     unit.owner = player.num
            #     player.hand.append(unit)