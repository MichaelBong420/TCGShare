from _helper_functions import *


class Draw_drinks():
    def __init__(self) -> None:
        self.drink_empty = load_image("drink empty.png", DRINK_WIDTH, DRINK_HEIGHT)
        self.drink_full = load_image("drink full.png", DRINK_WIDTH, DRINK_HEIGHT)

    def draw_drinks(self):
        '''draw the drinks images of both players'''

        for player in self.players:
            #draw totals, e.g. 3 / 10
            self.WIN.blit(player.drinks_img, (DRINK_TOTAL_START_X, DRINK_TOTAL_START_Y[player.num]))
            # self.WIN.blit(player.drinks_total_img, (DRINK_TOTAL_START_X + DRINK_WIDTH, WIN_HEIGHT - DRINK_HEIGHT*2))

            #draw drinks images
            for i in range(player.drinks_total):
                #draw the full drinks until they're done
                if i < player.drinks:
                    self.WIN.blit(self.drink_full, (DRINK_START_X, DRINK_START_Y[player.num] - DRINK_HEIGHT*i * pow(-1, player.num)))
                #remainder of drinks should be empty
                else:
                    self.WIN.blit(self.drink_empty, (DRINK_START_X, DRINK_START_Y[player.num] - DRINK_HEIGHT*i * pow(-1, player.num)))