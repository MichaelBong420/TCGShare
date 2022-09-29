from _helper_functions import *

class Play_card():
    def play_card(self, num = 0):
        player = self.get_player_turn()
        print(player.drinks, self.turn)



        #if hand is empty, skip
        if not len(player.hand):
            return

        #if card needs to do something before being played, it will return 0
        if not self.current_card.on_play(self):
            return


        #if that's all good:
        #if there's room on the field, and player has enough drinks to play card
        if len(self.field.fields[self.player_turn]) < MAX_FIELD_SIZE and player.drinks >= self.current_card.cost:
            #subtract cost from player's drinks
            player.update_drinks(player.drinks - self.current_card.cost)
            
            #update card location to field
            self.current_card.location = FIELD
            #pass to player's field
            self.field.fields[self.player_turn].append(self.current_card)
            #remove from player's hand
            player.hand.pop()

            #if card is doubly satisfied (=2), it has already done its on entry
            if self.current_card.satisfied != 2:
                #if num is not used
                if not num:
                    self.current_card.on_entry(self)
                else:
                    self.current_card.on_entry(self, num)

            #after this, if hand is not empty, update current card
            if len(player.hand) > 0:
                self.current_card = player.hand[-1]
                self.current_card_image = pygame.transform.scale(self.current_card.fullresimg, (CARD_WIDTH_CURRENT, CARD_HEIGHT_CURRENT))

            #otherwise wipe the current cards
            else:
                self.current_card = None
                self.current_card_image = None