import global_data as gd

def move():
    
    while True:
        response = input("Which cave do you want to move to?\n")
        # if response is an int
        try:
            response = int(response)
        except ValueError:
            print("You can not go there! Try Again.")
            continue
        # if response is a valid cave connection
        if response in gd.cave.connections:
            # search for cave with id of response
            gd.cave = [x for x in gd.caves if x.id == response][0]
            print("You have moved to cave " + str(gd.cave.id))
            break
        else:
            print("You can not go there! Try Again.")

def shoot():

    print("Pew! You shot.")

def decision():

    Q = input("Move or Shoot?\n").lower()

    if Q == "m" or Q == "move":
        move()

    elif Q == "s" or Q == "shoot":
        shoot()

    else:
        print("Sorry, I couldn't understand you. Try Again!")

def main():
    # MATRIX_COL = 3
    # MATRIX_ROW = 3
    # matrix = [[0 for x in range(MATRIX_COL)] for x in range(MATRIX_ROW)]
    
    # print intro
    print(gd.intro)
    # set cave to 0
    gd.cave = [x for x in gd.caves if x.id == 0][0]
    # game function
    while True:
        # print metadata
        print("Your are currently in cave " + str(gd.cave.id))
        print(gd.cave.desc)
        print("You can go to caves " + ", ".join([str(i) for i in gd.cave.connections]) + " from here")
        decision()

# if run as main
if __name__ == '__main__':
    main()
