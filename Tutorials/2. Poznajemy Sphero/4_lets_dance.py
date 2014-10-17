# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
Sphero tańczy tak, jak mu zagrasz!
1 uruchom ten program i zobacz co się stanie
2 dopisz dwa kroki ruchu kulki
"""

predkosc = 50
czas = 1
kroki_taneczne = [22,235,211,95,173]

for obrot in kroki_taneczne:
	print "jadę pod kątem " + str(obrot) + " stopni"
	s.roll(predkosc, obrot)
	time.sleep(czas)

# pamiętaj o stop na końcu!
print "stop!"
s.stop()

print "koniec."