import json
import winsound
from random import randint
from pyfiglet import Figlet
import colorama

CAVE_BAT = 0
CAVE_PIT = 1
CAVE_DESCRIPTION = 2
CAVE_CONNECTIONS = 3
CAVE_SOUND = 4

def initial_state():
    global caves
    global current_cave
    global alive
    global playing
    global wumpus_cave
    global wumpus_alive
    global CAVE_BAT
    caves = json.load(open("caves.json", "r"))
    current_cave = 0
    alive = True
    playing = True
    wumpus_cave = random_wumpus_cave()
    wumpus_alive = True
    bat_possible_count = randint(0, 3)
    for x in range(0, randint(0, bat_possible_count)):
        caves[random_hazzard_cave()][CAVE_BAT] = True
    pit_possible_count = 3 - bat_possible_count
    for x in range(0, randint(0, pit_possible_count)):
        caves[random_hazzard_cave()][CAVE_PIT] = True


def move(connections):
    global current_cave
    global caves
    global alive
    global wumpus_cave
    global CAVE_CONNECTIONS
    global CAVE_BAT
    move_to = int(input("Which cave do you want to move to?"))
    winsound.PlaySound(caves[move_to][CAVE_SOUND], winsound.SND_FILENAME | winsound.SND_ASYNC)
    if move_to in connections:
        print("you moved to cave " + str(move_to))
        current_cave = move_to
        if caves[current_cave][CAVE_PIT]:
            print(colorama.Fore.BLACK + colorama.Back.WHITE + "You fell into the bottomless pit.")
            alive = False
        if move_to is wumpus_cave:
            print(colorama.Back.YELLOW + "Before you die, you think you hear the wumpus burp. What bad manners it has.")
            alive = False
        if caves[current_cave][CAVE_BAT]:
            print(colorama.Back.MAGENTA + "This cave has bats. You are now going to be carried to a random, safe cave.")
            current_cave = random_dropoff_cave()
    else:
        print("You bump into a wall and hear the wumpus move 1 room.")
        wumpus_cave = random_tunnel(connections)
    print(colorama.Style.RESET_ALL)

def shoot(connections, caves):
    global wumpus_alive
    global wumpus_cave
    global CAVE_BAT
    global CAVE_CONNECTIONS
    global CAVE_PIT
    shoot_to = int(input("Which cave do you want to shoot to?"))
    if shoot_to not in connections:
        print("You cannot shoot there. Try again")
        shoot(caves[current_cave][CAVE_CONNECTIONS], caves)
    if shoot_to is wumpus_cave:
        print("")
        print(colorama.Fore.GREEN + "You shot the wumpus! You quickly escape and win.")
        wumpus_alive = False
    if caves[shoot_to][CAVE_BAT]:
        print(colorama.Back.BLUE + "You shot a bat and feel really bad. You promise to plan the funeral as soon as you kill the wumpus.")
        caves[shoot_to][CAVE_BAT] = False
    if caves[shoot_to][CAVE_PIT]:
        print(colorama.Back.WHITE + colorama.Fore.BLACK + "You killed a pit. You feel weird for breaking the rules of reality and promise to tell someone as soon "
              "as you kill the wumpus. The pit fills up and you can walk through it.")
        caves[shoot_to][CAVE_PIT] = False
    print(colorama.Style.RESET_ALL)

def random_tunnel(connections):
    chosen = randint(0, 3)
    while connections[chosen] == 8 or connections[chosen] == 1 or connections[chosen] == 15:
        chosen = randint(0, 3)
    return connections[chosen]



def random_dropoff_cave():
    global wumpus_cave
    global caves
    global CAVE_BAT
    global CAVE_PIT
    safe_random_cave = randint(0, 24)
    while wumpus_cave is safe_random_cave or caves[safe_random_cave][CAVE_BAT] or caves[safe_random_cave][CAVE_PIT]:
        safe_random_cave = randint(0, 24)
    return safe_random_cave

def random_wumpus_cave():
    return randint(1, 24)

def random_hazzard_cave():
    global wumpus_cave
    global caves
    global CAVE_BAT
    global CAVE_PIT
    choice = randint(1, 24)
    while choice is wumpus_cave or caves[choice][CAVE_BAT] or caves[choice][CAVE_PIT]:
        choice = randint(1, 24)
    return choice

def warnings(connections, caves):
    global wumpus_cave
    global CAVE_BAT
    global CAVE_PIT
    for cave_num in connections:
        if caves[cave_num][CAVE_BAT]:
            print("You hear bat's wings flapping.")
        if caves[cave_num][CAVE_PIT]:
            print("You feel the pit's breeze.")
        if cave_num is wumpus_cave:
            print("You smell the wumpus.")

