# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero
from random import randint

"""
1. Zwróć uwagę na to, jak zmienił się drugi element
	w liście kroki_taneczne
2. Uruchom ten program kilka razy, zobacz w którym kierunku
	pojechała kulka oraz porównaj trasę z tym, co zostało
	wypisane do konsoli. Spróbuj wytłumaczyć, co robi randint(1,359).
3. Zmodyfikuj listę kroków tak, aby Sphero zatańczyło w 5
	losowych kierunkach
"""

predkosc = 70
czas = 1

kroki_taneczne = [10, randint(1, 359), 50]

for obrot in kroki_taneczne:
	print "jadę pod kątem " + str(obrot)
	sphero.roll(predkosc, obrot)
	sphero.czekaj(czas)

print "stop!"
sphero.stop()

print "koniec."