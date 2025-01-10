#Simone Greicius
#Guessing Game
#November 11
import random

def guessingGame1(): #This function is my initial guessing game without any extensions
    print("Welcome to the guessing game! Try to guess the correct number!")
    secret = random.randint(0,10)
    user_guess = int(input("Enter a number 0 through 10"))
    if user_guess == secret:
        print("Congratulations! You guessed the correct number")
    else:
        print("You are incorrect, the correct number was " + str(secret))
def guessingGame2(): #This function includes extentions allowing for 3 tries and greater than or less than hints
    print("Welcome to the guessing game! Try to guess the correct number in three tries!")
    secret = random.randint(0,10)
    user_guess = int(input("Enter a number 0 through 10"))
    if user_guess == secret:
        print("Congratulations! You guessed the correct number")
    elif user_guess < secret:
        print("You guess is less than the correct number, you have two more tries!")
        user_guess = int(input("Enter a number 0 through 10"))
        if user_guess == secret:
            print("Congratulations! You guessed correctly!")
        elif user_guess > secret:
            print("Your guess is bigger than the correct number, you have one more try!")
            user_guess = int(input("Enter a number 0 through 10"))
            if user_guess == secret:
                print("Congratulations! You guessed correctly!")
            else:
                print("You were incorrect, the correct number was " + str(secret))
        else:
            print("Your guess is less than the correct number, you have one more try!")
            user_guess = int(input("Enter a number 0 through 10"))
            if user_guess == secret:
                print("Congratulations! You guessed correctly!")
            else:
                print("You were incorrect, the correct number was " + str(secret))
    else:
        print("You guess is more than the correct number, you have two more tries!")
        user_guess = int(input("Enter a number 0 through 10"))
        if user_guess == secret:
            print("Congratulations! You guessed correctly!")
        elif user_guess > secret:
            print("Your guess is bigger than the correct number, you have one more try!")
            user_guess = int(input("Enter a number 0 through 10"))
            if user_guess == secret:
                print("Congratulations! You guessed correctly!")
            else:
                print("You were incorrect, the correct number was " + str(secret))
        else:
            print("Your guess is less than the correct number, you have one more try!")
            user_guess = int(input("Enter a number 0 through 10"))
            if user_guess == secret:
                print("Congratulations! You guessed correctly!")
            else:
                print("You were incorrect, the correct number was " + str(secret))
    print("Would you like to play again?") #This allows the player to continue the game or exit the game. 
    answer = input("Yes or No?")
    if answer == "No" or  answer == "no":
        print("Thank you for playing! Have a nice day.")
    else:
        guessingGame2()


guessingGame2()

