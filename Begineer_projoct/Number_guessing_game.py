#Nhmber guessing game
import random
print("Welcome to the number guessing game")

play_game = ["yes", "no"]
while True:
    while True:
        upper_limit = int(input("Enter the upper limit of the number: "))
        lower_limit = int(input("Enter the lower limit of the number: "))
        if upper_limit < lower_limit:
            print("Upper limit cannot be lower than lower limit. \nPlease enter the correct limit")
            continue
        elif upper_limit == lower_limit:
            print("Upper and lower linit cannot be the same. \nPlease enter the correct limit")
            continue
        elif upper_limit - lower_limit < 10:
            print("You need an higher limit, atleast with a difference of ten \nPlease enter an higher limit")
            continue
        else:
            break

    #For easy mode
    number1 = random.randint(lower_limit, upper_limit)
    #For hard mode
    number = random.randint(number1, upper_limit)
    #difficulty level
    game_mode = ["easy", "hard"]
    chances = 5
    chances1 = 3
    tries = 0
    while True: 
        option = input("Do you want to play the game in easy mode or hard mode? Type 'easy' or 'hard': ").lower()
        #check if the user has entered the correct option
        if option not in game_mode:
            print("You have entered the wrong option \nPlease enter the correct option")
            continue
        else:
            break
    #game
    while chances > 0 and option== "easy":
                print("You have", chances, "chances to guess the number")
                guess = int(input("Guess the number: "))
                chances -= 1
                tries += 1
                if guess == number1:
                    print("You have guessed the number correctly in", tries, "tries")
                    break
                elif guess > number1:
                    print("Your guess is too high")
                    continue
                else:
                    print("Your guess is too low")
                    continue
    while chances1 > 0 and option== "hard":
                    print("You have", chances1, "chances to guess the number")
                    guess = int(input("Guess the number: "))
                    chances1 -= 1
                    tries += 1
                    if guess == number:
                        print("You have guessed the number correctly in",tries, "tries")
                        break
                    elif guess > number:
                        print("Your guess is too high")
                        continue
                    else:
                        print("Your guess is too low")
                        continue
    play_again = input("Do you want to play the game again? Type 'yes' or 'no': ").lower()
    if play_again not in play_game:
        print("You have entered the wrong option \nPlease enter the correct option")
        continue
    elif play_again == "no":
        print("Thank you for playing the game")
        break
    else:
        continue
