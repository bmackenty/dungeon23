# this program procedurally generates a rumour
import random
import os

# define the function
def generate_rumour():
    # define the lists
    who = ["A friend", "My neighbour", "My colleague", "A stranger", "My boss", "My ex", "My pet"]
    what = ["saw", "heard", "told me", "read on a scroll", "read in the newspaper", "read in a magazine", "read in a book"]
    where = ["in the park", "in the bazaar", "in the pub", "in the library", "in the theater", "in the gym", "in the swimming pond"]
    when = ["yesterday", "last week", "last month", "last year", "this morning", "this afternoon", "this evening"]
    why = ["because", "so", "therefore", "thus", "hence", "consequently", "ergo"]
    how = ["I don't know", "I don't care", "I don't understand", "I don't believe it", "I don't like it", "I don't want to know", "I don't want to hear it"]

    # generate the rumour
    rumour = random.choice(who) + " " + random.choice(what) + " " + random.choice(where) + " " + random.choice(when) + " " + random.choice(why) + " " + random.choice(how)

    # return the rumour
    return rumour

# define the main function

def main():
    # clear the screen
    os.system("clear")

    # generate the rumour
    rumour = generate_rumour()

    # display the rumour
    print("Rumour: " + rumour)



# call the main function
main()

