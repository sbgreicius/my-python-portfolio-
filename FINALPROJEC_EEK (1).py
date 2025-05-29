#MOVIE CHOOSER

#initialize
import random #This allows me to use random.choice to select a random movie from my filtered list
from PIL import Image #Importing lines 5-6 is used in the open_image function that we made in class
import requests
from io import BytesIO
#Some of the data was cut off due to the parameters of the pdf, the link below is a google sheet with all of the data used
#https://docs.google.com/spreadsheets/d/1hQVFB-pw9IEkzDn03MxB_XWo8mvEaPud7erUT1LGt0c/edit?usp=sharing

#functions
#The movieList function is used to append certain movies to the filteredList
movieList = ["Mama Mia","La La Land", "Grease","Hairspray","The Sound of Music","Moonlight","Call Me By Your Name", "A Real Pain","Goodbye Lenin","Palo Alto","Good Will Hunting","Fantastic Mr.Fox","My Neighbor Totoro","Sleeping Beauty","Zootopia", "Ponyo","Wild Child","Dazed and Confused","Wet Hot American Summer","Legally Blonde","Bring it On","Psycho","Hereditary","Midsommar","Barbarian","The Witch"]
links =["https://m.media-amazon.com/images/M/MV5BMTA2MDU0MjM0MzReQTJeQWpwZ15BbWU3MDYwNzgwNzE@._V1_.jpg", #This list is used to open the image of the movie selected!
         "https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BNGY0NzE0ZTctN2YzNC00M2IwLWI0OWYtMTAwZWU2NjZhMTQwXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BYzBiNjJhNmUtMjM0Yi00ZjZkLTliNzUtYWEyYmVkZTFhMmQzXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BYWJhYmU4MjQtZDJhYi00ZGVjLTlkNTEtNzkzNGVjOWQ3MjcwXkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BNzQxNTIyODAxMV5BMl5BanBnXkFtZTgwNzQyMDA3OTE@._V1_QL75_UX190_CR0,0,190,281_.jpg",
         "https://resizing.flixster.com/fqA2ALSWe0CIjYaDdkDiW4ONqLI=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p14169043_v_v13_at.jpg",
         "https://m.media-amazon.com/images/M/MV5BODY2YWYwM2YtZTVlNC00MjgyLTgzYTgtNmFmYWE5ZmY1MDM5XkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BMjhlNTY2YzUtOWIwYS00MjIwLThjZGUtMDNiNTQzZmM1MTdjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BMTU4MTA5MzA5MF5BMl5BanBnXkFtZTgwNzE4NzA1MTE@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BNDdjZGQ5YzEtNTc2My00Mjc0LWFlMTctYzkwMzZlNzdiZWYzXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BYTA1ZTIxZDUtNGFjYS00YTc5LTgzNDMtZWNjYjBlMzI2OTk3XkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BYWM3MDE3YjEtMzIzZC00ODE5LTgxNTItNmUyMTBkM2M2NmNiXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BYjVjNjZkNTQtOTRhZi00NTVhLThkMzktYzY4YjIwZWRhZjA0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BZDkzMzQ5ZmQtOTA3MC00MjhiLTk5M2UtNzk0MjEzZmVjN2UxXkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BNmVlZTY2ZGUtOTIzNi00N2E5LWI0YmItNjkyYTdjMjgwMDNjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BODQ3YjVmY2QtM2I3ZS00NmExLTk2MGEtNTRhZGZhZjc5NzNjXkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BMTc5MDM1Njg2Nl5BMl5BanBnXkFtZTgwODE1MjUxNjE@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BNTEyNjUwMTkxMV5BMl5BanBnXkFtZTcwNjk0NDk0NA@@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BYjNhNmI3YjUtOTY4NS00YmI0LWFhNGQtNzU2YmI5MjBlZTg5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
         "https://m.media-amazon.com/images/M/MV5BYjZhMzFiZjItODA3ZC00MmRhLWIzMGYtMmVjOWUwYTA3MTRjXkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BNTEyZGQwODctYWJjZi00NjFmLTg3YmEtMzlhNjljOGZhMWMyXkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BMzQxNzQzOTQwM15BMl5BanBnXkFtZTgwMDQ2NTcwODM@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BNWQ5MDgwMzMtNWZhMy00Y2Q4LWI5NTAtODA4MDIzYTExOGQzXkEyXkFqcGc@._V1_.jpg",
         "https://m.media-amazon.com/images/M/MV5BMTUyNzkwMzAxOF5BMl5BanBnXkFtZTgwMzc1OTk1NjE@._V1_FMjpg_UX1000_.jpg"]
