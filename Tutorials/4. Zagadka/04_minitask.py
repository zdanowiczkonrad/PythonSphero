# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
try:
    input = raw_input
except NameError:
    pass

"""
Kod, który pyta gracza o liczbę, przenieś do funkcji "zgadnij"
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

proba = int(input("Zgadnij liczbę (pierwsza próba): "))
if proba == tajemnicza_liczba:
    print("Zwycięstwo!")

