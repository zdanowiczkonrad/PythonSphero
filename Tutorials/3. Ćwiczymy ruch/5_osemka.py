# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
Na podstawie programu, w którym Sphero jeździ w kółko,
napisz program aby sphero zatoczyło ósemkę!
podpowiedź: wywołaj funkcję jazda z argumentem "reversed(range(1,359))"
"""

def jazda(sphero,lista_obrotow):		
	predkosc = 70
	czas = 0.1
	for obrot in lista_obrotow:
		if obrot % 30 == 0: #to jest do usuniecia, interwal ustawic w range'u
			sphero.roll(predkosc,obrot)
			time.sleep(czas)

# kółko
jazda(s,range(1,359))
# wywołaj jeszcze raz tę funkcję, ale z odwróconą listą obrotów


# pamiętaj o stop na końcu!
print "stop!"
s.stop()

print "koniec."