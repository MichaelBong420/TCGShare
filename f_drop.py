from _helper_functions import *

class Drop():
    def drop(self):

        if self.drag:
            self.drag_card.drag = False
            self.drag_card.hover = False
        self.drag = 0
        self.drag_card = None

        self.limbo = None

        set_targets(self)