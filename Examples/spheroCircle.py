from kulka import Kulka
import time


ADDR = 'XX:XX:XX:XX:XX:XX'


STEPS = 10
SPEED = 0x30
SLEEP_TIME = 0.3


def make_a_step(kulka, current_angle):
    kulka.roll(SPEED, current_angle)
    time.sleep(SLEEP_TIME)
    kulka.roll(0, current_angle)


def make_a_circle(kulka, steps):
    rotate_by = 360 // steps
    current_angle = 1

    for _ in range(steps):
        make_a_step(kulka, current_angle % 360)
        current_angle += rotate_by


def main():
    with Kulka(ADDR) as kulka:
        make_a_circle(kulka, STEPS)


main()
