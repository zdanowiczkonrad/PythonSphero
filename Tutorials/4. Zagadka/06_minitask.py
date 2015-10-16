# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
try:
    input = raw_input
except NameError:
    pass
"""
Coś tu nie gra! Gracz zgaduje kilka razy, ale widzi zawsze komunikat
"pierwsza próba"...  Dodaj do funkcji <<zgadnij>> argument "proba"
i wypisuj poprawny komunikat z numerem próby zamiast "pierwsza próba".
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

def zgadnij():
    proba = int(input("Zgadnij liczbę (pierwsza próba): "))
    if proba == tajemnicza_liczba:
        print("Zwycięstwo!")

for proba in range(10):
    zgadnij()