#The genre list is used to filter out movies based on which genre they are
genre = ["Musical","Musical","Musical","Musical","Musical","Drama","Drama","Drama","Drama","Drama","Drama","Animated","Animated","Animated","Animated","Animated","Comedy","Comedy","Comedy","Comedy","Comedy","Horror","Horror","Horror","Horror","Horror"]
filteredList = [] #This is the empty list that different movies will be added to depending on what genre the user chose

def open_image(url): #This is a function we made in class that opens an
    #image using a link provided (in this case it will use one of the links from my "links" list)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


def moviePicker(): #This function will randomly select a movie from the
                #filtered list and use the open_image function to display the image.
                # Additionally, it will print a one sentence blurb about what the movie is about
    randomMovie = random.choice(filteredList)
    if randomMovie == "Mama Mia":
        open_image(links[0])
        print("Mama Mia is a fun musical about a girl who invites three men to her wedding who may be he father! Enjoy")
    elif randomMovie == "La La Land":
        open_image(links[1])
        print("La La Land is a spirited musical about a pianist and actress who find themselves torn between choosing their love for each other or their careers. Enjoy!")
    elif randomMovie == "Grease":
        open_image(links[2])
        print("Grease is an upbeat musical about a good girl and greaser who fall in love during the summer and face trouble during the school year... Enjoy!")
    elif randomMovie == "Hairspray":
        open_image(links[3])
        print("Hairspray is a jubilant musical about a teenager who lands herself a spot on a local TV dance show! Enjoy!")
    elif randomMovie == "The Sound of Music":
        open_image(links[4])
        print("The Sound of Music is a thrilling and heartwarming story of a governess who transforms the lives of the Von Trapp Family")
    elif randomMovie == "Moonlight":
        open_image(links[5])
        print("Moonlight is a coming of age drama centered around the character Chiron")
    elif randomMovie == "Call Me By Your Name":
        open_image(links[6])
        print("Call Me By Your Name is a heartrbeaking romance about 17 year old Elio, set in Northern Italy")
    elif randomMovie == "A Real Pain":
        open_image(links[7])
        print("A Real Pain is a heartwarming and yet heartbreaking tale of two brothers who tour through Poland")
    elif randomMovie == "Goodbye Lenin":
        open_image(links[8])
        print("Goodbye Lenin is a story about a young man named Alex who tries to pretend communism still reigns in Berlin following the fall of the wall in order to protect his mother")
    elif randomMovie == "Palo Alto":
        open_image(links[9])
        print("Palo Alto is a raw, coming of age film centered around a rebellious teen in Palo Alto")
    elif randomMovie == "Good Will Hunting":
        open_image(links[10])
        print("Good Will Hunting is about Will, a genious janitor at MIT who befriends a psychologist to find some direction for his life")
    elif randomMovie == "Fantastic Mr. Fox":
        open_image(links[11])
        print("Fantastic Mr. Fox is an animated film about a fox who tries accidentally endangers the lives of his friends and family")
    elif randomMovie == "My Neighbor Totoro":
        open_image(links[12])
        print("My Neighbor Totoro is an adorable animated film about two young girls who befriend forest spirits!")
    elif randomMovie == "Sleeping Beauty":
        open_image(links[13])
        print("Sleeping Beauty is an animated film about a princess who is cursed to sleep for 100 years after being pricked by a spindle!")
    elif randomMovie == "Zootopia":
        open_image(links[14])
        print("Zootopia is a silly animated film about a young bunny finding her way in an animal city!")
    elif randomMovie == "Ponyo":
        open_image(links[15])
        print("Ponyo is a sweet animated film about a fish named Ponyo who befriends a human boy and begins to turn human!")
    elif randomMovie == "Wild Child":
        open_image(links[16])
        print("Wild Child is an exciting movie about 16 year old Poppy who is forced to go to boarding school in England!")
    elif randomMovie == "Dazed and Confused":
        open_image(links[17])
        print("Dazed and Confused is a comedy following teenagers in the 70s through their last night before summer break!")
    elif randomMovie == "Wet Hot American Summer":
        open_image(links[18])
        print("Wet Hot American Summer is a hilarious movie about camp counsellors in the 80s!")
    elif randomMovie == "Legally Blonde":
        open_image(links[19])
        print("Legally Blonde follows college student Elle Woods who enrolls in Harvard Law to get her boyfriend back, discovering her own talent and passion for law!")
    elif randomMovie == "Bring it On":
        open_image(links[20])
        print("Bring it On is an comedic and inspiring movie about teenage cheerleaders who make their way to nationals!")
    elif randomMovie == "Psycho":
        open_image(links[21])
        print("Psycho is a terrifying horror movie starring Anthony Perkins!")
    elif randomMovie == "Hereditary":
        open_image(links[22])
        print("Hereditary is a horrifying psychological thriller about the Graham family")
    elif randomMovie == "Midsommar":
        open_image(links[23])
        print("Midsommar is a psychological thriller about a group of friends who vacation to Sweden")
    elif randomMovie == "Barbarian":
        open_image(links[24])
        print("Barbarian is a terrifying movie about a girl who stays in an eerie Airbnb in Detroit")
    elif randomMovie == "The Witch ":
        open_image(links[25])
        print("The Witch is an eerie horror movie about a suspicous dissaperance in 1630 New England")

