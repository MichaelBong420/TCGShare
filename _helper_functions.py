from turtle import window_height
import pygame
import os

import asyncio

import types

import time

FPS = 60

WIN_WIDTH, WIN_HEIGHT = 1920, 1080


#----DECK----#
DECK_SIZE = 30


#----HOVER----#
HOVER_RATIO = 1.5

#----CARD DIMENSIONS----#
CARD_WIDTH, CARD_HEIGHT = 600, 800
#HAND
RATIO_HAND = 3/10
CARD_WIDTH_HAND, CARD_HEIGHT_HAND = CARD_WIDTH*RATIO_HAND, CARD_HEIGHT*RATIO_HAND

#DECK_BUILD
FULL_RES_RATIO = 2.5


#----MULLIGAN----#
MULLIGAN_X, MULLIGAN_Y = 100, 100

MULLIGAN_RATIO = 2
CARD_WIDTH_MULLIGAN, CARD_HEIGHT_MULLIGAN = CARD_WIDTH_HAND * MULLIGAN_RATIO, CARD_HEIGHT_HAND * MULLIGAN_RATIO


#----HAND----#
MAX_HAND_SIZE = 10

HAND_SPACING = CARD_WIDTH_HAND / 3

HAND_X, HAND_Y0, HAND_Y1 = 40, 1080 - CARD_HEIGHT_HAND, 0
HAND_Y = HAND_Y0, HAND_Y1


#----DRAG----#
DRAG_FROM_HAND = 1
DRAG_FROM_FIELD = 2


#----FIELD----#
MAX_FIELD_SIZE = 8

FIELD_WIDTH, FIELD_HEIGHT = CARD_WIDTH_HAND * MAX_FIELD_SIZE, CARD_HEIGHT_HAND * 2

FIELD_X, FIELD_Y = 200, [300 + CARD_HEIGHT_HAND, 300]

FIELD_SPACING = CARD_WIDTH_HAND # + CARD_WIDTH_HAND/2


#----BUTTONS----#
END_TURN_WIDTH, END_TURN_HEIGHT = 100, 25

CONFIRM_WIDTH, CONFIRM_HEIGHT = 800, 200
CONFIRM_X, CONFIRM_Y = WIN_WIDTH / 2 - CONFIRM_WIDTH / 2, WIN_HEIGHT - CONFIRM_HEIGHT


#----MISC----#
DECK_WIDTH, DECK_HEIGHT = 180, 240
DECK_X, DECK_Y = 1920 - DECK_WIDTH, [1080 - DECK_HEIGHT, 0]

#----STATS----#
COST, ATK, HP = 0, 1, 2


#----PLAYER----#
PLAYER_FRAME_WIDTH, PLAYER_FRAME_HEIGHT = 240, 300
PLAYER_FRAME_X, PLAYER_FRAME_Y = DECK_X - PLAYER_FRAME_WIDTH, [1080 - PLAYER_FRAME_HEIGHT, 0]

PLAYER_CARD_OFFSET_X, PLAYER_CARD_OFFSET_Y = -30, [ - CARD_HEIGHT_HAND * HOVER_RATIO, CARD_HEIGHT_HAND * HOVER_RATIO]


#--DRINKS--#
DRINK_WIDTH, DRINK_HEIGHT = 30, 30
DRINK_START_X, DRINK_START_Y = PLAYER_FRAME_X - DRINK_WIDTH, [1080 - DRINK_HEIGHT, 0]
DRINK_TOTAL_START_X = DRINK_START_X - 115

DRINK_TEXT_HEIGHT = 45
DRINK_TOTAL_START_Y = [1080 - DRINK_TEXT_HEIGHT, 0]

MAX_DRINKS = 10


#----HISTOGRAM----#
HIST_WIDTH, HIST_HEIGHT = 30, 30
HIST_X_SPACER = 60
HIST_X, HIST_Y = 500, WIN_HEIGHT - 60


