# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
1. uruchom program i zobacz co się stanie
2. sprawdź jak zachowuje się kulka dla prędkości od 0 do 255
3. sprawdź co się stanie, gdy czas zostanie zwiększony lub zmniejszony
"""

predkosc = 50
czas = 4

print "jazda!"
s.roll(predkosc,1)
time.sleep(czas)

print "stop!"
s.stop()

print "koniec."