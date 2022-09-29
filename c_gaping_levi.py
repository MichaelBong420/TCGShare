from Card import Card

class Gaping_levi(Card):
    def __init__(self, cost, atk, hp, card_string, font):
        super().__init__(cost, atk, hp, card_string, font)

        self.steadfast = 1