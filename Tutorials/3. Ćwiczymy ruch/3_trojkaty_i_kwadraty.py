# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
O ruchu wiadomo już wszystko :) Uruchom ten program i zobacz,
co się stanie.
1. Zmodyfikuj ten program tak, aby Sphero zakreśliło kształt trójkąta
2. Zmodyfikuj listę kroków, aby Sphero przejechało drogę
	w kształcie kwadraty
3. Wiesz jak narysować inne wielokąty? Da się w ten sposób narysować
	gwiazdę pięcioramienną?
"""

predkosc = 100
czas = 1.5

for obrot in [1, 120, 300]:
	sphero.roll(predkosc, obrot)
	sphero.czekaj(czas)

print "stop!"
sphero.stop()

print "koniec."