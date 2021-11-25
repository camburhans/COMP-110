"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730398410"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Generating the fortune."""
    x: str
    fortune_number: int = randint(1, 4)
    if fortune_number == 4:
        x = str("You will ace your next exam.")
    else:
        if fortune_number == 3:
            x = str("Within the next week, you will meet your soulmate.")
        else:
            if fortune_number == 2:
                x = str("A dubious friend may be an enemy in camouflage.")
            else:
                x = str("A fresh start will put you on your way.")
    return x


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
