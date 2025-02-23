import random
#from words import words
import string
words = ["apple", "banana", "grape", "orange", "strawberry"]
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
 
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("YOu have" ,lives, " lives left and You have used these letter: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word ]
        print("Current Word: ", " ".join(word_list))
     
        user_letter = input("Guess a Letter: ").upper()
        if user_letter in alphabet - used_letters:
         used_letters.add(user_letter)
         if user_letter in word_letters:
              word_letters.remove(user_letter)
         else: 
            lives = lives - 1
            print("Letter is not in the WOrd")
            
              

        elif user_letter in used_letters:
         print("You already used this Character")
    
        else:
         print("Invalid Character")

    if lives == 0:
       print(" You have died the word was", word)     
    else:
       print("You guessed the word", word)

   
   



hangman()

