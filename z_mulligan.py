from time import sleep
from _helper_functions import *
import random

import pygame

from s_opening_shot import Opening_shot

class Mulligan():
    def __init__(self) -> None:
        self.confirm_button = load_image("confirm.png", CONFIRM_WIDTH, CONFIRM_HEIGHT)


    def mulligan_setup(self, player):

        self.mulligan_cards = []

        for i in range(3+player.num):
            drawn_card = random.choice(player.deck)
            player.deck.remove(drawn_card)

            drawn_card.mulligan = 1

            self.mulligan_cards.append(drawn_card)

    def mulligan_loop(self, player):
        #draw cards
        #draw background to wipe old pics away
        self.WIN.blit(self.background_img, (0, 0))

        #draw confirm button
        self.WIN.blit(self.confirm_button, (CONFIRM_X, CONFIRM_Y))

        for num, card in enumerate(self.mulligan_cards):

            card.pos = [CARD_WIDTH_MULLIGAN*num + MULLIGAN_X, MULLIGAN_Y]

            draw_card(self, card, ratio = MULLIGAN_RATIO)

        pygame.display.update()


    def mulligan_loop_main(self):
        #MULLIGAN PHASE
        # self.build_deck_phase = True

        for player in self.players:

            decided = 0

            self.mulligan_setup(player)


            while not decided:

                self.clock.tick(FPS)

                self.mulligan_loop(player)
                
                for event in pygame.event.get():

                    #mousebutton left click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            for card in self.mulligan_cards:
                                if card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(pygame.mouse.get_pos()):
                                    card.mulligan = not card.mulligan

                            if self.confirm_button.get_rect(x = CONFIRM_X, y = CONFIRM_Y).collidepoint(event.pos):
                                self.mulligan_finish(player)
                                decided = 1


    def mulligan_finish(self, player):

        #wipe old images
        self.WIN.blit(self.background_img, (0,0))

        for num, card in enumerate(self.mulligan_cards):
            if card.mulligan:
                player.hand.append(card)

            else:
                # #remove card from mulligan cards
                self.mulligan_cards.remove(card)

                #draw new card to replace mulligan'd card
                drawn_card = random.choice(player.deck)
                player.deck.remove(drawn_card)
                player.hand.append(drawn_card)

                #put card back in deck at random point (done after so that it's not redrawn)
                random_index = random.randint(0, DECK_SIZE)
                player.deck.insert(random_index, card)

                #change card to drawn_card so that it's shown as being drawn
                #first update drawn_card pos so it replaces card
                drawn_card.pos = card.pos.copy()
                card = drawn_card

                self.mulligan_cards.append(card)

            #set owner
            card.owner = player.num

        
        #give player one the extra shot to compensate going second
        if player.num:
            unit = Opening_shot(0, "Opening shot 0", self.font)
            
            player.hand.append(unit)
            self.mulligan_cards.append(unit)

            unit.owner = player.num

            unit.pos = [CARD_WIDTH_MULLIGAN*4 + MULLIGAN_X, MULLIGAN_Y]


        for num, card in enumerate(self.mulligan_cards):
            if card.mulligan:
                card.mulligan = False
                draw_card(self, card, ratio = MULLIGAN_RATIO)

        pygame.display.update()

        sleep(2)

        for num, card in enumerate(self.mulligan_cards):
            if not card.mulligan:
                draw_card(self, card, ratio = MULLIGAN_RATIO)

                pygame.display.update()

                sleep(1)

        sleep(5)



            

        
        