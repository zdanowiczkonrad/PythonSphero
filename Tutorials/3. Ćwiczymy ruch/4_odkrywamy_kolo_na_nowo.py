# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time


"""
1. Zmodyfikuj poprzedni program, aby Sphero przejechało koło.
   podrasuj listę "LISTA_OBROTOW".  możesz użyć funkcji range(1, 359,
   40), która utworzy listę liczb od 1 do 359 co 40, czyli [1, 41, 81,...]
2. Utwórz funkcję "jazda(sphero, LISTA_OBROTOW)" i przenieś do jej
   definicji pętle for wraz instrukcjami, które powodują że Sphero się
   rolluje i czeka.
3. Zwiększ/zmniejsz CZAS i zobacz jak Sphero robi mniejsze lub większe koło!
"""

ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 70
CZAS = 0.5

LISTA_OBROTOW = [1, 20, 40, 60]


with Kulka(ADDR) as kulka:
    for obrot in LISTA_OBROTOW:
        print("obrot o kat " + str(obrot))
        kulka.roll(PREDKOSC, obrot)
        time.sleep(CZAS)

    # pamiętaj o stop na końcu!
    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
