# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint

try:
    input = raw_input
except NameError:
    pass

"""
Uruchom ten program i sprawdź co się stanie, gdy wpiszesz dowolną liczbę.
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

proba = input("Zgadnij liczbę (pierwsza próba): ")
print("Twój strzał to " + proba)
print("Tajemnicza liczba, którą wylosował komputer to" + str(tajemnicza_liczba))
