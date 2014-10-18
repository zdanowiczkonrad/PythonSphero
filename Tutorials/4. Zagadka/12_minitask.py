# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero
from random import randint

"""
Teraz możesz do woli przetestować grę i spróbować ograć komputer :)
Jeżeli jest za trudno - zmniejsz zakres losowania tajemniczej liczby,
bądź zwiększ liczbę szans :)
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

def pociesz():
	for i in range(5):
		sphero.set_rgb(randint(0,255),randint(0,255),randint(0,255))
		sphero.roll(100,randint(1,359))
		sphero.czekaj(0.1)
		sphero.stop()

def zrob_kolko():
	for obrot in [1,120,240,359,1]:
		sphero.roll(0,obrot)
		sphero.czekaj(0.00001)

def podpowiedz(tajemnicza_liczba, proba):
	if tajemnicza_liczba > proba:
		print " -> Większa."
	else:
		print " -> Mniejsza."

def zgadnij(numer_proby):
	proba = int(raw_input("Zgadnij liczbę (próba #%s): " % (numer_proby+1)))
	if proba is tajemnicza_liczba:
		print "Zwycięstwo!"
		sphero.set_rgb(0,255,0)
		zrob_kolko()
		return True
	else:
		podpowiedz(tajemnicza_liczba, proba)
		for i in range(3):
			sphero.set_rgb(255,120,0)
			sphero.czekaj(0.01)
			sphero.set_rgb(0,0,0)
			sphero.czekaj(0.01)
		return False
		
for proba in range(10):
	wynik = zgadnij(proba)
	if wynik is True:
		break
	elif proba is 9 and wynik is False:
		print "Porażka!"
		pociesz()