import json
from pprint import pprint
import winsound
from random import randint
from pyfiglet import Figlet

def initial_state(caves, current_cave, alive, playing, wumpus_cave, wumpus_alive):
    caves = json.load(open("caves.json", "r"))
    current_cave = 0
    alive = True
    playing = True
    wumpus_cave = random_cave(wumpus_cave)
    wumpus_alive = True
    return caves
    return current_cave
    return alive
    return playing
    return wumpus_cave
    return wumpus_alive

def move(connections, current_cave, alive, wumpus_cave):
    move_to = int(input("Which cave do you want to move to?"))
    winsound.PlaySound(caves[move_to][5], winsound.SND_FILENAME | winsound.SND_ASYNC)
    if move_to in connections:
        print("you  moved to cave " + str(move_to))
        current_cave = move_to
        if caves[current_cave][1]:
            print("You fell into the bottomless pit.")
            alive = False
        if caves[current_cave][2]:
            print("Before you die, you think you hear the wumpus burp. What bad manners it has.")
            alive = False
        if caves[current_cave][0]:
            print("This cave has bats. You are now going to be carried to a random, safe cave.")
            current_cave = random_cave(wumpus_cave)
    else:
        print("You bump into a wall and hear the wumpus move 1 room.")
        wumpus_cave = random_tunnel(connections)
    return current_cave
    return alive
    return wumpus_cave

def shoot(connections, caves, wumpus_alive)
    shoot_to = int(input("Which cave do you want to shoot to?"))
    if shoot_to not in connections:
        print("You cannot shoot there. Try again")
        shoot(caves[current_cave][4], caves)
    if caves[wumpus_cave][2]:
        print("You shot the wumpus! You quickly escape and win.")
        wumpus_alive = False
    if caves[shoot_to][0]:
        print("You shot a bat and feel really bad. You promise to plan the funeral as soon as you kill the wumpus.")
        caves[shoot_to][0] = False
        return caves
        return wumpus_alive

def random_tunnel(connections):
    chosen = randint(0, 3)
    while connections[chosen] == 8 or connections[chosen] == 1 or connections[chosen] == 15:
        chosen = randint(0, 3)
    return connections[chosen]



def random_cave(wumpus_cave)
    global wumpus_cave
    safeRandomCaveNumber = randint(0, 24)
    while wumpus_cave == safeRandomCaveNumber or 8 == safeRandomCaveNumber or 1 == safeRandomCaveNumber or 15 == safeRandomCaveNumber:
        safeRandomCaveNumber = randint(0, 24)
    return safeRandomCaveNumber

def warnings(connections, caves):
    for caveNum in connections:
        if caves[caveNum][0]:
            print("You hear bat's wings flapping.")
        if caves[caveNum][1]:
            print("You feel the pit's breeze.")
        if caves[caveNum][2]:
            print("You smell the wumpus.")

def decision(caves, current_cave, alive, wumpus_cave, wumpus_alive)
    print("You are currently in cave " + str(current_cave))
    print(caves[current_cave][3])
    warnings(caves[current_cave][4], caves)
    print("you can go to caves " + str(caves[current_cave][4]) + " from here")

    Q = input("move or shoot? (type m for move and s for shoot)").lower()

    if Q == "m":

        move(caves[current_cave][4], current_cave, alive, wumpus_cave)

    elif Q == "s":

        shoot(caves[current_cave][4], caves, wumpus_alive)

    else:

        print("Sorry, I couldn't understand you.")
    return caves
    return current_cave
    return alive
    return wumpus_cave
    return wumpus_alive



#pprint(caves)

#caves.append = [bat, pit, wumpus, text, [connections]]

#cave 19 has wumpus

#cave 8 has pit

#cave 1 has bats
              
#cave 15 has bats

f = Figlet(font = 'doh', width = 180)
print(f.renderText('HUNT THE WUMPUS'))

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
THE WUMPUS IS TOOBIG TO BE PICKED UP BY SUPER-BATS AND HAS SUCKER FEET, SO HE DOESN'T
FALL INTO THE PITS.
YOU CAN SMELL THE WUMPUS FROM ONE ROOM AWAY.  YOU WILL
TREMBLE WITH FEAR WHEN HE MOVES ABOUT.  YOU CAN HEAR SUPER-BATS FROM
ONE ROOM AWAY, AND FEEL DRAFTS (FROM BOTTOMLESS PITS) FROM ONE ROOM
AWAY.
TO SHOOT AN ARROW TYPE 's' INSTEAD OF A MOVE, AND THEN
SPECIFY WHICH ROOM THE ARROW SHOULD PASS THROUGH.  YOU ARE STRONG
ENOUGH TO SHOOT IT THROUGH ONE ROOM. IF YOU
SPECIFY AN IMPOSSIBLE PATH THE ARROW WILL RICOCHET OFF THE WALLS OF
THE ROOM, LOSING SPEED, AND WILL EVENTUALLY COME TO REST IN ONE OF
THE ADJOINING ROOMS.  THE PATH MAY BE TERMINATED BY SPECIFYING ROOM 0.
EACH ROOM IS CONNECTED TO FOUR OTHER ROOMS BY FOUR TUNNELS.  
YOU MUST ALWAYS MOVE BETWEEN ROOMS BY SPECIFYING WHICH
TUNNEL YOU WISH TO EXPLORE.  YOU CAN ALWAYS RETRACE YOUR FOOT STEPS
BY MOVING BACK USING THE SAME TUNNEL DESIGNATOR.
                GOOD LUCK HUNTING!!
                """)
alive = None
playing = None
current_cave = None
caves = None
wumpus_cave = None
wumpus_alive = None

initial_state(caves, current_cave, alive, playing, wumpus_cave, wumpus_alive)
print(alive, playing, current_cave, wumpus_cave, caves[wumpus_cave][2])

while alive and playing and caves[wumpus_cave][2]:

    decision(caves, current_cave, alive, wumpus_cave, wumpus_alive)
    if alive == False or caves[wumpus_cave][2] == False:
       play_again = input("Do you want to play again?")
       if play_again.lower() == "no":
           playing = False
       else:
           initial_state(caves, current_cave, alive, playing, wumpus_cave, wumpus_alive)
