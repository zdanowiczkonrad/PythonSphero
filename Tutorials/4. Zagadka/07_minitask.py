# -*- coding: utf-8 -*-
from random import randint
"""
Zmodyfikuj funkcję zgadnij(), aby zwracała True jeżeli użytkownik zgadł,
lub False jeżeli tajemnicza liczba nie została trafiona.
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

def zgadnij(numer_proby):
	proba = int(raw_input("Zgadnij liczbę (próba #%s)" % (numer_proby+1)))
	if proba is tajemnicza_liczba:
		print "Zwycięstwo!"
		
for proba in range(10):
	zgadnij(proba)