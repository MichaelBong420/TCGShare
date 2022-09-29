from twitchio.ext import commands

from _main import *

import asyncio

class Bot(commands.Bot, App):

    def __init__(self):
        App.__init__(self)
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        commands.Bot.__init__(self, token='', prefix='!', initial_channels=[''])


    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

        #Get channel to send messages to
        self.chan = self.connected_channels[0]

        print("game run")

        await self.pygame_main()

        print("game over")


    async def pygame_main(self):
        print(2, self.chan)
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
            # self.clock.tick(FPS)
            await asyncio.sleep(1/FPS)
            
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
                                            self.limbo = await self.cast_spell(card = card)
                                        
                                        elif card != self.limbo:
                                            #trigger its on_entry with the selected card as input
                                            self.limbo.on_entry(self, card)

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
                                            self.limbo = await self.cast_spell(card = card)
                                            continue
                                        else:
                                            #trigger its on_entry with the selected card as input
                                            self.limbo.on_entry(self, card)
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
                                            await self.atk_player(self.drag_card, player)

                                    if self.limbo:
                                        if self.limbo.spell:
                                            self.limbo = await self.cast_spell(player = player)
                                        else:
                                            self.limbo = self.limbo.on_entry(self, player = player)


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
    bot = Bot()
    bot.run()