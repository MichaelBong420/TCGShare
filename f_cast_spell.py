from _helper_functions import *

class Cast_spell():
    async def cast_spell(self, card = None, player = None, choice = None):
        '''cast the self.limbo spell, or a custom input card spell
        if self.limbo, input card should be target, else input card is card being played'''

        if self.limbo:
            output = await self.limbo.on_cast(self, card, player, choice)

            #wipe from player.card
            self.players[self.limbo.owner].card = None

        else:
            output = await card.on_cast(self, card, player, choice)

            #wipe from player.card
            self.players[card.owner].card = None


        

        set_targets(self)


        return output