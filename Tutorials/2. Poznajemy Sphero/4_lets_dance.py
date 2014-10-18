# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
Sphero tańczy tak, jak mu zagrasz!

1. Uruchom ten program i zobacz co się stanie
2. Dopisz kolejne dwa "kroki taneczne" - dodaj dwa elementy
	do listy kroki_taneczne
"""

predkosc = 70
czas = 1

kroki_taneczne = [22, 235, 120, 230, 350]

for obrot in kroki_taneczne:
	print "jadę pod kątem " + str(obrot)
	sphero.roll(predkosc, obrot)
	sphero.czekaj(czas)

print "stop!"
sphero.stop()

print "koniec."