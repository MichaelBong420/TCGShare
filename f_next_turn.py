from time import sleep
from _helper_functions import *

from f_end_of_turn import *

class Next_turn(End_of_turn):
    def __init__(self) -> None:
        super().__init__()

    def next_turn(self):
        self.end_of_turn()

        #wipe cards on last turn player's field's energy
        #if they have energy > 0
        for card in self.field.fields[self.turn]:
            if card.energy > 0:
                card.energy = 0
            
            #primarily for funeral units' spawn
            # elif card.energy < 0:
                # card.energy += 1


        #swap players turns
        self.turn = int(not(self.turn))


        player = self.players[self.turn]
        player.draw_card()


        #refresh cards on field's energy
        for card in self.field.fields[self.turn]:
            card.energy += 1

            #if card is ready to be unstuck, turn stuck off
            if card.energy > 0:
                card.stuck = 0

        #add 1 drink total and refresh player's drinks
        if player.drinks_total < MAX_DRINKS:
            player.update_drinks_total(1, self.font)
        
        player.update_drinks(reset = True, font = self.font)

        set_targets(self)