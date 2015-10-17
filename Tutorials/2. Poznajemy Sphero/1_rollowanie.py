# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time

"""
Przyszła pora na coś ciekawszego :) Uruchom ten program oraz
przedyskutujcie, co robi funkcja

>>> roll(predkosc, obrot)
"""


ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 0


with Kulka(ADDR) as kulka:
    # zapal tylnią diodkę, aby było wiadomo gdzie jest "tył" kulki
    kulka.set_back_led_output(255)


    for obrot in [1, 120, 240, 359, 1]:
        kulka.roll(PREDKOSC, obrot)
        print("Sphero obrócone do kąta " + str(obrot))
        time.sleep(0.01)

    kulka.roll(0, 0)

    print("koniec.")
