"""Tar Heels exercise redux as a structured program."""

__author__ = "730398410"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))


def tar_heels(random_num: int) -> str:
    """Deciding if integer is divisible by 2, 7, 2&7, or neither."""
    x: str
    if random_num % 2 == 0 and random_num % 7 == 0:
        x = str("TAR HEELS")
    else:
        if random_num % 2 == 0:
            x = str("TAR")
        else:
            if random_num % 7 == 0:
                x = str("HEELS")
            else:
                x = str("CAROLINA")
    return x


if __name__ == "__main__":
    main()