#----CHANNEL POINTS----#
POINTS_PER_DRAW = 100
POINTS_PER_HP = 200
POINTS_PER_ATK = 100



def load_image(local_dir, w, h):
    img = pygame.image.load(os.path.join("Assets", local_dir))
    return pygame.transform.smoothscale(img, (w, h))


def draw_card(app, card, ratio = 1, custom_x = None, custom_y = None, alpha = None, nostat = False, from_hand = False):
    '''draw a card on the window, with optional ratio'''

    if not card.animating:
        #update img
        card.img = pygame.transform.smoothscale(card.fullresimg, (CARD_WIDTH_HAND*ratio, CARD_HEIGHT_HAND*ratio))
        if alpha:
            card.img.set_alpha(alpha)

    #if no custom coords given, draw at object position
    if not custom_x:
        pos = card.pos.copy()

    #otherwise draw at custom position
    else:
        pos = [custom_x, custom_y]

    
    #----BORDERS----#

    #draw mulligan select
    if card.mulligan:
        img = pygame.transform.smoothscale(app.highlight_img_fullres, (CARD_WIDTH_HAND*ratio, CARD_HEIGHT_HAND*ratio))
        if alpha:
            img.set_alpha(alpha)
        app.WIN.blit(img, pos)

    
    

    #draw highlight
    if (card.energy > 0 and card.stats[ATK] > 0) or card.playable:
        img = pygame.transform.smoothscale(app.highlight_img_fullres, (CARD_WIDTH_HAND*ratio, CARD_HEIGHT_HAND*ratio))
        if alpha:
            img.set_alpha(alpha)
        app.WIN.blit(img, pos)

    #draw stuck
    if card.stuck:
        img = pygame.transform.smoothscale(app.stuck_img_fullres, (CARD_WIDTH_HAND*ratio, CARD_HEIGHT_HAND*ratio))
        if alpha:
            img.set_alpha(alpha)
        app.WIN.blit(img, pos)

    #draw limbo highlight
    if card == app.limbo:
        #draw self.limbo border
        img = pygame.transform.smoothscale(app.limbo_img_fullres, (CARD_WIDTH_HAND*ratio, CARD_HEIGHT_HAND*ratio))
        if alpha:
            img.set_alpha(alpha)
        app.WIN.blit(img, pos)

        

    #draw card itself
    app.WIN.blit(card.img, pos)


    #draw steadfast
    if card.steadfast:
        img = pygame.transform.smoothscale(app.steadfast_img_fullres, (CARD_WIDTH_HAND*ratio, CARD_HEIGHT_HAND*ratio))
        if alpha:
            img.set_alpha(alpha)
        app.WIN.blit(img, pos)

    #draw stats
    if not nostat:
        if ratio == MULLIGAN_RATIO:
            draw_stats(app, card, pos, mulligan = ratio, alpha = alpha)

        else:
            draw_stats(app, card, pos, alpha = alpha)

    #draw shield
    if card.shield:
        img = pygame.transform.smoothscale(app.shield_img_fullres, (CARD_WIDTH_HAND*ratio, CARD_HEIGHT_HAND*ratio))

        if alpha:
            img.set_alpha(alpha)

        app.WIN.blit(img, pos)



