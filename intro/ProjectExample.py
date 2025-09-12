# david friedman
# I pledge that this work reflects my own effort and the values of Tabor’s Honor Code


# this starts the game, abandoned on an island
def stranded():
    print("you're stranded in the middle of the jungle. what do you do?")
    print("a. climb a tree for a view")
    print("b. swim down the river")
    print("c. go hunting")

    choice = input().lower()

    if choice == 'a':
        climbTree()
    elif choice =='b':
        logInRiver()
    elif choice == 'c':
        hunt()
    else:
        print("invalid answer. try again")

# in this step the user climbs a tree and runs into a python halfway up
def climbTree():
    print("you get halfway up the tree and run into a python. what now?")
    print("a. fight the python")
    print("b. jump")

    choice = input()

    if choice == 'a':
        print("it eats you. bye")

    elif choice == 'b':
        jumpInRiver()

# the user chooses whether to climb onto a mysterious log
def logInRiver():
    print("you see a log floating in the river. what now?")
    print('a. climb on the log')
    print("b. steer clear of the log")

    choice = input()

    if choice == 'a':
        print("that wasn't a log! an alligator eats you")
    elif choice == 'b':
        swimToShore()

# the user gets out of the river
def swimToShore():
    print("You decide that the river is not a safe place. Where to next?")
    print("a. you see smoke in the distance")
    print("b. climb a tree for a view")

    choice = input()

    if choice == 'a':
        print("you find a friendly village and they take you in as their own. "
              "looks like you'll survive!")
    elif choice == 'b':
        climbTree()

# the user lands in the river
def jumpInRiver():
    print("you jump off the tree and land in the river")
    logInRiver()

# the user chooses how to go hunting
def hunt():
    print("you decide to hunt for some food. Do you want to make a weapon or catch something barehanded?")
    print("a. make a weapon")
    print("b. go barehanded")

    choice = input()

    if choice == 'a':
        buildSpear()
    elif choice == 'b':
        print("you quickly find a boar, but with no weapon you discover you're not very dangerous. "
              "It takes you out with its tusks. bye")

# the user makes a spear
def buildSpear():
    print("you build a spear out of rocks and wood. What do you want to hunt?")
    print("a. some small birds")
    print("b. boar")
    print("c. man")

    choice = input()

    if choice == 'a':
        chaseBirds()
    elif choice == 'b':
        chaseBoar()
    elif choice == 'c':
        chaseMan()

# the user hunts for birds unsuccsessfully
def chaseBirds():
    print("a spear is just not meant to hunt small birds. Let's try something else")
    buildSpear()


# the user hunts a boar and gets rescued
def chaseBoar():
    print("you're able to take a boar out with the spear. As you cook it, the smoke "
          "attracts a search helicopter and you are rescued")


# the user tries to hunt a person but dies
def chaseMan():
    print("the most dangerous game. You spend days trying to find someone to hunt, "
          "forgetting that you are stranded alone. In your mania you forget to eat, sleep, or "
          "drink. Game over")



# this starts the game (use whatever you call your first step)
stranded()

