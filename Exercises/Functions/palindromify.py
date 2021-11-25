"""EX03 - palindromify function."""

__author__: str = "730398410"


def palindromify(word: str, t_f: bool) -> str:
    """Will make any word/collection of letters a palindrome."""
    i: int = len(word) - 1
    string: str = ""
    new_string: str = ""
    if t_f == True:
        while i >= 0:
            letter: str = word[i]
            string = string + letter
            i -= 1
        else:
            new_string = word + string
    else:
        if t_f == False:
            while i > 0:
                letter: str = word[i - 1]
                string = string + letter
                i -= 1
            else:
                new_string = word + string
    return new_string


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


if __name__ == "__main__":
    main()