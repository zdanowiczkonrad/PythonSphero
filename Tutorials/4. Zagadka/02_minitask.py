# -*- coding: utf-8 -*-
from random import randint
"""
Uruchom ten program i sprawdź co się stanie, gdy wpiszesz dowolną liczbę. 
"""
# liczba, którą zna komputer
tajemnicza_liczba = randint(1,100)

proba = raw_input("Zgadnij liczbę (pierwsza próba): ")
print "Twój strzał to " + proba
print "Tajemnicza liczba, którą wylosował komputer to" + str(tajemnicza_liczba)