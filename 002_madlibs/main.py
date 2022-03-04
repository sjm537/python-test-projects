#string concatenation (how to put strings together)
#creating a string that says "subscribe to _____"
#youtuber = "sophie" #some string variable

#a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

playMadlib = input("Would you like to play? Y or N\n")

while playMadlib == "Y":
    n = input("Select Madlib 1, 2, or 3:\n")
    if n == "1":
        #Madlib 1
        adj = input("Adjective: ")
        verb1 = input("Verb: ")
        verb2 = input("Verb: ")
        famous_person = input("Famous Person: ")

        madlib1 = f"Why I Like Computer Programming\n\
            Computer programming is so {adj}!\n\
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

    elif n == "3":
        #Madlib 3
        noun1 = input("Noun: ")
        noun2 = input("Noun: ")
        famperson = input("Famous Person: ")
        scary = input("Something Scary: ")

        madlib3 = f"Nic Cage's Next Movie\n\
            In his next film, Nic Cage will star\n\
            as a {noun1} who has to hunt down a {noun2}\n\
            in order to save {famperson} from {scary}"
        
        print(madlib3)

    playMadlib = input("Would you like to play again? Y or N\n")

if playMadlib == "N":
    print ("Goodbye!")

else:
    print("That is not a valid selection.")






