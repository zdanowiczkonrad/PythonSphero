# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time


"""
1. Umieść napisany przez Ciebie kod w pętli, aby Sphero trzykrotnie
   przejechało w tę i z powrotem!
2. Z każdym kolejnym powtórzeniem, zmień prędkość Sphero!
   Wykorzystaj do tego listę "PREDKOSCI"
3. Z każdym kolejnym powtórzeniem, zmień kolor Sphero!  Wykorzystaj do
   listę kolory. funkcję set_rgb()
4. Dodaj własny krok z marchewkowym kolorem i prędkością 128
   - rozszerz listę PREDKOSCI o 128, oraz dodaj do tablicy kolory
     kolejny element z własnym kolorem
"""


PREDKOSCI = [100, 40, 80]
CZAS = 2

KOLORY = [
    [150, 210, 54],
    [251, 61, 10],
    [70, 51, 211]
]


with Kulka(ADDR) as kulka:
    # umieść ten kod w pętli
    # ----------------------------------------------------
    # 1. ustaw pierwszy kolor z tablicy KOLORY
    kulka.set_rgb(KOLORY[0][0], KOLORY[0][1], KOLORY[0][2])

    # 2. zatocz się z prędkością 100
    kulka.roll(PREDKOSCI[0], 1)
    time.sleep(CZAS)
    # 3. wielki powrót
    kulka.roll(PREDKOSCI[0], 180)
    time.sleep(CZAS)
    # ----------------------------------------------------

    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