def finalMovieChooser(inputGenre): #This is my final function that introduces
                                   #the user to the game and uses a parameter (inputGenre)
                                   # to determine which genre the user wants to watch
    global filteredList
    print("--------------Movie Picker--------------")
    print("""
    Hello! Welcome to movie chooser! We all know how hard
    it is to choose a movie for movie night, use this tool
    to find the perfect movie we will recommend based on the
    genre you just selected!!""")
    if inputGenre == "M": #This section of code appends movies to the filtered list
                          #based on what genre the user chooses
        for i in range(len(genre)):
            if genre[i] == "Musical":
                filteredList.append(movieList[i])
    elif inputGenre == "D":
        for i in range(len(genre)):
            if genre[i] == "Drama":
                filteredList.append(movieList[i])
    elif inputGenre == "A":
        for i in range(len(genre)):
            if genre[i] == "Animated":
                filteredList.append(movieList[i])
    elif inputGenre == "C":
        for i in range(len(genre)):
            if genre[i] == "Comedy":
                filteredList.append(movieList[i])
    else:
        for i in range(len(genre)):
            if genre[i] == "Horror":
                filteredList.append(movieList[i])
    moviePicker() #This is the function that displays the movie image and information
    while True: #The while loops allows for the function to keep repeating until the user says n,
                #meaning they do not want to continue and the while True loop will break
        print("Would you like us to choose another movie for you?")
        ans = str(input("Yes (y) or No (n)"))
        if ans == "y": #This will give the user a second movie
            filteredList=[]
            secondGenre = input("What genre would you like your second movie to be: M for musical, D for drama, A for animated, C for comedy, or H for horror?")
            if secondGenre == "M":
                for i in range(len(genre)):
                    if genre[i] == "Musical":
                        filteredList.append(movieList[i])
            elif secondGenre == "D":
                for i in range(len(genre)):
                    if genre[i] == "Drama":
                        filteredList.append(movieList[i])
            elif secondGenre == "A":
                for i in range(len(genre)):
                    if genre[i] == "Animated":
                        filteredList.append(movieList[i])
            elif secondGenre == "C":
                for i in range(len(genre)):
                    if genre[i] == "Comedy":
                        filteredList.append(movieList[i])
            else:
                for i in range(len(genre)):
                    if genre[i] == "Horror":
                        filteredList.append(movieList[i])
            moviePicker()
            print("We hope you like the movie!!")
        else:
            print("Thank you! Bye Bye :)")
            break #This will end the program
