def move(currentCaveX, currentCaveY, connections):

    cave = input("which cave do you want to move to?")

    print("you  moved to cave " + str(cave))


    if cave == 0:
        currentCaveX = 0
        currentCaveY = 0
    elif cave == 1:
        currentCaveX = 0
        currentCaveY = 1
    elif cave == 2:
        currentCaveX = 0
        currentCaveY = 2
    elif cave == 3:
        currentCaveX = 1
        currentCaveY = 0
    elif cave == 4:
        currentCaveX = 1
        currentCaveY = 1
    elif cave == 5:
        currentCaveX = 1
        currentCaveY = 2
    elif cave == 6:
        currentCaveX = 2
        currentCaveY = 0
    elif cave == 7:
        currentCaveX = 2
        currentCaveY = 1
    elif cave == 8:
        currentCaveX = 2
        currentCaveY = 2



def shoot():

    print("you shot")



def decision(currentCaveX, currentCaveY):

    print("Your are currently in cave " + str(matrix[currentCaveX][currentCaveY][0]))
    print(matrix[currentCaveX][currentCaveY][4])
    print("you can go to caves " + str(matrix[currentCaveX][currentCaveY][5]) + " from here")

    Q = input("move or shoot? (type m for move and s for shoot)").lower()

    if Q == "m":



        move(currentCaveX, currentCaveY, matrix[currentCaveX][currentCaveY][5])

    elif Q == "s":

        shoot()

    else:

        print("sorry I couldn't understand you. game over")



MATRIX_COL = 3

MATRIX_ROW = 3



matrix = [[0 for x in range(MATRIX_COL)] for x in range(MATRIX_ROW)]

matrix[0][0] = [0, False, False, False, "You have reached the first cave. This cave is said to be 9,999,999,999,999 eons old.", [1, 3]]

matrix[0][1] = [1, False, False, False, "Grand Duke Franz Ferdinand once walked this floor.", [2, 4, 0]]

matrix[0][2] = [2, True, False, False, "This is the largest of the caves with 3 square acres of space.", [5, 1]]

matrix[1][0] = [3, False, False, False, "George washington discovered thorium here.", [4, 6, 0]]

matrix[1][1] = [4, False, False, False, "This is the smallest of of the wumpus's caves, at one cubic nanometer", [5, 7, 3, 1]]

matrix[1][2] = [5, False, False, False, "This is the cave where the fountain of youth is said to be. (you notice a fountain but don't drink from it, knowing it was poisened by the wumpus many years ago", [8, 4, 2]]

matrix[2][0] = [6, False, True, False, "You notice a large sign saying 這是你死的地方 and you do not know what that means.", [7, 3]]

matrix[2][1] = [7, False, False, True, "If you're not dead, the wumpus must be on vacation and you win. Otherwise you lose.", [8, 6, 4]]

matrix[2][2] = [8, False, False, False, "In this cave lies your worst nightmare, a retail store where there is no one to help you and you can't find anything. Get out quick, you think you see a salesperson coming.", [7, 5]]

#matrix[x][y] = [num, bat, pit, wumpus, text, [connections]]

#cave 7 has wumpus

#cave 6 has pit

#cave 3 has bat

currentCaveX = 0
currentCaveY = 0


