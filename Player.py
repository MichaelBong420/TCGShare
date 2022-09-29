import pygame
from _helper_functions import *

import random

class Player():
    def __init__(self, deck, num, font):
        
        self.num = num

        self.deck = deck
        
        self.hand = []

        self.choice = 0

        #----FACE----#
        self.pos = [PLAYER_FRAME_X, PLAYER_FRAME_Y[self.num]]
        self.img = load_image("player frame.png", PLAYER_FRAME_WIDTH, PLAYER_FRAME_HEIGHT)
        self.rect = self.img.get_rect(x = self.pos[0], y = self.pos[1])

        self.atk = 0
        self.hp = 30
        self.hpbase = self.hp

        self.stats = [[],[]]

        self.update_hp(0, font)

        self.card = None


        #----DRINKS----#
        self.drinks = 0
        self.drinks_total = 0
        self.update_drinks_total(self.drinks_total, font)
        self.update_drinks(reset=True, font = font)


    #function to draw cards
    def draw_card(self):
        if len(self.deck):
            if len(self.hand) < MAX_HAND_SIZE:
                drawn_card = random.choice(self.deck)

                #set owner
                drawn_card.owner = self.num

                self.deck.remove(drawn_card)
                # drawncardimg = drawn_card.fullresimg

                self.hand.append(drawn_card)

    #function to discard random cards
    def discard_card(self, app, card = 0):
        '''discard a random card from player's hand
        include card argument to discard any card except itself'''
        if len(self.hand):
            #choose a random card from hand
            dcard = random.choice(self.hand)

            #if chosen card is the input card, and there's more than 1 card in hand
                #choose another random card until it's not the input card
            if len(self.hand) > 1:
                while card == dcard:
                    #choose another random card from hand
                    dcard = random.choice(self.hand)

            #if there's no other cards to discard, don't discard the input card, just return 0
            else:
                return 0

            #remove that card from hand
            self.hand.remove(dcard)

            #trigger animation
            dcard.discard_animation(app)


    #update stats
    def update_hp(self, num, font):
        '''update hp of player, input: change in hp'''

        #update the chosen stat
        self.hp += num

        #pick the colour
        if self.hp > self.hpbase:
            colour = (124,252,0)

        elif self.hp < self.hpbase:
            colour = (255,0,0)

        else:
            colour = (255,255,255)


        self.hpimg = font.render(str(self.hp), True, colour)


    def update_drinks(self, drinks = None, font = None, reset = False):
        '''update player's current drinks
        reset = True if just refreshing to player's total drinks'''
        if not reset:
            self.drinks += drinks
        
        else:
            self.drinks = self.drinks_total

        if self.drinks == 10 or self.drinks_total == 10:
            spacing_string = "/"
        else:
            spacing_string = " / "

        self.drinks_img = font.render(str(self.drinks) + spacing_string + str(self.drinks_total), True, "WHITE")

    def update_drinks_total(self, drinks, font):
        self.drinks_total += drinks
        self.drinks_total_img = font.render(str(drinks), True, "WHITE")