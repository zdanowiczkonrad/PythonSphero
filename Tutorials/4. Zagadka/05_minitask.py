# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
try:
    input = raw_input
except NameError:
    pass
"""
Pozwól graczowi zgadywać 10 razy. Umieść kod zgadywania w pętli,
która wykona się 10 razy
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

def zgadnij():
    proba = int(input("Zgadnij liczbę (pierwsza próba): "))
    if proba == tajemnicza_liczba:
        print("Zwycięstwo!")

zgadnij()
