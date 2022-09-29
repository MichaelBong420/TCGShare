from Card import Card

from _helper_functions import *

class Hot_sauce_andy(Card):

    def on_play(self, app, index):
        #list of descending andys to play
        string = "descending andy "
        name_list = [string + str(i+1) + " 1.1.1" for i in range(7)]

        #if there's still room
        i = 0
        while len(app.field.fields[self.owner]) < MAX_FIELD_SIZE:

            i += 1

            #summon an extra unit
            unit = Card(1, 1, 1, name_list[i-1], app.font)

            unit.owner = self.owner

            async def on_damage_deal(self, app = None, card=None):
                #award points to viewer who owns card
                await add_points(app, self.chat_owner, POINTS_PER_ATK)

            unit.on_damage_deal = types.MethodType(on_damage_deal, unit )

            unit.played = True

            app.field.fields[self.owner].insert(index + i, unit)

            unit.entry_animation(app)

            
           
        return 1


    def entry_animation(self, app):
        self.animating = 1

        ratio = RATIO_HAND
        
        for i in range(125):

            img = load_image("Cards/hot sauce andy 2/" + f"Untitled_{i:06d}.png", CARD_WIDTH, CARD_HEIGHT)

            self.img = pygame.transform.smoothscale(img, (CARD_WIDTH*RATIO_HAND, CARD_HEIGHT*RATIO_HAND))

            app.draw_loop()

        self.animating = 0

    # async def on_damage_deal(self, app = None, card=None):
    #     #award points to viewer who owns card
    #     await add_points(app, self.chat_owner, POINTS_PER_ATK)

    # async def on_damage_take(self, app = None, card=None):
    #     #award points to viewer who owns card
    #     await add_points(app, self.chat_owner, POINTS_PER_HP)