# -*- coding: utf-8 -*-
from random import randint
"""
Pozwól graczowi zgadywać 10 razy. Umieść kod zgadywania w pętli,
która wykona się 10 razy
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

def zgadnij():
	proba = int(raw_input("Zgadnij liczbę (pierwsza próba): "))
	if proba is tajemnicza_liczba:
		print "Zwycięstwo!"

zgadnij()