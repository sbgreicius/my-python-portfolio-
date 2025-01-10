#Simone Greicius
#This or that project
#10/17
print("Welcome to What Animal Are You") #This introduces the name of the game
print("Answer these questions to find out what animal you are!")
ans = input("summer or winter?") #This is the initial question, which will lead to following questions depending on what the answer is
if ans == "summer":
    ans = input ("hiking or swimming?")
    if ans == "hiking":
        ans = input ("shade or sun?")
        if ans == "shade":
            print("You are a fox!")
        else:
            print("You are a lizard!")
    if ans == "swimming":
        ans = input ("social or prefer to be alone?")
        if ans == "social":
            print("You are a fish!") #This is one of the final answers 
        else:
            print("You are an octopus!") #This is one of the final answers
if ans == "winter":
    ans = input ("shower or bath?")
    if ans == "shower":
        ans = input ("energetic or calm?")
        if ans == "energetic":
            print("You are a polar bear!")
        else:
            print("You are a reindeer!")
    if ans == "bath":
        ans = input ("quiet or loud?")
        if ans == "quiet":
            print("You are a snow owl!") #This is one of the final answers
        else:
            print("You are an sea lion!") #This is one of the final answers

