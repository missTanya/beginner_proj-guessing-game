
import random as r
import sys

class main():
    """
    This will ask the user to input a number between 0 and 20.
    """
    name = input("Hi, You are about to play a guessing game!\nWhat is your name? \n")
    tries = int(input("Welcome {}! How many tries do you want? ".format(name.title())))
    score = 0
    while (tries>0):
        answer = int(input("Enter a number between 0 and 20: "))
        choices = list(range(0,21))
        rand_num = r.choice(choices)
        if answer == rand_num:
            print("Congrats! You guessed the number!")
            break
        elif answer < rand_num:
            print("Your guess is too low! The random number is " + str(rand_num))
            tries -= 1
        else:
            print("Your guess is too high! The random number is " + str(rand_num))
            tries -= 1
    else:
        print("\nYou failed to guess the number. Thank you for playing")
        sys.exit(1)



if __name__ == "__main__":
    main()