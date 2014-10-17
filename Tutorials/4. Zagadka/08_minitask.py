# -*- coding: utf-8 -*-
from random import randint
"""
Dodaj wewnątrz pętli for warunek sprawdzający, czy użytkownik zgadł.
Jeżeli tak, zakończ pętlę poleceniem "break". Jeżeli jednak gracz nie zgadł za 10 razem,
wypisz "Porażka!"
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

def zgadnij(numer_proby):
	proba = int(raw_input("Zgadnij liczbę (próba #%s): " % (numer_proby+1)))
	if proba is tajemnicza_liczba:
		print "Zwycięstwo!"
		return True
	else:
		return False
		
for proba in range(10):
	zgadnij(proba)