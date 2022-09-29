from _helper_functions import *

class Check_playpos():

    def check_playpos(self, pos, player):
        '''check what position on the board a player tried to play a card
        returns what index the card should be inserted into the field'''

        # #first check if cards in player's hand are odd or even
        # if not len(player.hand) % 2:
        #     #hand contains even cards, so use the even pos array
        #     pos_array = self.field.pos_play_matrix[1]
        
        # else:
        #     #hand contains odd cards, so use the odd pos array
        #     pos_array = self.field.pos_play_matrix[0] 

        if len(self.field.fields[player.num]) >= MAX_FIELD_SIZE:
            return -1

        pos_array = self.field.pos_matrix[len(self.field.fields[player.num])]

        
        #scan through pos_array and see what segment played card is in
        for i in range(1, len(pos_array)):
            #if the x coord is less than the current element, and more than the prev element
            if pos[0] < pos_array[i] and pos[0] > pos_array[i-1]:
                #it must be being played between those two positions
                return i - 1

        #if not, it must be on either far end
        #check far left
        if pos[0] < pos_array[0]:
            return 0

        #check far right, and return l
        else:
            return MAX_FIELD_SIZE
