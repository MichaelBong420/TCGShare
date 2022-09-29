from _helper_functions import *

class Play_card():
    def play_card(self, card, playpos = -1):
        
        if not len(self.field.fields[self.turn]) < MAX_FIELD_SIZE:
            return None

        player = self.players[card.owner]
        #check if player has enough drinks to play
        if player.drinks < card.stats[COST]:
            return None

        else:
            player.update_drinks(drinks = - card.stats[COST], font = self.font)

        # drop card if it was being dragged
        if self.drag:
            self.drop()

        #pass the card to the field and remove from hand
        #append to the owner's field
        #used passed in position
        self.field.fields[card.owner].insert(playpos, card)

        #remove from owner's hand
        player.hand.remove(card)

        card.entry_animation(self)

        #stop highlighting in hand
        card.playable = 0

        #hover logic
        card.played = True

        #trigger card's on_play. if it returns 1, keep playing it as normal
        #else it needs another action - so return control back to main
        if not card.on_play(self, playpos):
            return card

        #once card is completely finished, wipe self.limbo
        return None