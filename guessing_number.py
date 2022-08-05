import random as rd
from tracemalloc import stop

class guess_a_number():
    def __init__(self):
        print("===== GUESS A NUMBER =====")
        print('\n')
        self.take_a_number()

    def take_a_number(self):
        self.limit_number = int(input("Please input a number ? "))
        self.guess = rd.randint(1, self.limit_number)
        print("You will guessing number between 1 till ", self.limit_number, "\n\n")
        self.loop()

    def loop(self):
        error = 0 # membuat program tetap berjalan
        while error != self.guess:
            answer = int(input("Input your answer "))

            if answer == self.guess:
                print("CONGRATULATONS you did it, the number is ", self.guess)
                error = self.guess 
            elif answer < self.guess:
                print("Wrong, it's too low, try higher number")
            elif answer > self.guess:
                print("Wrong, it's too high, try lower number")
            else:
                print("Your are an Idiot, it damn Number")

        self.computer_guess()
    
    def computer_guess(self):
        self.take_turn = input("\n\nWanna take a Turn ?\n type Yes or No \nYour answer : ")
        if self.take_turn == "Yes" or "yes":
            self.computer_loop()
            
        else:
            print("OK")

    def computer_loop(self):
        self.x = int(input("till what number ? "))
        print("I Will guess from 1 till ", self.x)
        error2 = 0
        low = 1
        high = self.x
        while error2 != 1:
            self.computer_answer = rd.randint(low, high)
            print()
            self.user_answer = str(input(f"If {self.computer_answer} is too low click L, too high H, and correct C\nHow : ")).lower()
            if self.user_answer == 'c':
                error2 = 1

            elif self.user_answer == 'h':
                high = self.computer_answer - 1

            elif self.user_answer == 'l':
                low = self.computer_answer + 1

            else:
                print("WTH")    

        print("Well, I am smart computer, with ", self.computer_answer, " as my answer")



            
guess_a_number()
