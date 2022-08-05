import random as rd


def start_game():
    print ("==========GAME START===========")
    h_points = 0
    c_points = 0
    while h_points != 3 or c_points != 3:
        c_choice = rd.choice(["r", "p", "s"])
        h_choice = str(input("press r for rock, p for paper, s for scissors. 3 point to win\nYour choice : "))
        if h_choice == c_choice:
            print("TIE\n")

        elif (h_choice == "r" and c_choice == "s") or (h_choice == "s" and c_choice == "p") or (h_choice == "p" and c_choice == "r"):
            h_points += 1
            print("You win\nYour point is : ", h_points,", while computer points is :", c_points)
            print("\n")

        elif (h_choice == "s" and c_choice == "r") or (h_choice == "r" and c_choice == "p") or (h_choice == "p" and c_choice == "s"):
            c_points += 1
            print("You lose\nYour point is : ", h_points,", while computer points is :", c_points)
            print("\n")

        else:
            print("Please choose correct key")
            print("\n")

    if h_points >= 3:
        print("You win the game")
    elif c_points >= 3:
        print("You lose the game")


    print ("==========GAME END===========")
    
start_game()

        

        