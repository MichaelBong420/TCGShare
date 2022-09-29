from _helper_functions import *

class Play_spell():
    async def play_spell(self, card):

        if not card.spell:
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

        
        #stop highlighting in hand
        card.playable = 0


        #remove from owner's hand
        player.hand.remove(card)

        #add to player until casted
        player.card = card

        #trigger card's on_play. if it returns 1, keep playing it as normal
        #else it needs another action - so return control back to main
        result = await card.on_play_spell(self)
        if result:
            return card
        
        else:
            return None