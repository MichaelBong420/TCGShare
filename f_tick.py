from _helper_functions import *

class Tick():
    def tick(self):
        #check if anything is dead and kill it if so
        #check if hp <=0 and delete + on_death
        for field in self.field.fields:
            for card in field:
                if card.stats[HP] <= 0:
                    #trigger the card's on death, and pass in its position
                    card.on_death(self, field.index(card))
                    #remove the card from the field
                    field.remove(card)

                    card.death_animation(self)

        #check if any players died
        for player in self.players:
            if player.hp <= 0:
                self.run = False
                print("Player ",player.num, " is dead!")


        #check which cards are playable
        player = self.players[self.turn]

        for card in player.hand:
            if card.stats[COST] <= player.drinks:
                card.playable = 1
            else:
                card.playable = 0