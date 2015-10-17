from __future__ import print_function
from Kulka import Kulka
from textwrap import dedent
from random import randint

try:
    input_ = raw_input
except NameError:
    input_ = input


ADDR = 'XX:XX:XX:XX:XX:XX'


"""
    This program is a simple implementation of a game, where the user is
    supposed to guess the number in a range 1 to 100, while the program
    can give him a hint, whether the number provided is greater, equal
    or less to the one provided by the player

    pulse rate means how close is user to guess the number the smaller
    the value is, the closer the user is.  range: 0-100
"""


def show_hint_in_sphero(kulka, pulse_rate):
    green_channel = abs(255 - int(pulse_rate * 2.55)) % 255
    kulka.set_rgb(0, green_channel, 0)
    print("pulse rate: %s" % pulse_rate)
    print("color: 10, {}, 10".format(green_channel))


def show_hint(kulka, difference):
    if difference > 0:
        print("My number is greater!")
    else:
        print("My number is smaller!")

    pulse_rate = abs(difference)
    show_hint_in_sphero(kulka, pulse_rate)


def game(kulka):
    print(dedent("""\
        Welcome to the SpheroRiddle game! Guess my number!
        If you want to have a hint about how close you are,
        take a look at the Sphero. The faster it blinks and
        the brighter it shines, the closer you are.
        --------------------------------------------------
        Type in the number!
        """))

    secret_number = randint(1, 100)
    guess = ''
    trials = 0

    while True:
        guess = input_("> ")

        if guess == 'q' or guess == 'quit':
            break
        elif guess.isdigit():
            guess = int(guess)
            trials += 1

            if secret_number is not guess:
                show_hint(kulka, secret_number - int(guess))
            else:
                print("Bravo! You've guessed my number in %s trials!" % trials)
                break
        else:
            print("Please input the number or 'q'/'quit' if you want to end "
                  "the game.")


def play_next():
    next_ = input_("Do you want to play another game? (y/n): ")
    return next_.lower() in ["y", "yes"]


def main():
    with Kulka(ADDR) as kulka:
        while True:
            game(kulka)

            if not play_next():
                break


main()
