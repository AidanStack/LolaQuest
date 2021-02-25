import random

#Core Game Functions

def combat(enemy):
    lola.in_combat = True
    print("""
                                                LOLA HAS ENTERED COMBAT!"
                                                                                        """)
    print("Lola's health is " + str(lola.health) + ", and Lola deals " + str(lola.damage) + " per turn.")
    print("Enemy has " + str(enemy.health) + " health points, and deals " + str(enemy.damage) + " per turn.")
    print("" )
    while lola.health > 0 and enemy.health > 0:
        user_choice = input("What will Lola do? Options: attack, ability, dodge, run, ")
        if user_choice.lower().strip(" ") == "attack":
            enemy.health += (-1 * lola.damage) - enemy.armor
            print(" ")
            print("Enemy hit!")
            print("Lola did " + str(lola.damage - enemy.armor) + " damage!")
            print("Enemy health is now " + str(enemy.health))
            if enemy.health > 0:
                lola.health += (-1 * enemy.damage) - lola.armor_strength
                print(" ")
                print("Lola has been hit! Her health is now " + str(lola.health) + ".")
        elif user_choice.lower().strip(" ") == "run":
            if lola.can_lola_run == True:
                print("You got away!")
                break
                lola.in_combat = False
            else:
                print(" ")
                print("There is nowhere to run!")
                lola.health += (-1 * enemy.damage)
                print("Lola has been hit! Her health is now " + str(lola.health) + ".")
                print(" ")
        elif user_choice.lower().strip(" ") == "dodge":
            random_instance = random.randint(0,9)
            if random_instance >= 4:
                lola.health += 20
                lola.dodge_counter += 1
                print("")
                print("Lola successfully dodged the attack!")
                print("Your health has increased to " + str(lola.health))
                print(" ")
            else:
                print(" ")
                print("Your attempt to dodge failed!")
                lola.health += (-1 * enemy.damage)
                print("Lola has been hit! Her health is now " + str(lola.health) + ".")
                print(" ")
        elif user_choice.lower().strip(" ") == "ability":
            if lola.does_ability_exist == True:
                enemy.health += (-1 * lola.ability_damage) - enemy.armor
                print(" ")
                print("Enemy hit!")
                print("Lola did " + str(lola.damage - enemy.armor) + " damage!")
                print("Enemy health is now " + str(enemy.health))
                if enemy.health > 0:
                    lola.health += (-1 * enemy.damage) - lola.armor_strength
                    print(" ")
                    print("Lola has been hit! Her health is now " + str(lola.health) + ".")
            else:
                print(" ")
                print("Lola does not have an ability yet!")
                print(" ")
                if enemy.health > 0:
                    lola.health += (-1 * enemy.damage) - lola.armor_strength
                    print(" ")
                    print("Lola has been hit! Her health is now " + str(lola.health) + ".")
    if enemy.health <= 0:
        print("Enemy Defeated!")
        lola.in_combat = False
    elif lola.health <= 0:
        if lola.num_of_ancestral_relics == 0:
            lose_state()
        else:
            lola.num_of_ancestral_relics += -1
            print(" ")
            print("Lola perished in combat, but using the power of an ancestral relic, she is revived.")
            print("The number of ancestral relics for Lola to use has been reduced from " + str(lola.num_of_ancestral_relics + 1) + " to " + str(lola.num_of_ancestral_relics) + ".")
            print("""
            Lola awakes half buried in black volcanic sand, in a crypt lit by a single torch.
            She recognizes it as the catacombs of the Church of Dani the All Mother, and sits up, sand 
            flowing off of her armor. Lola looks to her family's relics and sees one shattered on the ground.
            The loss of the relic stings, but Lola knows that the safety of the kingdom is worth the sacrifice.
            
            Lola goes up the stairs to the church's main hall, then walks out the open doors into the town square. 
                                                                                                              """)
            lola.in_combat = False
            arrival_at_location(town_square)

