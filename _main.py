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
from f_play_spell import *
from f_cast_spell import *
from f_drop import *
from f_check_playpos import *
from f_atk import *
from f_atk_player import *
from f_tick import *

from z_deck_build import *
from z_mulligan import *


#----TEST MODE----#
from _testmode import *


class App(Test_mode, Mulligan, Deck_build, Tick, Atk_player, Atk, Check_playpos, Drop, Next_turn, Cast_spell, Play_spell, Play_card, Field, Start_drag, Draw):
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("TCG")
        
        #----CUSTOM INITS----#
        Draw.__init__(self)
        Next_turn.__init__(self)

        


        #----MISC----#
        self.turn = 1
        

        #----FONT----#
        self.font = pygame.font.SysFont("verdana", 40)
        self.chat_owner_font = pygame.font.SysFont("verdana", 20)


        #----DECK BUILD & MULLIGAN----#
        #must be after font is initialised
        Deck_build.__init__(self)
        Mulligan.__init__(self)


        #----Players----#
        self.player0 = Player([], 0, self.font)
        self.player1 = Player([], 1, self.font)


        #list of players
        self.players = [self.player0, self.player1]


        #----MOVEMENT----#
        self.drag = False
        self.drag_card = None

        self.card_hovered = False


        #----FIELD----#
        self.field = Field()

        #----TARGET----#
        self.fcard = False
        self.ecard = False
        self.pcard = False

        self.limbo = None

    
    async def main(self):

        test = 1

        self.clock = pygame.time.Clock()


        #----DECK BUILD AND MULLIGAN----#
        if not test:
            # self.draw_histogram_allcards(all_cards(self.font))
            self.build_loop_main()
            self.mulligan_loop_main()

        else:
            #----TESTING----#
            self.test_mode()




        #----MAIN GAME LOOP----#
        self.run = True

        self.next_turn()

        while self.run:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                #mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #LMB click
                    if event.button == 1:

                        #----HAND----#
                        #if not already dragging and no card in limbo
                        if not self.drag and not self.limbo:
                            #check if clicked on a card in the hand
                            for player in self.players:
                                for card in player.hand:
                                    if card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(pygame.mouse.get_pos()):
                                        #drag
                                        ox, oy = self.start_drag(card, event, DRAG_FROM_HAND)


                        #----PLAY DRAGGED CARD ONTO FIELD----#
                        #if dragging a card from hand
                        elif self.drag == DRAG_FROM_HAND:
                            #check if clicked on the field

                            #but not if card is a spell, they must click on player to cast
                            if not self.drag_card.spell:
                                
                                if self.field.rect.collidepoint(event.pos):
                                    playpos = self.check_playpos(event.pos, self.players[self.turn])

                                    if playpos != -1:
                                        self.limbo = self.play_card(self.drag_card, playpos)
                                    continue

                        #----END TURN----#
                        if self.confirm_button_img_rect.collidepoint(pygame.mouse.get_pos()):
                            self.drop()
                            self.next_turn()

                        #----CARD ON CARD----#
                        #----FRIENDLY CARDS----#
                        if self.fcard:
                            for card in self.field.fields[self.turn]:
                                if card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(pygame.mouse.get_pos()):
                                    #if a card was waiting for card selection
                                    if self.limbo:
                                        if self.limbo.spell:
                                            self.limbo = self.cast_spell(card = card)
                                        
                                        elif card != self.limbo:
                                            #trigger its on_entry with the selected card as input
                                            self.limbo.on_entry(app, card)

                                    elif not self.drag and card.energy > 0:
                                        #drag
                                        ox, oy = self.start_drag(card, event, DRAG_FROM_FIELD)

                        
                        #----ENEMY CARDS----#
                        if self.ecard:
                            for card in self.field.fields[1 - self.turn]:
                                if card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(pygame.mouse.get_pos()):
                                    #if a card was waiting for card selection
                                    if self.limbo:
                                        if self.limbo.spell:
                                            self.limbo = self.cast_spell(card = card)
                                            continue
                                        else:
                                            #trigger its on_entry with the selected card as input
                                            self.limbo.on_entry(app, card)
                                            continue

                                    elif self.drag == DRAG_FROM_FIELD:
                                        await self.atk(self.drag_card, card)
                                        

                        #----PLAYER FRAMES----#
                        if self.pcard:
                            for player in self.players:
                                if player.rect.collidepoint(pygame.mouse.get_pos()):
                                    if self.drag:
                                        #check if spell is being played:
                                        #being dragged from hand AND clicked on their own player
                                        if self.drag == DRAG_FROM_HAND and self.drag_card.owner == player.num:
                                            #play spell
                                            self.limbo = await self.play_spell(self.drag_card)
                                            continue

                                        #otherwise it must be a card attacking a player, make sure they can't attack their own, and drag from field
                                        elif self.drag_card.owner != player.num and not self.drag_card.spell and self.drag == DRAG_FROM_FIELD:
                                            self.atk_player(self.drag_card, player)

                                    if self.limbo:
                                        if self.limbo.spell:
                                            self.limbo = self.cast_spell(player = player)
                                        else:
                                            self.limbo = self.limbo.on_entry(app, player = player)


                    #RMB click
                    #deselect dragged card and return it
                    elif event.button == 3:

                        #deselect dragged card and return it
                        if self.drag:
                            #deselect
                            self.drop()
                            




                elif event.type == pygame.MOUSEMOTION:
                    if self.drag:
                        mx = event.pos[0]
                        my = event.pos[1]
                        update_cardpos(self.drag_card, mx + ox, my + oy)
                        

                    #mouseover highlights cards unless a card is being dragged
                    else:
                        #check if mouseover any object
                        mouse_intersected_card = False
                        #cards in field
                        for field in self.field.fields:
                            for card in field:
                                if not mouse_intersected_card and card.img.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(event.pos):
                                
                                    self.card_hovered = True
                                    card.hover = True

                                    mouse_intersected_card = True

                                    # break

                                else:
                                    self.card_hovered = False
                                    card.hover = False

                        #cards in hand
                        
                        for card in self.players[self.turn].hand:
                            if not mouse_intersected_card and card.rect.collidepoint(event.pos):#.get_rect(x = card.pos[0], y = card.pos[1]).collidepoint(event.pos):
                                
                                self.card_hovered = True
                                card.hover = True

                                mouse_intersected_card = True

                            else:
                                self.card_hovered = False
                                card.hover = False

            self.tick()
            self.draw_loop()

        # input("enter to quit")
        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.main()