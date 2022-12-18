from random import randint


def get_number():
    """Get number from user.

    Try until user give proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            return int(input("Guess the number: "))
        except ValueError:
            print("It's not a number")


def guess_the_number():
    """Main function for our game."""
    secret_number = randint(1, 100)
    given_number = get_number()
    while not given_number == secret_number:
        if given_number < secret_number:
            print("Too small!")
        else:
            print("Too big!")
        given_number = get_number()
    print("You Win!")


if __name__ == "__main__":
    guess_the_number()
