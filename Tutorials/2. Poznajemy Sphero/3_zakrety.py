# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
1. Dodaj kolejny ruch tak, aby Sphero
	poruszyło się w kształcie litery L
2. Dodaj jeszcze kilka ruchów
3. Możesz poeksperymentować z wartościami prędkości i czasu
"""

predkosc = 50
czas = 4

sphero.roll(predkosc, 1)
sphero.czekaj(czas)


# tutaj dodaj kolejny ruch pod kątem 90 stopni
print "uwaga, zakręt!"

# pamiętajmy o stop na końcu!
print "stop!"
sphero.stop()

print "koniec."