# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
from random import randint
import time

"""
1. Zwróć uwagę na to, jak zmienił się drugi element w liście
   KROKI_TANECZNE
2. Uruchom ten program kilka razy, zobacz w którym kierunku
   pojechała kulka oraz porównaj trasę z tym, co zostało wypisane do
   konsoli. Spróbuj wytłumaczyć, co robi randint(1,359).
3. Zmodyfikuj listę kroków tak, aby Sphero zatańczyło w 5 losowych
   kierunkach
"""


ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 70
CZAS = 1
KROKI_TANECZNE = [10, randint(1, 359), 50]


with Kulka(ADDR) as kulka:
    for obrot in KROKI_TANECZNE:
        print("jadę pod kątem " + str(obrot))
        kulka.roll(PREDKOSC, obrot)
        time.sleep(CZAS)

    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
