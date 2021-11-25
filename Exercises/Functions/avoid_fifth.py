"""EX03 - avoid_fifth function."""

__author__: str = "730398410"


def avoid_fifth(words: str) -> str:
    """Makes sure that the letter is is avoided."""
    bad_letters = ["E", "e"]
    new_string: str = "".join(letters for letters in words if not letters in bad_letters)
    return new_string


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth(input("Type anything: ")))


if __name__ == "__main__":
    main()