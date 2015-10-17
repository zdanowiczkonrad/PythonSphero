# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
from random import randint
import time
try:
    input = raw_input
except NameError:
    pass

"""
Teraz możesz do woli przetestować grę i spróbować ograć komputer :)
Jeżeli jest za trudno - zmniejsz zakres losowania tajemniczej liczby,
bądź zwiększ liczbę szans :)
"""
ADDR = 'XX:XX:XX:XX:XX:XX'

# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

def pociesz(kulka):
    for _ in range(5):
        kulka.set_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
        kulka.roll(100, randint(1, 359))
        kulka.czekaj(0.1)
        kulka.stop()

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
        kulka.set_rgb(0, 255, 0)
        zrob_kolko(kulka)
        return True
    else:
        podpowiedz(tajemnicza_liczba, proba)
        for _ in range(3):
            kulka.set_rgb(255, 120, 0)
            time.sleep(0.01)
            kulka.set_rgb(0, 0, 0)
            time.sleep(0.01)
        return False

with Kulka(ADDR) as kulka:
    for proba in range(10):
        if zgadnij(kulka, proba):
            break
    else:
        print("Porażka!")
        pociesz(kulka)
