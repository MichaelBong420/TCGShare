from Card import Card

from _helper_functions import *

class Butthurt_chat(Card):
    def __init__(self, cost, card_string, font):
        
        #spells have no atk or hp
        atk, hp = "", ""
        super().__init__(cost, atk, hp, card_string, font)

        #card is a spell
        self.spell = 1

    async def on_play_spell(self, app):
        
        #call cast_spell and return none so that app knows we're done
        return await app.cast_spell(self)

    async def on_cast(self, app = None, card = None, player = None, choice = None):
        #deal two damage to all enemies and heal 2hp all allies

        #count how many cards damaged and healed
        dmg_counter = 0
        heal_counter = 0

        #deal two damage to all enemies
        dmg = -2

        enemy_num = 1 - self.owner
        enemy_field = app.field.fields[enemy_num]

        for card in enemy_field:
            dmg_counter += 1
            await card.on_damage_take(app)
            if card.shield:
                card.shield = 0
            else:
                card.update_stats(HP, dmg, app.font)
                

        #and enemy player
        app.players[enemy_num].update_hp(dmg, app.font)
        dmg_counter += 1


        #heal 2hp all allies
        heal = 2

        own_field = app.field.fields[self.owner]

        for card in own_field:
            heal_counter += 1
            heal_target(app, heal, card)

        print(heal_counter)

        #and own player
        heal_counter += heal_target(app, heal, player = app.players[self.owner])

        print(heal_counter)

        #let attacked cards do their channel points
        await asyncio.sleep(1)

        await add_points(app, self.chat_owner, dmg_counter * POINTS_PER_ATK/2 + heal_counter * POINTS_PER_HP/2)

        return None