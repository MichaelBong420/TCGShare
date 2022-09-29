import pygame

from _helper_functions import *

# class Draw_loop_drawable():
#     def draw_loop(self, draw_list):
#         #draw all objects in object list
#         for drawable in self.draw_list:
#             self.WIN.blit(drawable.img, (x, y))

#             if drawable.tick():
#                 draw_list.remove(drawable)


class Drawable(pygame.Surface):
    def __init__(self, width, height, frames = -1):
        super().__init__(self, width, height)

        #tell it how many frames it goes through before death, -1 for infinite
        self.decay = frames

    def tick(self):
        ''''what does the object do every tick? by default it decays once to change it's img+duration
        returns 1 if it's finished and is ready to die'''

        #update img if needed
        if self.decay < 0:
            self.img = load_image(self.img_string + str(self.decay), CARD_WIDTH, CARD_HEIGHT)


        self.decay -= 1

        #return not self.decay, which will be 0 unless self.decay = 0, so that loop can delete it
        return not self.decay