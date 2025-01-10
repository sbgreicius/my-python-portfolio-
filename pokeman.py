#Simone Greicius
#Pokeman Evolution
#November 21
#Init
pokemon_level = 0
pokemon_name = "Bulbasaur"
day = 1
level = 0
wins = 0
loss = 0
import random
#Functions
def draw_bulbasaur(): #This function draws the bulbasaur
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬜⬛⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜
⬜⬜⬛🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛🟦🟦🟦⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬜⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜⬜🟦🟦⬛🟦🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦🟦⬛🟥⬜🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def draw_ivysaur(): #This function draws the ivysaur
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🏻⬛🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛🏻🏻🏻⬛🟥⬛🏽🏽⬛⬜⬜⬜
⬜⬜⬜⬛⬜⬛🏽🏽⬛🏻🏻⬛🟥🟥⬛⬛⬛🟩⬛⬜⬜
⬜⬜⬛🟦⬛🟩🟩⬛⬛⬛🏻🟥🟥⬛🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬛🟦🟦⬛⬛🟩🟩🏽⬛⬛⬛⬛⬛⬛⬛🟩🟩⬛⬜
⬜⬜⬛🟦🏽🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬜⬛🟦🟦🏽🏽🟦🟦🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🏽🟦🟦🟦🟦⬛🟩⬛🟩⬛🟩⬛⬛
⬛⬛🟦🟦🟦🏽🏽🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛🟩🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🏽🟦⬛⬛⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🏽🟦🌫️⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟥🟥⬜🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def draw_venusaur(): #This function draws the venusaur 
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥🟨🟨⬛🟥🟨🟨🟥⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟥🟥🟥⬛⬛⬛🟥🟥🟨🟨🟥⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥🟥⬛⬛🟨🟨🟨⬛⬛⬛⬛🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥⬛⬛🟥🟥⬛⬛🟨🟨⬛🟥🟨⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟥🟨🟨🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟩⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛🟨🟨🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬛⬜⬜
⬜⬜⬜⬛🟦⬛⬛🟩⬛🟩🟩⬛⬛⬛🟥🟥🟥⬛⬛⬛⬛⬛⬛🟩⬛⬛⬜
⬜⬜⬜⬛🟦🟦⬛⬛⬛🟩⬛⬛🟩🟩⬛⬛⬛🟩⬛🟩🟩🟩⬛⬛🟩🟩⬛
⬜⬜⬜⬛🟦🟦🟦🟦🟦⬛⬛⬛⬛🟩🟩⬛🟩⬛⬛🟩⬛🟩🟩⬛🟩⬛⬛
⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛🟦⬛⬛🟩⬛🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬛🟩⬛🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦⬛🟦🟦🟦⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦🟦🟦⬛🟦🟦🌫️⬛⬜⬜
⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛🟦⬛🟦⬛🟦🌫️⬛⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦🟦🟦⬛⬜⬛⬛⬜⬜⬜⬜
⬜⬛⬛🟦🟦🟦🟦🟦⬛⬜⬜🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜""")
def train(): #This trains the pokemon, advancing it one level
    global level
    global day
    print("Train: " + str(pokemon_name) + " " + "did 10 pushups")
    level = level + 1
    print(str(pokemon_name) + " " + "is on level " + str(level))
    day = day + 1

def battle(): #has the pokemon battle
    global level
    global day
    global wins
    global loss
    print("Battle: ")
    if level < 16: #This is the normal battle when the pokemon has not reached its final form
        battles = int(input(pokemon_name + " is battling a wild pokemon! Will " + pokemon_name + " win? pick a number, 1 or 2?"))
        global pokemon_level
        if battles == random.randint(1,2):
            pokemon_level = pokemon_level + 2
            print(pokemon_name + " won the battle! " + pokemon_name + " gained 2 levels!")
            level = level + 2
            day = day + 1
            wins = wins + 1
        else:
            print(pokemon_name + " lost the battle :(")
            day = day +  1
            loss = loss + 1
    else: #This is the final battle when the pokemon is in final form
        print("You have reached the final battle with the final boss.")
        finalBattle = int(input(pokemon_name + " is battling the final boss! Will " + pokemon_name + " win? Pick a number 1 through 25"))
        if finalBattle == random.randint(1,25):
            print(pokemon_name + " has beat the final boss!")
            print("Congratulations! You have won the game! Keep playing for fun or quit game")
        else:
            print(pokemon_name + " lost the battle :(")
            print("Dont give up!! Keep trying, we believe in you!")

def evolve(): #This is the evolution for the pokemon that is displayed in the rest
    global pokemon_name
    global day
    global wins
    global loss
    if level <= 5: #This is the first level of the pokemon
        print("Rest: " + str(pokemon_name)+" is on level " + str(level))
        if wins == 1 and loss == 1:
            print(str(pokemon_name) + " has " + str(wins) + " win and " + str(loss) + " loss.")
        elif wins != 1 and loss == 1:
            print(str(pokemon_name) + " has " + str(wins) + " wins and " + str(loss) + " loss.")
        elif wins == 1 and loss != 1:
            print(str(pokemon_name) + " has " + str(wins) + " win and " + str(loss) + " losses.")
        draw_bulbasaur()
        print("Get to level 6 to evolve into venusar!")
        day = day + 1
    elif level < 5 <= 15: #This is the second level of the pokemon
        pokemon_name = "Ivysaur"
        print("Rest: ")
        print("Congrats! Your pokemon has evolved.")
        print(str(pokemon_name) + " is on level " + str(level))
        print(str(pokemon_name) + " has " + str(wins) + " wins and " + str(loss) + " losses.")
        draw_ivysaur()
        print("Get to level 16 to evolve into venusaur!")
        day = day + 1
    else: #This is the final level of the pokemon
        pokemon_name = "Venusaur"
        print("Rest: ")
        print("Congrats! You have evolved into the final form!")
        print(str(pokemon_name) + " has " + str(wins) + " wins and " + str(loss) + " losses.")
        print(str(pokemon_name)+ " is on level " + str(level))
        draw_venusaur()
        day = day + 1

def rest(): #This displays the pokemons level, wins and losses, and its image
    evolve()


def quit(): #This breaks the loop, allowing the player to end the game
    print("Thank you for playing!")

def pokemon_Game(): #this is the final function
    while True:
        print(" ")
        print("Welcome to Pokemon Evolution")
        print("Choose and activity for day " + str(day))
        print("""
        1.Train
        2.Battle
        3.Rest
        4.Quit""")
        activity= int(input("Choose an option 1 through 4"))
        if activity == 1:
            train()
        elif activity == 2:
            battle()
        elif activity == 3:
            rest()
        else:
            quit()



#Main

pokemon_Game()
