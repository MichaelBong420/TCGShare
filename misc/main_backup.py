# import random
# import pygame
# import os

# from deck1 import *

# from Player import Player

# from helper_functions import *

# WHITE = (255,255,255)

# FPS = 60

# CARD_WIDTH, CARD_HEIGHT = 180, 240
# CARD1_X, CARD1_Y = 980, 700

# DECK1_X, DECK1_Y = 1700, 800

# player_turn = 1

# player1 = Player(0)
# player2 = Player(1)

# players = [player1, player2]

# class App():
#     def __init__(self):
#         WIDTH, HEIGHT = 1920, 1080
#         self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("TCG")
#         self.backgroud_img = load_image("Assets", "background.png", 1920, 1080)
#         self.background_rect = pygame.Rect(0,0,1920,1080)
#         self.background = Visual_object(self.backgroud_img, self.background_rect)

#         self.visual_objects = [self.background]

#     def draw_visual_objects(self):
#         for visual_object in self.visual_objects:
#             self.WIN.blit(visual_object.img, (visual_object.rect.x, visual_object.rect.y))


# class Deck():
#     def __init__(self, x, y, deck):
#         self.x, self.y = x, y
#         self.width, self.height = CARD_WIDTH, CARD_HEIGHT
#         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
#         self.deck = deck



# class Hand():
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#         self.contents = []


# CARD1_IMAGE = pygame.image.load(os.path.join("Assets", "Cards\Card1.png"))
# CARD1 = pygame.transform.scale(CARD1_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

# DECK = load_image("Assets", "TCG Deck.png", CARD_WIDTH, CARD_HEIGHT)


# # def draw_window(card1_rect, deck1, player):
# #     WIN.fill(WHITE)
# #     WIN.blit(CARD1, (card1_rect.x, card1_rect.y))
# #     WIN.blit(DECK, (deck1.rect.x, deck1.rect.y))

# #     #draw player's hand
# #     for num, card in enumerate(player.hand):
# #         WIN.blit(card.img, (190*num + 100,800))
# #     pygame.display.update()


# def next_turn():
#     global player_turn
#     player_turn = int(not(player_turn))
#     player = players[player_turn]

#     if len(player.deck):
#         drawn_card = random.choice(player.deck)
#         player.deck.remove(drawn_card)
#         player.hand.append(drawn_card)

#     print(player.deck)

    


# def main():
#     deck1_obj = Deck(DECK1_X, DECK1_Y, deck1)
#     card1_rect = pygame.Rect(CARD1_X, CARD1_Y, CARD_WIDTH, CARD_HEIGHT)
    

#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if card1_rect.collidepoint(pygame.mouse.get_pos()):
#                     print("clicked on card1")

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     next_turn()

#         player = players[player_turn]

#         draw_window(card1_rect, deck1_obj, player)

        
#     pygame.quit()


# if __name__ == "__main__":
#     main()