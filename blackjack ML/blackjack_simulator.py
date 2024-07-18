import random

card_points = {
    "ace of spades": 1,
    "two of spades": 2,
    "three of spades": 3,
    "four of spades": 4,
    "five of spades": 5,
    "six of spades": 6,
    "seven of spades": 7,
    "eight of spades": 8,
    "nine of spades": 9,
    "ten of spades": 10,
    "king of spades": 10,
    "queen of spades": 10,
    "jack of spades": 10,

    "ace of diamonds": 1,
    "two of diamonds": 2,
    "three of diamonds": 3,
    "four of diamonds": 4,
    "five of diamonds": 5,
    "six of diamonds": 6,
    "seven of diamonds": 7,
    "eight of diamonds": 8,
    "nine of diamonds": 9,
    "ten of diamonds": 10,
    "king of diamonds": 10,
    "queen of diamonds": 10,
    "jack of diamonds": 10,

    "ace of hearts": 1,
    "two of hearts": 2,
    "three of hearts": 3,
    "four of hearts": 4,
    "five of hearts": 5,
    "six of hearts": 6,
    "seven of hearts": 7,
    "eight of hearts": 8,
    "nine of hearts": 9,
    "ten of hearts": 10,
    "king of hearts": 10,
    "queen of hearts": 10,
    "jack of hearts": 10,

    "ace of clubs": 1,
    "two of clubs": 2,
    "three of clubs": 3,
    "four of clubs": 4,
    "five of clubs": 5,
    "six of clubs": 6,
    "seven of clubs": 7,
    "eight of clubs": 8,
    "nine of clubs": 9,
    "ten of clubs": 10,
    "king of clubs": 10,
    "queen of clubs": 10,
    "jack of clubs": 10,
}

card_points_temporary = card_points.copy()

def generate_random_blackjack_values_for_dealer():
    global card_points_temporary
    name, numeric_value = random.choice(list(card_points_temporary.items()))
    card_value = numeric_value
    del card_points_temporary[name]  # Remove the selected card from card_points_temporary
    print(card_value)

def generate_random_blackjack_values_for_player():
    global card_points_temporary
    name, numeric_value = random.choice(list(card_points_temporary.items()))
    card_value = numeric_value
    del card_points_temporary[name]  # Remove the selected card from card_points_temporary
    print(card_value)

def reset_temporary_cards():
    global card_points_temporary
    card_points_temporary = card_points.copy()

for x in range(52):
    generate_random_blackjack_values_for_dealer()
