import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user has gussed
    
    # getting user input
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))


        word_list = [letter if letter in used_letter else '-' for letter in word ]
        print('Current word: ',' '.join(word_list)) 



        user_letters = input('Guess a letter: ').upper()
        if user_letters in alphabet - user_letters:
            user_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
        
        elif user_letters in user_letters:
            print("You have already used that character. Please try again.")
        
        else:
            print('Invalid character. Please try again.')



user_input = input('Type something: ')
print(user_input)