from Card import *

from c_atestcard import *

#----COIN----#
from s_opening_shot import *


#----UNITS----#
from c_hair_removal_levi import Hair_removal_levi
from c_hungry_henzie import Hungry_henzie
from c_mad_scientist_andy import *
from c_human_shield_michael import *
from c_egg_toss_levi import *
from c_do_double_shots_joey import *
from c_mayo_andy import *
from c_michael_giving_the_boys_a_milk_shower import *
from c_some_random_crazy_bitch_with_a_knife import *
from c_motivating_henzie import *
from c_levi_with_a_shield import *
from c_gaping_levi import *
from c_trash_king_michael import *
from c_two_pistol_levi import *
from c_hyped_levi import *
from c_tuna_breath_levi import *
from c_levi_smoking_a_fat_blunt import *
from c_hot_sauce_andy import *
from c_broken_grabber_michael import *
from c_sculling_rinzlow import *
from c_furious_michael import *
from c_blind_rage_jesse import *
from c_prestream_jesse import *
from c_rugged_up_bernie import *
from c_dutiful_rinzlow import *
from c_conjoined_boys import *
from c_sneaky_jesse import *
from c_frantic_chef_jesse import *
from c_slow_start_bernie import *
from c_stepbrother_levi import *
from c_makeup_artist_levi import *
from c_cinnamon_cough_levi import *
from c_steadfast_jesse import *
from c_michael_in_a_dress import *


#----SPELLS----#
from s_flamethrower import *
from s_rinzlows_tts import Rinzlows_tts
from s_a_barrage_of_eggs import A_barrage_of_eggs
from s_alcohol_ten_times_in_a_row import *
from s_face_melter import *
from s_iberique_first_sub import *
from s_cannon_ball import *
from s_stand_off import *
from s_profiting_from_a_clearly_inaccurate_ai_test import *
from s_butthurt_chat import *
from s_egg_went_everywhere import *
from s_show_em_some_leg import *
from s_encouraging_levi_to_drink_double import *
from s_show_em_some_leg import *
from s_smoke_alarm import *

all_cards_list = []

def new_card(card_name, cost, atk, hp, font, default = False, copies = 2):
    '''add a new card to all_cards_list, default = True if not a custom card class'''

    global all_cards_list


    if default:
        class_name = "Card"

    else:

        class_name = [char if char != " " else "_" for char in card_name]

        class_name[0] = class_name[0].upper()

        class_name = "".join(class_name)


    for i in range(copies):
        #for spell atk and hp inputs of ""
        if atk == "":
            temp = card_name + f" {cost}"

            # card_name = "".join(card_name)

            command = f"unit = {class_name}({cost}, '{temp}', font)"

        else:
            temp = card_name + f" {cost}.{atk}.{hp}"

            # card_name = "".join(card_name)

            command = f"unit = {class_name}({cost}, {atk}, {hp}, '{temp}', font)"
            
        exec(command)
        exec(f"all_cards_list.append(unit)")


def new_cards_list(font):

    global all_cards

    new_card("motivating henzie", 1, 2, 1, font)
    new_card("levi with a shield", 3, 3, 3, font)
    new_card("alcohol ten times in a row", 4, "", "", font)
    new_card("face melter", 10, "", "", font)
    new_card("iberique first sub", 3, "", "", font)
    new_card("cannon ball", 1, "","",font)
    new_card("gaping levi",1,1,2,font)
    new_card("stand off", 4, "", "",font)
    new_card("trash king michael", 5, 4, 4,font)
    new_card("two pistol levi", 5, 4, 2,font)
    new_card("butthurt chat", 5, "","",font)
    new_card("egg went everywhere", 6, "","", font, copies = 1)
    new_card("profiting from a clearly inaccurate ai test", 7,"","",font, copies = 1)
    new_card("hyped levi", 3, 3, 3, font)
    new_card("tuna breath levi", 3, 2, 3, font)
    new_card("levi smoking a fat blunt", 3, 2, 3, font)
    new_card("hot sauce andy", 9, 8, 8, font, copies = 1)
    new_card("broken grabber michael", 3, 2, 3, font)
    new_card("sculling rinzlow", 5, 5, 7, font)
    new_card("furious michael", 4, 4, 4, font)
    new_card("rugged up bernie", 4, 3, 3, font)
    new_card("blind rage jesse", 6, 4, 2, font)
    new_card("prestream jesse", 6,4,5,font, copies = 1)
    new_card("dutiful rinzlow", 5,4,4,font)
    new_card("encouraging levi to drink double", 3, "","",font)
    new_card("conjoined boys", 4,2,3, font)
    new_card("show em some leg",4,"","",font)
    new_card("sneaky jesse", 2, 2, 1, font)
    new_card("frantic chef jesse", 2, 2, 1, font)
    new_card("stepbrother levi", 3,3,2,font)
    new_card("slow start bernie",2,0,2,font)
    new_card("smoke alarm", 7,"","",font)
    new_card("big ugly brute levi",6,6,7,font, default=True)
    new_card("makeup artist levi", 6,5,5,font)
    new_card("cinnamon cough levi", 1,1,1,font)
    new_card("steadfast jesse", 8,8,8,font)
    new_card("michael in a dress", 8,7,7,font)

