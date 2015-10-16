# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint

try:
    input_ = raw_input
except NameError:
    intput_ = input

"""
Zmodyfikuj funkcję zgadnij(), aby zwracała True jeżeli użytkownik zgadł,
lub False jeżeli tajemnicza liczba nie została trafiona.
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1, 100)

def zgadnij(numer_proby):
    proba = int(input_("Zgadnij liczbę (próba #%s)" % (numer_proby + 1)))

    if proba == tajemnicza_liczba:
        print("Zwycięstwo!")

for proba in range(10):
    zgadnij(proba)
