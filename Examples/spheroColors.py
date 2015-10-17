from __future__ import print_function
from kulka import Kulka
import time


ADDR = 'XX:XX:XX:XX:XX:XX'


with Kulka(ADDR) as kulka:
    for _ in range(3):
        print("Setting color to red")
        kulka.set_rgb(255, 0, 0)
        time.sleep(0.1)

        print("Setting color to green")
        kulka.set_rgb(0, 255, 0)
        time.sleep(0.1)

        print("Setting color to blue")
        kulka.set_rgb(0, 0, 255)
        time.sleep(0.1)
