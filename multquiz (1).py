#Simone Greicius
#Multiplication quiz
#1/8/25

#init
import random #This was used to generate random numbers for the multiplication problems
score = 0
global score
#functions
def easy1(): #This was the easiest level of the game, randing from numbers 0 to 10. Easy mode is activated if the player chooses that level
    global score
    for i in range(quiz):
        one = random.randint(0,10)
        two = random.randint(0,10)
        print("What is " + str(one) + " times " + str(two))
        product = one * two
        answer = int(input("Enter your answer"))
        if product == answer:
            print("You are correct!")
            score = score + 1
        if product != answer:
            print("You are incorrect, the correct answer is " + str(product))
def medium1(): #This is the medium level of the game, ranging from numbers 0 to 20. Medium mode is activated if the player chooses that level
         global score
         for i in range(quiz):
              one = random.randint(0,20)
              two = random.randint(0,20)
              print("What is " + str(one) + " times " + str(two))
              product = one * two
              answer = int(input("Enter your answer"))
              if product == answer:
                   print("You are correct!")
                   score = score + 1
              else:
                    print("You are incorrect, the correct answer is " + str(product))
def hard1():#This is the hardest level, ranging from numbers 0 to 30. Activated if the player chooses this level
     global score
     for i in range(quiz):
        one = random.randint(0,30)
        two = random.randint(0,30)
        print("What is " + str(one) + " times " + str(two))
        product = one * two
        answer = int(input("Enter your answer"))
        if product == answer:
            print("You are correct!")
            score = score + 1
        if product != answer:
            print("You are incorrect, the correct answer is " + str(product))
def multiplication_quiz(): #This is the function for the game that allows the player to choose the number of questions along with the difficulty level 
    global score
    global quiz
    print("Hello! Welcome to the multiplication game!")
    print("I am going to ask you some multiplication problems!")
    print("How many questions would you like for there to be in this quiz?")
    quiz = int(input("Enter how many questions you would like")) #Lets the user choose the number of questions
    level = str(input("Enter which level you would like: easy, medium, or hard"))#lets the user determine their difficulty level
    if level == str("easy"):
         easy1()
    elif level == str("medium"):
         medium1()
    else:
         hard1()

    print("Good work!")
    print("Your score is " + str(score))

multiplication_quiz()
