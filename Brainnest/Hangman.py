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

''' 
The program starts by importing the random module.
The hangman function is defined and the word variable is assigned a random word from the list of words.
The word_list variable is assigned a list of the letters in the word variable.
The word_list_copy variable is assigned a copy of the word_list variable.
The word_list_copy variable is assigned a list of "-" the same length as the word_list_copy variable.
The tries variable is assigned the value 6.
The used_letters variable is assigned an empty list.
The while loop is used to run the game until the tries variable is less than or equal to 0.
The print function is used to print the number of tries left.
The print function is used to print the used letters.
The print function is used to print the word.
The guess variable is assigned the input from the user.
The if statement is used to check if the guess variable is more than one letter.
The print function is used to print the error message.
The elif statement is used to check if the guess variable is not a lowercase letter.
The print function is used to print the error message.
The elif statement is used to check if the guess variable is in the used_letters variable.
The print function is used to print the error message.
The elif statement is used to check if the guess variable is in the word_list variable.
The for loop is used to loop through the word_list variable.
The if statement is used to check if the letter in the word_list variable is equal to the guess variable.
The word_list_copy variable is assigned the letter in the word_list variable.
The used_letters variable is appended with the guess variable.
The else statement is used to run if the guess variable is not in the word_list variable.
The print function is used to print the error message.
The used_letters variable is appended with the guess variable.
The tries variable is subtracted by 1.
The if statement is used to check if the "-" is not in the word_list_copy variable.
The print function is used to print the word.
The break statement is used to exit the loop.
The else statement is used to run if the tries variable is less than or equal to 0.
The print function is used to print the error message.
The hangman function is called.
'''