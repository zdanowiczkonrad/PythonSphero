# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time


"""
1. Dodaj kolejny ruch tak, aby Sphero poruszyło się w kształcie litery L
2. Dodaj jeszcze kilka ruchów
3. Możesz poeksperymentować z wartościami prędkości i czasu
"""


ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 50
CZAS = 4


with Kulka(ADDR) as kulka:
    kulka.roll(PREDKOSC, 1)
    time.sleep(CZAS)

    # tutaj dodaj kolejny ruch pod kątem 90 stopni
    print("uwaga, zakręt!")

    # pamiętajmy o stop na końcu!
    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
