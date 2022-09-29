from time import sleep
from _helper_functions import *

import pygame

from f_atk import Atk

class Card():
    def __init__(self, cost, atk, hp, card_string, font):
        card_string = "Cards\\" + card_string + ".png"
        self.fullresimg = load_image(card_string, CARD_WIDTH, CARD_HEIGHT)

        self.pos = [0,0]

        self.img = pygame.transform.smoothscale(self.fullresimg, (CARD_WIDTH_HAND, CARD_HEIGHT_HAND))
        self.rect = pygame.Rect(self.pos, (CARD_WIDTH_HAND, CARD_HEIGHT_HAND))#self.img.get_rect(x = self.pos)

        #----STATS----#
        self.costbase = cost
        self.atkbase = atk
        self.hpbase = hp

        self.statsbase = [self.costbase, self.atkbase, self.hpbase]

        self.stats = [cost, atk, hp]

        self.statsimgs = [[], [], []]

        for stat, num in enumerate(self.stats):
            #make sure card actually has entries for those stats
            if num != "":
                self.update_stats(stat, 0, font)


        #Ownership
        self.owner = None

        #drag - set to false when wanting to drop
        #pos will then be reset by draw loop
        self.drag = False

        #mouseover
        self.hover = False
        self.played = False

        #energy so cards cant charge and only atk once per turn
        self.energy = 0

        #play, most cards have no entry so satisfied by default
        self.satisfied = 1

        #shield to block next damage
        self.shield = 0

        #stuck
        self.stuck = 0

        #spells
        self.spell = 0

        #mulligan
        self.mulligan = 0

        #steadfast
        self.steadfast = 0

        #highlight card in hand
        self.playable = 0

        #animation
        self.animating = 0

        #twitch
        self.chat_owner = "meandmichaelbot"


    #update stats
    def update_stats(self, stat, num, font):
        '''update stats of a card, input: COST, ATK or HP'''

        #update the chosen stat
        self.stats[stat] += num

        #pick the colour
        if self.stats[stat] > self.statsbase[stat]:
            colour = (124,252,0)

        elif self.stats[stat] < self.statsbase[stat]:
            colour = (255,0,0)

        else:
            colour = (255,255,255)


        self.statsimgs[stat] = font.render(str(self.stats[stat]), True, colour)

    def set_statsbase(self, list = None):
        '''set base stats to current stats
        primarily for mad scientist card etc.'''
        # self.statsbase = self.stats.copy()
        if list:
            self.statsbase = list
        else:
            self.statsbase = self.stats


    def on_death(self, app = None, index = None):
        pass

    def on_play(self, app = None, index = None):
        return self.satisfied
    
    def on_entry(self, app = None, card = None, index = None, choice = None, player = None):
        pass

    async def on_play_spell(self, app):
        pass

    async def on_cast(self, app = None, card = None, player = None, choice = None):
        pass

    async def on_damage_take(self, app = None, card = None):
        pass

    async def on_damage_deal(self, app = None, card = None):
        pass

    def discard_animation(self, app):
        alpha = 255
        # self.img = self.img.convert()
        t = int(FPS/4)
        for i in range(t):
            #call draw loop to wipe old images
            app.draw_loop()

            #increment based on which player
            self.pos[1] -= pow(-1,self.owner) * 4

            #fade out
            alpha -= 255 / t / 2

            draw_card(app, self, alpha = alpha)

            pygame.display.update()

            #allow time for screen to display before changing
            # app.clock.tick(FPS)

    def death_animation(self, app):
        alpha = 255
        # self.img = self.img.convert()
        t = int(FPS/4)
        for i in range(t):
            #call draw loop to wipe old images
            app.draw_loop()

            #fade out
            alpha -= 255 / t / 2

            draw_card(app, self, alpha = alpha)

            pygame.display.update()

    
    def entry_animation(self, app):
        # alpha = 0
        ratio = 2

        t = int(FPS/4)

        for i in range(t):
            #call draw loop to wipe old images
            app.draw_loop()

            #shrink in
            ratio -= 1 / t

            [hover_x, hover_y] = hover_card(self, ratio)

            draw_card(app, self, ratio = ratio, custom_x=hover_x, custom_y=hover_y, nostat = True)

            app.clock.tick(FPS)

            pygame.display.update()