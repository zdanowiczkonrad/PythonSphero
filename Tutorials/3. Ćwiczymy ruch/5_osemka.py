# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
Na podstawie programu, w którym Sphero jeździ w kółko,
napisz program, który toczy Sphero w znak ósemki!
podpowiedź: funkcja reversed(lista) przyjmuje listę i zwraca
	listę z elementami w odwrotnej kolejności, np.
		reversed([1, 2, 3])=[3, 2, 1]
"""

def jazda(sphero, lista_obrotow):		
	predkosc = 70
	czas = 0.2
	for obrot in lista_obrotow:
		print "obrot o kat " + str(obrot)
		sphero.roll(predkosc,obrot)
		sphero.czekaj(czas)

# wywolaj funkcje jazda
jazda(sphero, range(1, 359, 40))
print "---"
# wywołaj jeszcze raz tę funkcję, ale z odwróconą listą obrotów


# pamiętaj o stop na końcu!
print "stop!"
sphero.stop()

print "koniec."