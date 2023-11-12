#Nhmber guessing game
import random
print("Welcome to the number guessing game")
while True:
    upper_limit = int(input("Enter the upper limit of the number: "))
    lower_limit = int(input("Enter the lower limit of the number: "))
    if upper_limit < lower_limit:
        print("You have entered the wrong limit \nPlease enter the correct limit")
        continue
    elif upper_limit == lower_limit:
        print("You have entered the wrong limit \nPlease enter the correct limit")
        continue
    elif upper_limit - lower_limit < 10:
        print("You need an higher limit \nPlease enter the correct limit")
        continue
    else:
        break
#For easy mode
number1 = random.randint(lower_limit, upper_limit)
number2 = random.randint(lower_limit, upper_limit)
#For hard mode
number = random.randint(number1, number2)
#difficulty level
game_mode = ["easy", "hard"]
#check if the user has entered the correct option
while True: 
    option = input("Do you want to play the game in easy mode or hard mode? Type 'easy' or 'hard': ")
    if option not in game_mode:
        print("You have entered the wrong option \nPlease enter the correct option")
        continue
    if option == "easy":
        print("You have 5 chances to guess the number")
        chances = 0
        while chances <= 5:
            chances += 1
            guess = int(input("Guess the number: "))
            if guess == number1:
                print("You have guessed the number correctly in", chances, "chances")
                break
        else:
            continue
        break
            elif guess > number1:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
    if option == "hard":
        print("You have 3 chances to guess the number")
        chances = 0
        while chances <= 3:
            chances += 1
            guess = int(input("Guess the number: "))
            if guess == number:
                print("You have guessed the number correctly in", chances, "chances")
                break
            elif guess > number:
                print("Your guess is too high")
            else:
                print("Your guess is too low")