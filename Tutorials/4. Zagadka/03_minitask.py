# -*- coding: utf-8 -*-
from random import randint
"""
Sprawdź, czy liczba, którą podał człowiek (zmienna proba)
jest rowna tajemniczej liczbie, którą wylosował komputer
Jeżeli tak, wypisz "Zwycięstwo!"
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

proba = int(raw_input("Zgadnij liczbę (pierwsza próba): "))