def all_cards(font):

    global all_cards_list

    meat_gremlin_henzie0 = Card(2, 2, 3, "Meat Gremlin Henzie 2.2.3", font)
    meat_gremlin_henzie1 = Card(2, 2, 3, "Meat Gremlin Henzie 2.2.3", font)

    hungry_henzie0 = Hungry_henzie(3, 2, 3, "Hungry Henzie 3.2.3", font)
    hungry_henzie1 = Hungry_henzie(3, 2, 3, "Hungry Henzie 3.2.3", font)

    mad_scientist_andy0 = Mad_scientist_andy(2,2,2, "Mad Scientist Andy 2.2.2", font)
    mad_scientist_andy1 = Mad_scientist_andy(2,2,2, "Mad Scientist Andy 2.2.2", font)

    human_shield_michael0 = Human_shield_michael(2, 2, 2, "Human Shield Michael 2.2.2", font)
    human_shield_michael1 = Human_shield_michael(2, 2, 2, "Human Shield Michael 2.2.2", font)

    egg_toss_levi0 = Egg_toss_levi(2, 4, 3, "Egg Toss Levi 2.4.3", font)
    egg_toss_levi1 = Egg_toss_levi(2, 4, 3, "Egg Toss Levi 2.4.3", font)

    do_double_shots_joey0 = Do_double_shots_joey(2,2,2, "Do Double Shots Joey 2.2.2", font)
    do_double_shots_joey1 = Do_double_shots_joey(2,2,2, "Do Double Shots Joey 2.2.2", font)

    mayo_andy0 = Mayo_andy(4,3,6, "Mayo Andy 4.3.6", font)
    mayo_andy1 = Mayo_andy(4,3,6, "Mayo Andy 4.3.6", font)

    flamethrower0, flamethrower1 = Flamethrower(4, "Flamethrower 4.6", font), Flamethrower(4, "Flamethrower 4.6", font)

    a_barrage_of_eggs0, a_barrage_of_eggs1 = A_barrage_of_eggs(4, "A Barrage of Eggs 4.2", font), A_barrage_of_eggs(4, "A Barrage of Eggs 4.2", font)

    rinzlows_tts0, rinzlows_tts1 = Rinzlows_tts(2, "Rinzlow's TTS 2.3", font), Rinzlows_tts(2, "Rinzlow's TTS 2.3", font)

    michael_giving_the_boys_a_milk_shower0, michael_giving_the_boys_a_milk_shower1 = Michael_giving_the_boys_a_milk_shower(6, 6, 5, "Michael Giving the Boys a Milk Shower 6.5.5", font), Michael_giving_the_boys_a_milk_shower(6, 6, 5, "Michael Giving the Boys a Milk Shower 6.5.5", font)

    some_random_crazy_bitch_with_a_knife0 = Some_random_crazy_bitch_with_a_knife(9,8,8, "Some random crazy bitch with a knife 9.8.8", font)

    fat_suit_michael0, fat_suit_michael1 = Card(4,4,5,"Fat Suit Michael 4.4.5", font), Card(4,4,5,"Fat Suit Michael 4.4.5", font)

    hair_removal_levi0, hair_removal_levi1 = Hair_removal_levi(2,2,1, "Hair Removal Levi 2.2.1", font), Hair_removal_levi(2,2,1, "Hair Removal Levi 2.2.1", font)


    all_cards_list = [meat_gremlin_henzie0, hungry_henzie0, mad_scientist_andy0, human_shield_michael0, egg_toss_levi0, do_double_shots_joey0,\
    mayo_andy0, flamethrower0, michael_giving_the_boys_a_milk_shower0, michael_giving_the_boys_a_milk_shower1,\
    meat_gremlin_henzie1, hungry_henzie1, mad_scientist_andy1, human_shield_michael1, egg_toss_levi1, do_double_shots_joey1,\
    mayo_andy1, flamethrower1, a_barrage_of_eggs0, a_barrage_of_eggs1, rinzlows_tts0, rinzlows_tts1, some_random_crazy_bitch_with_a_knife0,\
    fat_suit_michael0, fat_suit_michael1, hair_removal_levi0, hair_removal_levi1]

    #----NEW CARDS----#
    new_cards_list(font)

    print("total cards: " + str(len(all_cards_list) / 2))

    return all_cards_list