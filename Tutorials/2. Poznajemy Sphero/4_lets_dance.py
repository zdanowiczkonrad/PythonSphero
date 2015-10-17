# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time


"""
Sphero tańczy tak, jak mu zagrasz!

1. Uruchom ten program i zobacz co się stanie
2. Dopisz kolejne dwa "kroki taneczne" - dodaj dwa elementy do listy
   KROKI_TANECZNE
"""


ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 70
CZAS = 1
KROKI_TANECZNE = [22, 235, 120, 230, 350]


with Kulka(ADDR) as kulka:
    for obrot in KROKI_TANECZNE:
        print("jadę pod kątem " + str(obrot))
        kulka.roll(PREDKOSC, obrot)
        time.sleep(CZAS)

    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
