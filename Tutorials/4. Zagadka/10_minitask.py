# -*- coding: utf-8 -*-
from random import randint
from sphero import core
import time
"""
Świetnie! Pamiętacie jeszcze o Sphero? 

Dodaj teraz kod, który zaświeci Sphero na zielono i zrobi obrót,
jeżeli gracz zgadnie liczbę, za każdą zaś błędną odpowiedź, Sphero 
zamiga 3 razy na pomarańczowo!
Extra task: im strzał jest bliżej wyniku, niech Sphero świeci się jaśniej!

Podpowiedzi:
zielony: R=0, G=255, B=0
pomarańczowy: R=255, G=120, B=0
Możesz użyć funkcji zrob_kolko(), która wykonuje obrót!
"""
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()

# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

def zrob_kolko():
	for obrot in [1,120,240,359,1]:
		s.roll(0,obrot)
		time.sleep(0.00001)

def podpowiedz(tajemnicza_liczba, proba):
	if tajemnicza_liczba > proba:
		print " -> Większa."
	else:
		print " -> Mniejsza."

def zgadnij(numer_proby):
	proba = int(raw_input("Zgadnij liczbę (próba #%s): " % (numer_proby+1)))
	if proba is tajemnicza_liczba:
		print "Zwycięstwo!"
		# tutaj ustaw kolor zwycięstwa!
		return True
	else:
		podpowiedz(tajemnicza_liczba, proba)
		# tutaj zamigaj trzy razy!
		return False
		
for proba in range(10):
	wynik = zgadnij(proba)
	if wynik is True:
		break
	elif proba is 9 and wynik is False:
		print "Porażka!"