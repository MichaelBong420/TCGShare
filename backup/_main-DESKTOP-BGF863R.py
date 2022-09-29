import pygame

from _helper_functions import *

#----CUSTOM FUNCTIONS----#
from f_draw import Draw
from f_start_drag import *
from f_next_turn import *

#----Players----#
from Player import Player


#----DECK AND CARDS----#
from cards import *

#----FIELD----#
from Field import *


#----OTHER FUNCS----#
from f_play_card import *
from f_drop import *


class App(Drop, Next_turn, Play_card, Field, Start_drag, Draw):
    def __init__(self):
        #----CUSTOM INITS----#
        Draw.__init__(self)

        pygame.init()
        self.WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("TCG")


        #----MISC----#
        self.turn = 0
        

        #----FONT----#
        # sysfont = pygame.font.get_default_font()
        self.STATS_FONT = pygame.font.SysFont('chalkduster.ttf', 70)


        #----Players----#
        self.player0 = Player(all_cards(0), 0)
        self.player1 = Player(all_cards(1), 1)

        #test
        # self.player0.hand = self.player0.deck
        # self.player1.hand = self.player1.deck

        #list of players
        self.players = [self.player0, self.player1]


        #----MOVEMENT----#
        self.drag = False
        self.drag_card = None

        self.card_hovered = False


        #----FIELD----#
        self.field = Field()

    
    def main(self):

        clock = pygame.time.Clock()

        #main game loop
        self.run = True

        # self.next_turn()

        while self.run:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                #mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #LMB click
                    if event.button == 1:

                        #if not already dragging
                        if not self.drag:
                            #check if clicked on a card in the hand
                            for player in self.players:
                                for card in player.hand:
                                    if card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(pygame.mouse.get_pos()):
                                        #drag
                                        ox, oy = self.start_drag(card, event, DRAG_FROM_HAND)

                        # if dragging a card from hand
                        elif self.drag == DRAG_FROM_HAND:
                            #check if clicked on the field
                            if self.field.rect.collidepoint(event.pos):
                                # playpos = self.check_playpos(event.pos, self.players[self.turn])
                                print(event.pos)
                                # self.play_card(self.drag_card, playpos)

                        #----END TURN----#
                        if self.confirm_button_img_rect.collidepoint(pygame.mouse.get_pos()):
                            self.next_turn()

                    #RMB click
                    #deselect dragged card and return it
                    elif event.button == 3:

                        #deselect dragged card and return it
                        if self.drag:
                            #deselect
                            self.drop()
                            




                elif event.type == pygame.MOUSEMOTION:
                    if self.drag:
                        # print("here2")
                        mx, my = event.pos
                        self.drag_card.pos[0] = mx + ox
                        self.drag_card.pos[1] = my + oy

                    #mouseover highlights cards unless a card is being dragged
                    else:
                        #check if mouseover any object
                        #cards in field
                        for field in self.field.fields:
                            for card in field:
                                if not mouse_intersected_card and card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(event.pos):
                                
                                    self.card_hovered = True
                                    card.hover = True

                                    break

                                else:
                                    self.card_hovered = False
                                    card.hover = False

                        #cards in hand
                        mouse_intersected_card = False
                        for card in self.players[self.turn].hand:
                            if not mouse_intersected_card and card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(event.pos):
                                
                                self.card_hovered = True
                                card.hover = True

                                mouse_intersected_card = True

                            else:
                                self.card_hovered = False
                                card.hover = False

            self.draw_loop()

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.main()