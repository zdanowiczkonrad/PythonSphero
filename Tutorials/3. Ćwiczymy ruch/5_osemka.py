# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time

"""
Na podstawie programu, w którym Sphero jeździ w kółko, napisz program,
który toczy Sphero w znak ósemki!  podpowiedź: funkcja reversed(lista)
przyjmuje listę i zwraca listę z elementami w odwrotnej kolejności, np.

>>> reversed([1, 2, 3])
[3, 2, 1]
"""


ADDR = 'XX:XX:XX:XX:XX:XX'


def jazda(kulka, lista_obrotow):
    predkosc = 70
    czas = 0.2

    for obrot in lista_obrotow:
        print("obrot o kat " + str(obrot))
        kulka.roll(predkosc, obrot)
        time.sleep(czas)


with Kulka(ADDR) as kulka:
    # wywolaj funkcje jazda
    jazda(kulka, range(1, 359, 40))
    print("---")
    # wywołaj jeszcze raz tę funkcję, ale z odwróconą listą obrotów

    # pamiętaj o stop na końcu!
    print("stop!")
    kulka.roll(0, 0)

    print("koniec.")