def draw_stats(app, card, pos, build = None, mulligan = None, alpha = None, from_hand = False):
    for stat, val in enumerate(card.stats):

        #if stat is blank, skip
        if val == "":
            continue

        if card.hover:
            # print(from_hand)
            ratio = HOVER_RATIO

            if not card.played:
                if card.owner:
                    x_offset0 = -9
                    y_offset0 = 25
                    x_offset1 = -15
                    y_offset1 = 40
                    x_offset2 = 63
                    y_offset2 = y_offset1

                else:
                    x_offset0 = -9
                    y_offset0 = -50
                    x_offset1 = -15
                    y_offset1 = 120
                    x_offset2 = 63
                    y_offset2 = y_offset1

            
            else:
                x_offset0 = -9
                y_offset0 = -17
                x_offset1 = -15
                y_offset1 = 77
                x_offset2 = 63
                y_offset2 = y_offset1

        
        elif build:
            ratio = build

            x_offset0 = 30
            y_offset0 = 50
            x_offset1 = 25
            y_offset1 = -40
            x_offset2 = -20
            y_offset2 = -40

        
        elif mulligan:
            ratio = mulligan

            x_offset0 = 23
            y_offset0 = 30
            x_offset1 = 16
            y_offset1 = 33
            x_offset2 = 32
            y_offset2 = y_offset1


        else:
            ratio = 1

            x_offset0 = 15
            y_offset0 = 10
            x_offset1 = 10
            y_offset1 = 45
            x_offset2 = 40
            y_offset2 = 50

        if stat == 0:
            x = card.pos[0] + (x_offset0) * ratio
            y = card.pos[1] + (y_offset0) * ratio

            #for drawing owner label
            owner_label_x = x
            owner_label_y = y
        
        elif stat == 1:
            x = card.pos[0] + (x_offset1) * ratio
            y = card.pos[1] + (CARD_HEIGHT_HAND - y_offset1) * ratio

        elif stat == 2:
            x = card.pos[0] + (CARD_WIDTH_HAND - x_offset2) * ratio
            y = card.pos[1] + (CARD_HEIGHT_HAND - y_offset2) * ratio

        if alpha:
            card.statsimgs[stat].set_alpha(alpha)

        else:
            card.statsimgs[stat].set_alpha(255)

        app.WIN.blit(card.statsimgs[stat], (x, y))

    #draw owner label
    #generate image from font
    colour = (255,255,255)
    chat_owner_img = app.chat_owner_font.render(card.chat_owner, True, colour)
    app.WIN.blit(chat_owner_img, (owner_label_x, owner_label_y))


def hover_card(card, ratio, if_hand = False):
    '''enlarge a card, primarily while mouse is hovering over it'''

    #make card look centered compared to unhovered image center
    x = card.pos[0] - (CARD_WIDTH_HAND*ratio - CARD_WIDTH_HAND) / 2

    if not if_hand:
        y = card.pos[1] - (CARD_HEIGHT_HAND*ratio - CARD_HEIGHT_HAND) / 2
    else:
        y = card.pos[1] - (1 - card.owner) * (CARD_HEIGHT_HAND*ratio - CARD_HEIGHT_HAND)

    # y = card.pos[1] - (CARD_HEIGHT_HAND*ratio - CARD_HEIGHT_HAND) / 2

    return [x, y]


def update_cardpos(card, x, y):
    card.pos[0] = x
    card.pos[1] = y
    card.rect.update(card.pos,  (CARD_WIDTH_HAND, CARD_HEIGHT_HAND))


def set_targets(app, vals = None):

    #if no custom vals given, just reset targets
    if not vals:
        #friendly cards targetable
        app.fcard = 1
        #enemy cards untargetable
        app.ecard = 0
        #player targetable
        app.pcard = 1

    else:
        app.fcard = vals[0]
        app.ecard = vals[1]
        app.pcard = vals[2]


def heal_target(app, dmg, card = None, player = None):
    '''heal a target player or card, return true if healing was done or false if card wasn't even damaged'''
    healed = False
    if card:
            #calculate hp difference
            difference = card.statsbase[HP] - card.stats[HP]

            if difference > 0:
                dmg = min(dmg, difference)
                card.update_stats(HP, dmg, app.font)

                healed = True

            else:
                pass

    elif player:
        #calculate hp difference
        difference = player.hpbase - player.hp

        if difference > 0:
            dmg = min(dmg, difference)
            player.update_hp(dmg, app.font)

            healed = True

        else:
            pass

    return healed


async def add_points(app, viewer, amount):
    '''add SE channel points through stream'''
    #award points to viewer who owns card
    await app.chan.send(f"!addpoints {viewer} {amount}")