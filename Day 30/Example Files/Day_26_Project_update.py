#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

alphabet_dict = {str(row.letter):str(row.code) for (index, row) in pandas.read_csv(r"Day 30\Example Files\nato_phonetic_alphabet.csv").iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
invalid_entry = True

while invalid_entry:
    user_word = input("Enter a word: ").upper()
    try:
        code_words = [alphabet_dict[letter] for letter in user_word]
        print(f"Code words are {code_words}")
    except KeyError:
        print("Sorry, only letters in the alphabel please.")
    else:
        invalid_entry = False
    