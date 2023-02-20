'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

# Code
import random

def hangman():
    word = random.choice(["python", "java", "kotlin", "javascript"])
    word_list = list(word)
    word_list_copy = list(word)
    word_list_copy = ["-" for i in range(len(word_list_copy))]
    tries = 6
    used_letters = []
    while tries > 0:
        print(f"You have {tries} tries left.")
        print("Used letters:", " ".join(used_letters))
        print("Word:", " ".join(word_list_copy))
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
        elif guess.islower() == False:
            print("It is not an ASCII lowercase letter")
        elif guess in used_letters:
            print("You already typed this letter")
        elif guess in word_list:
            for i in range(len(word_list)):
                if word_list[i] == guess:
                    word_list_copy[i] = guess
            used_letters.append(guess)
        else:
            print("No such letter in the word")
            used_letters.append(guess)
            tries -= 1
        if "-" not in word_list_copy:
            print("You guessed the word {} !".format(word))
            break
    else:
        print("You are hanged!")

hangman()