print("""
YOU ARE A FAMOUS HUNTER DESCENDING DOWN INTO THE CAVES OF DARKNESS,
LAIR OF THE INFAMOUS MAN-EATING WUMPUS.  YOU ARE EQUIPPED WITH FIVE
BENT ARROWS, AND ALL YOUR SENSES.  THERE ARE TWENTY CAVES CONNECTED
BY TUNNELS, AND THERE ARE TWO OTHER KINDS OF HAZARDS:
        A) PITS, WHICH ARE BOTTOMLESS, AND USUALLY FATAL TO FALL
        INTO.  THERE ARE THREE SUCH PITS IN THE NETWORK.
        B) SUPER-BATS, WHICH IF YOU STUMBLE INTO THEIR ROOM WILL
        PICK YOU UP AND DROP YOU IN SOME RANDOM ROOM IN THE NETWORK.
        YOU MAY SHOOT SUPER-BATS, THERE IS ONE IN EACH OF THREE OR
        FOUR ROOMS WITHIN THE NETWORK.  THE SUPER-BATS GENERALLY STAY
        IN THEIR OWN ROOMS, EXCEPT WHEN DISPOSING OF INTRUDERS OR
        SCAVENGING FOR FOOD IN THE PITS.
IF YOU BLUNDER INTO THE SAME ROOM AS THE WUMPUS, YOU LOSE....
THE NORMALLY SLEEPING WUMPUS DOES NOT MOVE (HAVING GORGED HIMSELF UPON
A PREVIOUS HUNTER).  HOWEVER SEVERAL THINGS CAN WAKE HIM UP:
        1) WALKING INTO HIS ROOM,
        2) SHOOTING AN ARROW ANYWHERE IN THE NETWORK,
        3) TRIPPING OVER DEBRIS (CLUMSINESS),
        4) TURNING ON THE LIGHTS, IN ORDER TO SEE WHERE YOU ARE
        HEADED.
IF HE WAKES UP THERE'S A POSSIBILITY HE WILL MOVE, HOWEVER, HE'S TOO
LAZY TO MOVE MORE THAN ONE ROOM BETWEEN SNOOZES.  THE WUMPUS IS TOO
BIG TO BE PICKED UP BY SUPER-BATS AND HAS SUCKER FEET, SO HE DOESN'T
FALL INTO THE PITS.
YOU CAN SMELL THE WUMPUS FROM ONE OR TWO ROOMS AWAY.  YOU WILL
TREMBLE WITH FEAR WHEN HE MOVES ABOUT.  YOU CAN HEAR SUPER-BATS FROM
ONE ROOM AWAY, AND FEEL DRAFTS (FROM BOTTOMLESS PITS) FROM ONE ROOM
AWAY (AND TASTE THE FEAR...).
TO SHOOT AN ARROW TYPE 'SHOOT' INSTEAD OF A MOVE, AND THEN
SPECIFY WHICH ROOMS THE ARROW SHOULD PASS THROUGH.  YOU ARE STRONG
ENOUGH TO SHOOT IT THROUGH AS MANY AS FIVE ROOMS.  BENT ARROWS HAVE
NO PROBLEM ROUNDING CORNERS OF LESS THAN 743 DEGREES.  IF YOU
SPECIFY AN IMPOSSIBLE PATH THE ARROW WILL RICOCHET OFF THE WALLS OF
THE ROOM, LOSING SPEED, AND WILL EVENTUALLY COME TO REST IN ONE OF
THE ADJOINING ROOMS.  THE PATH MAY BE TERMINATED BY SPECIFYING ROOM 0.
EACH ROOM IS CONNECTED TO THREE OTHER ROOMS BY THREE TUNNELS A, B
AND C.  YOU MUST ALWAYS MOVE BETWEEN ROOMS BY SPECIFYING WHICH
TUNNEL YOU WISH TO EXPLORE.  YOU CAN ALWAYS RETRACE YOUR FOOT STEPS
BY MOVING BACK USING THE SAME TUNNEL DESIGNATOR.
IF YOU WISH TO SEE WHICH ROOMS ARE AT THE ENDS OF THE TUNNELS YOU
MAY TYPE 'LIGHTS ON' INSTEAD OF A MOVE.  THIS MAY BE AN UNHEALTHY
LUXURY HOWEVER BECAUSE THE LIGHT GIVES THE WUMPUS INSOMNIA.  TO
EXTINGUISH THE LIGHTS SIMPLY TYPE 'LIGHTS OFF'.
                GOOD LUCK HUNTING!!
                """)



#print(matrix)



while True:

    decision(currentCaveX, currentCaveY)
