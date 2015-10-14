from __future__ import print_function
from kulka import Kulka
import time


ADDR = 'XX:XX:XX:XX:XX:XX'


def do_the_dance(kulka):
    speed = 0x88
    sleep_time = 1

    for angle in [1, 90, 180, 270]:
        kulka.roll(speed, angle)
        time.sleep(sleep_time)

    kulka.roll(0, 0)


def main():
    with Kulka(ADDR) as kulka:
        for _ in range(3):
            do_the_dance(kulka)
            time.sleep(0.1)

        print("The end. Sphero goes to bed.")
        kulka.sleep()
