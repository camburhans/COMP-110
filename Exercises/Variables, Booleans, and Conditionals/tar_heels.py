"""An exercise in remainders and boolean logic."""



# Begin your solution here...
random_num: int = int(input("Pick a number: "))
if random_num % 2 == 0 and random_num % 7 == 0:
    print("TAR HEELS")
else:
    if random_num % 2 == 0:
        print("TAR")
    else:
        if random_num % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