#Main
finalMovieChooser(input("Welcome to movie picker! What genre would you like your movie to be: M for musical, D for drama, A for animated, C for comedy, or H for horror"))
#Citations
#Mama Mia! Image Source: IMBD. 2008. Accessed via https://www.imdb.com/title/tt0795421/
#La La Land. Image Source: IMBD. 2016. Accessed via https://www.imdb.com/title/tt3783958/
#Grease. Image Source: IMBD. 1978. Accessed via https://www.imdb.com/title/tt0077631/
#Hairspray. Image Source: IMBD. 2007. Accessed via https://www.imdb.com/title/tt0427327/
#The Sound of Music. Image Source: IMBD. 1965. Accessed via https://www.imdb.com/title/tt0059742/
#Moonlight. Image Source: IMBD. 2016. Accessed via https://www.imdb.com/title/tt4975722/
#Call Me By Your Name. Image Source: IMBD. 2017.
 #Accessed via https://www.imdb.com/title/tt5726616/?ref_=fn_all_ttl_1
#A Real Pain. Image Source: IMBD. 2024.
 #Accessed via https://www.imdb.com/title/tt21823606/?ref_=fn_all_ttl_1
#Goodbye Lenin. Image Source: IMBD. 2003.
 #Accessed via https://www.imdb.com/title/tt0301357/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_goodbye%2520lenin
#Palo Alto. Image Source: IMBD. 2013. Accessed via https://www.imdb.com/title/tt2479800/?ref_=fn_all_ttl_1
#Good Will Hunting. Image Source: IMBD. 1997.
 #Accessed via https://www.imdb.com/title/tt0119217/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_good%2520will%2520hunting
#Fantastic Mr. Fox. Image Source: IMBD. 2009.
 #Accessed via https://www.imdb.com/title/tt0432283/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_fantastic%2520mr%2520fox
#My Neighbor Totoro. Image Source: IMBD. 1988. Accessed via https://www.imdb.com/title/tt0096283/?ref_=fn_all_ttl_1
#Sleeping Beauty. Image Source: IMBD. 1959. Accessed via https://www.imdb.com/title/tt0053285/?ref_=fn_all_ttl_1
#Zootopia. Image Source: IMBD. 2016. Accessed via https://www.imdb.com/title/tt2948356/?ref_=fn_all_ttl_1
#Ponyo. Image Source: IMBD. 2008. Accessed via https://www.imdb.com/title/tt0876563/?ref_=fn_all_ttl_1
#Wild Child. Image Source: IMBD. 2008. Accessed via https://www.imdb.com/title/tt1024255/?ref_=fn_all_ttl_1
#Dazed and Confused. Image Source: IMBD. 1993.
 #Accessed via https://www.imdb.com/title/tt0106677/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_dazed%2520and%2520conf
#Wet Hot American Summer. Image Source: IMBD. 2001.
 #Accessed via https://www.imdb.com/title/tt0243655/?ref_=nv_sr_srsg_0_tt_7_nm_1_in_0_q_wet%2520hot%2520ame
#Legally Blonde. Image Source: IMBD. 2001.
 #Accessed via https://www.imdb.com/title/tt0250494/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_legally
#Bring it On. Image Source: IMBD. 2000.
 #Accessed via https://www.imdb.com/title/tt0204946/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_bring%2520it%2520on
#Psycho. Image Source: IMBD. 1960.
 #Accessed via https://www.imdb.com/title/tt0054215/?ref_=fn_all_ttl_1
#Hereditary. Image Source: IMBD. 2018.
 #Accessed via https://www.imdb.com/title/tt7784604/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_hereditary
#Midsommar. Image Source: IMBD. 2019.
 #Accessed via https://www.imdb.com/title/tt8772262/?ref_=nv_sr_srsg_0_tt_7_nm_1_in_0_q_midsommar
#Barbarian. Image Source: IMBD. 2022.
 #Accessed via https://www.imdb.com/title/tt15791034/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_barbarian
#The Witch. Image Source: IMBD. 2015.
 #Accessed via https://www.imdb.com/title/tt4263482/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_The%2520witch

