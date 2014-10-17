# -*- coding: utf-8 -*-
from random import randint
from sphero import core
import time
"""
Wcale nie jest tak łatwo wygrać! Dodaj funkcję "pociesz()",
która zaświeci Sphero na losowy kolor i wykona dowolną sekwencję ruchów!
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
		s.set_rgb(0,255,0)
		zrob_kolko()
		return True
	else:
		podpowiedz(tajemnicza_liczba, proba)
		for i in range(3):
			s.set_rgb(255,120,0)
			time.sleep(0.01)
			s.set_rgb(0,0,0)
			time.sleep(0.01)
		return False
		
for proba in range(10):
	wynik = zgadnij(proba)
	if wynik is True:
		break
	elif proba is 9 and wynik is False:
		print "Porażka!"
		# tutaj wywołaj swoją oryginalną funkcję pociesz()!