#Simone Greicius
#Period 4
#12/10/24

#initialize

#functions
def madlib(): #This is the function containing the mad lib game
    print("""Hello! Welcome to the madlib story!
    Please complete the following  requests to build your story:""")
    animal = input("Enter an animal") #The following inputs are used to complete the blanks in the story
    food = input("Enter a food")
    noun = input("Enter a noun")
    verb = input("Enter a verb")
    verb2 = input("Enter a second verb")
    print("""Thank you for your inputs! Here is the story:
          """)
    print("""
    If you give a """ + str(animal) + " a " + str(food) + """, they are going to ask for a
    """ + str(noun) + ". When you give them the " + str(noun) + """, they will want to
    """ + str(verb) + ". Of course, when they are finished they will want to " + str(verb2) + """.
    Then they will ask for a """ + str(noun) + """ again,
    and chances are if you give them a """
    + str(noun) + " they will want a " + str(food) + " ! ") #This is the story that is filled in by the inputs above 

    print("""
    Wow, that was an amazing story! Thank you for playing!""")
#main
madlib()