def arrival_at_location(location):
    print(" ")
    print(location.arrival_message)
    print(" ")
    if location.visit_count == 0:
        print(location.initial_description)
    location.visit_count += 1
    print(location.primary_npc_message)
    print(" ")
    if location == town_square and location.visit_count == 0:
        print(story_element_town_square_aftermath)
    elif lola.in_combat == False:
        user_choice = input("Your options are...")
        if user_choice == location.option_1:
            pass
        else:
          pass

def lose_state():
    print(lose_state_message)
    quit()

#damage_message = "Your health has been reduced to " + (str(lola.health))

#Default Lola Status Variables

class lola_main:
    health = 100
    max_health = 100
    armor_strength = 15
    damage = 35
    ability_damage = 55
    does_ability_exist = False
    dodge_counter = 0
    equipped_armor = "Leather Armor"
    equipped_weapon = "Training Sword"
    inventory = {"Weapons": ["Steel Sword", "Ash Bow"], "Greenies": 1}
    num_of_ancestral_relics = 1
    is_lola_dead = False
    can_lola_run = False
    current_location = "Lola's Bed Cottage"
    in_lose_state = False
    quest_items_remaining = []
    quest_items_obtained = []
    in_combat = False
lola = lola_main()

class CarDoorGoblin:
    health = 30
    damage = 55
    armor = 0
car_door_goblin_1 = CarDoorGoblin()

class ElevatorOrc:
    health = 100
    damage = 20
    armor = 10
elevator_orc_1 = ElevatorOrc()

class Location:
    primary_npc_message = " "
    arrival_message = " "
    initial_description = " "
    items_for_sale = " "
    next_location_choices = []
    reason_can_run = " "
    reason_cannot_run = " "
    visit_count = 0
    option_1 = " "
    option_2 = " "
    option_3 = " "
    option_4 = " "
    option_5 = " "

town_square = Location()
town_square.arrival_message = "Lola has arrived in the town square."
town_square.initial_description = """
    The square is in a state of absolute pandemonium. A small contingent of royal guards fruitlessly attempt to shout over 
the din. Vendors scramble to pack their wares into carts and woven baskets. Windows and shutters slam shut as families take 
shelter in their homes. Shopkeepers and citizens stomp at several fires burning around the square. Screaming from the surrounding 
streets echoes over the flagstones. Out of the clamor, Lola picks up on the sounds of yelling and steel smashing into steel 
coming from one of the streets that radiate from the town square. She looks towards that avenue and sees a small group of 
royal guards, in a shield
 wall formation, backpedalling as fireballs and spears smash into their shields. People begin to 
flee the opposite direction, Lola pushes through them as they stampede past her. Just as Lola reaches the middle of the square, 
the shield wall breaks, and a group of Car-Door Goblins burst in accompanied by three Elevator-Orcs. Chaos ensues as the 
royal guards charge and begin to engage with the enemy. Lola draws her sword as an Elevator-Orc runs towards her, spear raised."""

armory_description = """

        Cut into the side of the mountain that the castle rises out of, the armory resembles a small fort. The courtyard 
    of the armory is half bathed in sunshine, while the other half is cool and dark in the shadow of the rock overhanging. 
    Three stone walls, ten feet thick, encircle the courtyard on the outside, while the back wall is natural stone, with 
    soldiers quarters cut out from the craggy granite wall. The armory stands at the foot of the castle, next to the gate
    that leads to the castle bridge. It overlooks the north side of town, pointing straight at the towns main gate."""

armory = Location()
armory.arrival_message = "Lola has arrived at the armory."
armory.primary_npc = "Sargeant Lou"
armory.initial_description = armory_description

lose_state_message = """

    Lola awakes in an inky black void, the only features visible are two moons, one red, one grey. The red moon smashing 
into the grey, shattering it into uncountable pieces, but both hang silently, permanently frozen in this moment of astronomical 
violence. A silky voice comes from the void, the celestial voice of Dani, All Mother.
      "You have fought valiantly for the forces of good young knight, but the fate of the world is no longer your burden. 
Join me in the halls of eternity my child."

                                                     Game Over!
                                                                                                """

