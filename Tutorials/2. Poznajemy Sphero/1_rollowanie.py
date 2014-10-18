# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
Przyszła pora na coś ciekawszego :)
Uruchom ten program oraz przedyskutujcie,
co robi funkcja
	roll(predkosc, obrot)!
"""
# zapal tylnią diodkę, aby było wiadomo gdzie jest "tył" kulki
sphero.set_back_led_output(255)

predkosc = 0

for obrot in [1, 120, 240, 359, 1]:
	sphero.roll(predkosc, obrot)
	print "Sphero obrócone do kąta " + str(obrot)
	sphero.czekaj(0.01)

print "koniec."