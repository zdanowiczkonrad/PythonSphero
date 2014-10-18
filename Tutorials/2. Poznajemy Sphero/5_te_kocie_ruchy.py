# -*- coding: utf-8 -*-
from sphero import core
from random import randint
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
1 Zwróć uwagę na to, co zmieniło się w krokach.
2 Uruchom program i spróbuj wytłumaczyć, co znaczy randint.
2 zmodyfikuj listę kroków tak, aby Sphero zatańczyło w 5
losowych kierunkach
"""

predkosc = 50
czas = 1
kroki_taneczne = [10, randint(1,359), 50]

for obrot in kroki_taneczne:
	print "jadę pod kątem " + str(obrot) + " stopni"
	s.roll(predkosc, obrot)
	time.sleep(czas)

# pamiętaj o stop na końcu!
print "stop!"
s.stop()

print "koniec."