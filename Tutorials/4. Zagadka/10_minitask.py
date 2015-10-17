# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
from kulka import Kulka
import time

try:
    input = raw_input
except NameError:
    pass

"""
Świetnie! Pamiętacie jeszcze o Sphero?

Dodaj teraz kod, który zaświeci Sphero na zielono i zrobi obrót,
jeżeli gracz zgadnie liczbę, za każdą zaś błędną odpowiedź,
Sphero zamiga 3 razy na pomarańczowo!
Extra task: im strzał jest bliżej wyniku, niech Sphero świeci się jaśniej!

Podpowiedzi:
zielony: R=0, G=255, B=0
pomarańczowy: R=255, G=120, B=0
Możesz użyć funkcji zrob_kolko(), która wykonuje obrót!
"""

ADDR = 'XX:XX:XX:XX:XX:XX'

# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

def zrob_kolko(kulka):
    for obrot in [1, 120, 240, 359, 1]:
        kulka.roll(0, obrot)
        time.sleep(0.01)

def podpowiedz(tajemnicza_liczba, proba):
    if tajemnicza_liczba > proba:
        print(" -> Większa.")
    else:
        print(" -> Mniejsza.")

def zgadnij(kulka, numer_proby):
    proba = int(input("Zgadnij liczbę (próba #%s): " % (numer_proby + 1)))
    if proba == tajemnicza_liczba:
        print("Zwycięstwo!")
        # tutaj ustaw kolor zwycięstwa!
        return True
    else:
        podpowiedz(tajemnicza_liczba, proba)
        # tutaj zamigaj trzy razy!
        return False

with Kulka(ADDR) as kulka:
    for proba in range(10):
        if zgadnij(kulka, proba):
            break
    else:
        print("Porażka!")
