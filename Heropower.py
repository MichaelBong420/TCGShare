class Heropower():
    def __init__(self, owner) -> None:

        #owner is type Player
        self.owner = owner

        self.energy = 1

        self.cost = 2

    def on_click(self, app):
        if self.owner.drinks >= self.cost:
            #owner spends 2 drinks
            self.owner.update_drinks(self, drinks = - self.cost, font = app.font)

            #owner draw 2 cards
            self.owner.draw_card()

            #owner loses 2hp
            self.owner.update_hp(-2, app.font)

            #spend hero power's energy
            self.energy -= 1