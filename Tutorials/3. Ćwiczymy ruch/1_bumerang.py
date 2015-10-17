# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time

"""
1. Przeanalizuj ten program i narysuj na kartce tor, po którym Twoim
   zdaniem przejedzie Sphero.
2. Następnie uruchom go i porównaj wyniki z przypuszczeniami
"""


ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 60
CZAS = 2


with Kulka(ADDR) as kulka:
    # bumerang
    kulka.roll(PREDKOSC, 1)
    time.sleep(CZAS)

    kulka.roll(PREDKOSC, 180)
    time.sleep(CZAS)

    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
