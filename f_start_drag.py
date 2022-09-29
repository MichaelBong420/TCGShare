from _helper_functions import *

class Start_drag():
    '''drag a card with the mouse movement
    returns the x and y offset'''
    def start_drag(self, card, event, type):# card_clicked = 1):
        self.drag = type
        # self.drag_initpos = [card.pos[0], card.pos[1]]#card.pos.copy()
        
        mx, my = event.pos
        ox, oy = card.pos[0] - mx, card.pos[1] - my

        #make sure card is hovering
        card.hover = 1

        #let draw() know to not update cards position anymore
        card.drag = True
        self.drag_card = card

        #let main know that a card was clicked on
        # self.card_clicked = card_clicked

        #targetable
        set_targets(self, (0, 1, 1))

        return ox, oy