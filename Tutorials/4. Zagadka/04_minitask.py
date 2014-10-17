# -*- coding: utf-8 -*-
from random import randint
"""
Kod, który pyta gracza o liczbę, przenieś do funkcji "zgadnij"
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

proba = int(raw_input("Zgadnij liczbę (pierwsza próba): "))
if proba is tajemnicza_liczba:
	print "Zwycięstwo!"

