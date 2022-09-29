from time import sleep
from _helper_functions import *
import random

import pygame

from cards import *

import pickle


class Deck_build():
    def __init__(self) -> None:
        self.all_cards = all_cards(font = self.font)

        self.histogram_img = load_image("drink full.png", HIST_WIDTH, HIST_HEIGHT)

    
    def draw_histogram(self, player):

        #generate list of costs of each card in player deck
        costs = []

        for card in player.deck:
            costs.append(card.stats[COST])

        
        #generate historgram
        for i in range(11):
            #draw the x axis
            img = self.font.render(str(i), True, "WHITE")
            self.WIN.blit(img, (HIST_X + i * HIST_X_SPACER, HIST_Y))


            #count how many cards have cost of i
            num = costs.count(i)

            #draw the bar graph
            for j in range(num):
                self.WIN.blit(self.histogram_img, (HIST_X + i * HIST_X_SPACER, HIST_Y - (j + 1) * HIST_HEIGHT))


    def build_turn(self):
        #create empty list to fill with 3 random options
        self.options = []

        #select 3 random cards and add to options
        for i in range(3):
            drawn_card = random.choice(self.all_cards)
            self.all_cards.remove(drawn_card)

            self.options.append(drawn_card)


    def build_loop(self, player, turn):
        #draw cards
        #draw background to wipe old pics away
        self.WIN.blit(self.background_img, (0, 0))


        for num, card in enumerate(self.options):

            card.pos = [CARD_WIDTH*num + 30, 30]

            draw_card(self, card, ratio = MULLIGAN_RATIO)


        #mana curve
        self.draw_histogram(player)


        #cards left
        img = self.font.render("Cards Picked: " + str(turn) + " / " + str(DECK_SIZE), True, "WHITE")
        self.WIN.blit(img, (HIST_X - 8 * HIST_X_SPACER, HIST_Y))

        pygame.display.update()


    def build_loop_main(self):
        #BUILD DECK PHASE
        self.build_deck_phase = True

        for player in self.players:
            choice = int(input(f"Player{player.num} do you want to use the saved deck? type 0 or 1 for no or yes:"))

            if choice:
                file = open(f"player{player.num} deck", "rb")

                player.deck = pickle.load(file)

                file.close()

                player.choice = choice


        for i in range(DECK_SIZE):
            for player in self.players:
                if player.choice:
                    continue
                
                decided = 0
                self.build_turn()

                self.build_loop(player, i)


                while not decided:
                    self.clock.tick(FPS)
                    
                    for event in pygame.event.get():

                        #mousebutton left click
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                for card in self.options:
                                    if card.fullresimg.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(pygame.mouse.get_pos()):

                                        self.options.remove(card)
                                        player.deck.append(card)
                                        self.all_cards.extend(self.options)

                                        self.build_discard(self.options, card)

                                        decided = 1
        
        for player in self.players:
            file = open(f"player{player.num} deck", "wb")

            pickle.dump(player.deck, file)
            
            file.close()


    def build_discard(self, cards, card):

        alpha = 255

        for i in range(FPS):

            #draw background to wipe old images
            self.WIN.blit(self.background_img, (0, 0))

            #draw kept card
            draw_card(self, card, ratio = MULLIGAN_RATIO)

            #fade out
            alpha -= 255 / FPS

            draw_card(self, cards[0], ratio = MULLIGAN_RATIO, alpha=alpha)
            draw_card(self, cards[1], ratio = MULLIGAN_RATIO, alpha=alpha)

            pygame.display.update()

            self.clock.tick(FPS)



    def draw_histogram_allcards(self, allcards):

        #generate list of costs of each card in player deck
        costs = []

        for num, card in enumerate(allcards):
            if num % 2:
                costs.append(card.stats[COST])

        
        #generate historgram
        for i in range(11):
            #draw the x axis
            img = self.font.render(str(i), True, "WHITE")
            self.WIN.blit(img, (HIST_X + i * HIST_X_SPACER, HIST_Y))


            #count how many cards have cost of i
            num = costs.count(i)

            #draw the bar graph
            for j in range(num):
                self.WIN.blit(self.histogram_img, (HIST_X + i * HIST_X_SPACER, HIST_Y - (j + 1) * HIST_HEIGHT))

        pygame.display.update()

        input()