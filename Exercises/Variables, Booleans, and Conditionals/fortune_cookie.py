"""Program that outputs one of at least four random, good fortunes."""

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune_number: int = randint(1, 4)
if fortune_number == 4:
    print("You will ace your next exam.")
else:
    if fortune_number == 3:
        print("Within the next week, you will meet your soulmate.")
    else:
        if fortune_number == 2:
            print("A dubious friend may be an enemy in camouflage.")
        else:
            print("A fresh start will put you on your way.")
print("Now, go spread positive vibes!")