def decision():
    global caves
    global current_cave
    global CAVE_DESCRIPTION
    global CAVE_CONNECTIONS
    print("")
    print("You are currently in cave " + str(current_cave))
    print(caves[current_cave][CAVE_DESCRIPTION])
    warnings(caves[current_cave][CAVE_CONNECTIONS], caves)
    print("you can go to caves " + str(caves[current_cave][CAVE_CONNECTIONS]) + " from here")

    Q = input("move or shoot? (type m for move and s for shoot)").lower()

    if Q == "m":



        move(caves[current_cave][CAVE_CONNECTIONS])

    elif Q == "s":

        shoot(caves[current_cave][CAVE_CONNECTIONS], caves)

    else:

        print("sorry, I couldn't understand you. try again.")






#cave 8 has pit

#cave 1 has bats
              
#cave 15 has bats

f = Figlet(font = 'doh', width = 180)
print(colorama.Fore.LIGHTBLUE_EX + f.renderText('HUNT THE WUMPUS'))
print(colorama.Style.RESET_ALL)

input("press enter to continue")

print("""
YOU ARE A FAMOUS HUNTER DESCENDING DOWN INTO THE CAVES OF DARKNESS,
LAIR OF THE INFAMOUS MAN-EATING WUMPUS.  YOU ARE EQUIPPED WITH INFINITE
ARROWS, AND ALL YOUR SENSES.  THERE ARE TWENTY-FIVE CAVES CONNECTED
BY TUNNELS, AND THERE ARE TWO OTHER KINDS OF HAZARDS:
        A) PITS, WHICH ARE BOTTOMLESS, AND USUALLY FATAL TO FALL
        INTO.  THERE IS ONE SUCH PIT IN THE NETWORK.
        B) SUPER-BATS, WHICH IF YOU STUMBLE INTO THEIR ROOM WILL
        PICK YOU UP AND DROP YOU IN SOME RANDOM ROOM IN THE NETWORK.
        YOU MAY SHOOT SUPER-BATS, THERE IS ONE IN EACH OF THREE OR
        FOUR ROOMS WITHIN THE NETWORK.  THE SUPER-BATS GENERALLY STAY
        IN THEIR OWN ROOMS, EXCEPT WHEN DISPOSING OF INTRUDERS OR
        SCAVENGING FOR FOOD IN THE PITS.
IF YOU BLUNDER INTO THE SAME ROOM AS THE WUMPUS, YOU LOSE....
THE NORMALLY SLEEPING WUMPUS DOES NOT MOVE (HAVING GORGED HIMSELF UPON
A PREVIOUS HUNTER).  HOWEVER ONE THING CAN WAKE HIM UP:
        WALKING INTO HIS ROOM,
THE WUMPUS IS TOO BIG TO BE PICKED UP BY SUPER-BATS AND HAS SUCKER FEET, SO HE DOESN'T
FALL INTO THE PITS.
YOU CAN SMELL THE WUMPUS FROM ONE ROOM AWAY. YOU CAN HEAR SUPER-BATS FROM
ONE ROOM AWAY, AND FEEL BREEZES (FROM BOTTOMLESS PITS) FROM ONE ROOM
AWAY.
TO SHOOT AN ARROW TYPE 's' INSTEAD OF A MOVE, AND THEN
SPECIFY WHICH ROOM THE ARROW SHOULD PASS THROUGH. YOU CAN ONLY SHOOT INTO THE NEXT ROOM.
SPECIFY AN IMPOSSIBLE PATH AND THE ARROW WILL NOT SHOOT.
EACH ROOM IS CONNECTED TO FOUR OTHER ROOMS BY FOUR TUNNELS.  
YOU MUST ALWAYS MOVE BETWEEN ROOMS BY SPECIFYING WHICH
TUNNEL YOU WISH TO EXPLORE.  YOU CAN ALWAYS RETRACE YOUR FOOT STEPS
BY MOVING BACK USING THE SAME TUNNEL DESIGNATOR.
                GOOD LUCK HUNTING!!
                """)

input("press enter to continue")

alive = None
playing = None
current_cave = None
caves = None
wumpus_cave = None 
wumpus_alive = None

initial_state()

while alive and playing and wumpus_alive:

    decision()
    if alive == False or wumpus_alive == False:
       play_again = input("Do you want to play again? type yes or no")
       if play_again.lower() is "yes":
           initial_state()
       elif play_again.lower() is "magic powers":
           print("You have found one of two easter eggs. You decide to use your magic powers to resurrect the wumpus and play again.")
           print("You have won")
           initial_state()
       else:
           playing = False