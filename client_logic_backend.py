# Alexa responses general
blacksmith_response_1 = "okay.Do you have time to enhance an item? Should I improve your sword, armor, or quarters?"
blacksmith_response_1_1 = "you got it.Can you fit me in for an upgrade?Should I upgrade your sword, armor, or quarters?"
blakcsmith_response_1_2 = "sure.Do you have time to enhance an item?Want me to empower your sword, armor, or quarters?"
blacksmith_response_1_3 = "ok. Greetings Giovanni! Can I empower your sword, armor, or quarters?"

backpack_main = "alright.In your backpack are 24 items of the following categories. Craft goods, Food, and Consumables.Which category do you want to choose?"


# Alexa responses fight

fight_1 = """
Centurion MONARK, (Rank (B (4))), is set to brawl, Blood Guard Buddy, from Germany, (Rank (B (4))). The knights quickly go into motion.Buddy, attacking first lunges.MONARK is fortunate saving himself, with a leap to the side.he clasps his hands before his chest. In a calm and focused stance, he murmurs softly and melodically, uttering the words of an ancient incantation.Before Buddy's eyes, a perfect replica of the opponent manifests, identical in armor and appearance.Swiftly, Buddy makes his choice and attacks the selected knight with resolute determination.The strike from Buddy is so powerful that it causes the mirror image of the false knight to burst into tiny splinters.MONARK takes advantage of the situation and moves behind Buddy.He takes his time and takes a long swing.1473 Damage.Buddy swiftly applies a field bandage (level 2).The magic gauze has restored 1200 health points.First Sergeant Search eve Kemper, rushes in to help his ally, MONARK. He gallops in on his small bronco, his sword swinging directly towards Buddy.But Buddy helps himself by jumping sideways.He strikes back.MONARK moves away. He parrys that attack.He swings back.That was a critical blow and it causes 2488 damage.Buddy only has 239 health points left before he is vanquished.At the end of his endurance, Buddy strives for one last attack.That was a critical hit, causing 2533 damage.MONARK has been clobbered!Your knight MONARK has lost this battle.He received 70 experience points.Do you want me to find you a new opponent now?
"""

fight_2 = """
Centurion MONARK, (Rank (B (9))), is about to battle, Legionnaire Big gator, (Rank (B (19))). The knights quickly go into motion.Before the fight even begins, MONARK crosses his hands in front of his chest. In a calm and focused posture, he softly murmurs the melodic words of an ancient spell.Big gator witnesses the manifestation of a complete mirror image of the opponent.Big gator quickly makes his decision and charges with determination towards one of the knights to attack.His blow lands with such force on the false knight that the mirror image shatters into a thousand fragments.MONARK takes advantage of the situation and sneaks behind Big gator.He takes his time and takes a fast swing.1472 Damage.Big gator has 338 health points left before he is beaten.MONARK slips under his opponents guard and whacks his rival.This brutal attack inflicts 589 damage.Big gator has been clobbered!Standing in the middle of the arena, he raises his arms, salutes, then spins and jogs off.MONARK wins. He earns 27 honor points, 67 experience, and one serf from Big gator.Rising 5 spots in the rookie standings B, MONARK now holds the 4th position.Do you want to fight  another opponent?
"""
fight_3 = """
Centurion MONARK, (Rank (B (4))), is set to brawl, Legionnaire Safira, the prophet, from Germany, (Rank (B (18))). The knights quickly go into motion.MONARK dominates with the first attack.That was a critical hit, causing 2788 damage.Safira was whipped!He raises his weapon, and parades around the arena, then walks out.MONARK receives 27 honor points, and 67 experience.MONARK has risen in group (A), and is now 50 on that list.The King enjoyed this duel and tosses him 5 diamonds.Do you want me to find you a new opponent now?
"""

fight_4 = """
A random opponent was selected.Centurion MONARK, (Rank (A (46))) brawls against Commander Krusty dreams, the grim reaper, (Rank (A (6))). They attack!Swiftly, Krusty dreams takes advantage of a flaw in his enemies defensive stance, and attacks MONARK with the special stab; PIERCE!.1920 damage was inflicted by this assault! Krusty dreams's opponent has been pierced.MONARK drops like a rock.Your knight has lost this battle.He acquired 31 experience points.Do you want me to find you another opponent now?
"""

# Client states
yes = "yes"
blacksmith = "blacksmith"

# create a dictionary for searching alexa's responses 

cient_logic_dictionary = [
    "blacksmith", blacksmith_response_1, blacksmith_response_1_1, blakcsmith_response_1_2, blacksmith_response_1_3,
    "backpack", backpack_main,
    "fights", fight_1, fight_2, fight_3
]
