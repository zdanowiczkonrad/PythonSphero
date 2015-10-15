# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time


"""
O ruchu wiadomo już wszystko :) Uruchom ten program i zobacz,
co się stanie.
1. Zmodyfikuj ten program tak, aby Sphero zakreśliło kształt trójkąta
2. Zmodyfikuj listę kroków, aby Sphero przejechało drogę
   w kształcie kwadraty
3. Wiesz jak narysować inne wielokąty? Da się w ten sposób narysować
   gwiazdę pięcioramienną?
"""

ADDR = 'XX:XX:XX:XX:XX:XX'
PREDKOSC = 100
CZAS = 1.5


with Kulka(ADDR) as kulka:
    for obrot in [1, 120, 300]:
        kulka.roll(PREDKOSC, obrot)
        time.sleep(CZAS)

    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
