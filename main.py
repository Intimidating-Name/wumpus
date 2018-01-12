import global_data as gd

def move():

    while True:
        response = input("Which cave do you want to move to?\n")
        try:
            response = int(response)
        except ValueError:
            print("You can not go there! Try Again.")
            continue
        if response in gd.cave.connections:
            gd.cave = gd.caves[response]
            print("You have moved to cave " + str(gd.cave.id))
            break
        else:
            print("You can not go there! Try Again.")

    print(gd.cave.id)

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
    print(gd.intro)
    gd.cave = gd.caves[0]
    while True:
        print("Your are currently in cave " + str(gd.cave.id))
        print(gd.cave.desc)
        print("You can go to caves " + ", ".join([str(i) for i in gd.cave.connections]) + " from here")
        decision()

if __name__ == '__main__':
    main()
