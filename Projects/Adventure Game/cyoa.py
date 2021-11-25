"""Interactive game based off of the famous game Clue."""
"""There are three components to the game: the Murderer, the Weapon, and the Room."""

__author__: str = "730398410"

from random import randint

player: str 
points: int = 0
GOOD_JOB: str = str("Good job \U0001F44D! Now do something else.\n")
MAN: str = str("\U0001F468")
WOMAN: str = str("\U0001F467")
KNIFE: str = str("\U0001F52A")
BAG: str = str("\U0001F45C")
YOYO: str = str("\U0001FA80")


def main() -> None:
    """Entrypoint of the program, starting the interactive game."""
    global points
    greet()
    choice()


def greet() -> None:
    """Welcoming the user to the game."""
    print("\nWelcome to the murder mystery!")
    print("In this game, you will rely on your luck as you try to identify three")
    print("things: The murderer, the weapon, and the room.")
    global player 
    player = input("Before we start, please insert your name: ")
    print(f"\n{player}, your goal is to stay at ZERO points.")
    print("Every mistake will reduce your score. Have fun, and may the force be with you.\n")


def choice() -> None:
    """Giving the user a choice as to which route they will take."""
    global points
    print("Your four options are: \"Murderer\", \"Weapon\", \"Room\", and \"Quit\".")
    print("You may choose these in any order, ideally doing the three tasks then quitting.")
    Option: str = str(input("Now, choose which mystery you would like to solve: "))
    if Option == "Murderer":
        murderer()
    else:
        if Option == "Weapon":
            points = int(weapon(points))
            choice()
        else:
            if Option == "Room":
                points = room(points)
                choice()
            else:
                if Option == "Quit":
                    Quit(points)


def murderer() -> None:
    """Determining who committed the murder."""
    global points
    print(f"\nWell {player}, it seems you have stumbled upon the scene of a murder!")
    print("Using the following list of names, try to correctly guess who committed the murder.")
    print(f"Trouty {MAN}\nHanson {MAN}\n{player} \U0001F914\nDaniel {MAN}")
    print(f"Taylor {WOMAN}\nLynn {WOMAN}\nAnnabel {WOMAN}\nLeland {MAN}")
    Murder_guess: str = str(input("Who did it? "))
    while Murder_guess != "Trouty":
        points -= 1
        Murder_guess = str(input("Try again: "))
    print(GOOD_JOB)
    choice()

    
def weapon(x: int) -> int:
    """Determining what weapon was used to kill the victim."""
    y: int = 0
    print("\nIt is now time to determine the weapon used during this murder.")
    print("There are only three to choose from, so a wrong guess will result in a greater loss.")
    print("These are the objects you have to choose from, pick wisely:")
    print(f"Knife {KNIFE}\nHandbag {BAG}\nYo-Yo {YOYO}")
    weapon_guess = str(input("What do you think was used? "))
    while weapon_guess != "Yo-Yo":
        y -= 2
        weapon_guess = str(input("\U0001F611 No. Try. Again. "))
    else:
        print(GOOD_JOB)
        new_points: int = x + y
        return new_points


def room(x: int) -> int:
    """Determining the room in which the murder took place."""
    z: int = 0
    murder_room: int = randint(1, 12)
    print("\nThere are going to be twelve different rooms to choose from.")
    print("Pick a number that speaks to you. Or don't. Your call.")
    room_guess: int = int(input("Where do you think the murder occurred?? "))
    while room_guess != murder_room:
        z -= 1
        room_guess = int(input("Really? You thought it happened there? No. Try again. "))
    else:
        print(GOOD_JOB)
        new_points: int = x + z
        return new_points


def Quit(x: int) -> None:
    """Quitting the interactive game."""
    print(f"\nYour final point total is... {x}!")


if __name__ == "__main__":
    main()