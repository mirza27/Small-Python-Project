from operator import le
import random as rd
from re import template
from library_hangman import words

def get_word(library):
    word = rd.choice(words) #choose a random word 
    return word # mengeluarkan variable word dari def get_word agar terbaca di def hangman()

    
def hangman():
    print("="*10, "WELOCOME TO MY MINI HANGMAN", "="*10)
    print("\n")
    word = get_word(words)
    word = list(word) # memecah huruf dari kata

    letter_number = len(word)
    letter_true = 0
    letter_has_guessed = []
    display = "X"*letter_number 
    display = list(display)
    wrong_point = 0 # limit points to get a hint or give up

    while letter_number != letter_true : # berhenti saat semua huruf dari kata terjawab
        print(word)
        print(f"This word has {len(word)} letters")
        print(f"Letter that has guessed ({letter_has_guessed})")
        user_guessed = str(input("Guess a letter : "))
        
        if user_guessed in word:
            print(f"\nYou are right, word {user_guessed} is in the word")
            index_anwswered = word.index(user_guessed) + 1 # mencari index huruf yang benar
            print("that is letter number ",index_anwswered)

            display[index_anwswered -1] = user_guessed
            print("".join(display).upper(), "\n") # menampilkan huruf yang terjawab

            letter_true += 1
            letter_has_guessed += user_guessed


        elif user_guessed in letter_has_guessed:
            print("\nYou have already guessed ", user_guessed)


        elif wrong_point == 5:
            #hint_or_surrend
            print("\nYou have already wrong 5 times\nPress H for hint and S for surrend")
            error = 0
            while error == 0:   
                user_hs = input("Your Answer: ")

                if user_hs == "h":
                    print("hint works")
                    hint = rd.choice(word)
                    print(f"{hint} is one of the letter\n\n")
                    error += 1

                elif user_hs == "s" or "S":
                    print("\nUGH sorry the word is ", word,"\n")
                    letter_true = letter_number
                    error += 1
                
                else:
                    pass

            wrong_point -= 5


        else:
            print("\nSorry You are wrong, guess another letter")
            letter_has_guessed += user_guessed
            wrong_point += 1
    

    print("="*10, "GAME END", "="*10)
    print()



hangman()