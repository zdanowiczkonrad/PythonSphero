# -*- coding: utf-8 -*-
from random import randint
"""
Coś tu nie gra! Gracz zgaduje kilka razy, ale widzi zawsze komunikat "pierwsza próba"...
Dodaj do funkcji <<zgadnij>> argument "proba" i wypisuj poprawny komunikat z numerem próby
zamiast "pierwsza próba".
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

def zgadnij():
	proba = int(raw_input("Zgadnij liczbę (pierwsza próba): "))
	if proba is tajemnicza_liczba:
		print "Zwycięstwo!"

for proba in range(10):
	zgadnij()