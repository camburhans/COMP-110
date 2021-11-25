"""EX03 - prime functions."""

__author__: str = "730398410"


def is_prime(num: int) -> bool:
    """Determines whether or not a number is a prime number or not."""
    x: int = 2
    tf: bool = True
    while x < num:
        if num % x != 0:
            tf = True
            x = x + 1
        else:
            tf = False
            x = x + 1
            break
    return tf
    

def list_primes(x: int, y: int) -> list[int]:
    """Deciphers which numbers out of a given range are prime numbers."""
    print(x)
    print(y)
    prime_list: list = []
    amount: int = y - x + 1
    print(amount)
    while amount > 0:
        if is_prime(x) == True:
            prime_list = prime_list.append(x)
            x = x + 1
            amount = amount - 1
        else:
            break
    return prime_list


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    print(list_primes(1, 4))


if __name__ == "__main__":
    main()