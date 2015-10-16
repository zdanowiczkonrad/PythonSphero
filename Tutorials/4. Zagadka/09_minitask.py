# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
try:
    input = raw_input
except NameError:
    pass
"""
Czas na podpowiedzi :) Rozszerz funkcję podpowiedz(tajemnicza_liczba,
proba), która będzie podpowiadać graczowi. Jeżeli tajemnicza liczba
jest większa od tej, którą podał gracz, wypisz "większa". Jeżeli
mniejsza, wypisz "mniejsza"
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

def podpowiedz(tajemnicza_liczba, proba):
    # Tutaj Twoja podpowiedź!
    pass

def zgadnij(numer_proby):
    proba = int(input("Zgadnij liczbę (próba #%s): " % (numer_proby + 1)))
    if proba == tajemnicza_liczba:
        print("Zwycięstwo!")
        return True
    else:
        # nie zapomnij wywołać funkcji podpowiedź() z właściwymi argumentami!
        return False

for proba in range(10):
    if zgadnij(proba):
        break
else:
    print("Porażka!")
