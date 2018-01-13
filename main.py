def move(connections):
    global currCaveNum
    move_to = int(input("which cave do you want to move to?"))

    if move_to in connections:
        print("you  moved to cave " + str(move_to))
        currCaveNum = move_to
    else:
       print("You cannot go there")

def shoot():

    print("you shot")



def decision():
    global caves
    global currCaveNum
    print("You are currently in cave " + str(currCaveNum))
    print(caves[currCaveNum][3])
    print("you can go to caves " + str(caves[currCaveNum][4]) + " from here")

    Q = input("move or shoot? (type m for move and s for shoot)").lower()

    if Q == "m":



        move(caves[currCaveNum][4])

    elif Q == "s":

        shoot()

    else:

        print("sorry I couldn't understand you. game over")

caves = []

caves.append([False, False, False, "You have reached the first cave. This cave is said to be 9,999,999,999,999 eons old.", [1, 5, 20, 4]])
caves.append([True, False, False, "Grand Duke Franz Ferdinand once walked this floor.", [2, 6, 0, 21]])
caves.append([False, False, False, "This is the largest of the caves with 3 square acres of space.", [3, 7, 1, 22]])
caves.append([False, False, False, "George washington discovered thorium here.", [4, 8, 2, 23]])
caves.append([False, False, False, "This is the smallest of of the wumpus's caves, at one cubic nanometer", [9, 3, 24, 0]])
caves.append([False, False, False, "This is the cave where the fountain of youth is said to be. (you notice a fountain but don't drink from it, knowing it was poisened by the wumpus many years ago", [0, 6, 10, 9]])
caves.append([False, False, False, "You notice a large sign saying 這是你死的地方 and you do not know what that means.", [1, 7, 11, 5]])
caves.append([False, False, False, "If the wumpus must be on vacation and you win. Ever think about that?", [2, 8, 12, 6]])
caves.append([False, True, False, "In this cave lies your worst nightmare, a retail store where there is no one to help you and you can't find anything. Get out quick, you think you see a salesperson coming.", [3, 9, 13, 7]])
caves.append([False, False, False, "This cave was where Scrooge McDuck found his first treasure.", [4, 14, 8, 5]])
caves.append([False, False, False, "This cave is full of life-sized teddy bears.", [5, 11, 15, 14]])
caves.append([False, False, False, "There is nothing in this cave. It is a vacuum.", [6, 12, 16, 10]])
caves.append([False, False, False, "This cave has argueing politicians. You hate it. The noise is driving you crazy.", [7, 13, 17, 11]])
caves.append([False, False, False, "You have reached the thirteenth cave, the cave of luck,good and bad.", [8, 14, 18, 12]])
caves.append([False, False, False, "This cave has a game show host who will not let you leave until you tell him the nationality of Nikola Tesla.", [9, 19, 13, 10]])
caves.append([True, False, False, "This cave is filled with monotonous teachers. Turn to page 394.", [10, 16, 20, 19]])
caves.append([False, False, False, "This is the cave of fandom. You meet your favorite celebrity here.", [11, 17, 21, 15]])
caves.append([False, False, False, "This cave has musical codes for the doors. You regret quiting those music lessons.", [12, 18, 22, 16]])
caves.append([False, False, False, "In this cave lies the grave of Algernon the mouse. Did you bring your flowers?", [13, 19, 23, 17]])
caves.append([False, False, True, "Consider this confirmation that you are not illiterate.", [14, 24, 18, 15]])
caves.append([False, False, False, "You have reached the cave of spoilers. Quick, cover your ears.", [15, 21, 0, 24]])
caves.append([False, False, False, "This cave has no hazards. You are safe in here.", [16, 22, 20, 1]])
caves.append([False, False, False, "You think the wumpus is scared of you and you feel bad.", [17, 23, 21, 2]])
caves.append([False, False, False, "You pull out your ocarina and play a little tune. You like it.", [18, 24, 22, 3]])
caves.append([False, False, False, "You are in the last of the caves. This one is the newest, being just created.", [19, 23, 20, 4]])

#caves.append = [bat, pit, wumpus, text, [connections]]

#cave 19 has wumpus

#cave 8 has pit

#cave 1 has bats
              
#cave 15 has bats

currCaveNum = 0


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
YOU CAN SMELL THE WUMPUS FROM ONE ROOM AWAY.  YOU WILL
TREMBLE WITH FEAR WHEN HE MOVES ABOUT.  YOU CAN HEAR SUPER-BATS FROM
ONE ROOM AWAY, AND FEEL DRAFTS (FROM BOTTOMLESS PITS) FROM ONE ROOM
AWAY (AND TASTE THE FEAR...).
TO SHOOT AN ARROW TYPE 'SHOOT' INSTEAD OF A MOVE, AND THEN
SPECIFY WHICH ROOMS THE ARROW SHOULD PASS THROUGH.  YOU ARE STRONG
ENOUGH TO SHOOT IT THROUGH AS MANY AS ONE ROOM.  BENT ARROWS HAVE
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



while True:

    decision()
