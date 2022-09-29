import pygame

from _helper_functions import *

from f_draw_drinks import Draw_drinks


class Draw(Draw_drinks):
    def __init__(self) -> None:
        Draw_drinks.__init__(self)

        self.background_img = load_image("background.png", 1920, 1080)
        self.confirm_button_img = load_image("CONFIRM.png", END_TURN_WIDTH, END_TURN_HEIGHT)
        self.confirm_button_img_rect = pygame.Rect(1920 - END_TURN_WIDTH, 540 - END_TURN_HEIGHT/2, END_TURN_WIDTH, END_TURN_HEIGHT)

        self.deck_img = load_image("deck.png", DECK_WIDTH, DECK_HEIGHT)

        self.card_back_img = load_image("Card Back.png", CARD_WIDTH_HAND, CARD_HEIGHT_HAND)

        self.highlight_img_fullres = load_image("highlight.png", CARD_WIDTH, CARD_HEIGHT)

        self.shield_img_fullres = load_image("shield.png", CARD_WIDTH, CARD_HEIGHT)

        self.stuck_img_fullres = load_image("stuck.png", CARD_WIDTH, CARD_HEIGHT)

        self.limbo_img_fullres = load_image("limbo.png", CARD_WIDTH, CARD_HEIGHT)

        self.steadfast_img_fullres = load_image("steadfast.png", CARD_WIDTH, CARD_HEIGHT)
    
    def draw_loop(self):
        #hover logic
        card_hovered = None
        from_hand = False

        #draw background
        self.WIN.blit(self.background_img, (0, 0))


        #draw end of turn button
        self.WIN.blit(self.confirm_button_img, (self.confirm_button_img_rect.x, self.confirm_button_img_rect.y))


        #draw deck imgs
        for i in range(2):
            self.WIN.blit(self.deck_img, (DECK_X, DECK_Y[i]))

        
        #draw field
        #set positions based on positions in field
        for player_num, pfield in enumerate(self.field.fields):
            #count how many cards are in pfield
            num_of_cards = len(pfield)
            #select which row of position matrix to use based on how many cards
            pos_vector = self.field.pos_matrix[num_of_cards - 1]
            for num, card in enumerate(pfield):
                if card != self.drag_card:
                    update_cardpos(card, pos_vector[num], FIELD_Y[player_num])

                #if card is being hovered by mouse
                if card.hover:
                    ratio = 1.5
                    [hover_x, hover_y] = hover_card(card, ratio)

                    #save card so it can be rendered last over everything else
                    card_hovered = card
                    
                    #if card is being hovered, don't draw yet because we are drawing it last
                    continue

                else:
                    ratio = 1
                
                draw_card(self, card, ratio)


        #draw hand
        for player in self.players:
            for num, card in enumerate(player.hand):
                if card != self.drag_card:
                    #update card pos
                    update_cardpos(card, HAND_X + (CARD_WIDTH_HAND - HAND_SPACING) * num, HAND_Y[player.num])

                #if not the player's turn, just render the card back img
                if player.num != self.turn:
                    self.WIN.blit(self.card_back_img, card.pos)
                    continue

                #if card is being hovered by mouse
                if card.hover:
                    ratio = 1.5
                    [hover_x, hover_y] = hover_card(card, ratio, if_hand = True)

                    #save card so it can be rendered last over everything else
                    card_hovered = card

                    from_hand = True
                    
                    #if card is being hovered, don't draw yet because we are drawing it last
                    continue
                else:
                    ratio = 1
                
                draw_card(self, card, ratio)


        self.draw_drinks()


        #draw player frames and player.card
        for player in self.players:
            self.WIN.blit(player.img, player.pos)
            self.WIN.blit(player.hpimg, player.pos)

            if player.card:
                player.card.pos = [player.pos[0] + PLAYER_CARD_OFFSET_X, player.pos[1] + PLAYER_CARD_OFFSET_Y[player.num]]
                draw_card(self, player.card, HOVER_RATIO)
                

        #draw card being hovered over last so it appears on top
        #if there even is one
        if card_hovered:
            draw_card(self, card_hovered, HOVER_RATIO, hover_x, hover_y)


        pygame.display.update()