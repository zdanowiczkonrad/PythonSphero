# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
1. Uruchom program i zobacz co się stanie
2. Sprawdź jak zachowuje się kulka dla prędkości od 0 do 255
3. Sprawdź co się stanie, gdy czas zostanie
	zwiększony lub zmniejszony
4. Usuń funkcję stop i zobacz co się dzieje
"""

predkosc = 50
czas = 4

print "jadę..."
sphero.roll(predkosc, 1)
sphero.czekaj(czas)

print "stop!"
sphero.stop()

print "koniec."