story_element_game_start = """

                                                Welcome to LolaQuest! 

                                You are about to embark on a thrilling adventure of old, 
                                where a young pup is called upon by destiny to defend her 
                                        homeland against the forces of evil.
                                                                                        """

story_element_lola_awakes = """

    Still clad in her leather training armor from the day before, Lola wakes from her deep sleep, her body aching from 
yesterday's training session. The words of Lou, the castle's Sargeant at arms, ring in her ears. 
    "You'll have to try harder than that if you want to be a knight some day!""
     Lola shifts in bed and all the newly formed bruises, left by the Sargeant's blunted training sword, began to make 
themselves known.She stares at the ceiling of her cottage as she comes to terms with the fact that the next few weeks will 
be some very sore ones. Her moment of self-pity is interrupted by the realization of what has woken her up. Her sensitive
nose has picked up the smell of smoke wafting through the gap under the door of her cottage. She takes off her leather helmet, 
allowing her capable, if not inordinately large, ears to tell her a fuller story. As she does she realizes that the noises 
she had mistaken as normal hustle and bustle of the castle in the morning are actually the sounds of full blown chaos.
Lola picks up her blunted steel training sword, and dashes across the room to the door, but the moment her paw touches 
the latch to open it.. 
   
                                                         BOOM!

     Lola is thrown back into her room by a fiery explosion. She lands in a heap, showered with thick splinters that used 
to be the door to her cottage. A Car-Door Goblin stands at her threshold, his left hand wielding a fireball, ready to throw. 
His right hand already making the fluid motions needed to conjure another. Lola hardly has the time to ponder how a Car-Door 
Goblin could possibly have gotten past the castle's defenses as she springs to her feet. """

story_element_greebo_arrives = """

    The goblin crumples in the doorway, a pool of sticky black blood pooling under him as the cinders on his hands fade 
from red hot to a warm glow. Lola steps over the wretched creature into the cramped, dark alleyway that her front door used 
to separate her cottage from. Coming from her left, a fireball zips inches over her head, obliterating a lantern that hung 
from her cottage entryway. Entering a defensive stance, Lola steels herself for another fight. Her heart drops when she looks 
to her left and sees a gang of ten goblins charging towards her, grinning as they cock their arms back, fireballs ready to 
throw. Lola raises her sword to strike the first of them, but in the moment before she brings the sword down, a brass sphere 
the size of an apple streaks down from directly above. And FWOOSH! In an instant the paving stones of the alley open into
a gaping maw where the brass relic hit, swallowing the goblins into the earth. The void disappears as fast as it had materialized, 
the goblins never even had time to scream. Shocked, Lola cranes her neck upward, to see The Royal Mage Greebo smiling down 
at her from the rooftops.
    "I thought Sargeant Lou would have taught you by now not to engage with so many enemies at once!"
    The wizard says with a wry smile. 
    "I hold that you would have become a fine young witch, this knight business is such a waste of talent."
    In one quick motion, Greebo wraps his cloak around himself, and leaps off the roof, out over the alley, 
transforming into a massive crow. The bird flies off in the direction of the town gate.
Lola sheaths her sword, and runs off down the alley towards the town square. 
"""

story_element_town_square_aftermath = """ 
    The Elevator Orc falls face down in front of Lola 
                    """

#End of world_building, start of game.
#End of world_building, start of game.
#End of world_building, start of game.
#End of world_building, start of game.
#End of world_building, start of game.

print(story_element_game_start)

user_choice = input("Enter \"play\" to continue. ")
if user_choice.lower().strip(" ") == "play":
    print(story_element_lola_awakes)

combat(car_door_goblin_1)

print(story_element_greebo_arrives)

user_choice = input("Enter the town square by typing enter. ")
if user_choice.lower() == "enter":
     pass

print(town_square.initial_description)

lola.in_combat = True

combat(elevator_orc_1)

print(story_element_town_square_aftermath)















