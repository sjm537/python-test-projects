#string concatenation (how to put strings together)
#creating a string that says "subscribe to _____"
#youtuber = "sophie" #some string variable

#a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

playMadlib = input("Would you like to play? Y or N\n")

while playMadlib == "Y":
    n = input("Select Madlib 1 or 2:\n")
    if n == "1":
        #Madlib 1
        adj = input("Adjective: ")
        verb1 = input("Verb: ")
        verb2 = input("Verb: ")
        famous_person = input("Famous Person: ")

        madlib1 = f"Computer programming is so {adj}!\n\
        It makes me so excited all the time because\n\
        I love to {verb1}. Stay hydrated and {verb2}\n\
        like you are {famous_person}!"

        print(madlib1)

    elif n == "2":
        #Madlib 2
        today = input("Today's Date: ")
        verb1 = input("Verb: ")
        animal = input("Animal: ")
        favFood = input("Favorite Food: ")
        verb2 = input("Verb: ")

        madlib2 = f"To Do List for {today}\n\
            1. {verb1} the {animal}\n\
            2. Cook {favFood} for dinner\n\
            3. Program app that {verb2}s for me"
        print(madlib2)

    playMadlib = input("Would you like to play again? Y or N\n")

if playMadlib == "N":
    print ("Goodbye!")

else:
    print("That is not a valid selection.")






