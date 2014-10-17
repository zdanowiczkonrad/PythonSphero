# -*- coding: utf-8 -*-
from random import randint
"""
Czas na podpowiedzi :) Rozszerz funkcję podpowiedz(tajemnicza_liczba, proba), 
która będzie podpowiadać graczowi. Jeżeli tajemnicza liczba jest większa od tej,
którą podał gracz, wypisz "większa". Jeżeli mniejsza, wypisz "mniejsza"
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

def podpowiedz(tajemnicza_liczba, proba):
	# Tutaj Twoja podpowiedź!

def zgadnij(numer_proby):
	proba = int(raw_input("Zgadnij liczbę (próba #%s): " % (numer_proby+1)))
	if proba is tajemnicza_liczba:
		print "Zwycięstwo!"
		return True
	else:
		# nie zapomnij wywołać funkcji podpowiedź() z właściwymi argumentami!
		return False
		
for proba in range(10):
	wynik = zgadnij(proba)
	if wynik is True:
		break
	elif proba is 9 and wynik is False:
		print "Porażka!"