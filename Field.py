from _helper_functions import *

class Field():
    def __init__(self):
        self.x, self.y = FIELD_X, FIELD_Y[1]
        self.width, self.height = 1920, FIELD_HEIGHT

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


        #----PLAYER FIELDS----#
        self.fields = [[],[]]

        #card drawing
        self.pos_matrix =\
        [[self.x + FIELD_WIDTH/2,0,0,0,0,0,0,0],
        [self.x + FIELD_WIDTH/2 - FIELD_SPACING*1/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*1/2, 0, 0, 0, 0, 0, 0],
        [self.x + FIELD_WIDTH/2 - FIELD_SPACING, self.x + FIELD_WIDTH/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING, 0, 0, 0, 0, 0],
        [self.x + FIELD_WIDTH/2 - FIELD_SPACING*3/2, self.x + FIELD_WIDTH/2 - FIELD_SPACING*1/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*1/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*3/2, 0, 0, 0, 0],
        [self.x + FIELD_WIDTH/2 - FIELD_SPACING*2, self.x + FIELD_WIDTH/2 - FIELD_SPACING, self.x + FIELD_WIDTH/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING, self.x + FIELD_WIDTH/2 + FIELD_SPACING*2, 0, 0, 0],
        [self.x + FIELD_WIDTH/2 - FIELD_SPACING*5/2, self.x + FIELD_WIDTH/2 - FIELD_SPACING*3/2, self.x + FIELD_WIDTH/2 - FIELD_SPACING*1/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*1/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*3/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*5/2, 0, 0],
        [self.x + FIELD_WIDTH/2 - FIELD_SPACING*3, self.x + FIELD_WIDTH/2 - FIELD_SPACING*2, self.x + FIELD_WIDTH/2 - FIELD_SPACING, self.x + FIELD_WIDTH/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING, self.x + FIELD_WIDTH/2 + FIELD_SPACING*2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*3, 0],
        [self.x + FIELD_WIDTH/2 - FIELD_SPACING*7/2, self.x + FIELD_WIDTH/2 - FIELD_SPACING*5/2, self.x + FIELD_WIDTH/2 - FIELD_SPACING*3/2, self.x + FIELD_WIDTH/2 - FIELD_SPACING*1/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*1/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*3/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*5/2, self.x + FIELD_WIDTH/2 + FIELD_SPACING*7/2]]

        self.pos_play_matrix = [self.pos_matrix[-2], self.pos_matrix[-1]]