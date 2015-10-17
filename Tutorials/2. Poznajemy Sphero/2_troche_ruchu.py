# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time


"""
1. Uruchom program i zobacz co się stanie
2. Sprawdź jak zachowuje się kulka dla prędkości od 0 do 255
3. Sprawdź co się stanie, gdy czas zostanie zwiększony lub zmniejszony
4. Usuń funkcję stop i zobacz co się dzieje
"""


ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 50
CZAS = 4


with Kulka(ADDR) as kulka:
    print("jadę...")
    kulka.roll(PREDKOSC, 1)
    time.sleep(CZAS)

    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
