import re

string_to_use = ''
# String below for testing
# string_to_use = "The first card is for me. 4 of hearts. 8 of Spades. Now two cards for you. Your first two cards are. 2 of hearts, and Ace of diamonds. That's 13 points. Do you want another card?"

card_points = {
    "Ace of Spades": 1,
    "2 of Spades": 2,
    "3 of Spades": 3,
    "4 of Spades": 4,
    "5 of Spades": 5,
    "6 of Spades": 6,
    "7 of Spades": 7,
    "8 of Spades": 8,
    "9 of Spades": 9,
    "10 of Spades": 10,
    "king of Spades": 10,
    "queen of Spades": 10,
    "jack of Spades": 10,
    "Ace of Diamonds": 1,
    "2 of Diamonds": 2,
    "3 of Diamonds": 3,
    "4 of Diamonds": 4,
    "5 of Diamonds": 5,
    "6 of Diamonds": 6,
    "7 of Diamonds": 7,
    "8 of Diamonds": 8,
    "9 of Diamonds": 9,
    "10 of Diamonds": 10,
    "king of Diamonds": 10,
    "queen of Diamonds": 10,
    "jack of Diamonds": 10,
    "Ace of Hearts": 1,
    "2 of Hearts": 2,
    "3 of Hearts": 3,
    "4 of Hearts": 4,
    "5 of Hearts": 5,
    "6 of Hearts": 6,
    "7 of Hearts": 7,
    "8 of Hearts": 8,
    "9 of Hearts": 9,
    "10 of Hearts": 10,
    "king of Hearts": 10,
    "queen of Hearts": 10,
    "jack of Hearts": 10,
    "Ace of Clubs": 1,
    "2 of Clubs": 2,
    "3 of Clubs": 3,
    "4 of Clubs": 4,
    "5 of Clubs": 5,
    "6 of Clubs": 6,
    "7 of Clubs": 7,
    "8 of Clubs": 8,
    "9 of Clubs": 9,
    "10 of Clubs": 10,
    "king of Clubs": 10,
    "queen of Clubs": 10,
    "jack of Clubs": 10,
}

def process_string(string):
    # Convert to lower case
    string = string.lower()
    # Remove all punctuation that's not a space
    string = re.sub(r'[^\w\s]', '', string)
    # Ensure that every word/number has only 1 space between it
    string = re.sub(r'\s+', ' ', string)
    return string

def search_phrases(dictionary, string):
    found_phrases = []
    numeric_values = []
    lower_string = string.lower()
    for i in range(len(lower_string)):
        for phrase in dictionary:
            lower_phrase = phrase.lower()
            if lower_string[i:i+len(lower_phrase)] == lower_phrase:
                found_phrases.append(phrase)
                numeric_values.append(dictionary[phrase])
                break  # Once a match is found, break out of the inner loop to avoid duplicate matches
    print(f"Phrases found:{found_phrases}")
    print(f"Found numeric values:{numeric_values}")
    return found_phrases, numeric_values

def process_find_and_sort(input_text):
    print(input_text)
    input_text = process_string(input_text)
    print(f"Cleaned text: {input_text}")
    search_phrases(card_points, input_text)

process_find_and_sort(string_to_use)
